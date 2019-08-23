from core.conf import utils
import mock
from djangae.test import TestCase
from collections import OrderedDict
from django.test import override_settings
from django.conf import settings
from core.tests.mocks import MOCKED_TENANTS, MOCKED_INTERNAL_TENANTS
from core.tests.mommy_recepies import make_survey, make_survey_result


class MapIndustriesTest(TestCase):
    """Test case for `core.conf.utils.map_industries` function."""

    def test_dictionary_flattened_correctly_single(self):

        industries = OrderedDict([
            ('afs', ('Accommodation and food service', None)),
        ])

        mapped_repr = utils.map_industries(industries, None, {})

        self.assertEqual(len(mapped_repr), 1)
        label, parent_industry = mapped_repr.get('afs')
        self.assertIsNone(parent_industry)
        self.assertEqual(label, 'Accommodation and food service')

    def test_dictionary_flattened_correctly_nested(self):

        industries = OrderedDict([
            ('edu', ('Education', OrderedDict([
                ('edu-o', ('Other', None)),
                ('edu-pe', ('Primary education', None)),
                ('edu-se', ('Secondary education', None)),
            ]))),
        ])

        mapped_repr = utils.map_industries(industries, None, {})

        self.assertEqual(len(mapped_repr), 4)
        # all children of Education have Education as parent
        for category in ['edu-o', 'edu-pe', 'edu-se']:
            label, parent_industry = mapped_repr.get(category)
            self.assertEqual(parent_industry, 'edu')

        # root element does not have parent category
        label, cat = mapped_repr.get('edu')
        self.assertEqual(label, 'Education')
        self.assertEqual(cat, None)

    def test_dictionary_flattened_correctly_multiple(self):

        industries = OrderedDict([
            ('afs', ('Accommodation and food service', None)),
            ('co', ('Construction', None)),
            ('edu', ('Education', OrderedDict([
                ('edu-o', ('Other', None)),
                ('edu-pe', ('Primary education', None)),
                ('edu-se', ('Secondary education', None)),
            ]))),
        ])

        mapped_repr = utils.map_industries(industries, None, {})

        self.assertEqual(len(mapped_repr), 6)
        label, parent_industry = mapped_repr.get('afs')
        self.assertIsNone(parent_industry)
        self.assertEqual(label, 'Accommodation and food service')

    def test_prefix(self):
        industries = OrderedDict([
            ('afs', ('Accommodation and food service', None)),
            ('co', ('Construction', None)),
            ('edu', ('Education', OrderedDict([
                ('edu-o', ('Other', None)),
                ('edu-pe', ('Primary education', None)),
                ('edu-se', ('Secondary education', None)),
            ]))),
        ])
        parent_prefix = 'root'

        mapped_repr = utils.map_industries(industries, parent_prefix, {})

        self.assertEqual(len(mapped_repr), 6)
        label, parent_industry = mapped_repr.get('afs')
        self.assertIsNotNone(parent_industry)
        self.assertEqual(parent_industry, parent_prefix)
        self.assertEqual(label, 'Accommodation and food service')


