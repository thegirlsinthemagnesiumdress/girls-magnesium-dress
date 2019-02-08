from django.http import HttpResponse
from core.tasks import sync_qualtrics, generate_csv_export
from djangae import deferred
import logging
from djangae.environment import task_or_admin_only
from core.management import migrations


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
def migrate_to_tenant_task(request):
    """Migrate existing surveys to a specific tenant."""
    msg = "Migrate existing surveys to a specific tenant"
    logging.info(msg)

    deferred.defer(
        migrations.migrate_to_tenant,
        _queue='default',
    )

    return HttpResponse(msg)