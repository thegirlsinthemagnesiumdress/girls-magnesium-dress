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

# explicitly disable tenant
ALL_TENANTS[CLOUD]['enabled'] = False

# explicitly set enabled LANGUAGES
LANGUAGES = [
    ('en', 'English'),
    ('es', 'Español'),
    ('it', 'Italiano'),
    ('pl', 'Polski'),
    ('tr', 'Türkçe'),
]


TENANTS = {k: v for k, v in ALL_TENANTS.items() if v['enabled']}

I18N_TENANTS = '|'.join([v['slug'] for k, v in TENANTS.items() if v['i18n']])
NOT_I18N_TENANTS = '|'.join([v['slug'] for k, v in TENANTS.items() if not v['i18n']])
ENABLED_TENANTS = '|'.join([v['slug'] for k, v in TENANTS.items()])


TENANTS_SLUG_TO_KEY = {v['slug']: k for k, v in TENANTS.items()}
TENANTS_CHOICES = [(k, v['label']) for k, v in TENANTS.items()]
