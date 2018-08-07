from core.settings.default import * # noqa

INSTALLED_APPS = tuple(list(INSTALLED_APPS) + [
    'debug_toolbar',
])

MIDDLEWARE_CLASSES = tuple([
    'core.middleware.WhitelistUser',
] + list(MIDDLEWARE_CLASSES))
