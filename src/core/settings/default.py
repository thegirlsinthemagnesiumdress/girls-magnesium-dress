# flake8: noqa
# coding=utf-8
from djangae.settings_base import * #Set up some AppEngine specific stuff
from djangae.contrib.gauth.settings import *
from django.utils.translation import gettext_lazy as _

from djangae.environment import application_id

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

from core.boot import get_app_config
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_app_config().secret_key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '.appspot.com',
    '.withgoogle.com',
]

# Application definition

INSTALLED_APPS = (
    'archivable',
    'gulpify',
    'djangae',  # Djangae should be before Django core/contrib things
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'djangae.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'csp',
    'djangae.contrib.gauth_datastore',
    'djangae.contrib.security',
    'svg',
    'rest_framework',
    'rest_framework.authtoken',
    'angular',

    # Application
    'core',
    'public',
    'api',
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
    }
}

MIDDLEWARE_CLASSES = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'djangae.contrib.gauth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'djangae.contrib.security.middleware.AppEngineSecurityMiddleware',
    'djangae.contrib.common.middleware.RequestStorageMiddleware',
    'google.appengine.ext.appstats.recording.AppStatsDjangoMiddleware',
    'public.middleware.RedirectToDefaultTenant',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static', 'dev'),
]

STATIC_URL = '/devstatic/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'devstatic')

THIRD_PARTY = os.path.join(os.path.dirname(BASE_DIR), "third_party")
NODE_PREFIX = os.path.join(BASE_DIR, "..")

NG_OPENING_TAG = '{['
NG_CLOSING_TAG = ']}'
NG_APP_MARKER = 'angular-app'


def check_session_csrf_enabled():
    if "session_csrf.CsrfMiddleware" not in MIDDLEWARE_CLASSES:
        return ["SESSION_CSRF_DISABLED"]

    return []

check_session_csrf_enabled.messages = {"SESSION_CSRF_DISABLED": "Please add 'session_csrf.CsrfMiddleware' to MIDDLEWARE_CLASSES"}

SECURE_CHECKS = [
    "djangosecure.check.sessions.check_session_cookie_secure",
    "djangosecure.check.sessions.check_session_cookie_httponly",
    "djangosecure.check.djangosecure.check_security_middleware",
    "djangosecure.check.djangosecure.check_sts",
    "djangosecure.check.djangosecure.check_frame_deny",
    "djangosecure.check.djangosecure.check_ssl_redirect"
]

ROOT_URLCONF = 'core.urls'

WSGI_APPLICATION = 'core.wsgi.application'

PROJECT_ROOT = os.path.dirname(BASE_DIR)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--config={}'.format(os.path.join(PROJECT_ROOT, "tox.ini")),
]

NOSE_PLUGINS = [
    'nose.plugins.logcapture.LogCapture',
    'disabledoc.plugin.DisableDocstring',
    'noseprogressive.plugin.ProgressivePlugin',
    'djangae.noseplugin.DjangaePlugin',
]

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en'

