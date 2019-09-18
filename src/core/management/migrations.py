from django.conf import settings

from core.models import Survey, SurveyResult, User
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
        try:
            survey.save()
        except AssertionError:
            logging.error("Something went wrong migrating survey {} ".format(survey.sid))

    for survey_result in SurveyResult.objects.all():
        survey_result.save()
    # Disable all tenants after task
    logging.info("Disabling cloud tenant")
    settings.ALL_TENANTS['cloud']['enabled'] = False
    settings.TENANTS = {k: v for k, v in settings.ALL_TENANTS.items() if v['enabled']}


def resave_surveys():
    for s in Survey.objects.all():
        try:
            s.save()
        except AssertionError:
            logging.error("Could not save {} ".format(s.sid))


def drop_search_index():
    from google.appengine.api import search
    for index in search.get_indexes(fetch_schema=True):
        logging.info("index %s", index.name)
        logging.info("schema: %s", index.schema)
        document_ids = [
            document.doc_id
            for document
            in index.get_range(ids_only=True)]
        index.delete(document_ids)
        index.delete_schema()


def link_surveys():
    for user in User.objects.all():
        surveys = Survey.objects.filter(engagement_lead=user.engagement_lead)
        for survey in surveys:
            survey.creator = user
            survey.save()
            if survey.sid not in user.accounts_ids:
                user.accounts.add(survey)
                user.save()
