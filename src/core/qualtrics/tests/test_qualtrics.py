from core.qualtrics import benchmark
from djangae.test import TestCase
from django.conf import settings
from django.test import override_settings


class CalculateResponseBenchmarkTest(TestCase):
    """Test class for `calculate_response_benchmark` function."""

    def test_calculate_response_benchmark_single_dimension(self):
        """Test for a single dimension."""
        responses = [
            ('Q1', 1.0, 1, 'dimension_A'),
            ('Q2', 3.0, 1, 'dimension_A'),
            ('Q3', 2.0, 2, 'dimension_A'),
        ]

        dmb, dmb_d_dictionary = benchmark.calculate_response_benchmark(responses)
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

        dmb, dmb_d_dictionary = benchmark.calculate_response_benchmark(responses)

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
class CalculateGroupFromRawResponsesBenchmarkTest(TestCase):
    """Test class for `calculate_group_benchmark_from_raw_responses` function."""

    def test_calculate_group_benchmark_from_raw_responses_single_response(self):
        """Test for a single reponse."""
        responses = [
            [
                ('Q1', 1.0, 1, 'dimension_A'),
                ('Q2', 3.0, 1, 'dimension_A'),
                ('Q3', 2.0, 2, 'dimension_B'),
            ]
        ]

        dmb, dmb_d_dictionary = benchmark.calculate_group_benchmark_from_raw_responses(responses)
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

        dmb, dmb_d_dictionary = benchmark.calculate_group_benchmark_from_raw_responses(responses)
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


@override_settings(
    DIMENSIONS={
        'dimension_A': ['Q1', 'Q2'],
        'dimension_B': ['Q3'],
        'dimension_C': ['Q2'],
        'dimension_D': ['Q1'],
    }
)
class CalculateDimensionBenchmarkTest(TestCase):
    """Test class for `calculate_group_benchmark` function."""

    def test_calculate_group_benchmark_from_raw_responses_single_response(self):
        """Test for a single reponse."""
        dmb_d_list = [
            {
                'dimension_A': 2.0,
                'dimension_B': 2.0,
            },
        ]

        dmb, dmb_d_dictionary = benchmark.calculate_group_benchmark(dmb_d_list)
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
        # weighted average of dimension_A for `dmb_d_list[0]` (that is 2.0)
        # so the average will be 2.0
        self.assertEqual(dimension_A_average, 2.0)

        # dimension_B:
        # weighted average for `dmb_d_list[0]`: 2.0
        # average: 2.0
        self.assertEqual(dimension_B_average, 2.0)

        # dimension_C:
        # weighted average for `dmb_d_list[0]`: 0 (there is not dimension_C in `resposes[0]`)
        # average: 0
        self.assertEqual(dimension_C_average, 0)

        # dimension_D:
        # weighted average for `dmb_d_list[0]`: 0
        # average: 0
        self.assertEqual(dimension_D_average, 0)

        # dmb represents the average between all elements of `dmb_d_dictionary`
        self.assertEqual(dmb, 1.0)

    def test_calculate_response_benchmark_multi_responses(self):
        """Test for a multiple dmb_d_list."""
        dmb_d_list = [
            {
                'dimension_A': 2.0,
                'dimension_B': 2.0,
            },
            {
                'dimension_A': 2.0,
                'dimension_C': 2.0,
            },
        ]

        dmb, dmb_d_dictionary = benchmark.calculate_group_benchmark(dmb_d_list)
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
        # dimension_A (weighted average) for `dmb_d_list[0]` (that is 2.0) and
        # dimension_A (weighted average) for `dmb_d_list[1]` (that is 2.0)
        # so the average will be 2.0
        self.assertEqual(dimension_A_average, 2.0)

        # dimension_B:
        # `dmb_d_list[0]`: 2.0
        # `dmb_d_list[1]`: 0 (there is not dimension_B in `resposes[1]`)
        # average: 1.0
        self.assertEqual(dimension_B_average, 1.0)

        # dimension_C:
        # `dmb_d_list[0]`: 0 (there is not dimension_C in `resposes[0]`)
        # `dmb_d_list[1]`: 2.0
        # average: 1.0
        self.assertEqual(dimension_C_average, 1.0)

        # dimension_D:
        # `dmb_d_list[0]`: 0
        # `dmb_d_list[1]`: 0
        # average: 0
        self.assertEqual(dimension_D_average, 0)

        # dmb represents the average between all elements of `dmb_d_dictionary`
        self.assertEqual(dmb, 1.0)