LANGUAGES = [
    ('en', 'English'),
    ('es', 'Español'),
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

INTERNAL_IPS = [
    '127.0.0.1',
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
CSP_DEFAULT_SRC = ("'self'",)
CSP_STYLE_SRC = (
    "'self'",
    "https://fonts.googleapis.com",
    "'unsafe-inline'",  # Required by use angular ng-style.
)
CSP_FONT_SRC = ("'self'", "data:", "https://fonts.gstatic.com")
CSP_CHILD_SRC = ("'self'",)
CSP_SCRIPT_SRC = (
    "'self'",
    "https://www.google-analytics.com",
    "ajax.googleapis.com",
)
CSP_IMG_SRC = ("'self'", "data:", "https://www.google-analytics.com")
CSP_MEDIA_SRC = ("'self'",)
CSP_CONNECT_SRC = ("'self'",)


# Djangae-specific settings
DJANGAE_SIMULATE_CONTENTTYPES = True

# Fluent settings
FLUENT_EXTRA_IGNORE_PATTERNS = ['*/sitepackages/*', '*/third_party/*']

KEY_PREFIX = "%s-%s" % (application_id(), os.environ.get('CURRENT_VERSION_ID', ""))

# USER_SPECIFIC_URL_SECRET = get_app_config().user_specific_url_secret

AUTH_USER_MODEL = "core.User"

EMAIL_BACKEND = 'djangae.mail.AsyncEmailBackend'

DEFAULT_FILE_STORAGE = 'djangae.storage.CloudStorage'

FILE_UPLOAD_MAX_MEMORY_SIZE = 1024 * 1024 * 10
FILE_UPLOAD_HANDLERS = (
    'django.core.files.uploadhandler.MemoryFileUploadHandler',
)

DJANGAE_RUNSERVER_IGNORED_FILES_REGEXES = ['^.+$(?<!\.py)(?<!\.yaml)(?<!\.html)']
GENERATE_SPECIAL_INDEXES_DURING_TESTING = True

# We allow uploading videos, so the upload file size should be bigger than
# Django's default 2.5MB. We allow files up to 50MB.
FILE_UPLOAD_MAX_MEMORY_SIZE = 52428800

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'templates')],
    'OPTIONS': {
        'debug': DEBUG,
        'loaders': [
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
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
            "django.template.context_processors.request",
        )
    },
}]

SVG_DIRS = [
    os.path.join(STATIC_ROOT, 'img')
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
}

DJANGAE_RUNSERVER_IGNORED_DIR_REGEXES += [
    r"^third_party$",
    r"^sitepackages$",
    r"^sitepackages_local$",
    r"^node_modules$",
    r"^tests$",
    r"^static$"
]

DJANGAE_RUNSERVER_IGNORED_FILES_REGEXES += [
    r".+\.(?!py)[a-z]+$",  # Anything with an extension that does not START with .py
    r".+\.py.$",  # Anything with an extension of .pyX, e.g. pyc or pyo
]


AUTHENTICATION_BACKENDS = (
    'djangae.contrib.gauth_datastore.backends.AppEngineUserAPIBackend',
)
DJANGAE_CREATE_UNKNOWN_USER = True

APPEND_SLASH = True

RESPONSE_EXPORT_BASE_URL = 'https://{0}.qualtrics.com/API/v3/responseexports/'.format('google.co1')
QUALTRICS_SURVEY_BASE_URL = 'https://{0}.qualtrics.com/API/v3/surveys/'.format('google.co1')
QUALTRICS_REQUEST_DEADLINE = 60


from .constants import *
from .tenants import *
from .internal import *

QUALTRICS_API_TOKEN = get_app_config().qualtrics_api_token

QUALTRICS_BASE_SURVEY_URL = 'https://google.qualtrics.com/jfe/form/{survey_id}?sid={sid}'
QUALTRICS_BASE_SURVEY_PREVIEW_URL = 'https://google.qualtrics.com/jfe/preview/{survey_id}?sid={sid}&Q_SurveyVersionID=current'

MIN_ITEMS_INDUSTRY_THRESHOLD = 25
MIN_ITEMS_BEST_PRACTICE_THRESHOLD = 5


SURVEY_ADMIN_AUTHORIZED_DOMAINS = (
    '@google.com',
    '@potatolondon.com',
)

REVISIONED_STATIC = False

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]

CSRF_USE_SESSIONS = True

ANGULAR_TEMPLATES = [
    'dimension-tab-legacy',
    'dimension-tab',
    'progress-grid',
    'progress-grid-fallback',
    'progress-table',
]

ALLOWED_ANGULAR_TEMPLATES = '|'.join(ANGULAR_TEMPLATES)

QUALTRICS_LANGS = {
    'EN': 'en',
    'ES-ES': 'es',
}

QUALTRICS_LANGS_REV = { v: k for k, v in QUALTRICS_LANGS.items() }

HTTP_HOST = os.environ['HTTP_HOST']

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100
}

DOMAIN = os.environ['HTTP_HOST']
