import logging
import os
import pytz

from core.models import Survey, SurveyResult, SurveyDefinition, IndustryBenchmark
from core.qualtrics import benchmark, download, exceptions, question
from django.conf import settings

from google.appengine.api import mail
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.shortcuts import reverse
from django.template.loader import get_template
from django.db import IntegrityError
from djangae.db import transaction
from django.utils.timezone import make_aware
from django.utils.dateparse import parse_datetime
import cloudstorage
from google.appengine.api import app_identity
import unicodecsv as csv
from datetime import datetime
from collections import defaultdict
from core.aggregate import updatable_industries

from core.conf.utils import get_tenant_slug
from django.utils import translation
from core.googleapi import sheets
from django.utils.functional import Promise
from django.utils.encoding import force_text


def sync_qualtrics():
    for tenant_key, tenant in settings.TENANTS.items():
        survey_definition = _get_definition(tenant_key, tenant['QUALTRICS_SURVEY_ID'])

        if survey_definition:
            _get_results(tenant, survey_definition)
        else:
            logging.error('Fetching survey definition failed, not fetching results')


def _get_definition(tenant, survey_id):
    """Download survey definition from Qualtrics and store it in `core.SurveyDefinition`.

    If a new survey definition is found, it's then saved as `core.SurveyDefinition` and returned,
    the latest `core.SurveyDefinition` is returned otherwise.

    :param survey_id: id of the survey the definition is fetched

    :returns: `core.SurveyDefinition` stored.
    """
    try:
        survey_definition = download.fetch_survey(survey_id)
        last_survey_definition = SurveyDefinition.objects.filter(tenant=tenant).latest('last_modified')
        downloaded_survey_last_modified = parse_datetime(survey_definition['lastModifiedDate'])
        if downloaded_survey_last_modified > last_survey_definition.last_modified:
            last_survey_definition = SurveyDefinition.objects.create(
                tenant=tenant,
                last_modified=downloaded_survey_last_modified,
                content=survey_definition
            )
    except SurveyDefinition.DoesNotExist:
        last_survey_definition = SurveyDefinition.objects.create(
            tenant=tenant,
            last_modified=survey_definition['lastModifiedDate'],
            content=survey_definition
        )
    except exceptions.FetchResultException as fe:
        logging.error('Fetching survey definition failed with: {}'.format(fe))
        return

    return last_survey_definition


def _get_results(tenant, survey_definition):
    """Download survey results from Qualtrics.

    :param tenant: dictionary containing 'QUALTRICS_SURVEY_ID', 'EMAIL_TO', 'EMAIL_BCC' keys
    :param survey_definition: `core.SurveyDefinition` object.


    The function will use the latest stored `response_id` if any, otherwise
    download all the available results from Qualtrics.
    """
    survey_id, email_to, email_bcc = tenant['QUALTRICS_SURVEY_ID'], tenant['EMAIL_TO'], tenant['EMAIL_BCC']
    try:
        survey_result = SurveyResult.objects.latest('started_at')
        started_after = survey_result.started_at
        logging.info('Some Survey results has already been downloaded, partially download new results.')
    except SurveyResult.DoesNotExist:
        started_after = None
        logging.info('No Survey results has already been downloaded so far, download all the results.')

    try:
        results = download.fetch_results(survey_id, started_after=started_after)
        responses = results.get('responses')
        results_text = download.fetch_results(survey_id, started_after=started_after, text=True)
        responses_text = results_text.get('responses')

        merged_responses = _update_responses_with_text(responses, responses_text)

        new_survey_results = _create_survey_results(merged_responses.values(), survey_definition, tenant)
        new_response_ids = [result.response_id for result in new_survey_results]

        langs_dict = settings.QUALTRICS_LANGS

        email_list = [(item.get(email_to),
                       item.get(email_bcc),
                       item.get('sid'),
                       langs_dict.get(item.get('Q_Language'), langs_dict['EN'])) for item in responses
                      if _survey_completed(item.get('Finished')) and item.get('ResponseID') in new_response_ids]
        if email_list:
            send_emails_for_new_reports(email_list)
    except exceptions.FetchResultException as fe:
        logging.error('Fetching results failed with: {}'.format(fe))


def _update_responses_with_text(responses, text_responses):
    responses_by_id = {k['ResponseID']: k for k in responses}
    response_text_by_id = {k['ResponseID']: k for k in text_responses}

    merged_responses = {}

    for key, val in responses_by_id.items():
        merged_responses[key] = {
            'value': val,
            'text': response_text_by_id.get(key)
        }

    return merged_responses


