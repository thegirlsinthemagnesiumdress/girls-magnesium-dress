from djangae.test import TestCase
from core.tasks import get_results
from mommy_recepies import SurveyRecipe, SurveyResultRecipe
import mock
from mocks import get_mocked_results
from core.models import Survey, SurveyResult


class GetResultsTestCase(TestCase):
    """Tests for get_result function"""

    @mock.patch('core.tasks.download_results')
    def test_cannot_find_any_survey(self, download_mock):
        get_results('somerandomuid')

        self.assertEqual(Survey.objects.count(), 0)
        self.assertEqual(SurveyResult.objects.count(), 0)

    @mock.patch('core.tasks.download_results', return_value=get_mocked_results())
    def test_new_survey_first_time_download(self, download_mock):
        survey = SurveyRecipe.make()
        self.assertEqual(Survey.objects.count(), 1)
        self.assertEqual(SurveyResult.objects.count(), 0)

        get_results(survey.uid)

        self.assertEqual(Survey.objects.count(), 1)
        self.assertEqual(SurveyResult.objects.count(), 3)

    @mock.patch('core.tasks.download_results', return_value=get_mocked_results(all=False, uid='AAB'))
    def test_partial_download_existing_survey(self, download_mock):
        survey = SurveyRecipe.make()
        SurveyResultRecipe.make(survey=survey, response_id='AAB')
        self.assertEqual(SurveyResult.objects.count(), 1)

        get_results(survey.uid)

        # only two new items will be created
        self.assertEqual(Survey.objects.count(), 1)
        self.assertEqual(SurveyResult.objects.count(), 3)
