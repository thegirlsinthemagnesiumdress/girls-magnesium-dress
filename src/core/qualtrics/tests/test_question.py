from core.qualtrics import question
from djangae.test import TestCase
import mock
from collections import defaultdict


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
        'dmb': '0.5',
        'Q1_1_TEXT': '',
        'Q1_2_TEXT': '',
        'Q2_1_TEXT': '',
        'Q2_2_TEXT': '',

        'Q3': '1',
        'Q12': '4',
        'Q13_133.1': '1',
        'Q13_100.2': '1',
        'Q13_150.3': '0',
        'Q13_233.4': '1',
    }

    def setUp(self):

        weights = {
            'Q1': 2,
            'Q3': 3,
        }
        dimensions = {
            'activation': ['Q3', 'Q12'],
            'audience': ['Q13'],
        }
        multi_answer_questions = ['Q13']

        questions = question.data_to_questions(self.survey_result, dimensions, multi_answer_questions, weights)
        self.question_dict = defaultdict(list)
        for item in questions:
            self.question_dict[item[0]].append(item)

    def test_question_tuple_correctly_generated(self):
        """When weight and category are found, should be set."""
        q3_list = self.question_dict.get('Q3')
        self.assertEqual(len(q3_list), 1)
        q3 = q3_list[0]

        question, answer, weight, category = q3

        self.assertEqual(question, 'Q3')
        self.assertItemsEqual(answer, [1.0])

        # weight should be applied to Q_3
        self.assertEqual(weight, 3)
        # category should be applied to Q_3
        self.assertTrue(category in ['activation'])

    def test_question_tuple_use_default_weight(self):
        """When a weight is not found should be set to the default one."""
        q12_list = self.question_dict.get('Q12')
        self.assertEqual(len(q12_list), 1)

        q12 = q12_list[0]
        question, answer, weight, category = q12

        self.assertEqual(question, 'Q12')
        self.assertItemsEqual(answer, [4.0])
        self.assertEqual(weight, 1)
        self.assertEqual(category, 'activation')

    def test_multiple_answer_question_tuple(self):
        q13_list = self.question_dict.get('Q13')
        self.assertEqual(len(q13_list), 1)
        q13 = q13_list[0]

        question, answer, weight, category = q13
        expected_answer = [1.33, 1, 0, 2.33]
        self.assertCountEqual(answer, expected_answer)

        self.assertEqual(set(expected_answer), set(answer))

    @mock.patch('core.qualtrics.question.logging')
    def test_multiple_answer_question_missing_in_settings(self, logging_mock):

        weights = {
            'Q1': 2,
            'Q3': 3,
        }
        dimensions = {
            'activation': ['Q3', 'Q12'],
            'audience': ['Q13'],
        }
        multi_answer_questions = []

        question.data_to_questions(self.survey_result, dimensions, multi_answer_questions, weights)
        self.assertTrue(logging_mock.warn.called)

    def test_reg_ex(self):
        matches = [
            ('Q1', {
                'question_id': 'Q1',
                'multi_answer_value': None,
            }),
            ('Q2_1', {
                'question_id': 'Q2_1',
                'multi_answer_value': None,
            }),
            ('Q3_1.33', {
                'question_id': None,
                'multi_answer_value': None,
            }),
            ('Q4_133.1', {
                'question_id': 'Q4',
                'multi_answer_value': '133',
            }),
            ('Q5_1_TEXT', {
                'question_id': None,
                'multi_answer_value': None,
            }),
            ('sid', {
                'question_id': None,
                'multi_answer_value': None,
            }),
            ('Q6_1_133.12', {
                'question_id': 'Q6_1',
                'multi_answer_value': '133',
            }),
        ]

        for m in matches:
            key, exp_match = m
            match = question.match_question_key(key)
            self.assertDictEqual(match, exp_match)

    def test_question_tuple_correctly_generated_multi_dim(self):
        """When weight and category are found, should be set."""

        weights = {
            'Q1': 2,
            'Q3': 3,
        }
        dimensions = {
            'activation': ['Q3', 'Q12'],
            'audience': ['Q3'],
        }
        multi_answer_questions = ['Q13']

        questions = question.data_to_questions(self.survey_result, dimensions, multi_answer_questions, weights)

        self.question_dict = defaultdict(list)
        for item in questions:
            self.question_dict[item[0]].append(item)

        q3_list = self.question_dict.get('Q3')

        # Q3 appears in 2 dimensions, so the lenght should be 2
        self.assertEqual(len(q3_list), 2)

        for q3 in q3_list:
            q, answer, weight, category = q3

            self.assertEqual(q, 'Q3')
            self.assertItemsEqual(answer, [1.0])

            # weight should be applied to Q_3
            self.assertEqual(weight, 3)
            # category should be applied to Q_3
            self.assertTrue(category in ['activation', 'audience'])


