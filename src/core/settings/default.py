from djangae.settings_base import * #Set up some AppEngine specific stuff
from djangae.contrib.gauth.settings import *

from django.utils.translation import ugettext_lazy as _
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

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Application definition

INSTALLED_APPS = (
    'archivable',
    'gulpify',
    'djangae', # Djangae should be before Django core/contrib things
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'djangae.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'djangosecure',
    'csp',
    'djangae.contrib.gauth_datastore',
    'djangae.contrib.security',
    'svg',

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
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'djangae.contrib.gauth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'csp.middleware.CSPMiddleware',
    'session_csrf.CsrfMiddleware',
    'djangae.contrib.security.middleware.AppEngineSecurityMiddleware',
    'djangosecure.middleware.SecurityMiddleware',
    'djangae.contrib.common.middleware.RequestStorageMiddleware',
    'google.appengine.ext.appstats.recording.AppStatsDjangoMiddleware'
)


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATIC_URL = '/devstatic/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'dev')

THIRD_PARTY = os.path.join(os.path.dirname(BASE_DIR), "third_party")
NODE_PREFIX = os.path.join(BASE_DIR, "..")


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

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--disable-docstring',
    '--progressive-bar-filled=4',
    '--progressive-function-color=4',
    '--with-coverage',
    '--cover-erase',
    '--cover-html',
    '--cover-html-dir=coverage_html',
    '--logging-level=CRITICAL'
]

NOSE_COVER_PACKAGES = [
    x for x in os.listdir(BASE_DIR)
    if (
        os.path.exists(os.path.join(BASE_DIR, x, "models.py")) or
        os.path.exists(os.path.join(BASE_DIR, x, "views.py")) or
        os.path.exists(os.path.join(BASE_DIR, x, "views"))
    )
]

for app in NOSE_COVER_PACKAGES:
    NOSE_ARGS.append('--cover-package=%s' % app)

if "--collect-only" not in sys.argv:
    NOSE_ARGS.append('--with-progressive')

NOSE_PLUGINS = [
    'nose.plugins.logcapture.LogCapture',
    'disabledoc.plugin.DisableDocstring',
    'noseprogressive.plugin.ProgressivePlugin',
    'djangae.noseplugin.DjangaePlugin',
    'core.test.WebdriverPlugin'
    # 'nose_exclude.NoseExclude'
]

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = [
    ('en-us', 'English'),
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
CSP_STYLE_SRC = ("'self'", "https://fonts.googleapis.com")
CSP_FONT_SRC = ("'self'", "data:", "https://fonts.gstatic.com/")
CSP_CHILD_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'",)
CSP_IMG_SRC = ("'self'", "data:")
CSP_MEDIA_SRC = ("'self'",)
CSP_CONNECT_SRC = ("'self'",)

if DEBUG:
    CSP_CONNECT_SRC += ("ws://127.0.0.1:35729/livereload",)
    CSP_SCRIPT_SRC += ("http://127.0.0.1:35729/livereload.js", "http://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js")


# Djangae-specific settings
DJANGAE_SIMULATE_CONTENTTYPES = True

# Fluent settings
FLUENT_EXTRA_IGNORE_PATTERNS = ['*/sitepackages/*', '*/third_party/*']

KEY_PREFIX = "%s-%s" % (application_id(), os.environ.get('CURRENT_VERSION_ID', ""))

USER_SPECIFIC_URL_SECRET = get_app_config().user_specific_url_secret

DJANGAE_CREATE_UNKNOWN_USER = False
AUTH_USER_MODEL = "core.User"

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

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

SVG_DIRS = [
    os.path.join(STATIC_ROOT, 'img')
]

DJANGAE_RUNSERVER_IGNORED_DIR_REGEXES += ['third_party', 'node_modules']

from .constants import *
