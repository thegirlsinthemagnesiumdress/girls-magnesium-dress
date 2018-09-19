import logging
import os

from core.models import Survey, SurveyResult
from core.qualtrics import benchmark, download, exceptions, question
from django.conf import settings
from django.core import mail
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.shortcuts import reverse
from django.template.loader import get_template
from djangae.db import transaction


def get_results():
    try:
        survey_result = SurveyResult.objects.latest('loaded_at')
        response_id = survey_result.response_id
        logging.info('Some Survey results has already been downloaded, partially download new results.')
    except SurveyResult.DoesNotExist:
        response_id = None
        logging.info('No Survey results has already been downloaded so far, download all the results.')

    try:
        results = download.fetch_results(response_id=response_id)
        responses = results.get('responses')
        _create_survey_result(responses)
        to_key, bcc_key = settings.QUALTRICS_EMAIL_TO, settings.QUALTRICS_EMAIL_BCC
        email_list = [(item.get(to_key), item.get(bcc_key), item.get('sid')) for item in responses]
        send_emails_for_new_reports(email_list)
    except exceptions.FetchResultException as fe:
        logging.error('Fetching results failed with: {}'.format(fe))


def _create_survey_result(results_data):
    """Create `SurveyResult` given a list of `result_data`.

    :param survey: `core.SurveyResult` which `results_data` refers to
    :param results_data: dictionary containing the downloaded response
        from Qualtrics API.
    """
    for data in results_data:
        questions = question.data_to_questions(data)
        dmb, dmb_d = benchmark.calculate_response_benchmark(questions)
        excluded_from_best_practice = question.discard_scores(data)
        with transaction.atomic(xg=True):
            survey_result = SurveyResult.objects.create(
                survey_id=data.get('sid'),
                response_id=data.get('ResponseID'),
                excluded_from_best_practice=excluded_from_best_practice,
                dmb=dmb,
                dmb_d=dmb_d,
            )
            try:
                s = Survey.objects.get(pk=data.get('sid'))
                s.last_survey_result = survey_result
                s.save(update_fields=['last_survey_result'])
            except Survey.DoesNotExist:
                logging.warning('Could not update Survey with sid {}'.format(data.get('sid')))


def send_emails_for_new_reports(email_list):
    """Send an email for every element of `email_list`.

    :param email_list: tuple of element (to, bcc, sid)
    """
    domain = os.environ['HTTP_HOST']
    subject_template = get_template("core/response_ready_email_subject.txt")
    html_message_template = get_template("core/response_ready_email_body.html")
    text_message_template = get_template("core/response_ready_email_body.txt")


    for email_data in email_list:
        to, bcc, sid = email_data
        # Last minute change, we should refactor this and pass the object in
        s = Survey.objects.get(pk=sid)
        if is_valid_email(to):
            link = reverse('report', kwargs={'sid': sid})
            bcc = [bcc] if is_valid_email(bcc) else None
            context = {
                'url': "http://{}{}".format(domain, link),
                'company_name': s.company_name,
                'industry': s.get_industry_display(),
                'country': s.get_country_display(),
            }

            message = mail.EmailMultiAlternatives(
                subject=subject_template.render(context).split("\n")[0],
                from_email=settings.CONTACT_EMAIL,
                to=[to],
                bcc=bcc
            )
            message.body = text_message_template
            message.html = html_message_template

            message.send()

            logging.info("Email sent to {} from {} for Survey with sid={}".format(to, settings.CONTACT_EMAIL, sid))


def is_valid_email(email):
    email_validator = EmailValidator()
    try:
        email_validator(email)
    except ValidationError:
        return False
    return True