class WeightedQuestionAverageTest(TestCase):
    """Test class for `core.qualtrics.question.weighted_questions_average` function."""

    def test_weighted_questions_average(self):
        """Test the right benchmark is calculated given an array of responses."""
        responses = [
            ('Q1', [1.0], 1, 'dimension_A'),
            ('Q2', [3.0], 1, 'dimension_A'),
            ('Q2', [1.0, 2.0], 1, 'dimension_A'),
        ]

        weighted_average = question.weighted_questions_average(responses)
        self.assertAlmostEqual(weighted_average, 2.33, places=2)

    def test_weighted_questions_average_complex(self):
        """Test that given an array of questions the right weighted average is calculated."""
        weighted_average = 1.907407407
        responses = [
            ('Q3', [2.0], 2, 'dimension_A'),
            ('Q4', [0.0], 0.5, 'dimension_A'),
            ('Q5_1', [2.0], 1, 'dimension_A'),
            ('Q5_2', [0.0], 1, 'dimension_A'),
            ('Q5_3', [3.0], 1, 'dimension_B'),
            ('Q6', [4.0], 1, 'dimension_B'),
            ('Q7', [2.0], 0.3, 'dimension_B'),
            ('Q8', [4.0], 1, 'dimension_C'),
            ('Q10', [0.0], 1, 'dimension_C'),
            ('Q11', [1.0], 1, 'dimension_C'),
            ('Q12', [2.0], 1, 'dimension_C'),
        ]
        average = question.weighted_questions_average(responses)
        self.assertAlmostEqual(average, weighted_average, places=4)


class GetQuestionDimensionTest(TestCase):
    """Test case for `core.qualtrics.question.get_question_dimension` function."""

    def test_question_with_dimension(self):
        """When question belongs to a dimension, it should be returned"""
        dimensions = {
            'activation': ['Q3', 'Q4'],
            'audience': ['Q2'],
        }
        dimension_list = question.get_question_dimension('Q3', dimensions)

        self.assertTrue(dimension_list, list)
        self.assertEqual(len(dimension_list), 1)
        dimension = dimension_list[0]
        self.assertTrue(dimension in ['activation'])

    def test_question_with_dimension_multi_dim(self):
        """
        When question belongs to more than a dimension, all of them
        should be returned
        """
        dimensions = {
            'activation': ['Q3', 'Q4'],
            'audience': ['Q3'],
        }
        dimension_list = question.get_question_dimension('Q3', dimensions)
        self.assertEqual(len(dimension_list), 2)
        for dimension in dimension_list:
            self.assertTrue(dimension in ['activation', 'audience'])


