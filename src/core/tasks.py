import logging

from core.models import Survey, SurveyResult
from core.qualtrics import benchmark, download, exceptions, question
from django.core import mail
from django.template.loader import get_template
from djangae.environment import application_id
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.shortcuts import reverse


CONTACT_EMAIL = "no-reply@{}.appspotmail.com".format(application_id())


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
        _create_survey_result(results.get('responses'))
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
        SurveyResult.objects.create(
            survey_id=data.get('sid'),
            response_id=data.get('ResponseID'),
            excluded_from_best_practice=excluded_from_best_practice,
            dmb=dmb,
            dmb_d=dmb_d,
        )
        try:
            s = Survey.objects.get(pk=data.get('sid'))
            s.industry = data.get('industry')
            s.save(update_fields=['industry'])
        except Survey.DoesNotExist:
            logging.warning('Could not update Survey with sid {}'.format(data.get('sid')))

        to, bcc = data.get('to'), data.get('bcc')
        if is_valid_email(to):
            link = reverse('report', kwargs={'sid': data.get('sid')})
            bcc = [bcc] if is_valid_email(bcc) else None
            send_mail_report(to=[to], bcc=bcc, context={'url': link})


def send_mail_report(to, bcc, context):
    """Send an email to everyone in the given `bcc`."""
    subject_template = get_template("core/response_ready_email_subject.txt")
    message_template = get_template("core/response_ready_email_body.txt")

    mail.EmailMessage(
        subject=subject_template.render(context).split("\n")[0],
        body=message_template.render(context),
        from_email=CONTACT_EMAIL,
        to=to,
        bcc=bcc
    ).send()


def is_valid_email(email):
    email_validator = EmailValidator()
    try:
        email_validator(email)
    except ValidationError:
        return False
    return True