class FlatIndustriesTest(TestCase):
    """Test case for `core.conf.utils.flatten` function."""

    def test_dictionary_flattened_correctly_single(self):
        industries = OrderedDict([
            ('afs', ('Accommodation and food service', None)),
        ])

        flattened_repr = utils.flatten(industries)

        self.assertEqual(len(flattened_repr), 1)

    def test_dictionary_flattened_correctly_single_nested(self):
        industries = OrderedDict([
            ('edu', ('Education', OrderedDict([
                ('edu-o', ('Other', None)),
                ('edu-pe', ('Primary education', None)),
                ('edu-se', ('Secondary education', None)),
            ]))),
        ])

        flattened_repr = utils.flatten(industries)

        self.assertEqual(len(flattened_repr), 3)
        for el in flattened_repr:
            key, label = el
            self.assertIn('Education -', label)

    def test_dictionary_flattened_correctly_multiple(self):
        industries = OrderedDict([
            ('afs', ('Accommodation and food service', None)),
            ('edu', ('Education', OrderedDict([
                ('edu-o', ('Other', None)),
                ('edu-pe', ('Primary education', None)),
                ('edu-se', ('Secondary education', None)),
            ]))),
        ])

        flattened_expected = [
            ('afs', 'Accommodation and food service'),
            ('edu-o', 'Education - Other'),
            ('edu-pe', 'Education - Primary education'),
            ('edu-se', 'Education - Secondary education'),
        ]

        flattened_repr = utils.flatten(industries)

        self.assertEqual(flattened_repr, flattened_expected)

    def test_dictionary_flattened_correctly_empty(self):
        industries = OrderedDict()

        flattened_repr = utils.flatten(industries)

        self.assertEqual(len(flattened_repr), 0)

    def test_dictionary_flattened_correctly_leaf_only_false(self):
        industries = OrderedDict([
            ('afs', ('Accommodation and food service', None)),
            ('edu', ('Education', OrderedDict([
                ('edu-o', ('Other', None)),
                ('edu-pe', ('Primary education', None)),
                ('edu-se', ('Secondary education', None)),
            ]))),
        ])

        flattened_repr = utils.flatten(industries, leaf_only=False)

        flattened_expected = [
            ('afs', 'Accommodation and food service'),
            ('edu-o', 'Education - Other'),
            ('edu-pe', 'Education - Primary education'),
            ('edu-se', 'Education - Secondary education'),
            ('edu', 'Education'),
        ]
        self.assertEqual(flattened_repr, flattened_expected)


class VersionInfoTest(TestCase):
    """Test for `core.utils.version_info` function."""

    @mock.patch('djangae.environment.is_development_environment', return_value=False)
    def production_domain_test(self, is_prod_mock):
        version, is_nightly, is_development, is_staging = utils.version_info('somedomain')

        is_prod_mock.assert_called()
        self.assertFalse(is_development)
        self.assertIsNone(version)
        self.assertFalse(is_nightly)
        self.assertFalse(is_staging)

    @mock.patch('djangae.environment.is_development_environment', return_value=True)
    def localhost_domain_test(self, is_prod_mock):
        domain = 'localhost:8000'
        expected_version = 'localhost'
        version, is_nightly, is_development, is_staging = utils.version_info(domain)
        self.assertEqual(version, expected_version)
        self.assertTrue(is_development)
        self.assertFalse(is_nightly)
        self.assertFalse(is_staging)

    @mock.patch('djangae.environment.is_development_environment', return_value=True)
    def localhost_domain_test_different_domain(self, is_prod_mock):
        domain = '0.0.0.0:8000'
        expected_version = 'localhost'
        version, is_nightly, is_development, is_staging = utils.version_info(domain)
        self.assertEqual(version, expected_version)
        self.assertTrue(is_development)
        self.assertFalse(is_nightly)
        self.assertFalse(is_staging)

    @mock.patch('djangae.environment.is_development_environment', return_value=False)
    @mock.patch('djangae.environment.application_id', return_value='dmb-staging')
    def staging_domain_test(self, app_id_mock, is_prod_mock):
        domain = 'gweb-digitalmaturity-staging.appspot.com'
        expected_version = 'staging'
        version, is_nightly, is_development, is_staging = utils.version_info(domain)
        self.assertEqual(version, expected_version)
        self.assertFalse(is_development)
        self.assertFalse(is_nightly)
        self.assertTrue(is_staging)

    @mock.patch('djangae.environment.is_development_environment', return_value=False)
    @mock.patch('djangae.environment.application_id', return_value='dmb-staging')
    def nightly_domain_test(self, app_id_mock, is_prod_mock):
        domain = 'ads-nightly-dot-gweb-digitalmaturity-staging.appspot.com'
        expected_version = 'ads-nightly'
        version, is_nightly, is_development, is_staging = utils.version_info(domain)
        self.assertFalse(is_development)
        self.assertTrue(is_nightly)
        self.assertTrue(is_staging)
        self.assertEqual(version, expected_version)

    @mock.patch('djangae.environment.is_development_environment', return_value=False)
    @mock.patch('djangae.environment.application_id', return_value='dmb-staging')
    def tenant_not_nightly_domain_test(self, app_id_mock, is_prod_mock):
        domain = 'ads-dot-gweb-digitalmaturity-staging.appspot.com'
        expected_version = 'ads'
        version, is_nightly, is_development, is_staging = utils.version_info(domain)
        self.assertEqual(version, expected_version)
        self.assertFalse(is_nightly)
        self.assertFalse(is_development)
        self.assertTrue(is_staging)


