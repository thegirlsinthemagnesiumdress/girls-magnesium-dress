from djangae.test import TestCase
from core.tasks import get_results
from mommy_recepies import SurveyRecipe, BenchmarkRecipe
import mock
from mocks import get_mocked_results


class GetResultsTestCase(TestCase):
    """Tests for get_result function"""

    @mock.patch('core.tasks.download_results')
    def test_cannot_find_any_survey(self, download_mock):
        self.assertNone(get_results('somerandomuid'))

    @mock.patch('core.tasks.download_results')
    def test_new_survey_first_time_download(self, download_mock):
        survey = SurveyRecipe.make()

        results = get_results(survey.uid)

        self.client.post(self.url, {})

    @mock.patch('core.tasks.download_results', return_value=get_mocked_results('AAB'))
    def test_partial_download_existing_survey(self, download_mock):
        survey = SurveyRecipe.make()
        BenchmarkRecipe.make(sid=survey.uid)

        results = get_results(survey.uid)
        print results
        assert 1 ==0
        self.client.post(self.url, {})
