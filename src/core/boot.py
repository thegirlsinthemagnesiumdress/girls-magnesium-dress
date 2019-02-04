import sys
from os.path import dirname, abspath, join, exists

PROJECT_DIR = dirname(dirname(abspath(__file__)))
SITEPACKAGES_DIR = join(PROJECT_DIR, "sitepackages")
SITEPACKAGES_LOCAL_DIR = join(PROJECT_DIR, "sitepackages_local")
APPENGINE_DIR = join(SITEPACKAGES_DIR, "google_appengine")


def fix_path():
    if exists(APPENGINE_DIR) and APPENGINE_DIR not in sys.path:
        sys.path.insert(1, APPENGINE_DIR)

    # This must be added before the main sitepackages dir (so that it ends up after it in sys.path)
    # because it contains some duplicate packages (due to dependencies), so we want our "proper"
    # sitepackages folder to come first and this one to come second, so that the duplicates do not
    # take precedence.
    # On production this folder shouldn't exist because `skip_files` should remove it.
    if exists(SITEPACKAGES_LOCAL_DIR) and SITEPACKAGES_LOCAL_DIR not in sys.path:
        sys.path.insert(1, SITEPACKAGES_LOCAL_DIR)

    if SITEPACKAGES_DIR not in sys.path:
        sys.path.insert(1, SITEPACKAGES_DIR)


def get_app_config():
    """Returns the application configuration, creating it if necessary."""
    from django.utils.crypto import get_random_string
    from google.appengine.ext import ndb

    class Config(ndb.Model):
        """A simple key-value store for application configuration settings."""
        secret_key = ndb.StringProperty()
        qualtrics_api_token = ndb.StringProperty()

    # Create a random SECRET_KEY
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'

    @ndb.transactional()
    def txn():
        # Get or create the Config in a transaction, so that if it doesn't exist we don't get 2
        # threads creating a Config object and one overwriting the other
        key = ndb.Key(Config, 'config')
        entity = key.get(use_cache=False)
        if not entity:
            entity = Config(key=key)
            entity.secret_key = get_random_string(50, chars)
            entity.qualtrics_api_token = ''
            entity.put()
        # add `qualtrics_api_token` as field if it's not there,
        # used to migrate the token as config field
        if not entity.qualtrics_api_token:
            entity.qualtrics_api_token = ''
            entity.put()
        return entity
    return txn()


def patch_sdk_logging():
    """ The local App Engine SDK logs every attempt to access files/folders outside of the
        project directory, which happens with every call to os.path.realpath. This causes heavy
        logging in the terminal and drastically slows down the local server.
        This patches that logging call out of the way, to bring less logging and more joy.
    """

    from google.appengine.tools.devappserver2.python import stubs

    def _log_access_check_fail_replacement(filename):
        return

    stubs.log_access_check_fail = _log_access_check_fail_replacement
    print("Patched `log_access_check_fail` function in SDK to avoid excess logging.")
