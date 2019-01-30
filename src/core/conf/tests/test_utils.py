from core.conf.utils import map_industries, flatten

from djangae.test import TestCase
from collections import OrderedDict


class MapIndustriesTest(TestCase):
    """Test case for `core.conf.utils.map_industries` function."""

    def test_dictionary_flattened_correctly_single(self):

        industries = OrderedDict([
            ('afs', ('Accommodation and food service', None)),
        ])

        mapped_repr = map_industries(industries, None, {})

        self.assertEquals(len(mapped_repr), 1)
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

        self.assertEquals(len(mapped_repr), 4)
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

        self.assertEquals(len(mapped_repr), 6)
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

        self.assertEquals(len(mapped_repr), 6)
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

        flattened_repr = flatten(industries)

        self.assertEqual(len(flattened_repr), 4)

    def test_dictionary_flattened_correctly_empty(self):
        industries = OrderedDict()

        flattened_repr = flatten(industries)

        self.assertEqual(len(flattened_repr), 0)
