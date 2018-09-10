import os  # noqa

from core.boot import fix_path, patch_sdk_logging
fix_path()

from djangae.environment import is_production_environment, application_id  # noqa
from djangae.wsgi import DjangaeApplication  # noqa
from django.core.wsgi import get_wsgi_application  # noqa

if not is_production_environment():
    patch_sdk_logging()

if is_production_environment():
    if "staging" in application_id():
        settings = "core.settings.staging"
    else:
        settings = "core.settings.live"
else:
    settings = "core.settings.local"

os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)

application = DjangaeApplication(get_wsgi_application())
