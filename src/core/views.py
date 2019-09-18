import logging

from django.http import HttpResponse

from djangae import deferred
from djangae.environment import task_or_admin_only

from core.management import migrations
from core.tasks import sync_qualtrics, generate_csv_export, calculate_industry_benchmark
from django.conf import settings
from django.shortcuts import render
import os


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
        'account_id',
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
        'account_id',
    ]

    publishers_survey_result_fields = [
        'strategic_direction',
        'reader_engagement',
        'reader_revenue',
        'advertising_revenue',
    ]

    retail_survey_fields = [
        'id',
        'company_name',
        'industry',
        'country',
        'created_at',
        'engagement_lead',
        'tenant',
        'excluded_from_best_practice',
        'dmb',
        'account_id',
    ]

    retail_survey_result_fields = [
        'strategic_direction',
        'user_engagement',
        'core_sales',
        'emerging_monetization',
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

    deferred.defer(
        generate_csv_export,
        settings.RETAIL,
        retail_survey_fields,
        retail_survey_result_fields,
        settings.RETAIL,
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


def receive_bounce(request, *args, **kwargs):
    if request.method != 'POST':
        return HttpResponse(status=405)
    original_to, original_from = request.POST['original-to'], request.POST['original-to']
    logging.error('Email bounced back original-to: {} , original-from: {}'.format(original_to, original_from))
    logging.error('Email bounced back original-text: {}'.format(request.POST['original-text']))
    return HttpResponse(status=200)


@task_or_admin_only
def resave_surveys_task(request):
    msg = "resave surveys"
    logging.info(msg)

    deferred.defer(
        migrations.resave_surveys,
        _queue='default',
    )

    return HttpResponse(msg)


@task_or_admin_only
def drop_search_index_task(request):
    msg = "drop_search_index"
    logging.info(msg)

    deferred.defer(
        migrations.drop_search_index,
        _queue='default',
    )

    return HttpResponse(msg)


@task_or_admin_only
def import_lite_users_and_accounts(request):
    msg = "Migrating users and accounts from csv"
    logging.info(msg)

    filename_emea = os.path.join(settings.BASE_DIR, "core/management/tests/dmb_lite_csv.csv")

    deferred.defer(
        migrations.import_dmb_lite,
        filename_emea,
        _queue='migrations',
    )

    return HttpResponse(msg)


@task_or_admin_only
def link_surveys_task(request):
    msg = "Lnking surveys to creators"
    logging.info(msg)

    deferred.defer(
        migrations.link_surveys,
        _queue='default',
    )

    return HttpResponse(msg)
