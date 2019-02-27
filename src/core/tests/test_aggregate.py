from core.tests.mocks import INDUSTRIES
from djangae.test import TestCase
from django.test import override_settings
from core.tests.mommy_recepies import make_survey, make_survey_result, make_industry_benchmark
from core import aggregate
from django.conf import settings
from core.models import SurveyResult


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

        survey_results, industry = aggregate.get_surveys_by_industry('ic-o', settings.MIN_ITEMS_INDUSTRY_THRESHOLD)
        self.assertEqual(len(survey_results), 3)
        self.assertEqual(industry, 'ic')

    def test_get_surveys_by_industry_current_industry(self):
        """Test if there are enough element for that industry."""

        self._make_survey_with_result(industry='ic-s')
        self._make_survey_with_result(industry='ic-s')
        self._make_survey_with_result(industry='ic-s')

        survey_results, industry = aggregate.get_surveys_by_industry('ic-s', settings.MIN_ITEMS_INDUSTRY_THRESHOLD)
        self.assertEqual(len(survey_results), 3)
        self.assertEqual(industry, 'ic-s')

    def test_get_surveys_by_industry_fallback_global(self):
        """Test if there are not enough elements for that industry and
        neither for the parent industry, use global."""

        survey_results, industry = aggregate.get_surveys_by_industry('edu-fe', settings.MIN_ITEMS_INDUSTRY_THRESHOLD)
        self.assertEqual(len(survey_results), 3)
        self.assertEqual(industry, None)

    def test_get_surveys_by_industry_global_industry(self):
        """Test if there are not enough elements for that industry and
        neither for the parent industry, use global."""

        survey_results, industry = aggregate.get_surveys_by_industry('edu', settings.MIN_ITEMS_INDUSTRY_THRESHOLD)
        self.assertEqual(len(survey_results), 3)
        self.assertIsNone(industry)

    @override_settings(
        MIN_ITEMS_INDUSTRY_THRESHOLD=10
    )
    def test_get_surveys_by_industry_global_industry_threshold_never_reached(self):
        """Test if there are not enough elements for that industry and
        neither for the parent industry, use global."""

        survey_results, industry = aggregate.get_surveys_by_industry('edu', settings.MIN_ITEMS_INDUSTRY_THRESHOLD)
        self.assertEqual(len(survey_results), 3)
        self.assertEqual(industry, None)

    def test_get_surveys_by_industry_invalid_industry(self):
        """Test if initial industry is not valid it should raise an `Exception`"""
        self.assertRaises(
            ValueError,
            aggregate.get_surveys_by_industry,
            'invalid',
            settings.MIN_ITEMS_INDUSTRY_THRESHOLD
        )


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
    """Test class for `core.aggregate.get_path` function."""

    def test_get_path_leaf_element(self):
        path = aggregate.get_path('co', settings.INDUSTRIES)
        self.assertIsInstance(path, list)
        self.assertEqual(len(path), 2)
        self.assertIn('co', path)
        self.assertIn(None, path)

    def test_get_path_nested_leaf_element(self):
        path = aggregate.get_path('fi-i', settings.INDUSTRIES)
        self.assertIsInstance(path, list)
        self.assertEqual(len(path), 3)
        self.assertIn('fi-i', path)
        self.assertIn('fi', path)
        self.assertIn(None, path)

    def test_get_path_intermediate_element(self):
        path = aggregate.get_path('fi', settings.INDUSTRIES)
        self.assertIsInstance(path, list)
        self.assertEqual(len(path), 2)
        self.assertIn('fi', path)
        self.assertIn(None, path)

    def test_get_path_root_element(self):
        path = aggregate.get_path(None, settings.INDUSTRIES)
        self.assertIsInstance(path, list)
        self.assertEqual(len(path), 1)
        self.assertIn(None, path)

    def test_get_path_root_element_custom(self):
        path = aggregate.get_path('fi', settings.INDUSTRIES, root_element='ROOT')
        self.assertIsInstance(path, list)
        self.assertEqual(len(path), 2)
        self.assertIn('fi', path)
        self.assertIn('ROOT', path)


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
    },
    ALL_INDUSTRIES=('all', 'all'),
)
class UpdatableIndustries(TestCase):
    """Test class for `core.aggregate.updatable_industries` function."""

    def _make_survey_with_result(self, industry):
        survey = make_survey(industry=industry)
        survey_res = make_survey_result(survey=survey)
        survey.last_survey_result = survey_res
        survey.save()
        return survey

    def setUp(self):
        self.result_1 = self._make_survey_with_result(industry='fi-b')
        self.result_2 = self._make_survey_with_result(industry='fi-b')
        self.result_3 = self._make_survey_with_result(industry='fi-o')
        self.result_4 = self._make_survey_with_result(industry='edu-o')

    def test_updatable_industries_return_full_hierarchy(self):
        survey_results = SurveyResult.objects.all()
        industry_to_be_updated = aggregate.updatable_industries(survey_results)

        fi_b = industry_to_be_updated.get('fi-b')
        fi_o = industry_to_be_updated.get('fi-o')
        fi = industry_to_be_updated.get('fi')
        all_ind = industry_to_be_updated.get('all')

        # check for fi-b industry
        self.assertEqual(len(fi_b), 2)
        fi_b_ids = set([res.pk for res in fi_b])
        expected_fi_b = set([self.result_1.last_survey_result.pk, self.result_2.last_survey_result.pk])
        self.assertSetEqual(fi_b_ids, expected_fi_b)

        # check for fi-o industry
        self.assertEqual(len(fi_o), 1)
        fi_o_ids = set([res.pk for res in fi_o])
        expected_fi_o = set([self.result_3.last_survey_result.pk])
        self.assertSetEqual(fi_o_ids, expected_fi_o)

        # check for fi industry
        self.assertEqual(len(fi), 3)
        fi_ids = set([res.pk for res in fi])
        expected_fi = set([
            self.result_1.last_survey_result.pk,
            self.result_2.last_survey_result.pk,
            self.result_3.last_survey_result.pk,
        ])
        self.assertSetEqual(fi_ids, expected_fi)

        # check for all industry
        self.assertEqual(len(all_ind), 4)
        all_ids = set([res.pk for res in all_ind])
        expected_all = set([
            self.result_1.last_survey_result.pk,
            self.result_2.last_survey_result.pk,
            self.result_3.last_survey_result.pk,
            self.result_4.last_survey_result.pk,
        ])
        self.assertSetEqual(all_ids, expected_all)


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
    },
    ALL_INDUSTRIES=('all', 'all'),
    MIN_ITEMS_INDUSTRY_THRESHOLD=2,
)
class IndustryBenchmark(TestCase):
    """Test class for `core.aggregate.industry_benchmark` function."""

    def setUp(self):
        make_industry_benchmark(industry='edu', dmb_value=2.0)
        make_industry_benchmark(industry='all', dmb_value=1.0)

    def test_industry_benchmark_industry_has_value(self):
        """When industry has a value for dmb, it should return it."""
        make_industry_benchmark(industry='edu-o', dmb_value=3.0)
        industry_to_be_updated = aggregate.industry_benchmark('edu-o')

        got_dmb, got_dmb_d, got_industry = industry_to_be_updated

        self.assertEqual(got_dmb, 3.0)
        self.assertEqual(got_industry, 'edu-o')

    def test_industry_benchmark_industry_fallback_parent(self):
        """When industry does not have a value for dmb, it should  fallback to parent."""
        make_industry_benchmark(industry='edu-o')
        industry_to_be_updated = aggregate.industry_benchmark('edu-o')
        got_dmb, got_dmb_d, got_industry = industry_to_be_updated

        self.assertEqual(got_dmb, 2.0)
        self.assertEqual(got_industry, 'edu')

    def test_industry_benchmark_industry_fallback_to_root(self):
        """When industry does not have a value for dmb, it should fallback to parent,
        and so on until you get eventualy to root."""
        industry_to_be_updated = aggregate.industry_benchmark('fi-b')
        got_dmb, got_dmb_d, got_industry = industry_to_be_updated

        self.assertEqual(got_dmb, 1.0)
        self.assertEqual(got_industry, 'all')


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
    },
    ALL_INDUSTRIES=('all', 'all'),
    MIN_ITEMS_INDUSTRY_THRESHOLD=2,
)
class IndustryBestPractice(TestCase):
    """Test class for `core.aggregate.industry_best_practice` function."""

    def setUp(self):
        make_industry_benchmark(industry='edu', dmb_bp_value=2.0)
        make_industry_benchmark(industry='all', dmb_bp_value=1.0)

    def test_industry_benchmark_industry_has_value(self):
        """When industry has a value for dmb, it should return it."""
        make_industry_benchmark(industry='edu-o', dmb_bp_value=3.0)
        industry_to_be_updated = aggregate.industry_best_practice('edu-o')

        got_dmb, got_dmb_d, got_industry = industry_to_be_updated

        self.assertEqual(got_dmb, 3.0)
        self.assertEqual(got_industry, 'edu-o')

    def test_industry_benchmark_industry_fallback_parent(self):
        """When industry does not have a value for dmb, it should  fallback to parent."""
        make_industry_benchmark(industry='edu-o')
        industry_to_be_updated = aggregate.industry_best_practice('edu-o')
        got_dmb, got_dmb_d, got_industry = industry_to_be_updated

        self.assertEqual(got_dmb, 2.0)
        self.assertEqual(got_industry, 'edu')

    def test_industry_benchmark_industry_fallback_to_root(self):
        """When industry does not have a value for dmb, it should fallback to parent,
        and so on until you get eventualy to root."""
        industry_to_be_updated = aggregate.industry_best_practice('fi-b')
        got_dmb, got_dmb_d, got_industry = industry_to_be_updated

        self.assertEqual(got_dmb, 1.0)
        self.assertEqual(got_industry, 'all')
