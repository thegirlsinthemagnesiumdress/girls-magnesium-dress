from core.qualtrics import question
from djangae.test import TestCase
from django.test import override_settings


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
class DataToQuestionTest(TestCase):
    """Test case for `core.qualtrics.question.data_to_questions` function."""

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
        questions = question.data_to_questions(self.survey_result)
        self.question_dict = {item[0]: item for item in questions}

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


class WeightedQuestionAverageTest(TestCase):
    """Test class for `core.qualtrics.question.weighted_questions_average` function."""

    def test_weighted_questions_average(self):
        """Test the right benchmark is calculated given an array of responses."""
        responses = [
            ('Q1', 1.0, 1, 'dimension_A'),
            ('Q2', 3.0, 1, 'dimension_A'),
        ]

        weighted_average = question.weighted_questions_average(responses)
        self.assertEqual(weighted_average, 2)

    def test_weighted_questions_average_complex(self):
        """Test that given an array of questions the right weighted average is calculated."""
        weighted_average = 1.907407407
        responses = [
            ('Q3', 2.0, 2, 'dimension_A'),
            ('Q4', 0.0, 0.5, 'dimension_A'),
            ('Q5_1', 2.0, 1, 'dimension_A'),
            ('Q5_2', 0.0, 1, 'dimension_A'),
            ('Q5_3', 3.0, 1, 'dimension_B'),
            ('Q6', 4.0, 1, 'dimension_B'),
            ('Q7', 2.0, 0.3, 'dimension_B'),
            ('Q8', 4.0, 1, 'dimension_C'),
            ('Q10', 0.0, 1, 'dimension_C'),
            ('Q11', 1.0, 1, 'dimension_C'),
            ('Q12', 2.0, 1, 'dimension_C'),
        ]
        average = question.weighted_questions_average(responses)
        self.assertAlmostEqual(average, weighted_average, places=4)


@override_settings(
    DIMENSIONS={
        'activation': ['Q3', 'Q4'],
        'audience': ['Q2'],
    }
)
class GetQuestionDimensionTest(TestCase):
    """Test case for `core.qualtrics.question.get_question_dimension` function."""

    def test_question_with_dimension(self):
        """When question belongs to a dimension, it should be returned"""
        dimension = question.get_question_dimension('Q3')

        self.assertEqual(dimension, 'activation')

    def test_no_dimension_found_for_question(self):
        """When a dimension cannot be found for a question it should return `None`."""
        dimension = question.get_question_dimension('Q1')

        self.assertIsNone(dimension)
