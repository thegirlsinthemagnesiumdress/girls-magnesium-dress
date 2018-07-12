from djangae.test import TestCase
from core.models import Survey
from core.tests.mocks import generate_surveys
from mommy_recepies import SurveyRecipe, SurveyResultRecipe

import re


class SurveyTest(TestCase):
    def setUp(self):
        self.surveys = generate_surveys()

    def test_uid_is_generated_on_save(self):
        """
        Test that the survey generates a uid on save.
        """
        s = Survey(company_name="1")
        self.assertFalse(s.uid)
        s.save()
        self.assertTrue(s.uid)
        self.surveys = generate_surveys()

    def test_link(self):
        """
        Test that the link has the uid set
        in the query string,
        """
        survey = self.surveys[0]
        match = re.search(r'sid=([^&]*)', survey.link)
        self.assertEqual(match.groups(1)[0], survey.uid)

    def test_sponsor_link(self):
        """
        Test that the sponsor link has both the uid and sponsor flag
        in the query string,
        """
        survey = self.surveys[0]
        match = re.search(r'sid=([^&]*)', survey.link_sponsor)
        self.assertEqual(match.groups(1)[0], survey.uid)
        match = re.search(r'sp=([^&]*)', survey.link_sponsor)
        self.assertEqual(match.groups(1)[0], 'true')


class SurveyResultTest(TestCase):
    def setUp(self):
        survey = SurveyRecipe.make()
        # survey_result = SurveyResultRecipe(sid=survey.uid)

    def test_uid_is_generated_on_save(self):
        weights = {
            'Q1': 2,
            'Q3': 3,
        }

        dimensions = {
            'activation': ['Q3', 'Q4'],
            'audience': ['Q2'],
        }

        survey_result = {
            'Organization-sum': '0.0',
            'Organization-weightedAvg': '0.0',
            'Organization-weightedStdDev': '0.0',
            'sid': '2',
            'ResponseID': 'AAC',
            'Enter Embedded Data Field Name Here...': '',
            'sponsor': '',
            'company_name': 'new survey',
            'industry': 'B',
            'dmb': '0.5',
            'Q1_1_TEXT': '',
            'Q1_2_TEXT': '',
            'Q2_1_TEXT': '',
            'Q2_2_TEXT': '',

            'Q3': '1',
            'Q4': '1',
            'Q5_1': '1',

            'Q5_2': '0',
            'Q5_3': '2',
            'Q6': '0',
            'Q7': '1',

            'Q8': '0',
            'Q10': '0',
            'Q11': '1',
            'Q12': '4',
        }

        survey = SurveyRecipe.make(weight=weights, dimension=dimensions)
        survey_result = SurveyResultRecipe.make(survey=survey, data=survey_result)

        print(survey_result.questions)
        assert 1 == 0
