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
]

QUALTRICS_SURVEY_ID = 'SV_beH0HTFtnk4A5rD'

DJANGAE_CREATE_UNKNOWN_USER = True

WHITELISTED_QUALTRICS_RESOURCES = (
    os.path.join(STATIC_URL, 'css/survey.css'),
    os.path.join(STATIC_URL, 'js/survey.min.js'),
)
