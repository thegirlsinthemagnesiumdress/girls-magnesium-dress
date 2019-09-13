from core.models import Survey
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import override_settings
from django.urls import NoReverseMatch
import mock
from rest_framework import status
from rest_framework.test import APITestCase
from core.tests.mommy_recepies import make_survey, make_survey_result, make_industry_benchmark
from core.tests.mocks import MOCKED_TENANTS_SLUG_TO_KEY, MOCKED_TENANTS
from core.conf.utils import get_tenant_slug
from core.test import reload_urlconf, with_appengine_user, with_appengine_anon


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
        survey = make_survey(tenant='ads', company_name='test company no last result', industry="ic-o", country="IT")
        url = reverse('survey_report', kwargs={'sid': survey.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNone(response.data.get('survey_result'))
        self.assertEqual(response.data.get('company_name'), 'test company no last result')


class CreateSurveyTest(APITestCase):
    """Tests for `api.views.CreateSurveyView` view."""

    def setUp(self):
        self.user = User.objects.create(
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

        self.client.force_authenticate(self.user)
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
        self.assertEqual(post_response.get('creator'), self.user.pk)

    def test_required_fields_not_matched(self):
        """Posting data not matching required parameters should fail."""
        response = self.client.post(self.url, {'randomkey': 'randomvalue'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_industry_not_valid(self):
        """Posting data not matching required parameters should fail."""
        self.data['industry'] = 'invalid'
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_tenant_not_valid(self):
        """Posting invalid tenant should not be allowed."""
        self.data['tenant'] = 'invalid'
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_survey_is_created_with_right_keys(self):
        """Posting valid data should create survey"""
        survey_count = Survey.objects.count()

        response = self.client.post(self.url, self.data)
        response_data_keys = response.json().keys()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(set(response_data_keys), {
            'sid',
            'company_name',
            'link',
            'link_sponsor',
            'engagement_lead',
            'creator',
            'industry',
            'country',
            'tenant',
            'account_id',
            'slug',
        })
        self.assertEqual(Survey.objects.count(), survey_count + 1)

    def test_survey_is_created_correctly(self):
        """Posting valid data should create survey"""
        response = self.client.post(self.url, self.data)
        response_data = response.json()
        self.assertEqual(response.status_code, 201)

        survey = Survey.objects.first()

        self.assertEqual(response_data['company_name'], survey.company_name)
        self.assertEqual(response_data['account_id'], survey.account_id)
        self.assertEqual(response_data['tenant'], survey.tenant)
        self.assertEqual(response_data['creator'], self.user.pk)
        self.assertEqual(self.user.accounts.count(), 1)

    def test_non_admin_survey_is_created_correctly(self):
        """Posting valid data from a non-admin user should create survey"""
        self.client.force_authenticate(None)
        response = self.client.post(self.url, self.data)
        response_data = response.json()
        self.assertEqual(response.status_code, 201)

        survey = Survey.objects.first()

        self.assertEqual(response_data['company_name'], survey.company_name)
        self.assertEqual(response_data['account_id'], survey.account_id)
        self.assertEqual(response_data['tenant'], survey.tenant)
        self.assertEqual(response_data['creator'], None)
        self.assertEqual(self.user.accounts.count(), 0)

    def test_creating_duplicate_survey(self):
        """Posting duplicate data should add another account to the user (for now...)"""
        response = self.client.post(self.url, self.data)
        response_data = response.json()

        survey = Survey.objects.get(sid=response_data['sid'])

        self.assertEqual(survey.creator, self.user)
        self.assertEqual(self.user.accounts.count(), 1)

        self.client.post(self.url, self.data)

        self.assertEqual(self.user.accounts.count(), 2)


class AddSurveyTest(APITestCase):
    """Tests for `api.views.AddSurveyView` view."""

    def setUp(self):
        self.user = User.objects.create(
            username='test1',
            email='test@example.com',
            password='pass',
        )

        self.client.force_authenticate(self.user)

    def test_adding_survey(self):
        """Adding an survey should add it to the users' account list"""
        survey = make_survey()

        url = reverse('add_survey', kwargs={'sid': survey.sid})
        self.client.put(url)

        self.assertEqual(self.user.accounts.count(), 1)
        self.assertEqual(self.user.accounts.first(), survey)

    def test_adding_invalid_survey(self):
        """Adding an non-existant survey should not create it or add it to the users' account list"""
        with self.assertRaises(NoReverseMatch):
            reverse('add_survey', kwargs={'sid': 'random53dd2e47e6aa85c77318f4a0e9'})

        self.assertEqual(self.user.accounts.count(), 0)

    def test_adding_duplicate_survey(self):
        """Adding an survey that has already added should not add it again"""
        survey = make_survey()

        url = reverse('add_survey', kwargs={'sid': survey.sid})
        self.client.put(url)
        self.client.put(url)

        self.assertEqual(self.user.accounts.count(), 1)

    def test_adding_survey_not_creator(self):
        """Adding an survey which you did not create should not set you as the creator"""
        self.client.force_authenticate(None)
        survey = make_survey()
        self.client.force_authenticate(self.user)

        url = reverse('add_survey', kwargs={'sid': survey.sid})
        self.client.put(url)

        self.assertEqual(survey.creator, None)
        self.assertEqual(self.user.accounts.count(), 1)
        self.assertEqual(self.user.accounts.first(), survey)


@override_settings(
    TENANTS=MOCKED_TENANTS,
    TENANTS_SLUG_TO_KEY=MOCKED_TENANTS_SLUG_TO_KEY,
    MIN_ITEMS_INDUSTRY_THRESHOLD=1,
    MIN_ITEMS_BEST_PRACTICE_THRESHOLD=2
)
class SurveyIndustryResultTest(APITestCase):
    """Tests for `api.views.SurveyResultsIndustryDetail` view."""

    @classmethod
    def tearDownClass(cls):
        super(SurveyIndustryResultTest, cls).tearDownClass()
        reload_urlconf()

    @classmethod
    def setUpClass(cls):
        super(SurveyIndustryResultTest, cls).setUpClass()
        reload_urlconf()

    def setUp(self):
        make_industry_benchmark(industry='all', tenant='tenant1')
        make_industry_benchmark(industry='ic', tenant='tenant1')
        make_industry_benchmark(industry='ic-o', tenant='tenant1')

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
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data_keys = response.data.keys()

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

    @mock.patch('core.aggregate.industry_best_practice', return_value=(None, None, None))
    @mock.patch('core.aggregate.industry_benchmark', return_value=(None, None, None))
    def test_tenant_does_not_exist(self, mocked_industry_benchmark, mocked_industry_best_practice):
        """When `tenant` paramenter is not a valid tenant, it should return 400 bad request."""
        url = '{}?tenant=notatenant'.format(reverse('survey_industry', kwargs={'industry': 'ic-o'}))
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        mocked_industry_benchmark.assert_not_called()
        mocked_industry_best_practice.assert_not_called()

    @mock.patch('core.aggregate.industry_best_practice', return_value=(None, None, None))
    @mock.patch('core.aggregate.industry_benchmark', return_value=(None, None, None))
    def test_industry_with_results_unicode(self, mocked_industry_benchmark, mocked_industry_best_practice):
        """Unicode industry name should be correctly returned."""
        make_industry_benchmark(industry='all', tenant='tenant3')
        make_industry_benchmark(industry='ic', tenant='tenant3')
        make_industry_benchmark(industry='ic-o', tenant='tenant3')

        url = '{}?tenant=tenant3'.format(reverse('survey_industry', kwargs={'industry': 'ic-o'}))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data_keys = response.data.keys()

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
            'tenant',
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
            'tenant',
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


class AdminSurveyListViewTest(APITestCase):
    """Tests for `api.views.AdminSurveyListView` view."""

    def setUp(self):
        slug = get_tenant_slug('ads')
        self.url = reverse('admin_surveys', kwargs={'tenant': slug})

    def test_fail_not_authenticated(self):
        """Ensure we can't hit the api if not authenticated."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    @with_appengine_user("test@google.com")
    def test_survey_exists(self):
        """Should return the `company_name` related to `sid` provided."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @with_appengine_user("test@gmail.com")
    def test_survey__user_does_not_have_permission(self):
        """Should return the `company_name` related to `sid` provided."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    @with_appengine_anon
    def test_survey__anonn_does_not_have_permission(self):
        """Should return the `company_name` related to `sid` provided."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class UpdateAccountIdSurveyTest(APITestCase):
    """Tests for `api.views.UpdateAccountIdSurvey` view."""

    def setUp(self):

        self.survey_1 = make_survey(company_name='test company', country="IT")
        self.survey_2 = make_survey(company_name='test company 2', country="IT", account_id='111111')

        self.data = {
            'account_id': '123456'
        }

        self.url_1 = reverse('update_survey', kwargs={'sid': self.survey_1.sid})
        self.url_2 = reverse('update_survey', kwargs={'sid': self.survey_2.sid})

    @with_appengine_anon
    def test_unauthenticated_user(self):
        """Unauthenticated users should return 403 Forbidden."""
        response = self.client.put(self.url_1, self.data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    @with_appengine_user("test@google.com")
    def test_post_is_not_allowed(self):
        """Post method should not be allowed, it should return 405."""
        response = self.client.post(self.url_1, self.data)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    @with_appengine_user("test@google.com")
    def test_only_account_id_is_updated(self):
        """Updating data matching required parameters should succed."""
        self.data["company_name"] = "New company name"
        response = self.client.put(self.url_1, self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        content = response.json()
        # account id should still be null
        self.assertEqual(content.get('account_id'), '123456')
        self.assertEqual(self.survey_1.company_name, 'test company')

        response = self.client.put(self.url_2, self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        content = response.json()
        # account id should still be the odl value
        self.assertEqual(content.get('account_id'), '123456')
        self.assertEqual(self.survey_2.company_name, 'test company 2')

    @with_appengine_user("test@google.com")
    def test_fields_other_than_account_id_are_ignored_invalid_key(self):
        """Updating data with random keys should return 200 and ignore invalid keys."""
        response = self.client.put(self.url_1, {'randomkey': 'randomvalue'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        content = response.json()
        # account id should still be null
        self.assertIsNone(content.get('account_id'))

        response = self.client.put(self.url_2, {'randomkey': 'randomvalue'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        content = response.json()
        # account id should still be the odl value
        self.assertEqual(content.get('account_id'), '111111')

    @with_appengine_user("test@google.com")
    def test_fields_other_than_account_id_are_ignored_invalid_value(self):
        """Updating data with invalid values for fields, it still succedes."""
        invalid_data = {
            'industry': 'invalid'
        }

        response = self.client.put(self.url_1, invalid_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        content = response.json()
        # account id should still be null
        self.assertIsNone(content.get('account_id'))

        response = self.client.put(self.url_2, invalid_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        content = response.json()
        # account id should still be the odl value
        self.assertEqual(content.get('account_id'), '111111')

    @with_appengine_user("test@example.com")
    def test_not_admin_forbidden(self):
        """Updating data matching required parameters should succed."""
        self.data["company_name"] = "New company name"
        response = self.client.put(self.url_1, self.data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)



class AccountViewSet(APITestCase):
    """Tests for `api.views.AccountViewSet` view."""

    def setUp(self):
        make_survey(company_name='test company', country="IT", tenant="ads")
        make_survey(company_name='test company 2', country="IT", tenant="ads", account_id='22222')
        make_survey(company_name='company 3', country="IT", tenant="ads", account_id='111111')

        slug = get_tenant_slug('ads')
        self.url = reverse('admin_surveys_search', kwargs={'tenant': slug})

    @with_appengine_anon
    def test_unauthenticated_user(self):
        """Unauthenticated users should return 403 Forbidden."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    @with_appengine_user("test@example.com")
    def test_get_without_q_param(self):
        """
        Get method without `q` parameter, it should return 200 as well as the list
        of `Survey` objects belonging to a `tenant`."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    @with_appengine_user("test@example.com")
    def test_get_with_q_param(self):
        """
        Get method with `q` parameter, it should return 200 as well as the list
        of `Survey` objects belonging to a `tenant` filtered by search term."""
        response = self.client.get(self.url, {
            'q': 'test',
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    @with_appengine_user("test@example.com")
    def test_get_with_q_param_empty(self):
        """
        Get method with empty `q` parameter, it should return 200 as well as the list
        of `Survey` objects belonging to a `tenant` filtered by search term."""
        response = self.client.get(self.url, {
            'q': '',
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    @with_appengine_user("test@example.com")
    def test_get_with_q_param_search_by_account_id(self):
        """
        Get method without `q` parameter, it should return 200 as well as the list
        of `Survey` objects belonging to a `tenant` filtered by search term."""
        account_id = '22222'
        response = self.client.get(self.url, {
            'q': account_id,
        })
        first_el = response.data[0]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(first_el.get('account_id'), account_id)

    @with_appengine_user("test@example.com")
    def test_get_empty_tenant_should_return_empty(self):
        """
        Get method without `q` parameter, it should return 200 as well as an empty list."""
        slug = get_tenant_slug('retail')
        url_retail = reverse('admin_surveys_search', kwargs={'tenant': slug})
        response = self.client.get(url_retail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    @with_appengine_user("test@example.com")
    def test_get_empty_tenant_with_q_param_should_return_empty(self):
        """
        Get method with `q` parameter, it should return 200 as well as an empty list."""
        slug = get_tenant_slug('retail')
        url_retail = reverse('admin_surveys_search', kwargs={'tenant': slug})
        response = self.client.get(url_retail, {
            'q': 'test',
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
