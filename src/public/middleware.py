from django.core.urlresolvers import resolve
from django.conf import settings
from django.http import Http404
from django.shortcuts import redirect
from django.template.exceptions import TemplateDoesNotExist
from core.conf.utils import get_tenant_key


class RedirectToDefaultTenant(object):

    def process_request(self, request, *args, **kwargs):
        match = resolve(request.path)
        url = match.url_name

        match_in_legacy_namespace = 'legacy' in match.namespaces
        if match_in_legacy_namespace:
            match.kwargs.update({'tenant': settings.TENANTS[settings.ADS].get('slug')})
            return redirect(url, *match.args, **match.kwargs)

    def process_view(self, request, view_func, view_args, view_kwargs):
        if 'tenant' in view_kwargs:
            view_kwargs.update({'tenant': get_tenant_key(view_kwargs['tenant'])})

    def process_exception(self, request, exception):
        if isinstance(exception, TemplateDoesNotExist):
            raise Http404
