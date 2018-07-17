import mock

from core.models import Survey, SurveyResult
from core.tasks import get_results
from django.shortcuts import reverse
from djangae.test import TestCase
from mocks import get_mocked_results
from mommy_recepies import make_survey, make_survey_result


class GetResultsTestCase(TestCase):
    """Tests for get_result function"""

    @mock.patch('core.tasks.download_results', return_value=get_mocked_results())
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

    @mock.patch('core.tasks.download_results', return_value=get_mocked_results())
    def test_surveys_results_are_always_saved(self, download_mock):
        """Survey results are saved anyway, regardless Survey's related object exists."""
        self.assertEqual(Survey.objects.count(), 0)
        self.assertEqual(SurveyResult.objects.count(), 0)

        get_results()

        self.assertEqual(Survey.objects.count(), 0)
        self.assertEqual(SurveyResult.objects.count(), 3)

    @mock.patch('core.tasks.download_results', return_value=get_mocked_results(response_id='AAB'))
    def test_partial_download_existing_survey(self, download_mock):
        survey = make_survey(sid='1')
        make_survey_result(survey=survey, response_id='AAB')
        self.assertEqual(SurveyResult.objects.count(), 1)

        get_results()

        # no new Survey objects are created
        self.assertEqual(Survey.objects.count(), 1)
        # mock is called with response_id
        download_mock.assert_called_once_with('AAB')
        # only two new items will be created
        self.assertEqual(SurveyResult.objects.count(), 3)


class SyncQualtricsTestCase(TestCase):

    @mock.patch('core.tasks.download_results')
    def test_sync_ok(self, download_mock):
        url = reverse('pull-qualtrics-results')
        response = self.client.get(url)
        self.process_task_queues()
        download_mock.assert_called_once()
