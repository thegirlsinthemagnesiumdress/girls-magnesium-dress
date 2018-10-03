from functools import wraps

from django.core.exceptions import PermissionDenied
from django.conf import settings


def survey_admin_required(view_func):
    """
    Decorator for views that checks that the user has enough permissions to see
    the view. Authorised domains are set in `settings.SURVEY_ADMIN_AUTHORIZED_DOMAINS`.
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.email.endswith(settings.SURVEY_ADMIN_AUTHORIZED_DOMAINS):
            return view_func(request, *args, **kwargs)
        raise PermissionDenied
    return _wrapped_view
