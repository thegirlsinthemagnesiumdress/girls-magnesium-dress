from django.conf import settings
from djangae.db import transaction
from django.core.management.base import BaseCommand
from core.tests.mommy_recepies import make_survey, make_survey_result

import numpy
import random
import logging


class Command(BaseCommand):
    help = 'Generates sample surveys and survey results'

    def handle(self, *args, **options):
        tenants = settings.TENANTS
        for tenant in tenants.keys():
            # Create a blank survey to tie the results to.
            with transaction.atomic(xg=True):
                survey = make_survey(company_name='ACME Inc.', tenant=tenant)
                # Create sample survey result
                dimensions = tenants[tenant]['CONTENT_DATA']['dimensions']
                max_level = tenants[tenant]['CONTENT_DATA']['levels_max']
                dmb_d = {d: random.random() * max_level for d in dimensions}
                dmb = numpy.average(dmb_d.values())
                result = make_survey_result(survey=survey, dmb=dmb, dmb_d=dmb_d)
                survey.last_survey_result = result
                survey.save()
                logging.info('Created survey and result for {} with id {}'.format(tenant, survey.sid))
