from djangae.test import TestCase
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from django.test import override_settings

from core.test import with_appengine_admin, with_appengine_user, get_bootstrap_data, with_appengine_anon
from core.tests.mommy_recepies import make_survey, make_survey_result, make_survey_with_result
from core.tests import mocks
from django.conf import settings
import os
from core.test import reload_urlconf, TempTemplateFolder, angular_context_to_object
import json
import mock
from core import tasks
from core.tests.mommy_recepies import make_user, make_survey_definition


@override_settings(
    TENANTS=mocks.MOCKED_TENANTS,
    I18N_TENANTS=mocks.MOCKED_I18N_TENANTS,
    NOT_I18N_TENANTS=mocks.MOCKED_NOT_I18N_TENANTS,
    TENANTS_SLUG_TO_KEY=mocks.MOCKED_TENANTS_SLUG_TO_KEY,
    DEFAULT_TENANT='tenant1',
)
class ReportsAdminTestCase(TestCase):
    """Tests for `reports_admin` view."""

    @classmethod
    def tearDownClass(cls):
        super(ReportsAdminTestCase, cls).tearDownClass()
        reload_urlconf()

    @classmethod
    def setUpClass(cls):
        super(ReportsAdminTestCase, cls).setUpClass()
        reload_urlconf()

    def setUp(self):
        self.url = reverse('accounts', kwargs={'tenant': 'tenant1-slug'})
        self.survey_1 = make_survey(tenant='tenant1')
        self.survey_2 = make_survey(tenant='tenant1')
        self.survey_3 = make_survey(tenant='tenant2')

        self.survey_result_1 = make_survey_result(
            survey=self.survey_1,
            response_id='AAA',
            dmb=1.0,
            dmb_d='{}'
        )

        self.survey_result_2 = make_survey_result(
            survey=self.survey_2,
            response_id='BBB',
            dmb=1.0,
            dmb_d='{}'
        )

    @with_appengine_user('test@google.com')
    def test_standard_user_logged_in(self):
        """Standard user can retrieve reports belonging to their account 'list' within a specific tenant."""

        self.user = get_user_model().objects.create(email='test@google.com')

        # set a survey to belong to logged user
        self.survey_1.engagement_lead = self.user.engagement_lead
        self.survey_1.creator = self.user
        self.survey_1.save()
        self.user.accounts.add(self.survey_1)
        self.user.save()

        templates_path = os.path.join(settings.BASE_DIR, 'public', 'templates', 'public', 'tenant1')
        with TempTemplateFolder(templates_path, 'accounts.html'):
            response = self.client.get(self.url)
            self.assertEqual(response.status_code, 200)

            bootstrap_data = get_bootstrap_data(response.context)
            surveys = bootstrap_data.get('results')

            self.assertTrue(surveys)
            self.assertEqual(len(surveys), 1)

    @with_appengine_admin('test@google.com')
    def test_whitelisted_user_logged_in(self):
        """Whitelisted user retrieve reports belonging to their account 'list' within that tenant."""
        self.user = get_user_model().objects.create(email='test@google.com')

        # set a survey to belong to logged user
        self.survey_1.engagement_lead = self.user.engagement_lead
        self.survey_1.creator = self.user
        self.survey_1.save()
        self.user.accounts.add(self.survey_1)
        self.user.save()

        templates_path = os.path.join(settings.BASE_DIR, 'public', 'templates', 'public', 'tenant1')
        with TempTemplateFolder(templates_path, 'accounts.html'):
            response = self.client.get(self.url)
            self.assertEqual(response.status_code, 200)
            bootstrap_data = get_bootstrap_data(response.context)
            surveys = bootstrap_data.get('results')

            self.assertTrue(surveys)
            self.assertEqual(len(surveys), 1)

    @with_appengine_admin('test@google.com')
    def test_whitelisted_user_logged_in_tenant_2(self):
        """Whitelisted user can retrieve reports belonging to all companies within that tenant."""
        self.user = get_user_model().objects.create(email='test@google.com')

        # set a survey to belong to logged user
        self.survey_3.engagement_lead = self.user.engagement_lead
        self.survey_3.creator = self.user
        self.survey_3.save()
        self.user.accounts.add(self.survey_3)
        self.user.save()

        url = reverse('accounts', kwargs={'tenant': 'tenant2-slug'})
        templates_path = os.path.join(settings.BASE_DIR, 'public', 'templates', 'public', 'tenant2')
        with TempTemplateFolder(templates_path, 'accounts.html'):
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            bootstrap_data = get_bootstrap_data(response.context)
            surveys = bootstrap_data.get('results')

            self.assertTrue(surveys)
            self.assertEqual(len(surveys), 1)

    def test_user_not_logged_in(self):
        """Anonymous user cannot retrieve any report."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(reverse('djangae_login_redirect') in response.get('Location'))

    @with_appengine_user('notenoughpermissions@gmail.com')
    def test_user_logged_in_not_in_permission_domains(self):
        """User could be logged in, but not having enough permissions to access to the resource."""
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 403)


@override_settings(
    TENANTS=mocks.MOCKED_TENANTS,
    I18N_TENANTS=mocks.MOCKED_I18N_TENANTS,
    NOT_I18N_TENANTS=mocks.MOCKED_NOT_I18N_TENANTS,
    INTERNAL_TENANTS=mocks.MOCKED_INTERNAL_TENANTS,
    TENANTS_SLUG_TO_KEY=mocks.MOCKED_TENANTS_SLUG_TO_KEY,
)
class ReportDetailTestCase(TestCase):
    """Tests for `report_static` view."""

    def setUp(self):
        reload_urlconf()
        self.tenant_slug = 'tenant2-slug'
        self.survey_1 = make_survey()
        self.survey_2 = make_survey()

        self.survey_result_1 = make_survey_result(
            survey=self.survey_1,
            response_id='AAA',
            dmb=1.0,
            dmb_d='{}'
        )
        self.internal_result_1 = make_survey_result(
            survey=self.survey_1,
            internal_survey=self.survey_1,
            response_id='BBB',
            dmb=1.0,
            dmb_d='{}'
        )
        self.survey_1.last_survey_result = self.survey_result_1
        self.survey_1.last_internal_result = self.internal_result_1
        self.survey_1.save()

    def test_survey_has_survey_result(self):
        """If a a`Survey` exists and it has a result, it should return 200."""
        templates_path = os.path.join(settings.BASE_DIR, 'public', 'templates', 'public', 'tenant2')
        with TempTemplateFolder(templates_path, 'report-static.html'):
            url = reverse('report', kwargs={'tenant': self.tenant_slug, 'sid': self.survey_1.sid})
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)

    def test_survey_has_internal_result(self):
        """If a survey exists and it has an internal result it should return 200."""
        templates_path = os.path.join(settings.BASE_DIR, 'public', 'templates', 'public', 'tenant2')
        with TempTemplateFolder(templates_path, 'report-internal.html'):
            url = reverse('report-internal', kwargs={'tenant': self.tenant_slug, 'sid': self.survey_1.sid})
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)

    def test_survey_does_not_exist(self):
        """If a a`Survey` does not exists it should raise 404."""
        with override_settings(
            TENANTS=mocks.MOCKED_TENANTS,
            TENANTS_SLUG_TO_KEY=mocks.MOCKED_TENANTS_SLUG_TO_KEY,
        ):

            url = reverse('report', kwargs={'tenant': self.tenant_slug, 'sid': '12345678890'})
            response = self.client.get(url)
            self.assertEqual(response.status_code, 404)

    def test_survey_does_not_have_a_result(self):
        """If a a`Survey` exists, but doesn't have a result, it should raise 404."""
        url = reverse('report', kwargs={'tenant': self.tenant_slug, 'sid': self.survey_2.sid})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_staging_context_variable(self):
        """Tests if the staging boolean is passed into the context to trigger the debug menu"""
        templates_path = os.path.join(settings.BASE_DIR, 'public', 'templates', 'public', 'tenant2')
        with TempTemplateFolder(templates_path, 'report-static.html'):
            url = reverse('report', kwargs={'tenant': self.tenant_slug, 'sid': self.survey_1.sid})
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.context['staging'], False)

    def test_survey_does_not_have_a_internal_result(self):
        """If a survey exists but doesnt have a result then a 404 should be raised."""
        url = reverse('report-internal', kwargs={'tenant': self.tenant_slug, 'sid': self.survey_2.sid})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)


