from core.tests.mocks import  qualtrics_export, weights, dimensions, response_0_questions, response_1_questions, DMB, response_1_overall
from djangae.test import TestCase
import core.qualtrics as qualtrics
from mock import Mock, patch

def sortQuestion(q):
    question_key_regex = re.compile(r'^Q(\d+)(_\d+)?$')


class QualtricsTest(TestCase):
    def setUp(self):
        self.qualtrics_export = qualtrics_export
        qualtrics.weights = weights
        qualtrics.dimensions = dimensions

    def assert_questions_array_equality(self, qs_mock, qs):
        for q in qs_mock:
            not_sorted_q = filter(lambda not_sorted_q:  not_sorted_q[0] == q[0], qs)[0]
            self.assertEqual(q, not_sorted_q)

    @patch('project.requests.get')
    def test_get_results(self, mock_get):
        mock_get.return_value.ok = True

        # Call the service, which will send a request to the server.
        data = qualtrics.get_results()

        # If the request is sent successfully, then I expect a response to be returned.
        self.assertIsInstance(data, dict)

    def test_get_question_dimension(self):
        """
        Test that the given a question_id the given dimension is returned
        """
        dimension = qualtrics.get_question_dimension('Q6')
        self.assertEqual(dimension, 'dimension_B')

    def test_to_questions_array(self):
        """
        Test that given a qualtrics export data object an array of questions object is returned
        """
        questions = qualtrics.to_questions_array(qualtrics_export['responses'][0])
        self.assert_questions_array_equality(response_0_questions, questions)


    def test_weighted_questions_average(self):
        """
        Test that given an array of questions the right weighetd average is calculated
        """
        average = qualtrics.weighted_questions_average(response_0_questions)
        self.assertAlmostEqual(average, response_1_overall, places=4)

    def test_get_responses_by_field(self):
        """
        Test that given a qualtrics export data object it can be queried/filterd by field
        """
        responses_by_field = qualtrics.get_responses_by_field(qualtrics_export, 'sid')
        self.assertEqual(responses_by_field.keys(), ['1', '2'])
        self.assert_questions_array_equality(response_0_questions, responses_by_field['1'][0])
        self.assert_questions_array_equality(response_1_questions, responses_by_field['1'][1])

    def test_calculate_benchmark(self):
        """
        Test the right benchmark is calculated given an array of responses.
        """
        b = qualtrics.calculate_benchmark([response_0_questions, response_1_questions])
        self.assertEqual(b, DMB['survey']['1']['overall'])

    def test_calculate_benchmark_by_dimension(self):
        """
        Test the right benchmark is calculated given an array of responses.
        """
        b = qualtrics.calculate_benchmark([response_0_questions, response_1_questions], by_dimension=True)
        self.assertIsInstance(b, dict)
        self.assertEqual(b.keys(), dimensions.keys())
        self.assertAlmostEqual(b['dimension_A'], DMB['survey']['1']['category_overall']['dimension_A'], places=4)



