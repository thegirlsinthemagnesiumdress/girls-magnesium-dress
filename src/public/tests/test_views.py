import os

from djangae.test import TestCase
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from django.test import override_settings

from core.models import SurveyResult
from core.tests.mommy_recepies import make_survey


@override_settings(
    SURVEY_ADMIN_AUTHORIZED_DOMAINS=(
        '@example.com',
        '@google.com',
        '@potatolondon.com',
    )
)
class ReportsAdminTestCase(TestCase):
    """Tests for `reports_admin` view."""
    def setUp(self):
        self.url = reverse('reports')

        self.survey_1 = make_survey()
        self.survey_2 = make_survey()

        self.survey_result_1 = SurveyResult.objects.create(
            survey=self.survey_1,
            response_id='AAA',
            dmb=1.0,
            dmb_d='{}'
        )

        self.survey_result_2 = SurveyResult.objects.create(
            survey=self.survey_2,
            response_id='BBB',
            dmb=1.0,
            dmb_d='{}'
        )

    def login(self, admin=False, email='member@google.com'):
        self.user = get_user_model().objects.create(email=email)
        self._appengine_login(self.user, is_admin=admin)
        self.client.force_login(self.user)

    def _appengine_login(self, user, is_admin=False):
        os.environ["USER_IS_ADMIN"] = '1' if is_admin else '0'
        os.environ["USER_EMAIL"] = user.email
        os.environ["USER_ID"] = str(user.id)

    def test_standard_user_logged_in(self):
        """Standard user can retrieve reports belonging to its engagement_lead."""
        self.login()

        # set a survey to belong to logged user
        self.survey_1.engagement_lead = self.user.engagement_lead
        self.survey_1.save()

        response = self.client.get(self.url)
        surveys = list(response.context.get('surveys'))

        self.assertEqual(response.status_code, 200)
        self.assertTrue(surveys)
        self.assertEqual(len(surveys), 1)
        self.assertEqual(surveys[0].engagement_lead, self.survey_1.engagement_lead)

    @override_settings(
        SUPER_USERS=[
            'superuser@example.com',
        ]
    )
    def test_whitelisted_user_logged_in(self):
        """Whitelisted user can retrieve reports belonging to all companies."""
        self.login(admin=True, email='superuser@example.com')
        response = self.client.get(self.url)
        surveys = list(response.context.get('surveys'))
        engagement_lead_ids = [el.engagement_lead for el in surveys]

        self.assertEqual(response.status_code, 200)
        self.assertTrue(surveys)
        self.assertEqual(len(surveys), 2)
        self.assertTrue(self.survey_1.engagement_lead in engagement_lead_ids)
        self.assertTrue(self.survey_2.engagement_lead in engagement_lead_ids)

    def test_user_not_logged_in(self):
        """Anonymous user cannot retrieve any report."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(reverse('djangae_login_redirect') in response.get('Location'))

    def test_user_logged_in_not_in_permission_domains(self):
        """User could be logged in, but not having enough permissions to access to the resource."""
        self.login(email='user@notenoughpermissions.com')
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 403)
