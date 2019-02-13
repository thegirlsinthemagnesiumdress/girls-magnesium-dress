from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template.exceptions import TemplateDoesNotExist
from django.test.client import RequestFactory

from djangae.test import TestCase

from public.middleware import RedirectToDefaultTenant


class TestRedirectToDefaultTenantMiddleware(TestCase):

    def setUp(self):
        self.middleware = RedirectToDefaultTenant()
        self.factory = RequestFactory()

    def test_process_request_redirects_if_legacy_url(self):
        legacy_url = reverse('legacy:reports')
        request = self.factory.get(legacy_url)

        response = self.middleware.process_request(request)

        self.assertIsInstance(response, HttpResponseRedirect)
        self.assertEqual(response.url, reverse('reports', kwargs={'tenant': settings.ADS}))

    def test_process_request_no_redirect_if_url_with_tenant(self):
        url_with_tenant = reverse('reports', kwargs={'tenant': settings.ADS})
        request = self.factory.get(url_with_tenant)

        response = self.middleware.process_request(request)

        self.assertIsNone(response)

    def test_process_exception_returns_404_on_template_does_not_exist(self):
        request = self.factory.get('/')

        with self.assertRaises(Http404):
            self.middleware.process_exception(request, TemplateDoesNotExist(''))
