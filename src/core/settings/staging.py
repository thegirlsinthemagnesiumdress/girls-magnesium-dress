from core.settings.live import *  # noqa
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

LIVE_DOMAIN = os.environ['HTTP_HOST']

# override QUALTRICS_SURVEY_ID for staging environment
TENANTS[ADS]['QUALTRICS_SURVEY_ID'] = 'SV_beH0HTFtnk4A5rD'
