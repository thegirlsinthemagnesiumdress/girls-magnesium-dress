from django.conf import settings
from djangae.db import transaction
from django.core.management.base import BaseCommand
from core.models import IndustryBenchmark
from core.tests.mommy_recepies import make_survey, make_survey_result

import numpy
import logging


SAMPLE_DMB_D = {
    'ads': {
        "organization": 2.1,
        "attribution": 1.6,
        "access": 2.3,
        "ads": 3.7,
        "audience": 0.6,
        "automation": 2.0
    },
    'retail': {
        "emerging_monetization": 1.6,
        "user_engagement": 2.0,
        "core_sales": 3.0,
        "strategic_direction": 0.95
    },
    'news': {
        "reader_revenue": 1.2,
        "reader_engagement": 2.8,
        "strategic_direction": 3.5,
        "advertising_revenue": 0.9
    },
    'cloud': {
        "learn": 1.2,
        "lead": 0.8,
        "scale": 3.5,
        "secure": 2.9
    }
}

INITIAL_INDUSTRY_BENCHMARKS = {
    'ads': {
        "organization": 2.5,
        "attribution": 1,
        "access": 3.2,
        "ads": 3,
        "audience": 1,
        "automation": 2.0
    },
    'retail': {
        "emerging_monetization": 1.5,
        "user_engagement": 2.4,
        "core_sales": 3.0,
        "strategic_direction": 1.3
    },
    'news': {
        "reader_revenue": 1,
        "reader_engagement": 3,
        "strategic_direction": 2.3,
        "advertising_revenue": 1.4
    },
    'cloud': {
        "learn": 1.5,
        "lead": 0.5,
        "scale": 3,
        "secure": 2.6
    }
}

BP_INDUSTRY_BENCHMARKS = {
    'ads': {
        "organization": 3.5,
        "attribution": 2,
        "access": 3.8,
        "ads": 3.5,
        "audience": 2,
        "automation": 3.0
    },
    'retail': {
        "emerging_monetization": 2.5,
        "user_engagement": 3.4,
        "core_sales": 3.5,
        "strategic_direction": 2.3
    },
    'news': {
        "reader_revenue": 2,
        "reader_engagement": 3,
        "strategic_direction": 2.8,
        "advertising_revenue": 1.9
    },
    'cloud': {
        "learn": 2.5,
        "lead": 1.5,
        "scale": 3,
        "secure": 2.9
    }
}


class Command(BaseCommand):
    help = 'Generates sample surveys and survey results'

    def handle(self, *args, **options):
        tenants = settings.TENANTS
        for tenant in tenants.keys():
            # Create a blank survey to tie the results to.
            with transaction.atomic(xg=True):
                survey = make_survey(company_name='ACME Corp.', tenant=tenant)
                # Create sample survey result
                dmb_d = SAMPLE_DMB_D[tenant]
                dmb = numpy.average(dmb_d.values())
                result = make_survey_result(survey=survey, dmb=dmb, dmb_d=dmb_d)
                # Explicitly links the result to the survey as this isn't always completed.
                survey.last_survey_result = result
                survey.save()
                logging.info('Created survey and result for {} with id {}'.format(tenant, survey.sid))

            # Create a mock industry benchmark for this tenant.
            initial_benchmark_dmb_d = INITIAL_INDUSTRY_BENCHMARKS[tenant]
            bp_benchmark_dmb_d = BP_INDUSTRY_BENCHMARKS[tenant]
            initial_benchmark_dmb = numpy.average(initial_benchmark_dmb_d.values())
            bp_benchmark_dmb = numpy.average(bp_benchmark_dmb_d.values())
            IndustryBenchmark.objects.update_or_create(
                industry=survey.industry,
                tenant=tenant,
                defaults={
                    'dmb_value': initial_benchmark_dmb,
                    'dmb_d_value': initial_benchmark_dmb_d,
                    'dmb_bp_value': bp_benchmark_dmb,
                    'dmb_d_bp_value': bp_benchmark_dmb_d
                }
            )
            logging.info('Created industry benchmark for tenant {}'.format(tenant))
