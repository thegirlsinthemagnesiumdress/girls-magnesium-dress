from core.conf.utils import map_industries, flatten, version_info, get_other_tenant_footers
import mock
from djangae.test import TestCase
from collections import OrderedDict
from django.test import override_settings
from core.tests.mocks import MOCKED_TENANTS


class MapIndustriesTest(TestCase):
    """Test case for `core.conf.utils.map_industries` function."""

    def test_dictionary_flattened_correctly_single(self):

        industries = OrderedDict([
            ('afs', ('Accommodation and food service', None)),
        ])

        mapped_repr = map_industries(industries, None, {})

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

        mapped_repr = map_industries(industries, None, {})

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

        mapped_repr = map_industries(industries, None, {})

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

        mapped_repr = map_industries(industries, parent_prefix, {})

        self.assertEqual(len(mapped_repr), 6)
        label, parent_industry = mapped_repr.get('afs')
        self.assertIsNotNone(parent_industry)
        self.assertEqual(parent_industry, parent_prefix)
        self.assertEqual(label, 'Accommodation and food service')


class FlatIndustriesTest(TestCase):
    """Test case for `core.conf.utils.flat` function."""

    def test_dictionary_flattened_correctly_single(self):
        industries = OrderedDict([
            ('afs', ('Accommodation and food service', None)),
        ])

        flattened_repr = flatten(industries)

        self.assertEqual(len(flattened_repr), 1)

    def test_dictionary_flattened_correctly_single_nested(self):
        industries = OrderedDict([
            ('edu', ('Education', OrderedDict([
                ('edu-o', ('Other', None)),
                ('edu-pe', ('Primary education', None)),
                ('edu-se', ('Secondary education', None)),
            ]))),
        ])

        flattened_repr = flatten(industries)

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

        flattened_repr = flatten(industries)

        self.assertEqual(flattened_repr, flattened_expected)

    def test_dictionary_flattened_correctly_empty(self):
        industries = OrderedDict()

        flattened_repr = flatten(industries)

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

        flattened_repr = flatten(industries, leaf_only=False)

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
        version, is_nightly, is_development = version_info('somedomain')

        is_prod_mock.assert_called()
        self.assertFalse(is_development)
        self.assertIsNone(version)
        self.assertFalse(is_nightly)

    @mock.patch('djangae.environment.is_development_environment', return_value=True)
    def localhost_domain_test(self, is_prod_mock):
        domain = 'localhost:8000'
        expected_version = 'localhost'
        version, is_nightly, is_development = version_info(domain)
        self.assertEqual(version, expected_version)
        self.assertTrue(is_development)
        self.assertFalse(is_nightly)

    @mock.patch('djangae.environment.is_development_environment', return_value=True)
    def localhost_domain_test_different_domain(self, is_prod_mock):
        domain = '0.0.0.0:8000'
        expected_version = 'localhost'
        version, is_nightly, is_development = version_info(domain)
        self.assertEqual(version, expected_version)
        self.assertTrue(is_development)
        self.assertFalse(is_nightly)

    @mock.patch('djangae.environment.is_development_environment', return_value=False)
    @mock.patch('djangae.environment.application_id', return_value='dmb-staging')
    def staging_domain_test(self, app_id_mock, is_prod_mock):
        domain = 'gweb-digitalmaturity-staging.appspot.com'
        expected_version = 'staging'
        version, is_nightly, is_development = version_info(domain)
        self.assertEqual(version, expected_version)
        self.assertFalse(is_development)
        self.assertFalse(is_nightly)

    @mock.patch('djangae.environment.is_development_environment', return_value=False)
    @mock.patch('djangae.environment.application_id', return_value='dmb-staging')
    def nightly_domain_test(self, app_id_mock, is_prod_mock):
        domain = 'ads-nightly-dot-gweb-digitalmaturity-staging.appspot.com'
        expected_version = 'ads-nightly'
        version, is_nightly, is_development = version_info(domain)
        self.assertFalse(is_development)
        self.assertTrue(is_nightly)
        self.assertEqual(version, expected_version)

    @mock.patch('djangae.environment.is_development_environment', return_value=False)
    @mock.patch('djangae.environment.application_id', return_value='dmb-staging')
    def tenant_not_nightly_domain_test(self, app_id_mock, is_prod_mock):
        domain = 'ads-dot-gweb-digitalmaturity-staging.appspot.com'
        expected_version = 'ads'
        version, is_nightly, is_development = version_info(domain)
        self.assertEqual(version, expected_version)
        self.assertFalse(is_nightly)
        self.assertFalse(is_development)


@override_settings(
    TENANTS=MOCKED_TENANTS,
)
class GetOtherTenantFootersTest(TestCase):
    """Test for `core.utils.get_other_tenant_footers` function."""

    def one_result_test(self):
        expected = [('Tenant 2 Footer Label', 'tenant2-slug')]
        got = get_other_tenant_footers('tenant1')

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
        got = get_other_tenant_footers('tenant1')

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
        got = get_other_tenant_footers('tenant3')

        self.assertListEqual(expected, got)

    def no_in_tenant_list_test(self):
        expected = []
        got = get_other_tenant_footers('tenant4')

        self.assertListEqual(expected, got)