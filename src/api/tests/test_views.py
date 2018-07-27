from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from core.models import Survey
from core.tests.mocks import generate_surveys


User = get_user_model()


class SurveyTest(APITestCase):
    user_email = 'test@example.com'

    def setUp(self):
        user = User.objects.create(
            username='test1',
            email=self.user_email,
            password='pass',
        )

        self.qualtrics_user = User.objects.create(
            username='test2',
            email='qualtrics@qualtrics.com',
            password='qualtrics',
            is_qualtrics=True,
        )

        surveys = generate_surveys()
        self.sids = [survey.sid for survey in surveys]

        self.client.force_authenticate(user)
        self.url = reverse('survey-list')


    def test_fail_not_authenticated(self):
        """
        Ensure we can't hit the api if not authenticated
        """
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_surveys_should_be_empty(self):
        """
        List surveys should return an empty list.
        Not exposing all companies it for now.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_filtered(self):
        """
        Should return the filtered list.
        """
        response = self.client.get(self.url, {
            "sid": self.sids[0]
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_list_filtered_qualtrics_user(self):
        """
        Should return the filtered list for a qualtrics user.
        """
        self.client.force_authenticate(user=self.qualtrics_user)
        response = self.client.get(self.url, {
            "sid": self.sids[0]
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_qualtrics_not_authorized(self):
        """
        Should not allow qualtrics user to list companies only.
        """
        self.client.force_authenticate(user=self.qualtrics_user)
        response = self.client.post(self.url, {
            "sid": self.sids[0]
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # from nose.tools import set_trace; set_trace()
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.client.put(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.client.patch(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class CreateSurveyTest(APITestCase):
    """Tests for `api.views.CreateSurveyView` view."""

    def setUp(self):
        user = User.objects.create(
            username='test1',
            email='test@example.com',
            password='pass',
        )

        self.data = {
            'company_name': 'test company',
        }

        self.client.force_authenticate(user)
        self.url = reverse('create_survey')

    def test_unauthenticated_user(self):
        """Unauthenticated users should not be able to post."""
        self.client.force_authenticate(None)
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_required_fields_matched(self):
        """Posting data matching required parameters should succed."""
        response = self.client.post(self.url, self.data)
        post_response = response.data
        survey_db = Survey.objects.get(company_name=self.data.get('company_name'))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(post_response.get('company_name'), survey_db.company_name)
        self.assertEqual(post_response.get('link'), survey_db.link)
        self.assertEqual(post_response.get('link_sponsor'), survey_db.link_sponsor)

    def test_required_fields_not_matched(self):
        """Posting data not matching required parameters should fail."""
        response = self.client.post(self.url, {'randomkey': 'randomvalue'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
