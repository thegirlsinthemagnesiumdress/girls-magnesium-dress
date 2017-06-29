
from core.settings.default import *

INSTALLED_APPS = tuple(list(INSTALLED_APPS) + [
    'debug_toolbar',
])

MIDDLEWARE_CLASSES = tuple([
    'core.middleware.ProfileMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware'
] + list(MIDDLEWARE_CLASSES))

INTERNAL_IPS = [
    '127.0.0.1',
    '::1'
]

# This is just to allow the inline styles on Django error pages when DEBUG = True
# this settings file won't be used on production only during local development
CSP_STYLE_SRC = ("'self'", "'unsafe-inline'")

CHROMEDRIVER_PATH = os.path.join(NODE_PREFIX, "node_modules", ".bin", "chromedriver")
JASMINE_NODE_PATH = os.path.join(NODE_PREFIX, "node_modules", "jasmine-node", "lib", "jasmine-node", "cli.js")
BABEL_NODE_PATH = os.path.join(NODE_PREFIX, "node_modules", ".bin", "babel-node")