@override_settings(
    TENANTS=mocks.MOCKED_TENANTS,
    I18N_TENANTS=mocks.MOCKED_I18N_TENANTS,
    NOT_I18N_TENANTS=mocks.MOCKED_NOT_I18N_TENANTS,
    TENANTS_SLUG_TO_KEY=mocks.MOCKED_TENANTS_SLUG_TO_KEY,
)
class IndexPage(TestCase):
    """Tests for the `index` view."""

    def setUp(self):
        reload_urlconf()
        self.tenant_slug = 'tenant1-slug'
        self.survey_1 = make_survey()
        self.survey_2 = make_survey()

        self.survey_result_1 = make_survey_result(
            survey=self.survey_1,
            response_id='AAA',
            dmb=1.0,
            dmb_d='{}'
        )
        self.survey_1.last_survey_result = self.survey_result_1
        self.survey_1.save()

    def test_custom_index_page(self):
        """If template exists should return 200."""
        templates_path = os.path.join(settings.BASE_DIR, 'public', 'templates', 'public', 'tenant1')
        with TempTemplateFolder(templates_path, 'index.html'):
            url = reverse('index', kwargs={'tenant': self.tenant_slug})
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)

    def test_index_page_exists(self):
        """Index page should always exist, and return 200."""
        templates_path = os.path.join(settings.BASE_DIR, 'public', 'templates', 'public', 'tenant1')
        with TempTemplateFolder(templates_path, 'index.html'):
            url = reverse('index', kwargs={'tenant': self.tenant_slug})
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)

    def test_index_footers_exists(self):
        """Dynamically generated footer links should be present, and not include current tennant."""
        templates_path = os.path.join(settings.BASE_DIR, 'public', 'templates', 'public', 'tenant1')
        with TempTemplateFolder(templates_path, 'index.html'):
            url = reverse('index', kwargs={'tenant': self.tenant_slug})
            response = self.client.get(url)
            other_tenants = angular_context_to_object(response.context['other_tenants'])
            # tenant-3 should be excluded because `in_dmb_footer` is False
            expected = [('Tenant 2 Footer Label', 'tenant2-slug')]
            self.assertListEqual(other_tenants, expected)


