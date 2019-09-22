from django.conf import settings
from djangae import deferred
from core.models import Survey, SurveyResult, User
import logging

import unicodecsv as csv
from datetime import datetime
from django.utils.timezone import make_aware
import pytz
from core.conf import utils
from django.db import IntegrityError
from django.core.exceptions import MultipleObjectsReturned


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

        file_data = {}

        for row in reader:

            company_name = row['parent']
            country = row['country']
            industry = INDUSTRY_MAP[row['sector']]
            ldap = row['ldap']
            account_id = None

            if row['greentea_fix'] and row['greentea_fix'] != 'undefined':
                account_id = row['greentea_fix']
            elif row['greentea']:
                account_id = row['greentea']
            else:
                logging.warning("Could not set greentea id for {}, `None` will be used.".format(company_name))

            date = make_aware(datetime.strptime(row['timestamp'], '%d/%m/%Y %H:%M:%S'), pytz.timezone('GMT'))  # noqa

            row_data = {
                "company_name": company_name,
                "country": country,
                "industry": industry,
                "ldap": ldap,
                "account_id": account_id,
                "date": date,
            }

            key = (company_name, account_id, country, industry)

            # if there is already an item and the new one has an older date override it
            dup_item = file_data.get(key)
            if dup_item:
                if date < dup_item["date"]:
                    file_data[key] = row_data
            else:
                file_data[key] = row_data

        # defer csv file in batches
        num_items = len(file_data)
        deferred_items = 0
        for c in utils.chunks(file_data.values(), 100):
            deferred_items += len(c)
            logging.info("Deferring {}/{}".format(deferred_items, num_items))
            deferred.defer(
                _import_row,
                c,
                _queue='migrations',
            )


def _import_row(data):
    tenant = "ads"
    added = 0
    updated = 0
    already_exist = 0
    for row in data:
        try:
            company_name = row["company_name"]
            country = row["country"]
            industry = row["industry"]
            ldap = row["ldap"]
            account_id = row["account_id"]
            date = row["date"]

            user = create_user_(ldap)
            try:
                s, created = Survey.objects.get_or_create(
                    company_name=company_name,
                    account_id=account_id,
                    country=country,
                    industry=industry,
                    defaults={
                        "tenant": tenant,
                        "creator": user,
                        "created_at": date,
                        "imported_from_dmb_lite": True,
                    }
                )
                if not created:
                    logging.info("An existing Account has been found")
                    s.existed_before_dmb_lite = True
                    already_exist += 1

                    if date < s.created_at:
                        logging.error("Updating: company name:{}  account_id: {} country: {}  industry: {}".format(company_name, account_id, country, industry))  # noqa
                        s.created_at = date
                        s.creator = user
                        updated += 1

                s.save()

                if s.pk not in user.accounts_ids:
                    user.accounts.add(s)
                    user.save()
                added += 1

            except IntegrityError as ie:
                logging.error("Raised: {} for survey: company name:{}  account_id: {} country: {}  industry: {}".format(ie, company_name, account_id, country, industry))  # noqa
            except MultipleObjectsReturned:
                logging.error("Multiple occurencies returned for survey: company name:{}  account_id: {} country: {}  industry: {}".format(company_name, account_id, country, industry))  # noqa
        except Exception as e:
            logging.error("".format(e))
    logging.info("Added: {}".format(added))
    logging.info("Already exist: {}".format(already_exist))
    logging.info("Updated: {}".format(updated))


def create_user_(ldap):
    email = '{}@google.com'.format(ldap.lower())
    user, _ = User.objects.get_or_create(email_lower=email, defaults={"email": email})

    return user


def link_surveys():
    for user in User.objects.all():
        surveys = Survey.objects.filter(engagement_lead=user.engagement_lead)
        for survey in surveys:
            if not survey.creator:
                survey.creator = user
                survey.save()
            if survey.sid not in user.accounts_ids:
                user.accounts.add(survey)
                user.save()


def delete_imported_data():
    Survey.objects.filter(imported_from_dmb_lite=True).delete()
