from core.settings.live import *  # noqa

MIDDLEWARE_CLASSES = tuple(
    list(MIDDLEWARE_CLASSES) +
    [
        'core.middleware.DomainRestrictionMiddleware',
    ])

ALLOWED_AUTH_DOMAINS = [
    'google.com',
    'potatolondon.com',
]

QUALTRICS_SURVEY_ID = 'SV_beH0HTFtnk4A5rD'
