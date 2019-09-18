from django.conf import settings

from core.models import Survey, SurveyResult, User
import logging

import unicodecsv as csv
from datetime import datetime
from django.utils.timezone import make_aware
import pytz


INDUSTRY_MAP = {
    'Automotive': 'ma-v',
    'Retail': 'rt-o',
    'Healthcare': 'ma-p',
    'Education & Government': 'edu-o',
    'Technology': 'ma-e',
    'Services All Verticals': 'other',
    'Finance': 'fi-o',
    'Consumer Packaged Goods': 'ma-ctd',
    'Classifieds & Local': 'r-mc',
    'Business & Industrial Markets': 'ma-me',
    'Travel': 'tt-o',
    'Media & Entertainment': 'aer',
    'Consumer, Government & Entertainment': 'other',
    'GCAS - Global': 'other',
    'Integrated Solutions': 'other',
    'Multichannel Solutions': 'other',
    'Services & Distribution Solutions': 'other',
    '': 'other',
}


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


def import_dmb_lite(filename):
    with open(filename, 'rb') as csvfile:
        reader = csv.DictReader(csvfile)

        # exclude the next 3 lines as part of "headers"
        reader.next()
        reader.next()
        reader.next()

        tenant = "ads"
        added = 0
        updated = 0

        for row in reader:

            try:
                company_name = row['parent']
                country = row['country']
                industry = INDUSTRY_MAP[row['sector']]
                user = create_user_(row['ldap'])
                account_id = None

                if row['greentea_fix'] and row['greentea_fix'] != 'undefined':
                    account_id = row['greentea_fix']
                elif row['greentea']:
                    account_id = row['greentea']
                else:
                    logging.warning("Could not set greentea id for {}, `None` will be used.".format(company_name))

                date = make_aware(datetime.strptime(row['timestamp'], '%d/%m/%Y %H:%M:%S'), pytz.timezone('US/Mountain'))  # noqa

                existing_accounts = Survey.objects.filter(
                    company_name=company_name,
                    account_id=account_id,
                    country=country,
                    industry=industry
                )

                # if it doesn't yet exists
                if existing_accounts.count() == 0:
                    logging.info("Creating company name: {} greentea id: {}  creator: {}".format(company_name.encode('utf-8'), row['greentea'], row['ldap']))  # noqa
                    s = Survey(
                        company_name=company_name,
                        industry=industry,
                        country=country,
                        tenant=tenant,
                        account_id=account_id,
                        creator=user,
                        created_at=date,
                        imported_from_dmb_lite=True,
                    )
                # if it exists
                else:
                    logging.info("An existing Account has been found")
                    s = existing_accounts[0]
                    s.existed_before_dmb_lite = True
                    updated += 1

                # if row to be imported is older than the survey creation time
                if date < s.created_at:
                    logging.info("Updating survey with sid: {}".format(s.sid))
                    s.created_at = date
                    s.creator = user

                s.save()

                if s.pk not in user.accounts_ids:
                    user.accounts.add(s)
                    user.save()
                added += 1
            except Exception:
                logging.info("Creating company name: {} greentea id: {}  creator: {}  failed".format(company_name.encode('utf-8'), row['greentea'], row['ldap']))  # noqa

        logging.info("Imported {} surveys".format(added))
        logging.info("Updated {} surveys".format(updated))


def create_user_(ldap):
    email = '{}@google.com'.format(ldap.lower())
    user, _ = User.objects.get_or_create(email_lower=email, defaults={"email": email})

    return user


def link_surveys():
    for user in User.objects.all():
        surveys = Survey.objects.filter(engagement_lead=user.engagement_lead)
        for survey in surveys:
            survey.creator = user
            survey.save()
            if survey.sid not in user.accounts_ids:
                user.accounts.add(survey)
                user.save()