@override_settings(
    TENANTS=mocks.MOCKED_TENANTS,
    I18N_TENANTS=mocks.MOCKED_I18N_TENANTS,
    NOT_I18N_TENANTS=mocks.MOCKED_NOT_I18N_TENANTS,
    TENANTS_SLUG_TO_KEY=mocks.MOCKED_TENANTS_SLUG_TO_KEY,
)
class ThankyouPage(TestCase):
    """Tests for `thankyou` view."""

    def setUp(self):
        reload_urlconf()
        self.tenant_slug = 'tenant1-slug'
        self.survey_1 = make_survey()
        self.survey_2 = make_survey()

        self.survey_result_1 = make_survey_result(
            survey=self.survey_1,
            response_id='AAA',
            dmb=1.0,
            dmb_d='{}'
        )
        self.survey_1.last_survey_result = self.survey_result_1
        self.survey_1.save()

    def test_custom_thank_you_page(self):
        """If template exists should return 200."""
        templates_path = os.path.join(settings.BASE_DIR, 'public', 'templates', 'public', 'tenant1')
        with TempTemplateFolder(templates_path, 'thank-you.html'):
            url = reverse('thank-you', kwargs={'tenant': self.tenant_slug})
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)

    def test_thank_you_page_exists(self):
        """Thank you page should always exist, and return 200."""
        url = reverse('thank-you', kwargs={'tenant': 'tenant2-slug'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

@override_settings(
    TENANTS=mocks.MOCKED_TENANTS,
    I18N_TENANTS=mocks.MOCKED_I18N_TENANTS,
    NOT_I18N_TENANTS=mocks.MOCKED_NOT_I18N_TENANTS,
    TENANTS_SLUG_TO_KEY=mocks.MOCKED_TENANTS_SLUG_TO_KEY,
)
class ResultDetail(TestCase):
    """Tests for `thankyou` view."""

    def setUp(self):
        reload_urlconf()
        self.user = make_user(email='test@google.com')
        self.tenant_slug = 'tenant1-slug'
        self.survey_internal = make_survey()
        self.survey_external = make_survey()
        definition = make_survey_definition()

        self.survey_result_internal = make_survey_result(
            response_id='AAA',
            dmb=1,
            dmb_d={u"dim1": 0.4, u"dim2": 1.6},
            raw='{}',
            survey_definition=definition,
            completed_by=self.user,
            internal_survey=self.survey_internal,
        )

        self.survey_result_external = make_survey_result(
            response_id='BBB',
            dmb=1,
            dmb_d={u"dim1": 0.4, u"dim2": 1.6},
            raw='{}',
            survey_definition=definition,
            completed_by=self.user,
            survey=self.survey_internal,
        )

        self.survey_internal.last_survey_result = self.survey_result_internal
        self.survey_internal.save()
        self.survey_external.last_survey_result = self.survey_result_external
        self.survey_external.save()

    @with_appengine_user("test@google.com")
    @mock.patch('public.views.get_response_detail', return_value={})
    def test_result_detail_internal_page(self, mock_get_response):
        """Internal result detail page should always exist, and return 200 if result exists."""
        templates_path = os.path.join(settings.BASE_DIR, 'public', 'templates', 'public', 'tenant2')
        with TempTemplateFolder(templates_path, 'result-detail.html'):
            url = reverse('result-detail', kwargs={'tenant': 'tenant2-slug', 'response_id':self.survey_result_internal.response_id})
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)

    @with_appengine_user("test@gmail.com")
    @mock.patch('public.views.get_response_detail', return_value={})
    def test_result_detail_internal_page_forbidden(self, mock_get_response):
        """Internal result detail page should not be accessible if you aren't a survey admin"""
        templates_path = os.path.join(settings.BASE_DIR, 'public', 'templates', 'public', 'tenant2')
        with TempTemplateFolder(templates_path, 'result-detail.html'):
            url = reverse('result-detail', kwargs={'tenant': 'tenant2-slug', 'response_id':self.survey_result_internal.response_id})
            response = self.client.get(url)
            self.assertEqual(response.status_code, 403)

    @with_appengine_anon
    @mock.patch('public.views.get_response_detail', return_value={})
    def test_result_detail_internal_page_forbidden_anon(self, mock_get_response):
        """Internal result detail page should redirect if you're not logged in"""
        templates_path = os.path.join(settings.BASE_DIR, 'public', 'templates', 'public', 'tenant2')
        with TempTemplateFolder(templates_path, 'result-detail.html'):
            url = reverse('result-detail', kwargs={'tenant': 'tenant2-slug', 'response_id':self.survey_result_internal.response_id})
            response = self.client.get(url)
            self.assertEqual(response.status_code, 302)

    @with_appengine_user("test1@google.com")
    @mock.patch('public.views.get_response_detail', return_value={})
    def test_result_detail_internal_page_forbidden_not_completed_by(self, mock_get_response):
        """Internal result detail page should not be accessible by a user that didn't completed it """
        templates_path = os.path.join(settings.BASE_DIR, 'public', 'templates', 'public', 'tenant2')
        with TempTemplateFolder(templates_path, 'result-detail.html'):
            url = reverse('result-detail', kwargs={'tenant': 'tenant2-slug', 'response_id':self.survey_result_internal.response_id})
            response = self.client.get(url)
            self.assertEqual(response.status_code, 403)

    @with_appengine_user("test@google.com")
    @mock.patch('public.views.get_response_detail', return_value={})
    def test_result_detail_external_page(self, mock_get_response):
        """External result detail page should always exist, and return 200 if result exists."""
        templates_path = os.path.join(settings.BASE_DIR, 'public', 'templates', 'public', 'tenant2')
        with TempTemplateFolder(templates_path, 'result-detail.html'):
            url = reverse('result-detail', kwargs={'tenant': 'tenant2-slug', 'response_id':self.survey_result_external.response_id})
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)

    @with_appengine_user("test@gmail.com")
    @mock.patch('public.views.get_response_detail', return_value={})
    def test_result_detail_external_page_forbidden(self, mock_get_response):
        """External result detail page should not be accessible if you aren't a survey admin""""
        templates_path = os.path.join(settings.BASE_DIR, 'public', 'templates', 'public', 'tenant2')
        with TempTemplateFolder(templates_path, 'result-detail.html'):
            url = reverse('result-detail', kwargs={'tenant': 'tenant2-slug', 'response_id':self.survey_result_external.response_id})
            response = self.client.get(url)
            self.assertEqual(response.status_code, 403)

    @with_appengine_anon
    @mock.patch('public.views.get_response_detail', return_value={})
    def test_result_detail_external_page_forbidden_anon(self, mock_get_response):
        """External result detail page should redirect if you're not logged in"""
        templates_path = os.path.join(settings.BASE_DIR, 'public', 'templates', 'public', 'tenant2')
        with TempTemplateFolder(templates_path, 'result-detail.html'):
            url = reverse('result-detail', kwargs={'tenant': 'tenant2-slug', 'response_id':self.survey_result_external.response_id})
            response = self.client.get(url)
            self.assertEqual(response.status_code, 302)

    @with_appengine_user("test1@google.com")
    @mock.patch('public.views.get_response_detail', return_value={})
    def test_result_detail_external_page_forbidden_not_completed_by(self, mock_get_response):
        """External result detail page should always exist, and return 200 if result exists"""
        templates_path = os.path.join(settings.BASE_DIR, 'public', 'templates', 'public', 'tenant2')
        with TempTemplateFolder(templates_path, 'result-detail.html'):
            url = reverse('result-detail', kwargs={'tenant': 'tenant2-slug', 'response_id':self.survey_result_external.response_id})
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)