@override_settings(
    TENANTS=MOCKED_TENANTS,
)
class GetOtherTenantFootersTest(TestCase):
    """Test for `core.utils.get_other_tenant_footers` function."""

    def one_result_test(self):
        expected = [('Tenant 2 Footer Label', 'tenant2-slug')]
        got = utils.get_other_tenant_footers('tenant1')

        self.assertListEqual(expected, got)

    @override_settings(
        TENANTS={
            'tenant1': {
                'slug': 'tenant1-slug',
                'in_dmb_footer': True,
                'footer_label': 'Tenant 1 Footer Label',
            },
            'tenant2': {
                'slug': 'tenant2-slug',
                'in_dmb_footer': True,
                'footer_label': 'Tenant 2 Footer Label',
            },
            'tenant3': {
                'slug': 'tenant3-slug',
                'in_dmb_footer': True,
                'footer_label': 'Tenant 3 Footer Label',
            },
        }
    )
    def mulitple_results_test(self):
        expected = [('Tenant 3 Footer Label', 'tenant3-slug'), ('Tenant 2 Footer Label', 'tenant2-slug')]
        got = utils.get_other_tenant_footers('tenant1')

        self.assertListEqual(expected, got)

    @override_settings(
        TENANTS={
            'tenant1': {
                'slug': 'tenant1-slug',
                'in_dmb_footer': True,
                'footer_label': 'Tenant 1 Footer Label',
            },
            'tenant2': {
                'slug': 'tenant2-slug',
                'in_dmb_footer': True,
                'footer_label': 'Tenant 2 Footer Label',
            },
            'tenant3': {
                'slug': 'tenant3-slug',
                'in_dmb_footer': False,
                'footer_label': 'Tenant 3 Footer Label',
            },
        }
    )
    def not_in_dmb_test(self):
        expected = []
        got = utils.get_other_tenant_footers('tenant3')

        self.assertListEqual(expected, got)

    def no_in_tenant_list_test(self):
        expected = []
        got = utils.get_other_tenant_footers('tenant4')

        self.assertListEqual(expected, got)


class GetLevelKey(TestCase):
    """Test for functions in `core.utils.get_level_key`."""

    def get_lower_bound_level_key_test(self):
        """Checks that values on the level boundary and just above are clasified corrctly"""
        level_ranges = [(0, 1), (1, 2), (2, 3)]
        level = 1
        # If score is boundary then its the level
        self.assertEqual(
            utils.get_level_key(level_ranges, level),
            level
        )
        # If score is more than boundary but less than the one above its still the level
        self.assertEqual(
            utils.get_level_key(level_ranges, level + 0.1),
            level
        )

    def get_upper_bound_level_key_test(self):
        """Checks that values just below the next level boundary are clasified corrctly"""
        level_ranges = [(0, 1), (1, 2), (2, 3)]
        level = 1
        # If score is more than boundary but less than the one above its still the level
        self.assertEqual(
            utils.get_level_key(level_ranges, 2 - 0.1),
            level
        )

    def get_level_key_out_of_bounds_test(self):
        """Tests that a scores out of bounds return the correct level key"""
        # Check scores outside ranges are classified correctly.
        level_ranges = [(0, 1), (1, 2), (2, 3)]
        self.assertEqual(
            utils.get_level_key(level_ranges, level_ranges[0][0] - 100),
            level_ranges[0][0]
        )
        self.assertEqual(
            utils.get_level_key(level_ranges, level_ranges[-1][1] + 100),
            level_ranges[-1][0]
        )


