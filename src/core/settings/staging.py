# flake8: noqa
from core.settings.live import *
import os

MIDDLEWARE_CLASSES = tuple(
    list(MIDDLEWARE_CLASSES) +
    [
        'core.middleware.UsersRestrictionMiddleware',
    ])

ALLOWED_AUTH_DOMAINS = [
    'google.com',
    'potatolondon.com',
    'deloitte.corp-partner.google.com',
]

DJANGAE_CREATE_UNKNOWN_USER = True

DOMAIN = os.environ['HTTP_HOST']

# override QUALTRICS_SURVEY_ID for staging environment
ALL_TENANTS[ADS]['QUALTRICS_SURVEY_ID'] = 'SV_6igS0eu8kjbqV5H'
ALL_TENANTS[NEWS]['QUALTRICS_SURVEY_ID'] = 'SV_4JxgntrYg5uiMyp'
ALL_TENANTS[RETAIL]['QUALTRICS_SURVEY_ID'] = 'SV_b1OV8m7xVD337rD'
ALL_TENANTS[CLOUD]['QUALTRICS_SURVEY_ID'] = 'SV_eRioRXZ4UcKYpVj'
