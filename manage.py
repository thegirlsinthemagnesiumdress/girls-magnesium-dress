#!/usr/bin/env python
import os
import sys

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
APPENGINE_DIR = os.path.join(PROJECT_DIR, "third_party", "google_appengine")

# We add the symlinked version of this folder, inside the GAE project folder, otherwise it's not
# accessible when running the local server because it's outside the sandbox
DEVELOPMENT_DIR = os.path.join(PROJECT_DIR, "src", "sitepackages_local")

sys.path[0:0] = [
    os.path.join(PROJECT_DIR, "src"),
    APPENGINE_DIR,
    DEVELOPMENT_DIR
]

from core.boot import fix_path, patch_sdk_logging
fix_path()
patch_sdk_logging()

_SERVICE_ACCOUNT_MISSING_CONF_MESSAGE = (
    "==============================================================\n"
    "WARNING: No keyfile found for the service account. See README.\n"
    "Spreadsheet functionality will be unavailable.\n"
    "==============================================================\n"
)

_SERVICE_ACCOUNT_INFO_MESSAGE = (
    "==============================================================\n"
    "Service account {service_email} enabled!\n"
    "NEVER STORE PII IN THIS SERVICE ACCOUNT! YOU HAVE BEEN WARNED!\n"
    "==============================================================\n"
)


def _configure_service_account():
    PEM_FILE = os.path.join(PROJECT_DIR, "src", "keys", "secret.pem")
    if not os.path.exists(PEM_FILE):
        print(_SERVICE_ACCOUNT_MISSING_CONF_MESSAGE)
        return {}

    EMAIL_ARG = "--appidentity_email_address"
    KEY_ARG = "--appidentity_private_key_path"
    SERVICE_EMAIL = "gweb-digitalmaturity-staging@appspot.gserviceaccount.com"

    # Look for all the parameters passed to manage.py
    param_search = [x.split("=")[0] for x in sys.argv]

    kwargs = {}

    # Add the email arg if it wasn't specified
    if EMAIL_ARG not in param_search:
        kwargs[EMAIL_ARG.lstrip("-")] = SERVICE_EMAIL

    # Add the keyfile arg if it wasn't specified
    if KEY_ARG not in param_search:
        kwargs[KEY_ARG.lstrip("-")] = "./keys/secret.pem"

    print(_SERVICE_ACCOUNT_INFO_MESSAGE.format(service_email=SERVICE_EMAIL))
    return kwargs


if __name__ == "__main__":
    # Make sure that if we are deploying and we don't specify any settings
    # that we use the live ones
    from djangae.core.management import execute_from_command_line
    from djangae.core.management import test_execute_from_command_line

    kwargs = {}
    if "deploy" in sys.argv and "--settings" not in sys.argv:
        print("NOTE: Using core.settings.live as we are deploying")
        os.environ["DJANGO_SETTINGS_MODULE"] = "core.settings.live"
        execute_from_command_line(sys.argv, **kwargs)
    elif "test" in sys.argv:
        print("NOTE: Using core.settings.local as we are testing")
        os.environ["DJANGO_SETTINGS_MODULE"] = "core.settings.local"
        test_execute_from_command_line(sys.argv)
    else:
        print("NOTE: Using core.settings.local as we are on local env")
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.local")
        kwargs = _configure_service_account()
        execute_from_command_line(sys.argv, **kwargs)
