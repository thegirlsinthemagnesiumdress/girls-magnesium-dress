import functools
import os


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