class GetNextLevelKey(TestCase):
    """Test for functions in `core.utils.get_next_level_key`."""
    def setUp(self):
        self.level_ranges = [(0, 1), (1, 2), (2, 3)]

    def get_next_level_key_test(self):
        """Tests that the next level of a score is calculated correctly."""
        level = 1
        # If level is not in top range then next level should be one above.
        self.assertEqual(
            utils.get_next_level_key(self.level_ranges, level),
            2
        )

    def get_top_next_level_key_test(self):
        """Tests that the next level of a score is calculated correctly."""
        level = 2
        # If level is not in top range then next level should be one above.
        self.assertEqual(
            utils.get_next_level_key(self.level_ranges, level),
            2
        )

    def get_next_level_key_out_of_bounds_test(self):
        """Tests that a scores out of bounds return the correct level key"""
        # Check scores outside ranges are classified correctly.
        self.assertEqual(
            utils.get_next_level_key(self.level_ranges, self.level_ranges[0][0] - 100),
            self.level_ranges[0][1]
        )
        self.assertEqual(
            utils.get_next_level_key(self.level_ranges, self.level_ranges[-1][1] + 100),
            self.level_ranges[-1][0]
        )


class InTopLevel(TestCase):
    """Test for functions in `core.utils.in_top_level`."""

    def is_top_level_test(self):
        """Tests that a top score is classified correctly."""
        # Check that a top score is has the highest level.
        level_ranges = [(0, 1), (1, 2), (2, 3)]
        level = 3
        self.assertTrue(utils.in_top_level(level_ranges, level))

    def is_not_top_level_test(self):
        """Tests that a non-top score is classified correctly."""
        # Check that a low score does not have the highest level.
        level_ranges = [(0, 1), (1, 2), (2, 3)]
        level = 0
        self.assertFalse(utils.in_top_level(level_ranges, level))


