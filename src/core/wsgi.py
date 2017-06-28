from core.boot import fix_path
fix_path()

import os
from django.core.wsgi import get_wsgi_application
from djangae.wsgi import DjangaeApplication
from djangae.environment import is_production_environment


if is_production_environment():
    settings = "core.settings.live"
else:
    settings = "core.settings.local"

os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)

application = DjangaeApplication(get_wsgi_application())
