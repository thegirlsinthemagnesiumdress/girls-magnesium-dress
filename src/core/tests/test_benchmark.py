from core.tests.mocks import INDUSTRIES
from djangae.test import TestCase
from django.test import override_settings
from core.tests.mommy_recepies import make_survey, make_survey_result
from core import benchmark
from django.conf import settings


@override_settings(
    INDUSTRIES=INDUSTRIES,
    MIN_ITEMS_INDUSTRY_THRESHOLD=2
)
class SurveyDMBListTest(TestCase):
    """Test case for `core.Survey.get_surveys_by_industry` function."""

    def _make_survey_with_result(self, industry):
        survey = make_survey(industry=industry)
        survey_res = make_survey_result(survey=survey)
        survey.last_survey_result = survey_res
        survey.save()

    def setUp(self):
        self._make_survey_with_result(industry='ic-o')
        self._make_survey_with_result(industry='ic-o')
        self._make_survey_with_result(industry='ic-t')

    def test_get_surveys_by_industry_fallback_to_parent_industry(self):
        """Test if there are not enough element for that industry,
        it will fall back to parent industry."""

        surveys, industry = benchmark.get_surveys_by_industry(initial_industry='ic-o')
        self.assertEqual(len(surveys), 3)
        self.assertEqual(industry, 'ic')

    def test_get_surveys_by_industry_current_industry(self):
        """Test if there are enough element for that industry."""

        self._make_survey_with_result(industry='ic-s')
        self._make_survey_with_result(industry='ic-s')
        self._make_survey_with_result(industry='ic-s')

        surveys, industry = benchmark.get_surveys_by_industry(initial_industry='ic-s')
        self.assertEqual(len(surveys), 3)
        self.assertEqual(industry, 'ic-s')

    def test_get_surveys_by_industry_fallback_global(self):
        """Test if there are not enough elements for that industry and
        neither for the parent industry, use global."""

        surveys, industry = benchmark.get_surveys_by_industry(initial_industry='edu-fe')
        self.assertEqual(len(surveys), 3)
        self.assertEqual(industry, None)

    def test_get_surveys_by_industry_global_industry(self):
        """Test if there are not enough elements for that industry and
        neither for the parent industry, use global."""

        surveys, industry = benchmark.get_surveys_by_industry(initial_industry='edu')
        self.assertEqual(len(surveys), 3)
        self.assertIsNone(industry)

    @override_settings(
        MIN_ITEMS_INDUSTRY_THRESHOLD=10
    )
    def test_get_surveys_by_industry_global_industry_threshold_never_reached(self):
        """Test if there are not enough elements for that industry and
        neither for the parent industry, use global."""

        surveys, industry = benchmark.get_surveys_by_industry(initial_industry='edu')
        self.assertEqual(len(surveys), 3)
        self.assertEqual(industry, None)

    def test_get_surveys_by_industry_invalid_industry(self):
        """Test if initial industry is not valid it should raise an `Exception`"""
        self.assertRaises(ValueError, benchmark.get_surveys_by_industry, 'invalid')


@override_settings(
    INDUSTRIES={
        'co': ('Construction', None),
        'edu': ('Education', None),
        'edu-fe': ('Further education', 'edu'),
        'edu-o': ('Other', 'edu'),
        'edu-pe': ('Primary education', 'edu'),
        'edu-se': ('Secondary education', 'edu'),
        'egsw': ('Electricity, gas, steam, water', None),
        'fi': ('Financial and Insurance', None),
        'fi-b': ('Banking', 'fi'),
        'fi-i': ('Insurance', 'fi'),
        'fi-o': ('Other', 'fi'),
    }
)
class GetPathTest(TestCase):
    """Test class for `core.benchmark._get_path` function."""

    def test_get_path_leaf_element(self):
        path = benchmark._get_path('co', settings.INDUSTRIES)
        self.assertIsInstance(path, list)
        self.assertEqual(len(path), 2)
        self.assertIn('co', path)
        self.assertIn(None, path)

    def test_get_path_nested_leaf_element(self):
        path = benchmark._get_path('fi-i', settings.INDUSTRIES)
        self.assertIsInstance(path, list)
        self.assertEqual(len(path), 3)
        self.assertIn('fi-i', path)
        self.assertIn('fi', path)
        self.assertIn(None, path)

    def test_get_path_intermediate_element(self):
        path = benchmark._get_path('fi', settings.INDUSTRIES)
        self.assertIsInstance(path, list)
        self.assertEqual(len(path), 2)
        self.assertIn('fi', path)
        self.assertIn(None, path)

    def test_get_path_root_element(self):
        path = benchmark._get_path(None, settings.INDUSTRIES)
        self.assertIsInstance(path, list)
        self.assertEqual(len(path), 1)
        self.assertIn(None, path)
