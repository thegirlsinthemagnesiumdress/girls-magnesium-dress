from core.models import Survey
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import override_settings
import mock
from rest_framework import status
from rest_framework.test import APITestCase
from core.tests.mommy_recepies import make_survey, make_survey_result, make_industry_benchmark
from core.tests.mocks import INDUSTRIES


User = get_user_model()


class SurveyTest(APITestCase):
    """Tests for `api.views.SurveyCompanyNameFromUIDView` view."""
    user_email = 'test@example.com'

    def setUp(self):
        user = User.objects.create(
            username='test1',
            email=self.user_email,
            password='pass',
        )

        self.client.force_authenticate(user)
        self.url = reverse('company_name')

    def test_fail_not_authenticated(self):
        """Ensure we can't hit the api if not authenticated."""
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_not_provide_company_name(self):
        """Get survey without providing `sid` in url should return 404."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_survey_exists(self):
        """Should return the `company_name` related to `sid` provided."""
        survey = make_survey()
        response = self.client.get(self.url, {
            "sid": survey.sid
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data.get('company_name'), survey.company_name)


class SurveyResultTest(APITestCase):
    """Tests for `api.views.SurveyResultsDetail` view."""
    user_email = 'test@example.com'

    def setUp(self):
        self.survey = make_survey(sid="92345123451234512345123451234512")

        self.survey_result = make_survey_result(
            survey=self.survey,
            response_id='AAA',
            dmb=1.0,
            dmb_d='{}'
        )

    def test_survey_result_not_found(self):
        url = reverse('survey_report', kwargs={'sid': '12345123451234512345123451234512'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_cors_not_supported(self):
        url = reverse('survey_report', kwargs={'sid': self.survey.pk})
        headers = {
            'HTTP_ORIGIN': 'http://example.com',
            'HTTP_ACCESS_CONTROL_REQUEST_METHOD': 'POST',
            'HTTP_ACCESS_CONTROL_REQUEST_HEADERS': 'X-Requested-With',

        }
        response = self.client.get(url, **headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(response.has_header('access-control-allow-origin'))


class SurveyDetailView(APITestCase):
    """Tests for `api.views.SurveyResultsDetail` view."""
    user_email = 'test@example.com'

    def setUp(self):
        self.survey = make_survey(company_name='test company', country="IT")
        self.survey_result = make_survey_result(
            survey=self.survey,
            response_id='AAA',
            dmb=1.0,
            dmb_d='{}'
        )
        self.survey.last_survey_result = self.survey_result
        self.survey.save()
        self.url = reverse('survey_report', kwargs={'sid': self.survey.pk})

    def test_survey_result_found(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertAlmostEqual(float(response.data.get('survey_result').get('dmb')), self.survey_result.dmb)
        self.assertEqual(response.data.get('survey_result').get('response_id'), self.survey_result.response_id)

    def test_survey_result_not_found(self):
        url = reverse('survey_report', kwargs={'sid': '12345123451234512345123451234512'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_cors_not_supported(self):
        url = reverse('survey_report', kwargs={'sid': self.survey.pk})
        headers = {
            'HTTP_ORIGIN': 'http://example.com',
            'HTTP_ACCESS_CONTROL_REQUEST_METHOD': 'POST',
            'HTTP_ACCESS_CONTROL_REQUEST_HEADERS': 'X-Requested-With',

        }
        response = self.client.get(url, **headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(response.has_header('access-control-allow-origin'))

    def test_survey_result_get_last(self):
        survey_result = make_survey_result(
            survey=self.survey,
            response_id='BBB',
            dmb=2.0,
            dmb_d='{}'
        )
        self.survey.last_survey_result = survey_result
        self.survey.save()

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertAlmostEqual(float(response.data.get('survey_result').get('dmb')), 2.0)
        self.assertEqual(response.data.get('survey_result').get('response_id'), 'BBB')

    def test_survey_does_not_have_last_result(self):
        survey = make_survey(company_name='test company no last result', industry="ic-o", country="IT")
        url = reverse('survey_report', kwargs={'sid': survey.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNone(response.data.get('survey_result'))
        self.assertEqual(response.data.get('company_name'), 'test company no last result')


@override_settings(
    INDUSTRIES=INDUSTRIES
)
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
            'industry': 'ic-o',
            'country': 'GB',
            'tenant': 'ads',
        }

        self.client.force_authenticate(user)
        self.url = reverse('create_survey')

    def test_unauthenticated_user(self):
        """Unauthenticated users should be able to post."""
        self.client.force_authenticate(None)
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_required_fields_matched(self):
        """Posting data matching required parameters should succed."""
        response = self.client.post(self.url, self.data)
        post_response = response.data
        survey_db = Survey.objects.get(company_name=self.data.get('company_name'))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(post_response.get('company_name'), survey_db.company_name)
        self.assertEqual(post_response.get('industry'), survey_db.industry)
        self.assertEqual(post_response.get('country'), survey_db.country)
        self.assertEqual(post_response.get('link'), survey_db.link)
        self.assertEqual(post_response.get('link_sponsor'), survey_db.link_sponsor)
        self.assertEqual(post_response.get('engagement_lead'), survey_db.engagement_lead)

    def test_required_fields_not_matched(self):
        """Posting data not matching required parameters should fail."""
        response = self.client.post(self.url, {'randomkey': 'randomvalue'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_industry_not_valid(self):
        """Posting data not matching required parameters should fail."""
        self.data['industry'] = 'invalid'
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_survey_is_created_with_right_keys(self):
        """Posting valid data should create survey"""
        survey_count = Survey.objects.count()

        response = self.client.post(self.url, self.data)
        response_data_keys = response.json().keys()
        self.assertEqual(set(response_data_keys), {
            'company_name',
            'link',
            'link_sponsor',
            'engagement_lead',
            'industry',
            'country',
            'tenant',
        })
        self.assertEqual(Survey.objects.count(), survey_count + 1)


@override_settings(
    INDUSTRIES=INDUSTRIES,
    MIN_ITEMS_INDUSTRY_THRESHOLD=1,
    MIN_ITEMS_BEST_PRACTICE_THRESHOLD=2
)
class SurveyIndustryResultTest(APITestCase):
    """Tests for `api.views.SurveyResultsIndustryDetail` view."""

    def setUp(self):
        make_industry_benchmark(industry='all')
        make_industry_benchmark(industry='ic')
        make_industry_benchmark(industry='ic-o')

    @mock.patch('core.aggregate.industry_best_practice', return_value=(None, None, None))
    @mock.patch('core.aggregate.industry_benchmark', return_value=(None, None, None))
    def test_industry_no_tenant_in_url(self, mocked_industry_benchmark, mocked_industry_best_practice):
        """When `tenant` paramenter is not in url, it should return 400 bad request."""
        url = reverse('survey_industry', kwargs={'industry': 'ic-o'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        mocked_industry_benchmark.assert_not_called()
        mocked_industry_best_practice.assert_not_called()

    @mock.patch('core.aggregate.industry_best_practice', return_value=(None, None, None))
    @mock.patch('core.aggregate.industry_benchmark', return_value=(None, None, None))
    def test_industry_with_results(self, mocked_industry_benchmark, mocked_industry_best_practice):
        """
        When there are some results for an industry, and we are above minimum
        threshold, we expect some results back.
        """
        url = '{}?tenant=tenant1'.format(reverse('survey_industry', kwargs={'industry': 'ic-o'}))
        response = self.client.get(url)
        response_data_keys = response.data.keys()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        mocked_industry_benchmark.assert_called()
        mocked_industry_best_practice.assert_called()

        self.assertEqual(set(response_data_keys), {
            'industry',
            'dmb_industry',
            'dmb_bp_industry',
            'dmb',
            'dmb_d',
            'dmb_bp',
            'dmb_d_bp'
        })

    @mock.patch('core.aggregate.industry_best_practice', return_value=(None, None, None))
    @mock.patch('core.aggregate.industry_benchmark', return_value=(None, None, None))
    def test_industry_does_not_exist(self, mocked_industry_benchmark, mocked_industry_best_practice):
        """
        When there are some results for an industry, and we are above minimum
        threshold, we expect some results back, excluded the one where
        `excluded_from_best_practice` is True.
        """
        url = '{}?tenant=tenant1'.format(reverse('survey_industry', kwargs={'industry': 'notanind'}))
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        mocked_industry_benchmark.assert_not_called()
        mocked_industry_best_practice.assert_not_called()


class SurveyResultDetailView(APITestCase):
    """Tests for `api.views.SurveyResultDetailView` view."""
    user_email = 'test@example.com'

    def setUp(self):
        self.survey = make_survey(company_name='test company', country="IT")
        self.survey_result = make_survey_result(
            survey=self.survey,
            response_id='R_3ozFIv81JgJ5zok',
            dmb=1.0,
            dmb_d='{}'
        )
        self.survey.last_survey_result = self.survey_result
        self.survey.save()

    def test_survey_result_found(self):

        url = reverse('survey_result_report', kwargs={'response_id': self.survey_result.response_id})
        response = self.client.get(url)
        response_data_keys = response.data.keys()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(set(response_data_keys), {
            'company_name',
            'industry',
            'industry_name',
            'country_name',
            'survey_result',
            'created_at',
        })

    def test_survey_result_not_found(self):
        url = reverse('survey_result_report', kwargs={'response_id': 'AAA'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_survey_result_found_multi_result(self):
        survey_result = make_survey_result(
            survey=self.survey,
            response_id='R_22222',
            dmb=2.0,
            dmb_d='{}'
        )

        url = reverse('survey_result_report', kwargs={'response_id': survey_result.response_id})
        response = self.client.get(url)
        response_data_keys = response.data.keys()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('company_name'), 'test company')
        self.assertAlmostEqual(float(response.data.get('survey_result').get('dmb')), 2.0)

        self.assertEqual(set(response_data_keys), {
            'company_name',
            'industry',
            'industry_name',
            'country_name',
            'survey_result',
            'created_at',
        })

    def test_survey_result_no_survey_attached(self):
        survey_result = make_survey_result(
            response_id='R_22222',
            dmb=2.0,
            dmb_d='{}'
        )

        url = reverse('survey_result_report', kwargs={'response_id': survey_result.response_id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
