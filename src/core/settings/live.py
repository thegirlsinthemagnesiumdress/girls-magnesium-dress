import os
from core.settings.default import *


SESSION_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 2592000 #30 days
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_FRAME_DENY = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True

SECURE_REDIRECT_EXEMPT = [
    # App Engine doesn't use HTTPS internally, so the /_ah/.* URLs need to be exempt.
    # djangosecure compares these to request.path.lstrip("/"), hence the lack of preceding /
    r"^_ah/",
    r"^cron/",
]

DEBUG = False
for template_config in TEMPLATES:
    template_config['OPTIONS']['debug'] = False

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'dist')

ALLOWED_HOSTS = [
    '.appspot.com'
]

EMAIL_BACKEND = 'djangae.mail.AsyncEmailBackend'

from google.appengine.api import app_identity

# Remove the appstats middleware on prod
if "test" not in app_identity.get_application_id():
    appstats_middleware = "google.appengine.ext.appstats.recording.AppStatsDjangoMiddleware"
    if appstats_middleware in MIDDLEWARE_CLASSES:
        middleware = list(MIDDLEWARE_CLASSES)
        middleware.remove(appstats_middleware)
        MIDDLEWARE_CLASSES = tuple(middleware)

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'templates')],
    'OPTIONS': {
        'debug': DEBUG,
        'loaders': [
            ('django.template.loaders.cached.Loader', [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ]),
        ],
        'context_processors': (
            "django.contrib.auth.context_processors.auth",
            "django.template.context_processors.debug",
            "django.template.context_processors.i18n",
            "django.template.context_processors.media",
            "django.template.context_processors.static",
            "django.template.context_processors.tz",
            "django.template.context_processors.request",
            "django.contrib.messages.context_processors.messages",
            "session_csrf.context_processor",
            "django.template.context_processors.request",
        )
    },
}]

# Disable REST Framework's browsable API in staging/production
REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = ('rest_framework.renderers.JSONRenderer',)
