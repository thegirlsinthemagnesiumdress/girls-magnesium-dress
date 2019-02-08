from django.core.urlresolvers import resolve
from django.shortcuts import redirect
from django.conf import settings
from django.http import Http404
from django.template.exceptions import TemplateDoesNotExist


class RedirectToDefaultTenant(object):

    def process_request(self, request, *args, **kwargs):
        view = resolve(request.path)
        current_url = resolve(request.path_info).url_name
        if current_url and 'legacy' in view.namespaces and not view.kwargs.get('tenant'):
            view.kwargs.update({'tenant': settings.ADS})
            return redirect(current_url, *view.args, **view.kwargs)

    def process_exception(self, request, exception):
        if isinstance(exception, TemplateDoesNotExist):
            raise Http404
