import functools
import os
from importlib import import_module
from django.core.urlresolvers import clear_url_caches
from django.conf import settings
import sys
import shutil
import json

# App Engine login decorators


def _user_wrapper(func, email, admin, uid):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        original_email = os.environ.get("USER_EMAIL")
        original_admin = os.environ.get("USER_IS_ADMIN")
        original_user_id = os.environ.get("USER_ID")
        try:
            os.environ["USER_EMAIL"] = email
            os.environ["USER_IS_ADMIN"] = admin
            os.environ["USER_ID"] = uid

            return func(*args, **kwargs)
        finally:
            for param, value in (
                ("USER_EMAIL", original_email),
                ("USER_IS_ADMIN", original_admin),
                ("USER_ID", original_user_id)
            ):

                if value is None:
                    del os.environ[param]
                else:
                    os.environ[param] = value
    return wrapped


def with_appengine_admin(email):
    def with_appengine_dec(func):
        wrapped = _user_wrapper(
            func,
            email,
            "1",
            "".join(["9"] * 21)
        )

        return wrapped
    return with_appengine_dec


def with_appengine_user(email):
    def with_appengine_dec(func):
        wrapped = _user_wrapper(
            func,
            email,
            "0",
            "".join(["8"] * 21)
        )

        return wrapped
    return with_appengine_dec


def with_appengine_anon(func):
    wrapped = _user_wrapper(
        func,
        "", "", ""
    )

    return wrapped


class TempTemplateFolder(object):
    def __init__(self, dirname, filename):
        self.dirname = dirname
        self.filename = os.path.join(dirname, filename)

    def __enter__(self):
        if not os.path.exists(self.dirname):
            os.makedirs(self.dirname)

        return open(self.filename, 'w+b')

    def __exit__(self, exc_type, exc_value, traceback):
        os.remove(self.filename)
        if not os.listdir(self.dirname):
            shutil.rmtree(self.dirname)


def reload_urlconf():
    clear_url_caches()
    if settings.ROOT_URLCONF in sys.modules:
        reload(sys.modules[settings.ROOT_URLCONF])
    return import_module(settings.ROOT_URLCONF)


def get_bootstrap_data(context, field_name='bootstrap_data'):
    # We use django-angular-protect (see https://github.com/potatolondon/django-angular-protect)
    # which wraps our context values in an object.
    # This gets us at our original value.
    bootstrap_data = context.get(field_name)._original
    bootstrap_data = json.loads(bootstrap_data)
    return bootstrap_data
