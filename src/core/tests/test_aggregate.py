from djangae.test import TestCase
from django.test import override_settings
from core.tests import mommy_recepies
from core import aggregate
from core.models import SurveyResult
from core.tests import mocks


class GetPathTest(TestCase):
    """Test class for `core.aggregate.get_path` function."""

    def setUp(self):
        self.industries_list = {
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

    def test_get_path_leaf_element(self):
        path = aggregate.get_path('co', self.industries_list)
        self.assertIsInstance(path, list)
        self.assertEqual(len(path), 2)
        self.assertIn('co', path)
        self.assertIn(None, path)

    def test_get_path_nested_leaf_element(self):
        path = aggregate.get_path('fi-i', self.industries_list)
        self.assertIsInstance(path, list)
        self.assertEqual(len(path), 3)
        self.assertIn('fi-i', path)
        self.assertIn('fi', path)
        self.assertIn(None, path)

    def test_get_path_intermediate_element(self):
        path = aggregate.get_path('fi', self.industries_list)
        self.assertIsInstance(path, list)
        self.assertEqual(len(path), 2)
        self.assertIn('fi', path)
        self.assertIn(None, path)

    def test_get_path_root_element(self):
        path = aggregate.get_path(None, self.industries_list)
        self.assertIsInstance(path, list)
        self.assertEqual(len(path), 1)
        self.assertIn(None, path)

    def test_get_path_root_element_custom(self):
        path = aggregate.get_path('fi', self.industries_list, root_element='ROOT')
        self.assertIsInstance(path, list)
        self.assertEqual(len(path), 2)
        self.assertIn('fi', path)
        self.assertIn('ROOT', path)


@override_settings(
    TENANTS=mocks.MOCKED_TENANTS,
    ALL_INDUSTRIES=('all', 'all'),
)
class UpdatableIndustries(TestCase):
    """Test class for `core.aggregate.updatable_industries` function."""

    def setUp(self):
        self.result_1 = mommy_recepies.make_survey_with_result(industry='fi-b', tenant='tenant1')
        self.result_2 = mommy_recepies.make_survey_with_result(industry='fi-b', tenant='tenant1')
        self.result_3 = mommy_recepies.make_survey_with_result(industry='fi-o', tenant='tenant1')
        self.result_4 = mommy_recepies.make_survey_with_result(industry='edu-o', tenant='tenant1')

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
    ALL_INDUSTRIES=('all', 'all'),
    MIN_ITEMS_INDUSTRY_THRESHOLD=2,
    TENANTS=mocks.MOCKED_TENANTS,
)
class IndustryBenchmark(TestCase):
    """Test class for `core.aggregate.industry_benchmark` function."""

    def setUp(self):
        mommy_recepies.make_industry_benchmark(tenant='tenant1', industry='edu', dmb_value=2.0)
        mommy_recepies.make_industry_benchmark(tenant='tenant1', industry='all', dmb_value=1.0)

    def test_industry_benchmark_industry_has_value(self):
        """When industry has a value for dmb, it should return it."""
        mommy_recepies.make_industry_benchmark(tenant='tenant1', industry='edu-o', dmb_value=3.0)
        industry_to_be_updated = aggregate.industry_benchmark('tenant1', 'edu-o')

        got_dmb, got_dmb_d, got_industry = industry_to_be_updated

        self.assertEqual(got_dmb, 3.0)
        self.assertEqual(got_industry, 'edu-o')

    def test_industry_benchmark_industry_fallback_parent(self):
        """When industry does not have a value for dmb, it should  fallback to parent."""
        mommy_recepies.make_industry_benchmark(tenant='tenant1', industry='edu-o')
        industry_to_be_updated = aggregate.industry_benchmark('tenant1', 'edu-o')
        got_dmb, got_dmb_d, got_industry = industry_to_be_updated

        self.assertEqual(got_dmb, 2.0)
        self.assertEqual(got_industry, 'edu')

    def test_industry_benchmark_industry_fallback_to_root(self):
        """When industry does not have a value for dmb, it should fallback to parent,
        and so on until you get eventualy to root."""
        industry_to_be_updated = aggregate.industry_benchmark('tenant1', 'fi-b')
        got_dmb, got_dmb_d, got_industry = industry_to_be_updated

        self.assertEqual(got_dmb, 1.0)
        self.assertEqual(got_industry, 'all')

    def test_industry_benchmark_industry_in_more_than_one_tenant(self):
        """When industry has the same name in more than one tenant, it should return the
        correct one."""
        mommy_recepies.make_industry_benchmark(tenant='tenant1', industry='edu-o', dmb_value=2.0)
        mommy_recepies.make_industry_benchmark(tenant='tenant2', industry='edu-o', dmb_value=4.0)
        industry_to_be_updated = aggregate.industry_benchmark('tenant1', 'edu-o')
        got_dmb, got_dmb_d, got_industry = industry_to_be_updated

        self.assertEqual(got_dmb, 2.0)
        self.assertEqual(got_industry, 'edu-o')

        industry_to_be_updated = aggregate.industry_benchmark('tenant2', 'edu-o')
        got_dmb, got_dmb_d, got_industry = industry_to_be_updated

        self.assertEqual(got_dmb, 4.0)
        self.assertEqual(got_industry, 'edu-o')


