from django.core.urlresolvers import resolve
from django.conf import settings
from django.http import Http404
from django.shortcuts import redirect
from django.template.exceptions import TemplateDoesNotExist


class RedirectToDefaultTenant(object):

    def process_request(self, request, *args, **kwargs):
        match = resolve(request.path)
        url = match.url_name

        match_in_legacy_namespace = 'legacy' in match.namespaces
        if match_in_legacy_namespace:
            match.kwargs.update({'tenant': settings.ADS})
            return redirect(url, *match.args, **match.kwargs)

    def process_exception(self, request, exception):
        if isinstance(exception, TemplateDoesNotExist):
            raise Http404
