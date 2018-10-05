
from core.settings.default import *

INSTALLED_APPS = tuple(list(INSTALLED_APPS) + [
    'debug_toolbar',
])

MIDDLEWARE_CLASSES = tuple([
    'debug_toolbar.middleware.DebugToolbarMiddleware'
] + list(MIDDLEWARE_CLASSES))

INTERNAL_IPS = [
    '127.0.0.1',
    '::1'
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# This is just to allow the inline styles on Django error pages when DEBUG = True
# this settings file won't be used on production only during local development
CSP_STYLE_SRC = ("'self'", "'unsafe-inline'", "https://fonts.googleapis.com")  + ("localhost:8000",)

# Enable this for Hot Module Replacement on development only
CSP_SCRIPT_SRC = CSP_SCRIPT_SRC + ("'unsafe-eval'", "localhost:8000",)
CSP_CONNECT_SRC = CSP_CONNECT_SRC + ("localhost:8000", "ws://localhost:8000")

CHROMEDRIVER_PATH = os.path.join(NODE_PREFIX, "node_modules", ".bin", "chromedriver")
JASMINE_NODE_PATH = os.path.join(NODE_PREFIX, "node_modules", "jasmine-node", "lib", "jasmine-node", "cli.js")
BABEL_NODE_PATH = os.path.join(NODE_PREFIX, "node_modules", ".bin", "babel-node")

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ALLOWED_HOSTS = [
    '*',
]

SUPER_USERS = ['pchillari@google.com']
