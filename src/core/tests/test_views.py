import mock

from core.tasks import sync_results
from djangae.test import TestCase
from django.shortcuts import reverse
import os
from django.contrib.auth import get_user_model


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
            sync_results,
            _queue='default'
        )

    @mock.patch('djangae.deferred.defer')
    def test_sync_access_defined_if_user_not_logged_in(self, mock_defer):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 403)
        mock_defer.assert_not_called()
