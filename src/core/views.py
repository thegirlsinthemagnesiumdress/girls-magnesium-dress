import logging

from django.http import HttpResponse

from djangae import deferred
from djangae.environment import task_or_admin_only

from core.management import migrations
from core.tasks import sync_qualtrics, generate_csv_export, calculate_industry_benchmark
from django.conf import settings


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
def generate_export(request):
    """Generate surveys export from Datastore."""
    msg = "Generating surveys export from Datastore"
    logging.info(msg)

    deferred.defer(
        generate_csv_export,
        _queue='default',
    )

    return HttpResponse(msg)


@task_or_admin_only
def migrate_to_default_tenant_task(request):
    """Migrate existing surveys to the default tenant.

    The default tenant is ADS.
    """
    msg = "Migrate existing surveys to the default tenant"
    logging.info(msg)

    deferred.defer(
        migrations.migrate_to_default_tenant,
        _queue='default',
    )

    return HttpResponse(msg)


@task_or_admin_only
def migrate_to_tenant_task(request):
    """Migrate existing surveys from a tenant to another.

    The default tenant is ADS.
    """
    msg = "Migrate existing surveys to the default tenant"
    logging.info(msg)

    deferred.defer(
        migrations.migrate_to_tenant,
        'advertisers',
        settings.ADS,
        _queue='default',
    )

    return HttpResponse(msg)


@task_or_admin_only
def migrate_deloitte_data_task(request):
    """Migrate deafult values provided by Deloitte."""
    msg = "Migrate deafult values provided by Deloitte"
    logging.info(msg)

    deferred.defer(
        migrations.migrate_deloitte_data,
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