def _create_survey_results(results_data, last_survey_definition, tenant):
    """Create `SurveyResult` given a list of `result_data`.

    :param results_data: dictionary containing the downloaded responses
        from Qualtrics API.
    :param last_survey_definition: `core.SurveyDefinition` object,
        reprensenting the last definition stored in the model.

    :returns: list of `response_id` for each `core.SurveyResult` created.
    """
    new_survey_results = []
    for data in results_data:
        try:
            new_survey_result = _create_survey_result(data, last_survey_definition, tenant)
            if new_survey_result:
                new_survey_results.append(new_survey_result)
        except exceptions.InvalidResponseData as e:
            logging.error(e)
    return new_survey_results


def _create_survey_result(survey_data, last_survey_definition, tenant):
    """Create `SurveyResult` given a single `result_data`.

    :param data: dictionary of data downloaded from Qualtrics
    :param last_survey_definition: `core.SurveyDefinition` object,
        reprensenting the last definition stored in the model.

    :returns: `response_id` if a `core.SurveyResult` is created, None
        otherwise.
    """
    response_data, response_text = survey_data['value'], survey_data['text']
    if not _survey_completed(response_data.get('Finished')):
        logging.warning('Found unfinshed survey {}: SKIP'.format(response_data.get('sid')))
        return

    response_id = response_data['ResponseID']
    new_survey_result = None
    try:
        with transaction.atomic(xg=True):
            dimensions, multianswers, weights = tenant['DIMENSIONS'], tenant['MULTI_ANSWER_QUESTIONS'], tenant['WEIGHTS']  # noqa
            questions = question.data_to_questions(response_data, dimensions, multianswers, weights)
            questions_text = question.data_to_questions_text(response_text, dimensions, multianswers)

            raw_data = question.to_raw(questions, questions_text)
            dmb, dmb_d = _response_benchmark(questions, response_data, tenant)
            excluded_from_best_practice = question.discard_scores(response_data, tenant['EXCLUDED_TIME_THRESHOLD'])
            survey_result = SurveyResult.objects.create(
                survey_id=response_data.get('sid'),
                response_id=response_id,
                started_at=make_aware(parse_datetime(response_data.get('StartDate')), pytz.timezone('US/Mountain')),
                excluded_from_best_practice=excluded_from_best_practice,
                dmb=dmb,
                dmb_d=dmb_d,
                raw=raw_data,
                survey_definition=last_survey_definition,
            )
            new_survey_result = survey_result
            try:
                s = Survey.objects.get(pk=response_data.get('sid'))
                s.last_survey_result = survey_result
                s.save()
            except Survey.DoesNotExist:
                logging.warning('Could not update Survey with sid {}'.format(response_data.get('sid')))
    except IntegrityError:
        logging.info('SurveyResult with response_id: {} has already been saved.'.format(response_id))
    return new_survey_result


def _response_benchmark(questions, response_data, tenant):
    if tenant['key'] == settings.NEWS:
        answer_value = question.get_question(tenant['DIMENSIONS_WEIGHTS_QUESTION_ID'], response_data)
        dimensions_weights = tenant['DIMENSIONS_WEIGHTS'][answer_value]
    elif tenant['key'] == settings.RETAIL:
        dimensions_weights = tenant['DIMENSIONS_WEIGHTS']
    else:
        dimensions_weights = None
    return benchmark.calculate_response_benchmark(questions, dimensions_weights=dimensions_weights)