class DataReliableTest(TestCase):
    """Test case for `core.qualtrics.question.discard_scores` function."""

    one_minute_survey_result = {
        'Organization-sum': '0.0',
        'Organization-weightedAvg': '0.0',
        'Organization-weightedStdDev': '0.0',
        'sid': '2',
        'ResponseID': 'AAC',
        'Enter Embedded Data Field Name Here...': '',
        'sponsor': '',
        'company_name': 'new survey',
        'dmb': '0.5',
        'StartDate': '2018-07-31 14:16:06',
        'EndDate': '2018-07-31 14:17:06',

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

    four_minute_survey_result = {
        'Organization-sum': '0.0',
        'Organization-weightedAvg': '0.0',
        'Organization-weightedStdDev': '0.0',
        'sid': '2',
        'ResponseID': 'AAC',
        'Enter Embedded Data Field Name Here...': '',
        'sponsor': '',
        'company_name': 'new survey',
        'dmb': '0.5',
        'StartDate': '2018-07-31 14:16:06',
        'EndDate': '2018-07-31 14:20:06',

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

    ten_minute_survey_result = {
        'Organization-sum': '0.0',
        'Organization-weightedAvg': '0.0',
        'Organization-weightedStdDev': '0.0',
        'sid': '2',
        'ResponseID': 'AAC',
        'Enter Embedded Data Field Name Here...': '',
        'sponsor': '',
        'company_name': 'new survey',
        'dmb': '0.5',
        'StartDate': '2018-07-31 14:16:06',
        'EndDate': '2018-07-31 14:26:06',

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

    def test_survey_valid_time_check(self):
        exclude_score = question.discard_scores(self.one_minute_survey_result, 2)
        self.assertTrue(exclude_score)
        exclude_score = question.discard_scores(self.four_minute_survey_result, 2)
        self.assertFalse(exclude_score)
        exclude_score = question.discard_scores(self.ten_minute_survey_result, 2)
        self.assertFalse(exclude_score)

        exclude_score = question.discard_scores(self.one_minute_survey_result, 15)
        self.assertTrue(exclude_score)
        exclude_score = question.discard_scores(self.four_minute_survey_result, 15)
        self.assertTrue(exclude_score)
        exclude_score = question.discard_scores(self.ten_minute_survey_result, 15)
        self.assertTrue(exclude_score)


class CleanDataTest(TestCase):
    """Test `core.qualtrics.question.clean_survey_data` function."""

    def test_survey_clean(self):
        """Should return the expected cleaned dictionary"""

        dimensions = {
            'activation': ['Q3', 'Q4'],
            'audience': ['Q5_1', 'Q13'],
        }
        multi_answer_questions = ['Q13']

        survey_result = {
            'Organization-sum': '0.0',
            'Organization-weightedAvg': '0.0',
            'Organization-weightedStdDev': '0.0',
            'sid': '2',
            'ResponseID': 'AAC',
            'Enter Embedded Data Field Name Here...': '',
            'sponsor': '',
            'company_name': 'new survey',
            'dmb': '0.5',
            'StartDate': '2018-07-31 14:16:06',
            'EndDate': '2018-07-31 14:18:56',

            'Q1_1_TEXT': '',
            'Q1_2_TEXT': '',
            'Q2_1_TEXT': '',
            'Q2_2_TEXT': '',

            'Q3': '1',
            'Q4': '1',
            'Q5_1': '1',
            'Q13_133.1': '1',
            'Q13_100.2': '1',
            'Q13_150.3': '0',
            'Q13_233.4': '1',

        }
        expected_clean_data = {
            'Q3': ['1'],
            'Q4': ['1'],
            'Q5_1': ['1'],
            'Q13': ['1.33', '1.0', '0', '2.33'],

        }

        data = question.clean_survey_data(survey_result, dimensions, multi_answer_questions)
        self.assertCountEqual(expected_clean_data.keys(), data.keys())
        for k, v in expected_clean_data.items():
            self.assertListEqual(sorted(v), sorted(data[k]))

    def test_survey_clean_empty_q_answer(self):
        """Should keep the question with empty value"""
        survey_result = {
            'Organization-sum': '0.0',
            'Organization-weightedAvg': '0.0',
            'Organization-weightedStdDev': '0.0',
            'sid': '2',
            'ResponseID': 'AAC',
            'Enter Embedded Data Field Name Here...': '',
            'sponsor': '',
            'company_name': 'new survey',
            'dmb': '0.5',
            'StartDate': '2018-07-31 14:16:06',
            'EndDate': '2018-07-31 14:18:56',

            'Q1_1_TEXT': '',
            'Q1_2_TEXT': '',
            'Q2_1_TEXT': '',
            'Q2_2_TEXT': '',

            'Q3': '',
            'Q4': '1',
            'Q5_1': '1',
            'Q13_133.1': '1',
            'Q13_100.2': '1',
            'Q13_150.3': '0',
            'Q13_233.4': '1',

        }

        dimensions = {
            'activation': ['Q3', 'Q4'],
            'audience': ['Q5_1', 'Q13'],
        }
        multi_answer_questions = ['Q13']

        expected_clean_data = {
            'Q3': [''],
            'Q4': ['1'],
            'Q5_1': ['1'],
            'Q13': ['1.33', '1.0', '0', '2.33'],
        }

        data = question.clean_survey_data(survey_result, dimensions, multi_answer_questions)
        self.assertCountEqual(expected_clean_data.keys(), data.keys())
        for k, v in expected_clean_data.items():
            self.assertListEqual(sorted(v), sorted(data[k]))

    def test_survey_clean_text(self):
        """Should return the expected cleaned dictionary"""
        survey_result = {
            'Organization-sum': '0.0',
            'Organization-weightedAvg': '0.0',
            'Organization-weightedStdDev': '0.0',
            'sid': '2',
            'ResponseID': 'AAC',
            'Enter Embedded Data Field Name Here...': '',
            'sponsor': '',
            'company_name': 'new survey',
            'dmb': '0.5',
            'StartDate': '2018-07-31 14:16:06',
            'EndDate': '2018-07-31 14:18:56',

            'Q1_1_TEXT': '',
            'Q1_2_TEXT': '',
            'Q2_1_TEXT': '',
            'Q2_2_TEXT': '',

            'Q3': 'Some answer for Q3',
            'Q4': 'Some answer for Q4',
            'Q5_1': 'Some answer for Q5_1',
            'Q13_133.1': 'Some answer for Q13_133',
            'Q13_100.2': '0',
            'Q13_150.3': 'Some answer for Q13_150',
            'Q13_233.4': 'Some answer for Q13_233',

        }
        expected_clean_data = {
            'Q3': ['Some answer for Q3'],
            'Q4': ['Some answer for Q4'],
            'Q5_1': ['Some answer for Q5_1'],
            'Q13': ['Some answer for Q13_133', '0', 'Some answer for Q13_150', 'Some answer for Q13_233'],

        }

        dimensions = {
            'activation': ['Q3', 'Q4'],
            'audience': ['Q5_1', 'Q13'],
        }
        multi_answer_questions = ['Q13']

        data = question.clean_survey_data(survey_result, dimensions, multi_answer_questions)
        self.assertCountEqual(expected_clean_data.keys(), data.keys())
        for k, v in expected_clean_data.items():
            self.assertListEqual(sorted(v), sorted(data[k]))

    def test_question_tuple_skipped_if_not_found_by_regex(self):
        """When a question does not match the regex is not return by questions property."""
        survey_result = {
            'Organization-sum': '0.0',
            'Organization-weightedAvg': '0.0',
            'Organization-weightedStdDev': '0.0',
            'sid': '2',
            'ResponseID': 'AAC',
            'Enter Embedded Data Field Name Here...': '',
            'sponsor': '',
            'company_name': 'new survey',
            'dmb': '0.5',
            'StartDate': '2018-07-31 14:16:06',
            'EndDate': '2018-07-31 14:18:56',

            'Q1_1_TEXT': '',
            'Q1_2_TEXT': '',
            'Q2_1_TEXT': '',
            'Q2_2_TEXT': '',

            'Q3': '1',
            'Q4': '1',
            'Q5_1': '1',
            'Q13_133.1': '1',
            'Q13_100.2': '1',
            'Q13_150.3': '0',
            'Q13_233.4': '1',

        }

        dimensions = {
            'activation': ['Q3', 'Q4'],
            'audience': ['Q5_1', 'Q13'],
        }
        multi_answer_questions = ['Q13']

        data = question.clean_survey_data(survey_result, dimensions, multi_answer_questions)
        self.assertIsNone(data.get('Q1_1_TEXT'))


class DataToQuestionTextTest(TestCase):
    """Test case for `core.qualtrics.question.data_to_questions_text` function."""

    survey_result = {
        'Organization-sum': '0.0',
        'Organization-weightedAvg': '0.0',
        'Organization-weightedStdDev': '0.0',
        'sid': '2',
        'ResponseID': 'AAC',
        'Enter Embedded Data Field Name Here...': '',
        'sponsor': '',
        'company_name': 'new survey',
        'dmb': '0.5',
        'Q1_1_TEXT': '',
        'Q1_2_TEXT': '',
        'Q2_1_TEXT': '',
        'Q2_2_TEXT': '',

        'Q3': 'Some answer for Q3',
        'Q4': 'Some answer for Q4',
        'Q12': 'Some answer for Q12',
        'Q13_133.1': 'Some answer for Q13_133',
        'Q13_100.2': '0',
        'Q13_150.3': 'Some answer for Q13_150',
        'Q13_233.4': 'Some answer for Q13_233',
    }

    def setUp(self):

        dimensions = {
            'activation': ['Q3', 'Q12'],
            'audience': ['Q13'],
        }
        multi_answer_questions = ['Q13']

        questions = question.data_to_questions_text(self.survey_result, dimensions, multi_answer_questions)
        self.question_dict = {item[0]: item for item in questions}

    def test_question_tuple_correctly_generated(self):
        """When weight and category are found, should be set."""
        question, answers = self.question_dict.get('Q3')

        self.assertEqual(question, 'Q3')
        self.assertItemsEqual(answers, ['Some answer for Q3'])

    def test_multiple_answer_question_tuple(self):
        """When an element is not selected on multiselect text, it should be set to empty string."""
        question, answers = self.question_dict.get('Q13')
        expected_answers = ['Some answer for Q13_133', '', 'Some answer for Q13_150', 'Some answer for Q13_233']
        self.assertItemsEqual(answers, expected_answers)
        self.assertCountEqual(answers, expected_answers)

        self.assertEqual(set(expected_answers), set(answers))
