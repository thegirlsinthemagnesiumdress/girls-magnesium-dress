import core.qualtrics as qualtrics
from djangae.test import TestCase
from django.conf import settings
from django.test import override_settings


class QualtricsTest(TestCase):
    """Test class for utility funcions in qualtrics module."""
    def test__weighted_questions_average(self):
        """Test the right benchmark is calculated given an array of responses."""
        responses = [
            ('Q1', 1.0, 1, 'dimension_A'),
            ('Q2', 3.0, 1, 'dimension_A'),
        ]

        weighted_average = qualtrics._weighted_questions_average(responses)
        self.assertEqual(weighted_average, 2)

    def test__weighted_questions_average_complex(self):
        """Test that given an array of questions the right weighetd average is calculated."""
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
        average = qualtrics._weighted_questions_average(responses)
        self.assertAlmostEqual(average, weighted_average, places=4)

    def test__weighted_questions_average_empty_list(self):
        """Test the right benchmark is calculated given an array of responses."""
        responses = []

        weighted_average = qualtrics._weighted_questions_average(responses)
        self.assertEqual(weighted_average, 1)


class CalculateResponseBenchmarkTest(TestCase):
    """Test class for `calculate_response_benchmark` function."""

    def test_calculate_response_benchmark_single_dimension(self):
        """Test for a single dimension."""
        responses = [
            ('Q1', 1.0, 1, 'dimension_A'),
            ('Q2', 3.0, 1, 'dimension_A'),
            ('Q3', 2.0, 2, 'dimension_A'),
        ]

        dmb, dmb_d_dictionary = qualtrics.calculate_response_benchmark(responses)
        self.assertIsInstance(dmb_d_dictionary, dict)
        self.assertEqual(len(dmb_d_dictionary), 1)
        self.assertTrue('dimension_A' in dmb_d_dictionary)
        self.assertEqual(dmb_d_dictionary.get('dimension_A'), 2)
        self.assertEqual(dmb, 2)

    def test_calculate_response_benchmark_multi_dimensions(self):
        """Test for a multiple dimension."""
        responses = [
            ('Q1', 1.0, 1, 'dimension_A'),
            ('Q2', 3.0, 1, 'dimension_A'),
            ('Q3', 2.0, 2, 'dimension_A'),
            ('Q4', 1.0, 4, 'dimension_B'),
            ('Q5', 1.0, 2, 'dimension_B'),
        ]

        dmb, dmb_d_dictionary = qualtrics.calculate_response_benchmark(responses)

        self.assertIsInstance(dmb_d_dictionary, dict)
        self.assertEqual(len(dmb_d_dictionary), 2)
        self.assertTrue('dimension_A' in dmb_d_dictionary)
        self.assertTrue('dimension_B' in dmb_d_dictionary)
        self.assertEqual(dmb_d_dictionary.get('dimension_A'), 2)
        self.assertEqual(dmb_d_dictionary.get('dimension_B'), 1)
        self.assertEqual(dmb, 1.5)


@override_settings(
    DIMENSIONS={
        'dimension_A': ['Q1', 'Q2'],
        'dimension_B': ['Q3'],
        'dimension_C': ['Q2'],
        'dimension_D': ['Q1'],
    }
)
class CalculateGroupBenchmarkTest(TestCase):
    """Test class for `calculate_group_benchmark` function."""

    def test_calculate_group_benchmark_single_response(self):
        """Test for a single reponse."""
        responses = [
            [
                ('Q1', 1.0, 1, 'dimension_A'),
                ('Q2', 3.0, 1, 'dimension_A'),
                ('Q3', 2.0, 2, 'dimension_B'),
            ]
        ]

        dmb, dmb_d_dictionary = qualtrics.calculate_group_benchmark(responses)
        self.assertIsInstance(dmb_d_dictionary, dict)
        self.assertEqual(len(dmb_d_dictionary), len(settings.DIMENSIONS))

        # check all dimensions defined in settings are in the response dictionary
        for dimension in settings.DIMENSIONS.keys():
            self.assertTrue(dimension in dmb_d_dictionary)

        # each element of `dmb_d_dictionary` will be the average of weighted averages by dimension
        dimension_A_average = dmb_d_dictionary.get('dimension_A') # noqa
        dimension_B_average = dmb_d_dictionary.get('dimension_B') # noqa
        dimension_C_average = dmb_d_dictionary.get('dimension_C') # noqa
        dimension_D_average = dmb_d_dictionary.get('dimension_D') # noqa

        # for dimension_A it will be the average between:
        # weighted average of dimension_A for `responses[0]` (that is 2.0)
        # so the average will be 2.0
        self.assertEqual(dimension_A_average, 2.0)

        # dimension_B:
        # weighted average for `responses[0]`: 2.0
        # average: 2.0
        self.assertEqual(dimension_B_average, 2.0)

        # dimension_C:
        # weighted average for `responses[0]`: 0 (there is not dimension_C in `resposes[0]`)
        # average: 0
        self.assertEqual(dimension_C_average, 0)

        # dimension_D:
        # weighted average for `responses[0]`: 0
        # average: 0
        self.assertEqual(dimension_D_average, 0)

        # dmb represents the average between all elements of `dmb_d_dictionary`
        self.assertEqual(dmb, 1.0)

    def test_calculate_response_benchmark_multi_responses(self):
        """Test for a multiple responses."""
        responses = [
            [
                ('Q1', 1.0, 1, 'dimension_A'),
                ('Q2', 3.0, 1, 'dimension_A'),
                ('Q3', 2.0, 2, 'dimension_B'),
            ],
            [
                ('Q1', 1.0, 1, 'dimension_C'),
                ('Q2', 3.0, 1, 'dimension_C'),
                ('Q3', 2.0, 2, 'dimension_A'),
            ]
        ]

        dmb, dmb_d_dictionary = qualtrics.calculate_group_benchmark(responses)
        self.assertIsInstance(dmb_d_dictionary, dict)
        self.assertEqual(len(dmb_d_dictionary), len(settings.DIMENSIONS))

        # check all dimensions defined in settings are in the response dictionary
        for dimension in settings.DIMENSIONS.keys():
            self.assertTrue(dimension in dmb_d_dictionary)

        # each element of `dmb_d_dictionary` will be the average of weighted averages by dimension
        dimension_A_average = dmb_d_dictionary.get('dimension_A') # noqa
        dimension_B_average = dmb_d_dictionary.get('dimension_B') # noqa
        dimension_C_average = dmb_d_dictionary.get('dimension_C') # noqa
        dimension_D_average = dmb_d_dictionary.get('dimension_D') # noqa

        # for dimension_A it will be the average between:
        # weighted average of dimension_A for `responses[0]` (that is 2.0) and
        # weighted average of dimension_A for `response[1]` (that is 2.0)
        # so the average will be 2.0
        self.assertEqual(dimension_A_average, 2.0)

        # dimension_B:
        # weighted average for `responses[0]`: 2.0
        # weighted average for `response[1]`: 0 (there is not dimension_B in `resposes[1]`)
        # average: 1.0
        self.assertEqual(dimension_B_average, 1.0)

        # dimension_C:
        # weighted average for `responses[0]`: 0 (there is not dimension_C in `resposes[0]`)
        # weighted average for `response[1]`: 2.0
        # average: 1.0
        self.assertEqual(dimension_C_average, 1.0)

        # dimension_D:
        # weighted average for `responses[0]`: 0
        # weighted average for `response[1]`: 0
        # average: 0
        self.assertEqual(dimension_D_average, 0)

        # dmb represents the average between all elements of `dmb_d_dictionary`
        self.assertEqual(dmb, 1.0)