def send_emails_for_new_reports(email_list):
    """Send an email for every element of `email_list`.

    :param email_list: tuple of element (to, bcc, sid, Q_Language)
    """
    domain = getattr(settings, 'LIVE_DOMAIN', os.environ['HTTP_HOST'])

    for email_data in email_list:
        to, bcc, sid, q_lang = email_data
        logging.info("Preparing to send email for: sid: {} to: {} bcc: {}".format(sid, to, bcc))

        # Last minute change, we should refactor this and pass the object in
        try:
            s = Survey.objects.get(pk=sid)
            company_name = s.company_name
            industry = s.get_industry_display()
            country = s.get_country_display()
            tenant = s.tenant
            if is_valid_email(to):
                bcc = [bcc] if is_valid_email(bcc) else None
                slug = get_tenant_slug(tenant)
                link = _localised_link(q_lang, slug, sid)
                context = {
                    'url': "http://{}{}".format(domain, link),
                    'company_name': company_name,
                    'industry': industry,
                    'country': country,
                }

                subject, text_message, html_message = render_email_template(tenant, context, q_lang)
                sender = settings.TENANTS[tenant]['CONTACT_EMAIL']

                email_kwargs = {
                    'to': [to],
                    'subject': subject,
                    'sender': sender,
                    'body': text_message,
                    'html': html_message,
                }

                if getattr(settings, 'REPLY_TO_EMAIL', None):
                    email_kwargs['reply_to'] = settings.REPLY_TO_EMAIL

                message = mail.EmailMessage(**email_kwargs)

                if bcc:
                    message.bcc = bcc

                message.send()

                logging.info("Email sent to {} from {} for Survey with sid={}".format(to, sender, sid))
        except Survey.DoesNotExist:
            # if the survey does not exist, we should not send emails
            logging.warning('Could not find Survey with sid {} to get context string for email'.format(sid))


def _localised_link(language, slug, sid):
    cur_language = translation.get_language()
    try:
        translation.activate(language)
        link = reverse('report', kwargs={'tenant': slug, 'sid': sid})
    finally:
        translation.activate(cur_language)

    return link


def render_email_template(tenant, context, language):
    cur_language = translation.get_language()
    try:
        translation.activate(language)

        subject_template = get_template("public/{}/email/response_ready_email_subject.txt".format(tenant))
        html_message_template = get_template("public/{}/email/response_ready_email_body.html".format(tenant))
        text_message_template = get_template("public/{}/email/response_ready_email_body.txt".format(tenant))

        try:
            subject_rendered = subject_template.render(context).split("\n")[1]
        except IndexError:
            subject_rendered = subject_template.render(context).split("\n")[0]
        text_message_rendered = text_message_template.render(context)
        html_message_rendered = html_message_template.render(context)
    finally:
        translation.activate(cur_language)
    return subject_rendered, text_message_rendered, html_message_rendered


def is_valid_email(email):
    email_validator = EmailValidator()
    try:
        email_validator(email)
    except ValidationError:
        return False
    return True


def _survey_completed(is_finished):
    is_finished = int(is_finished)
    return bool(is_finished)


def generate_csv_export(surveys, survey_fields, survey_result_fields, prefix):
    """Generate csv export for a list of surveys, and store it on configured bucket.

    :param surveys: list of `core.models.Survey` to be exported to csv
    :param survey_fields: list of `core.models.Survey` fields to be exported
    :param survey_result_fields: list of `core.models.SurveyResult` fields to be exported
    :param prefix: filename prefix to use in addition of filename

    """
    bucket_name = os.environ.get('BUCKET_NAME', app_identity.get_default_gcs_bucket_name())
    filename = os.path.join(
        '/',
        bucket_name,
        '{}-export-{}.csv'.format(prefix, datetime.now().strftime('%Y%m%d-%H%M%S'))
    )

    logging.info("Creating export in {}".format(filename))

    all_fields = survey_fields + survey_result_fields

    write_retry_params = cloudstorage.RetryParams(backoff_factor=1.1)
    with cloudstorage.open(filename, 'w', content_type='text/csv', retry_params=write_retry_params) as gcs_file:
        fieldnames = all_fields
        writer = csv.DictWriter(gcs_file, fieldnames=fieldnames, lineterminator='\n')
        writer.writeheader()

        for survey in surveys:
            survey_data = {field: None for field in all_fields}
            try:
                survey_data.update({
                    'id': survey.pk,
                    'company_name': survey.company_name,
                    'industry': settings.INDUSTRIES.get(survey.industry),
                    'country': settings.COUNTRIES.get(survey.country),
                    'created_at': survey.created_at,
                    'engagement_lead': survey.engagement_lead,
                    'tenant': survey.tenant
                })
                if survey.last_survey_result:
                    survey_data['excluded_from_best_practice'] = survey.last_survey_result.excluded_from_best_practice
                    survey_data['dmb'] = survey.last_survey_result.dmb
                    survey_data.update(survey.last_survey_result.dmb_d)
            except SurveyResult.DoesNotExist:
                # In case we have a survey, but has not been completed yet
                pass
            writer.writerow(survey_data)

    latest = os.path.join('/', bucket_name, '{}-latest.csv'.format(prefix))
    logging.info("Copying {} as {}".format(filename, latest))
    cloudstorage.copy2(filename, latest, metadata=None, retry_params=write_retry_params)
    logging.info("Export completed")


