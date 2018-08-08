import mock

from core.models import Survey, SurveyResult
from core.tasks import get_results
from djangae.test import TestCase
from mocks import get_mocked_results
from mommy_recepies import make_survey, make_survey_result
from core.qualtrics.exceptions import FetchResultException


class GetResultsTestCase(TestCase):
    """Tests for get_result function"""

    @mock.patch('core.qualtrics.download.fetch_results', return_value=get_mocked_results())
    def test_new_survey_first_time_download(self, download_mock):
        """We're assuming that all the Surveys have been created previously."""
        make_survey(sid='1')
        make_survey(sid='2')
        make_survey(sid='3')

        self.assertEqual(Survey.objects.count(), 3)
        self.assertEqual(SurveyResult.objects.count(), 0)

        get_results()

        self.assertEqual(Survey.objects.count(), 3)
        self.assertEqual(SurveyResult.objects.count(), 3)

    @mock.patch('core.qualtrics.download.fetch_results', return_value=get_mocked_results())
    def test_surveys_results_and_survey_updated(self, download_mock):
        """Survey results are saved anyway, regardless Survey's related object exists."""
        self.assertEqual(Survey.objects.count(), 0)
        self.assertEqual(SurveyResult.objects.count(), 0)

        get_results()
        survey_1 = Survey.objects.get(pk='1')
        # Industry is updated.
        self.assertEqual(survey_1.industry, 'A')
        # Last result is updated.
        self.assertNotNone(survey_1.last_survey_result)

    @mock.patch('core.qualtrics.download.fetch_results', return_value=get_mocked_results())
    def test_surveys_results_are_always_saved(self, download_mock):
        """Survey results are saved anyway, regardless Survey's related object exists."""
        self.assertEqual(Survey.objects.count(), 0)
        self.assertEqual(SurveyResult.objects.count(), 0)

        get_results()

        self.assertEqual(Survey.objects.count(), 0)
        self.assertEqual(SurveyResult.objects.count(), 3)

    @mock.patch('core.qualtrics.download.fetch_results', return_value=get_mocked_results(response_id='AAB'))
    def test_partial_download_existing_survey(self, download_mock):
        # survey has been created on datastore
        survey = make_survey(sid='1')
        make_survey(sid='2')
        make_survey(sid='3')

        # only survey result with response_id='AAB' has been downloaded
        make_survey_result(survey=survey, response_id='AAB')

        self.assertEqual(Survey.objects.count(), 3)
        self.assertEqual(SurveyResult.objects.count(), 1)

        get_results()

        # no new Survey objects are created
        self.assertEqual(Survey.objects.count(), 3)
        # mock is called with response_id
        download_mock.assert_called_once_with(response_id='AAB')
        # only two new items will be created
        self.assertEqual(SurveyResult.objects.count(), 3)

    @mock.patch('core.qualtrics.download.fetch_results')
    def test_fetch_results_fails(self, download_mock):
        exception_body = {
            'meta': {
                'httpStatus': 400,
                'error': {
                    'errorMesasge': 'some error'
                }
            }
        }
        download_mock.side_effect = FetchResultException(exception_body)

        survey = make_survey(sid='1')
        make_survey_result(survey=survey, response_id='AAB')
        self.assertEqual(SurveyResult.objects.count(), 1)

        with mock.patch('core.tasks._create_survey_result') as survey_result_mock:
            get_results()
            survey_result_mock.assert_not_called()
            download_mock.assert_called_once_with(response_id='AAB')
            self.assertEqual(Survey.objects.count(), 1)
            self.assertEqual(SurveyResult.objects.count(), 1)
