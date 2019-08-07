from django.conf import settings

from core.models import Survey
import logging


def migrate_to_dmblite_survey():
    # Enable all tenants since the Survey.save method will
    # error if a Survey is using a disabled tenant
    logging.info("Enabling cloud tenant")
    settings.ALL_TENANTS['cloud']['enabled'] = True
    settings.TENANTS = {k: v for k, v in settings.ALL_TENANTS.items() if v['enabled']}

    logging.info("Adding DMBLite fields to surveys")
    surveys = Survey.objects.all()
    logging.info("Found {} surveys to be converted".format(surveys.count()))
    for survey in surveys:
        survey.save()

    # Disable all tenants after task
    logging.info("Disabling cloud tenant")
    settings.ALL_TENANTS['cloud']['enabled'] = False
    settings.TENANTS = {k: v for k, v in settings.ALL_TENANTS.items() if v['enabled']}
