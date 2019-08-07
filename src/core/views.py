import logging

from django.http import HttpResponse

from djangae import deferred
from djangae.environment import task_or_admin_only

from core.management import migrations
from core.tasks import sync_qualtrics, generate_csv_export, calculate_industry_benchmark
from django.conf import settings
from django.shortcuts import render


@task_or_admin_only
def sync_qualtrics_results(request):
    """Download new survey results using Qualtrics API."""
    msg = "Getting results from Qualtrics API started"
    logging.info(msg)

    deferred.defer(
        sync_qualtrics,
        _queue='default',
    )

    return HttpResponse(msg)


@task_or_admin_only
def generate_exports_task(request):
    """Generate surveys exports from Datastore."""
    msg = "Generating surveys exports from Datastore"
    logging.info(msg)

    advertisers_survey_fields = [
        'id',
        'company_name',
        'industry',
        'country',
        'created_at',
        'engagement_lead',
        'tenant',
        'excluded_from_best_practice',
        'dmb',
    ]

    advertisers_survey_result_fields = [
        'access',
        'audience',
        'attribution',
        'ads',
        'organization',
        'automation',
    ]

    publishers_survey_fields = [
        'id',
        'company_name',
        'industry',
        'country',
        'created_at',
        'engagement_lead',
        'tenant',
        'excluded_from_best_practice',
        'dmb',
    ]

    publishers_survey_result_fields = [
        'strategic_direction',
        'reader_engagement',
        'reader_revenue',
        'advertising_revenue',
    ]

    deferred.defer(
        generate_csv_export,
        settings.ADS,
        advertisers_survey_fields,
        advertisers_survey_result_fields,
        settings.ADS,
        _queue='default',
    )

    deferred.defer(
        generate_csv_export,
        settings.NEWS,
        publishers_survey_fields,
        publishers_survey_result_fields,
        settings.NEWS,
        _queue='default',
    )

    return HttpResponse(msg)


@task_or_admin_only
def update_industries_benchmarks_task(request):
    """Update benchmarks for each industry, for each tenant."""
    msg = "Update industries benchmarks"
    logging.info(msg)

    for tenant in settings.TENANTS.keys():
        logging.info("Defer update task for {}".format(tenant))
        deferred.defer(
            calculate_industry_benchmark,
            tenant,
            _queue='default',
        )

    return HttpResponse(msg)


@task_or_admin_only
def update_survey_model_task(request):
    """Update survey models to incorperate new fields for DMBLite"""
    msg = "Update survey models"
    logging.info(msg)

    deferred.defer(
        migrations.migrate_to_dmblite_survey,
        _queue='default',
    )

    return HttpResponse(msg)


def angular_templates(request, template_name):
    return render(request, 'public/angular/{}.html'.format(template_name))
