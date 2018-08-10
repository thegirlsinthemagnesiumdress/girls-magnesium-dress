from core.settings.default import *  # noqa


INSTALLED_APPS = tuple(list(INSTALLED_APPS) + [
    'debug_toolbar',
])

MIDDLEWARE_CLASSES = tuple(
    list(MIDDLEWARE_CLASSES) +
    [
        'core.middleware.DomainRestrictionMiddleware',
    ])

ALLOWED_AUTH_DOMAINS = [
    'google.com',
    'potatolondon.com',
]
