from django.core.management.base import BaseCommand
from core.models import Survey, SurveyResult
from djangae.db import transaction
from django.db import IntegrityError
from django.utils import timezone


tenant = 'ads'
dmb_d = {
    "organization": 2.1,
    "attribution": 1.6,
    "access": 2.3,
    "ads": 3.7,
    "audience": 0.6,
    "automation": 2.0,
}

dmb = 3.6


def create_surveys(quantity):
    for i in range(quantity):
        with transaction.atomic(xg=True):
            company_name = 'ACME Corp. {}'.format(i)
            try:
                survey = Survey.objects.create(company_name=company_name, tenant=tenant, country='IT', industry='edu')
                result = SurveyResult.objects.create(survey=survey, dmb=dmb, dmb_d=dmb_d, started_at=timezone.now(), response_id='R_xxxxx{}'.format(i))
                survey.last_survey_result = result
                survey.save()
                print("Company:  {}  created".format(company_name))
            except IntegrityError:
                pass


class Command(BaseCommand):
    help = 'Create a number of dummy surveys'

    def add_arguments(self, parser):
        parser.add_argument('quantity')

    def handle(self, *args, **options):
        quantity = int(options['quantity'])
        create_surveys(quantity)
