from django.http import HttpResponse
from core.tasks import get_results
from djangae import deferred
import logging
from djangae.environment import task_or_admin_only


@task_or_admin_only
def sync_qualtrics_results(request):
    """Download new survey results using Qualtrics API."""
    msg = "Getting results from Qualtrics API started"
    logging.info(msg)

    deferred.defer(
        get_results,
        _queue='default',
    )

    return HttpResponse(msg)