@override_settings(
    ALL_INDUSTRIES=('all', 'all'),
    MIN_ITEMS_INDUSTRY_THRESHOLD=2,
    TENANTS=mocks.MOCKED_TENANTS,
)
class IndustryBestPractice(TestCase):
    """Test class for `core.aggregate.industry_best_practice` function."""

    def setUp(self):
        mommy_recepies.make_industry_benchmark(tenant='tenant1', industry='edu', dmb_bp_value=2.0)
        mommy_recepies.make_industry_benchmark(tenant='tenant1', industry='all', dmb_bp_value=1.0)

    def test_industry_benchmark_industry_has_value(self):
        """When industry has a value for dmb, it should return it."""
        mommy_recepies.make_industry_benchmark(tenant='tenant1', industry='edu-o', dmb_bp_value=3.0)
        industry_to_be_updated = aggregate.industry_best_practice('tenant1', 'edu-o')

        got_dmb, got_dmb_d, got_industry = industry_to_be_updated

        self.assertEqual(got_dmb, 3.0)
        self.assertEqual(got_industry, 'edu-o')

    def test_industry_benchmark_industry_fallback_parent(self):
        """When industry does not have a value for dmb, it should  fallback to parent."""
        mommy_recepies.make_industry_benchmark(tenant='tenant1', industry='edu-o')
        industry_to_be_updated = aggregate.industry_best_practice('tenant1', 'edu-o')
        got_dmb, got_dmb_d, got_industry = industry_to_be_updated

        self.assertEqual(got_dmb, 2.0)
        self.assertEqual(got_industry, 'edu')

    def test_industry_benchmark_industry_fallback_to_root(self):
        """When industry does not have a value for dmb, it should fallback to parent,
        and so on until you get eventualy to root."""
        industry_to_be_updated = aggregate.industry_best_practice('tenant1', 'fi-b')
        got_dmb, got_dmb_d, got_industry = industry_to_be_updated

        self.assertEqual(got_dmb, 1.0)
        self.assertEqual(got_industry, 'all')

    def test_industry_benchmark_industry_in_more_than_one_tenant(self):
        """When industry has the same name in more than one tenant, it should return the
        correct one."""
        mommy_recepies.make_industry_benchmark(tenant='tenant1', industry='edu-o', dmb_bp_value=2.5)
        mommy_recepies.make_industry_benchmark(tenant='tenant2', industry='edu-o', dmb_bp_value=3.0)
        industry_to_be_updated = aggregate.industry_best_practice('tenant1', 'edu-o')
        got_dmb, got_dmb_d, got_industry = industry_to_be_updated

        self.assertEqual(got_dmb, 2.5)
        self.assertEqual(got_industry, 'edu-o')

        industry_to_be_updated = aggregate.industry_best_practice('tenant2', 'edu-o')
        got_dmb, got_dmb_d, got_industry = industry_to_be_updated
        self.assertEqual(got_dmb, 3.0)
        self.assertEqual(got_industry, 'edu-o')