@override_settings(
    DIMENSIONS={
        'dimension_A': ['Q1', 'Q2'],
        'dimension_B': ['Q3'],
        'dimension_C': ['Q2'],
        'dimension_D': ['Q1'],
    }
)
class CalculateBestPracticeTest(TestCase):
    """Test class for `calculate_best_practice` function."""

    def test_calculate_best_practice_single_response(self):
        """Test for a single reponse."""
        dmb_d_list = [
            {
                'dimension_A': 2.0,
                'dimension_B': 2.0,
            },
        ]

        dmb, dmb_d_max_dictionary = benchmark.calculate_best_practice(dmb_d_list)
        self.assertIsInstance(dmb_d_max_dictionary, dict)
        self.assertEqual(len(dmb_d_max_dictionary), len(settings.DIMENSIONS))

        # check all dimensions defined in settings are in the response dictionary
        for dimension in settings.DIMENSIONS.keys():
            self.assertTrue(dimension in dmb_d_max_dictionary)

        # each element of `dmb_d_max_dictionary` will be the max of weighted averages by dimension
        dimension_A_max = dmb_d_max_dictionary.get('dimension_A') # noqa
        dimension_B_max = dmb_d_max_dictionary.get('dimension_B') # noqa
        dimension_C_max = dmb_d_max_dictionary.get('dimension_C') # noqa
        dimension_D_max = dmb_d_max_dictionary.get('dimension_D') # noqa

        self.assertEqual(dimension_A_max, 2.0)
        self.assertEqual(dimension_B_max, 2.0)
        self.assertEqual(dimension_C_max, 0)
        self.assertEqual(dimension_D_max, 0)

        # dmb represents the average between all elements of `dmb_d_max_dictionary`
        self.assertEqual(dmb, 1.0)

    def test_calculate_response_benchmark_multi_responses(self):
        """Test for a multiple dmb_d_list."""
        dmb_d_list = [
            {
                'dimension_A': 2.0,
                'dimension_B': 2.0,
            },
            {
                'dimension_A': 1.0,
                'dimension_C': 2.0,
            },
        ]

        dmb, dmb_d_max_dictionary = benchmark.calculate_best_practice(dmb_d_list)
        self.assertIsInstance(dmb_d_max_dictionary, dict)
        self.assertEqual(len(dmb_d_max_dictionary), len(settings.DIMENSIONS))

        # check all dimensions defined in settings are in the response dictionary
        for dimension in settings.DIMENSIONS.keys():
            self.assertTrue(dimension in dmb_d_max_dictionary)

        # each element of `dmb_d_max_dictionary` will be the max of weighted averages by dimension
        dimension_A_max = dmb_d_max_dictionary.get('dimension_A') # noqa
        dimension_B_max = dmb_d_max_dictionary.get('dimension_B') # noqa
        dimension_C_max = dmb_d_max_dictionary.get('dimension_C') # noqa
        dimension_D_max = dmb_d_max_dictionary.get('dimension_D') # noqa

        self.assertEqual(dimension_A_max, 2.0)
        self.assertEqual(dimension_B_max, 2.0)
        self.assertEqual(dimension_C_max, 2.0)
        self.assertEqual(dimension_D_max, 0)

        # dmb represents the average between all elements of `dmb_d_max_dictionary`
        self.assertEqual(dmb, 1.5)
