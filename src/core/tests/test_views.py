import mock

from core import tasks
from djangae.test import TestCase
from django.shortcuts import reverse
import os
from django.contrib.auth import get_user_model
from core.test import with_appengine_admin, with_appengine_user
from django.test import override_settings
from core.tests.mocks import MOCKED_TENANTS


class SyncQualtricsTestCase(TestCase):
    """Tests for `sync_qualtrics_results` function."""
    def setUp(self):
        self.url = reverse('pull-qualtrics-results')

    def login_as_admin(self):
        self.user = get_user_model().objects.create(email='member@google.com')
        self._appengine_login(self.user, is_admin=True)
        self.client.force_login(self.user)

    def _appengine_login(self, user, is_admin=False):
        os.environ["USER_IS_ADMIN"] = '1' if is_admin else '0'
        os.environ["USER_EMAIL"] = user.email
        os.environ["USER_ID"] = str(user.id)

    @mock.patch('djangae.deferred.defer')
    def test_sync_ok(self, mock_defer):
        self.login_as_admin()
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        mock_defer.assert_called_once_with(
            tasks.sync_qualtrics,
            _queue='default'
        )

    @mock.patch('djangae.deferred.defer')
    def test_sync_access_defined_if_user_not_logged_in(self, mock_defer):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 403)
        mock_defer.assert_not_called()


@override_settings(
    TENANTS=MOCKED_TENANTS
)
class UpdateIndustriesBenchmarksTask(TestCase):
    """Tests for `update_industries_benchmarks_task` function."""
    def setUp(self):
        self.url = reverse('update-benchmarks')

    @with_appengine_admin("test@google.com")
    @mock.patch('djangae.deferred.defer')
    def test_update_industries_benchmarks_task_called_correctly(self, mock_defer):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(mock_defer.call_count, 3)

        args, kwargs = mock_defer.call_args_list[0]
        self.assertEqual(args[0], tasks.calculate_industry_benchmark)
        self.assertTrue(args[1] in MOCKED_TENANTS.keys())

        args, kwargs = mock_defer.call_args_list[1]
        self.assertEqual(args[0], tasks.calculate_industry_benchmark)
        self.assertTrue(args[1] in MOCKED_TENANTS.keys())

        args, kwargs = mock_defer.call_args_list[2]
        self.assertEqual(args[0], tasks.calculate_industry_benchmark)
        self.assertTrue(args[1] in MOCKED_TENANTS.keys())

    @with_appengine_user("test@gmail.com")
    @mock.patch('djangae.deferred.defer')
    def test_update_industries_benchmarks_access_denied_if_user_not_logged_in(self, mock_defer):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 403)
        mock_defer.assert_not_called()


class GenerateExportsTask(TestCase):
    """Tests for `generate_exports_task` function."""
    def setUp(self):
        self.url = reverse('export-datastore-data')

    @with_appengine_admin("test@google.com")
    @mock.patch('djangae.deferred.defer')
    def test_generate_exports_task_called_correctly_advertisers(self, mock_defer):
        response = self.client.get(self.url)

        survey_fields = [
            'id',
            'company_name',
            'industry',
            'country',
            'created_at',
            'engagement_lead',
            'tenant',
            'excluded_from_best_practice',
            'dmb',
            'account_id',
        ]

        survey_result_fields = [
            'access',
            'audience',
            'attribution',
            'ads',
            'organization',
            'automation',
        ]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(mock_defer.call_count, 3)

        # check paremeters for advertisers call
        args, kwargs = mock_defer.call_args_list[0]
        self.assertEqual(args[0], tasks.generate_csv_export)
        self.assertListEqual(args[2], survey_fields)
        self.assertListEqual(args[3], survey_result_fields)

    @with_appengine_admin("test@google.com")
    @mock.patch('djangae.deferred.defer')
    def test_generate_exports_task_called_correctly_news(self, mock_defer):
        response = self.client.get(self.url)

        survey_fields = [
            'id',
            'company_name',
            'industry',
            'country',
            'created_at',
            'engagement_lead',
            'tenant',
            'excluded_from_best_practice',
            'dmb',
            'account_id',
        ]

        survey_result_fields = [
            'strategic_direction',
            'reader_engagement',
            'reader_revenue',
            'advertising_revenue',
        ]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(mock_defer.call_count, 3)

        # check paremeters for news call
        args, kwargs = mock_defer.call_args_list[1]
        self.assertEqual(args[0], tasks.generate_csv_export)
        self.assertListEqual(args[2], survey_fields)
        self.assertListEqual(args[3], survey_result_fields)

    @with_appengine_user("test@gmail.com")
    @mock.patch('djangae.deferred.defer')
    def test_update_industries_benchmarks_access_denied_if_user_not_logged_in(self, mock_defer):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 403)
        mock_defer.assert_not_called()