def update_industries_benchmarks(survey_results):
    """
    Update industries benchmarks for each element in `survey_results` parameter.

    :param survey_results: a list of `core.models.SurveyResults` used to update
        `core.models.IndustryBenchmark`
    """
    results_by_industry = defaultdict(list)
    for s in survey_results:
        if s.survey:
            results_by_industry[s.survey.industry].append(s)


def calculate_industry_benchmark(tenant):
    logging.info("calculate_industry_benchmark called for tenant: {}".format(tenant))
    if tenant == settings.NEWS:
        return

    last_survey_results_pks = Survey.objects.filter(
        tenant=tenant,
        last_survey_result__isnull=False).values_list('last_survey_result', flat=True)
    valid_survey_results = SurveyResult.valid_results.filter(pk__in=list(last_survey_results_pks))

    survey_results_by_industry = updatable_industries(valid_survey_results)
    dimensions = settings.TENANTS[tenant]['DIMENSIONS']

    for industry, survey_results in survey_results_by_industry.items():
        logging.info("Updating industry: {}".format(industry))

        dmb_d_list = [result.dmb_d for result in survey_results]
        dmb_d_bp_list = [result.dmb_d for result in survey_results]

        dmb, dmb_d = None, None
        if len(dmb_d_list) >= settings.MIN_ITEMS_INDUSTRY_THRESHOLD:
            logging.info("Number of survey results above MIN_ITEMS_INDUSTRY_THRESHOLD for industry: {} tenant: {}".format(industry, tenant))  # noqa
            dmb, dmb_d = benchmark.calculate_group_benchmark(dmb_d_list, dimensions)
            logging.info("Calculated dmb: {} , dmb_d: {}".format(dmb, dmb_d))

        dmb_bp, dmb_d_bp = None, None
        if len(dmb_d_bp_list) >= settings.MIN_ITEMS_BEST_PRACTICE_THRESHOLD:
            logging.info("Number of survey results above MIN_ITEMS_BEST_PRACTICE_THRESHOLD for industry: {} tenant: {}".format(industry, tenant))  # noqa
            dmb_bp, dmb_d_bp = benchmark.calculate_best_practice(dmb_d_bp_list, dimensions)
            logging.info("Calculated dmb_bp: {} , dmb_d_bp: {} for best practice".format(dmb_bp, dmb_d_bp))

        IndustryBenchmark.objects.update_or_create(
            tenant=tenant,
            industry=industry,
            defaults={
                'dmb_value': dmb,
                'dmb_d_value': dmb_d,
                'dmb_bp_value': dmb_bp,
                'dmb_d_bp_value': dmb_d_bp,
            }
        )


def _format_type(value, dateformat="%Y/%m/%d %H:%M:%S"):
    if isinstance(value, datetime):
        return value.strftime(dateformat)
    if isinstance(value, Promise):
        return force_text(value)
    return str(value)


def export_tenant_data(title, data, survey_fields, survey_result_fields, share_with, dateformat="%Y/%m/%d %H:%M:%S"):
    """Export tenant data to Google Spreadsheet."""

    export_data = []
    survey_columns = sorted(survey_fields.keys())
    survey_result_columns = sorted(survey_result_fields.keys())

    survey_names = [_format_type(survey_fields.get(col), dateformat=dateformat) for col in survey_columns]
    survey_result_names = [_format_type(survey_result_fields.get(col), dateformat=dateformat)
                           for col in survey_result_columns]

    for v in data:
        survey_data = [_format_type(getattr(v, col), dateformat=dateformat) for col in survey_columns]
        survey_result_data = [''] * len(survey_result_columns)
        try:
            if v.last_survey_result:
                survey_result = v.last_survey_result
                dim_dict = survey_result.dmb_d
                if dim_dict:
                    survey_result_data = []
                    for col in survey_result_columns:
                        dim = dim_dict.get(col)
                        if dim:
                            survey_result_data.append(dim)
                        else:
                            survey_result_data.append(_format_type(getattr(survey_result, col), dateformat=dateformat))
        except SurveyResult.DoesNotExist:
            # In case we have a survey, but has not been completed yet
            pass
        export_data.append(survey_data + survey_result_data)

    sheet_url = sheets.export_data(title, survey_names + survey_result_names, export_data, share_with)
    logging.info("Export created {} and shared with: {}".format(sheet_url, share_with))
