from django.conf import settings

from core.models import Survey, IndustryBenchmark


def migrate_to_default_tenant():
    default_tenant = settings.DEFAULT_TENANT

    Survey.objects.update(tenant=default_tenant)


def migrate_deloitte_data():

    DIMENSION_TITLES = {
        'strategic_choices': 'Strategic choices and Ambition for data',
        'audience_engagement': 'Audience Engagement',
        'consumer_revenue': 'Consumer Revenue',
        'advertising_revenue': 'Advertising Revenue',
    }

    dmb = 2.45
    dmb_bp = 3.65
    samples = 46
    dmb_d = {
        'strategic_choices': 2.86,
        'audience_engagement': 2.3,
        'consumer_revenue': 2.0,
        'advertising_revenue': 2.2,
    }

    dmb_d_bp = {
        'strategic_choices': 4.0,
        'audience_engagement': 3.7,
        'consumer_revenue': 3.55,
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
