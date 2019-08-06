from django.conf import settings

from core.models import Survey, IndustryBenchmark, SurveyDefinition
import logging


def migrate_to_default_tenant():
    default_tenant = settings.DEFAULT_TENANT

    Survey.objects.update(tenant=default_tenant)
    SurveyDefinition.objects.update(tenant=default_tenant)


def migrate_deloitte_data():

    dmb = 1.76
    dmb_bp = 3.65
    samples = 46
    dmb_d = {
        'strategic_direction': 2.23,
        'reader_engagement': 1.81,
        'reader_revenue': 1.56,
        'advertising_revenue': 1.75,
    }

    dmb_d_bp = {
        'strategic_direction': 4.0,
        'reader_engagement': 3.7,
        'reader_revenue': 3.55,
        'advertising_revenue': 3.5,
    }

    IndustryBenchmark.objects.create(
        tenant=settings.NEWS,
        industry='ic-bnpj',
        initial_dmb=dmb,
        initial_dmb_d=dmb_d,
        initial_best_practice=dmb_bp,
        initial_best_practice_d=dmb_d_bp,
        dmb_value=dmb,
        dmb_d_value=dmb_d,
        dmb_bp_value=dmb_bp,
        dmb_d_bp_value=dmb_d_bp,
        sample_size=samples,
    )


def migrate_to_tenant(old_tenant, new_tenant):
    logging.info("Migrating from tenant {} to {}".format(old_tenant, new_tenant))
    old_tenants = Survey.objects.filter(tenant=old_tenant)
    logging.info("Found {} with tenant {}".format(old_tenants.count(), old_tenant))
    updated = old_tenants.update(tenant=new_tenant)
    logging.info("{} updated to tenant {}".format(updated, new_tenant))


def migrate_to_dmblite_survey():
    # Ensure that all tenants with stored surveys are enabled before running this migration
    logging.info("Adding DMBLite fields to surveys")
    surveys = Survey.objects.all()
    logging.info("Found {} surveys to be converted".format(surveys.count()))
    for survey in surveys:
        survey.save()
