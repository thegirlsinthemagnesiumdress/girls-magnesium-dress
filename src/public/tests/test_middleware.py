from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.test.client import RequestFactory

from djangae.test import TestCase
from core.tests import mocks
from django.test import override_settings
from core.test import reload_urlconf
from public.middleware import RedirectToDefaultTenant


@override_settings(
    TENANTS=mocks.MOCKED_TENANTS,
    I18N_TENANTS=mocks.MOCKED_I18N_TENANTS,
    NOT_I18N_TENANTS=mocks.MOCKED_NOT_I18N_TENANTS,
    TENANTS_SLUG_TO_KEY=mocks.MOCKED_TENANTS_SLUG_TO_KEY,
    DEFAULT_TENANT='tenant1',
)
class TestRedirectToDefaultTenantMiddleware(TestCase):

    @classmethod
    def tearDownClass(cls):
        super(TestRedirectToDefaultTenantMiddleware, cls).tearDownClass()
        reload_urlconf()

    @classmethod
    def setUpClass(cls):
        super(TestRedirectToDefaultTenantMiddleware, cls).setUpClass()
        reload_urlconf()

    def setUp(self):
        self.middleware = RedirectToDefaultTenant()
        self.factory = RequestFactory()

    def test_process_request_redirects_if_legacy_url(self):
        legacy_url = reverse('legacy:reports')
        request = self.factory.get(legacy_url)

        response = self.middleware.process_request(request)

        self.assertIsInstance(response, HttpResponseRedirect)
        self.assertEqual(response.url, reverse('reports', kwargs={'tenant': 'tenant1-slug'}))

    def test_process_request_no_redirect_if_url_with_tenant(self):
        url_with_tenant = reverse('reports', kwargs={'tenant': 'tenant1-slug'})
        request = self.factory.get(url_with_tenant)

        response = self.middleware.process_request(request)

        self.assertIsNone(response)
