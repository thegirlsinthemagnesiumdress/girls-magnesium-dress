from django.conf import settings

from core.models import Survey, IndustryBenchmark


def migrate_to_default_tenant():
    default_tenant = settings.DEFAULT_TENANT

    Survey.objects.update(tenant=default_tenant)


def migrate_deloitte_data():

    dmb = 2.45
    dmb_bp = 3.65
    samples = 46
    dmb_d = {
        'strategic_direction': 2.86,
        'reader_engagement': 2.3,
        'reader_revenue': 2.0,
        'advertising_revenue': 2.2,
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
        sample_size=samples,
    )