@override_settings(
    TENANTS=mocks.MOCKED_TENANTS,
    I18N_TENANTS=mocks.MOCKED_I18N_TENANTS,
    NOT_I18N_TENANTS=mocks.MOCKED_NOT_I18N_TENANTS,
    TENANTS_SLUG_TO_KEY=mocks.MOCKED_TENANTS_SLUG_TO_KEY,
)
class GenerateExportPage(TestCase):
    """Tests for `generate_spreadsheet_export` view."""

    def setUp(self):
        reload_urlconf()
        self.tenant_slug = 'tenant1-slug'
        self.survey_1 = make_survey_with_result(industry='ic-o', tenant='tenant1')
        self.survey_2 = make_survey_with_result(industry='ic-o', tenant='tenant1')
        self.survey_1.last_survey_result.dmb_d = {
            'access': 1.5,
            'audience': 1.3,
            'attribution': 1.6,
            'ads': 1.5,
            'organization': 2.0,
            'automation': 3.0,
        }
        self.survey_1.save()

        self.survey_2.last_survey_result.dmb_d = {
            'access': 2.5,
            'audience': 2.3,
            'attribution': 2.6,
            'ads': 2.5,
            'organization': 4.0,
            'automation': 3.0,
        }
        self.survey_2.save()

    def test_user_not_logged_in(self):
        """If a user is not logged in, it should return 302."""
        url = reverse('reports_export', kwargs={'tenant': self.tenant_slug})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)

    @with_appengine_user("test@google.com")
    def test_get_not_allowed(self):
        """Method GET should not be allowed, it returns 405."""
        url = reverse('reports_export', kwargs={'tenant': self.tenant_slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 405)

    @mock.patch('djangae.deferred.defer')
    @with_appengine_user("test@google.com")
    def test_engagement_lead_missing(self, mock_defer):
        """If enagagement lead parameter is missing, it returns an error."""
        url = reverse('reports_export', kwargs={'tenant': self.tenant_slug})
        response = self.client.post(url, data=json.dumps({}), content_type="application/json")
        self.assertEqual(response.status_code, 400)
        mock_defer.assert_not_called()

    @mock.patch('djangae.deferred.defer')
    @with_appengine_user("test@google.com")
    def test_standard_user(self, mock_defer):
        """If it's a standard user is_super_admin should be `False`"""
        engagement_lead = '1234'
        data = {
            'engagement_lead': engagement_lead
        }
        url = reverse('reports_export', kwargs={'tenant': self.tenant_slug})
        response = self.client.post(url, data=json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, 200)
        mock_defer.assert_called_once()
        args, kwargs = mock_defer.call_args
        got_func, got_title, got_tenant, got_is_super_admin, got_el, got_headers, got_rows, got_share_with = args
        self.assertEqual(got_func, tasks.export_tenant_data)
        self.assertTrue("Digital Maturity Benchmark | Data Export |" in got_title)
        self.assertEqual(got_tenant, 'tenant1')
        self.assertFalse(got_is_super_admin)
        self.assertNotEqual(got_el, engagement_lead)
        self.assertEqual(got_el, response.wsgi_request.user.engagement_lead)
        self.assertEqual(got_share_with, response.wsgi_request.user.email)

    @mock.patch('djangae.deferred.defer')
    @with_appengine_admin('standard@google.com')
    def test_super_admin(self, mock_defer):
        """All tenant data should be returned if is_super_admin is `True`."""
        # Different tenant survey
        make_survey_with_result(industry='ic-o', tenant='tenant2')
        data = {
            'engagement_lead': '3',
        }
        self.survey_1.engagement_lead = '1'
        self.survey_2.engagement_lead = '2'
        self.survey_1.save()
        self.survey_2.save()

        url = reverse('reports_export', kwargs={'tenant': self.tenant_slug})
        response = self.client.post(url, data=json.dumps(data), content_type="application/json")

        self.assertEqual(response.status_code, 200)
        mock_defer.assert_called_once()

        args, kwargs = mock_defer.call_args
        got_func, got_title, got_tenant, got_is_super_admin, got_el, got_headers, got_rows, got_share_with = args
        self.assertEqual(got_func, tasks.export_tenant_data)
        self.assertEqual(got_tenant, 'tenant1')
        self.assertEqual(got_share_with, response.wsgi_request.user.email)
        self.assertEqual(got_el, response.wsgi_request.user.engagement_lead)
