from functools import wraps
from django.http import HttpResponseBadRequest


def ajax_required(func):
    @wraps(func)
    def wrapped(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest("AJAX only view")

        return func(request, *args, **kwargs)

    return wrapped