@override_settings(
    TENANTS=MOCKED_TENANTS,
    INTERNAL_TENANTS=MOCKED_INTERNAL_TENANTS,
)
class GetLevelAttributesTest(TestCase):
    """Test for functions in `core.utils` for getting level-dependent properties/attributes."""

    def setUp(self):
        self.content_data = settings.TENANTS['tenant1']['CONTENT_DATA']
        self.level_ranges = self.content_data['level_ranges']

    def get_level_info_test(self):
        """Tests that a score returns the correct level information"""
        levels = self.content_data['levels']
        level = levels.keys()[1]
        # Check correct level info is given for each level.
        level_info = utils.get_level_info(self.content_data, level)['levels']
        # Check current level info
        self.assertEqual(level, level_info['current']['value'])
        self.assertEqual(levels[level], level_info['current']['name'])
        self.assertEqual(self.content_data['level_descriptions'][level], level_info['current']['description'])
        # Check next level info
        next_level = levels.keys()[2]
        self.assertEqual(next_level, level_info['next']['value'])
        self.assertEqual(levels[next_level], level_info['next']['name'])
        self.assertEqual(self.content_data['level_descriptions'][next_level], level_info['next']['description'])

    def get_level_info_last_level_test(self):
        """Tests that a score returns the correct level information, when we are in the next level"""
        levels = self.content_data['levels']
        level = 2
        next_level = 2
        # Check correct level info is given for each level.
        level_info = utils.get_level_info(self.content_data, level)['levels']
        # Check current level info
        self.assertEqual(level, level_info['current']['value'])
        self.assertEqual(levels[level], level_info['current']['name'])
        self.assertEqual(self.content_data['level_descriptions'][level], level_info['current']['description'])
        # Check next level info
        self.assertEqual(next_level, level_info['next']['value'])
        self.assertEqual(levels[next_level], level_info['next']['name'])
        self.assertEqual(self.content_data['level_descriptions'][next_level], level_info['next']['description'])

    def get_dimension_level_info_test(self):
        """Tests that a score returns the correct dimension level info"""
        levels = self.content_data['levels']
        level = levels.keys()[1]
        dimension = 'dim1'
        # Check correct level info is given for each level.
        level_info = utils.get_dimension_level_info(self.content_data, dimension, level)['levels']
        # Check current level info
        self.assertEqual(level, level_info['current']['value'])
        self.assertEqual(levels[level], level_info['current']['name'])
        self.assertEqual(
            self.content_data['dimension_level_description'][dimension][level],
            level_info['current']['description']
        )
        # Check next level info
        next_level = levels.keys()[2]
        self.assertEqual(next_level, level_info['next']['value'])
        self.assertEqual(levels[next_level], level_info['next']['name'])
        self.assertEqual(
            self.content_data['dimension_level_description'][dimension][next_level],
            level_info['next']['description']
        )

    def get_dimension_level_info_dimension_does_not_exist_test(self):
        """Tests that a score returns the correct dimension level info"""
        level = 1
        dimension = 'dim5'
        # If a dimensions does not exist, we raise a KeyError.
        self.assertRaises(KeyError, utils.get_dimension_level_info, self.content_data, dimension, level)

    def get_detailed_survey_result_data_test(self):
        """Tests that a survey results data is correctly returned"""
        # Make fake survey results.
        survey = make_survey(tenant="tenant1")
        survey_result = make_survey_result(
            survey=survey,
            response_id='AAA',
            dmb=1,
            dmb_d={u"dim1": 0.4, u"dim2": 1.6}
        )
        # Get survey result data.
        survey_result_data = utils.get_detailed_survey_result_data(self.content_data, survey_result)
        # Check required fields are present
        self.assertIsNotNone(survey_result_data['date'])
        self.assertIsNotNone(survey_result_data['overall'])
        self.assertEqual(survey_result_data['overall']['value'], 1)

        dimension = self.content_data['dimensions'][0]
        self.assertEqual(
            survey_result_data['dimensions'][dimension]['value'],
            survey_result.dmb_d[dimension]
        )
        self.assertEqual(
            survey_result_data['dimensions'][dimension]['name'],
            self.content_data['dimension_labels'][dimension]
        )
        self.assertEqual(survey_result_data['dimensions'][dimension]['in_top_level'], False)
        self.assertIsNotNone(survey_result_data['dimensions'][dimension]['levels'])

    def get_empty_account_detail_data_test(self):
        """Tests that correct value is returned when a empty account is provided."""
        # Make fake survey results.
        survey = make_survey(tenant="tenant1")
        account_info, external_surveys, internal_surveys = utils.get_account_detail_data(self.content_data, survey)
        self.assertIsNotNone(account_info)
        self.assertListEqual(external_surveys, [])
        self.assertListEqual(internal_surveys, [])

    def get_account_detail_data_external_test(self):
        """Tests that correct value is returned when an account is provided."""
        # Make survey with 2 results.
        survey = make_survey(tenant="tenant1")
        make_survey_result(
            survey=survey,
            response_id='AAA',
            dmb=1,
            dmb_d={u"dim1": 0.4, u"dim2": 1.6}
        )
        survey_result_2 = make_survey_result(
            survey=survey,
            response_id='BBB',
            dmb=1,
            dmb_d={u"dim1": 0.4, u"dim2": 1.6}
        )
        survey.last_survey_result = survey_result_2
        survey.save()

        account_info, external_surveys, internal_surveys = utils.get_account_detail_data(self.content_data, survey)
        self.assertIsNotNone(account_info)
        self.assertEqual(len(external_surveys), 2)
        self.assertEqual(len(internal_surveys), 0)

    def get_account_detail_data_internal_test(self):
        """Tests that correct value is returned when an account is provided."""
        # Make survey with 2 internal results.
        survey = make_survey(tenant="tenant1")
        make_survey_result(
            internal_survey=survey,
            response_id='AAA',
            dmb=1,
            dmb_d={u"dim1": 0.4, u"dim2": 1.6}
        )
        survey_result_2 = make_survey_result(
            internal_survey=survey,
            response_id='BBB',
            dmb=1,
            dmb_d={u"dim1": 0.4, u"dim2": 1.6}
        )
        survey.last_internal_result = survey_result_2
        survey.save()

        account_info, external_surveys, internal_surveys = utils.get_account_detail_data(self.content_data, survey)
        self.assertIsNotNone(account_info)
        self.assertEqual(len(external_surveys), 0)
        self.assertEqual(len(internal_surveys), 2)
