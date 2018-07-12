import re

from core.models import Survey
from core.tests.mocks import generate_surveys
from djangae.test import TestCase
from django.test import override_settings
from mommy_recepies import SurveyRecipe, SurveyResultRecipe


class SurveyTest(TestCase):
    """Test case for `core.Survey` model."""

    def setUp(self):
        self.surveys = generate_surveys()

    def test_uid_is_generated_on_save(self):
        """Test that the survey generates a sid on save."""
        s = Survey(company_name="1")
        self.assertFalse(s.sid)
        s.save()
        self.assertTrue(s.sid)
        self.surveys = generate_surveys()

    def test_link(self):
        """
        Test that the link has the sid set
        in the query string,
        """
        survey = self.surveys[0]
        match = re.search(r'sid=([^&]*)', survey.link)
        self.assertEqual(match.groups(1)[0], survey.sid)

    def test_sponsor_link(self):
        """
        Test that the sponsor link has both the sid and sponsor flag
        in the query string,
        """
        survey = self.surveys[0]
        match = re.search(r'sid=([^&]*)', survey.link_sponsor)
        self.assertEqual(match.groups(1)[0], survey.sid)
        match = re.search(r'sp=([^&]*)', survey.link_sponsor)
        self.assertEqual(match.groups(1)[0], 'true')


@override_settings(
    WEIGHTS={
        'Q1': 2,
        'Q3': 3,
    },
    DIMENSIONS={
        'activation': ['Q3', 'Q4'],
        'audience': ['Q2'],
    }
)
class SurveyResultTest(TestCase):
    """Test case for `core.SurveyResult` model."""

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

    def setUp(self):
        survey = SurveyRecipe.make()
        survey_result = SurveyResultRecipe.make(survey=survey, data=self.survey_result)
        self.question_dict = {item[0]: item for item in survey_result.questions}

    def test_question_tuple_correctly_generated(self):
        """When weight and category are found, should be set."""
        question, answer, weight, category = self.question_dict.get('Q3')

        self.assertEqual(question, 'Q3')
        self.assertEqual(answer, 1.0)

        # weight should be applied to Q_3
        self.assertEqual(weight, 3)
        # category should be applied to Q_3
        self.assertEqual(category, 'activation')

    def test_question_tuple_empty_category_is_none(self):
        """When a category is not found should be set to None."""
        question, answer, weight, category = self.question_dict.get('Q10')

        self.assertEqual(question, 'Q10')
        self.assertEqual(answer, 0.0)
        self.assertEqual(weight, 1)
        self.assertIsNone(category)

    def test_question_tuple_use_default_weight(self):
        """When a weight is not found should be set to the default one."""
        question, answer, weight, category = self.question_dict.get('Q12')

        self.assertEqual(question, 'Q12')
        self.assertEqual(answer, 4.0)
        self.assertEqual(weight, 1)
        self.assertIsNone(category)

    def test_question_tuple_skipped_if_not_found_by_regex(self):
        """When a question does not match the regex is not return by questions property."""
        self.assertIsNone(self.question_dict.get('Q1_1_TEXT'))
