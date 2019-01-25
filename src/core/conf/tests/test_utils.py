from core.conf.utils import map_industries

from djangae.test import TestCase
from collections import OrderedDict


class MapIndustriesTest(TestCase):
    """Test case for `core.conf.utils.map_industries` function."""

    def test_dictionary_flattened_correctly_single(self):

        categories = OrderedDict([
            ('afs', ('Accommodation and food service', None)),
        ])

        mapped_repr = map_industries(categories, None, {})

        self.assertEquals(len(mapped_repr), 1)
        label, parent_cat = mapped_repr.get('afs')
        self.assertIsNone(parent_cat)
        self.assertEqual(label, 'Accommodation and food service')

    def test_dictionary_flattened_correctly_nested(self):

        categories = OrderedDict([
            ('edu', ('Education', OrderedDict([
                ('edu-o', ('Other', None)),
                ('edu-pe', ('Primary education', None)),
                ('edu-se', ('Secondary education', None)),
            ]))),
        ])

        mapped_repr = map_industries(categories, None, {})

        self.assertEquals(len(mapped_repr), 4)
        # all children of Education have Education as parent
        for category in ['edu-o', 'edu-pe', 'edu-se']:
            label, parent_cat = mapped_repr.get(category)
            self.assertIsNotNone(parent_cat)
            self.assertEqual(parent_cat, 'edu')

        # root element does not have parent category
        label, cat = mapped_repr.get('edu')
        self.assertEqual(label, 'Education')
        self.assertEqual(cat, None)

    def test_dictionary_flattened_correctly_multiple(self):

        categories = OrderedDict([
            ('afs', ('Accommodation and food service', None)),
            ('co', ('Construction', None)),
            ('edu', ('Education', OrderedDict([
                ('edu-o', ('Other', None)),
                ('edu-pe', ('Primary education', None)),
                ('edu-se', ('Secondary education', None)),
            ]))),
        ])

        mapped_repr = map_industries(categories, None, {})

        self.assertEquals(len(mapped_repr), 6)
        label, parent_cat = mapped_repr.get('afs')
        self.assertIsNone(parent_cat)
        self.assertEqual(label, 'Accommodation and food service')

    def test_prefix(self):
        categories = OrderedDict([
            ('afs', ('Accommodation and food service', None)),
            ('co', ('Construction', None)),
            ('edu', ('Education', OrderedDict([
                ('edu-o', ('Other', None)),
                ('edu-pe', ('Primary education', None)),
                ('edu-se', ('Secondary education', None)),
            ]))),
        ])
        parent_prefix = 'root'

        mapped_repr = map_industries(categories, parent_prefix, {})

        self.assertEquals(len(mapped_repr), 6)
        label, parent_cat = mapped_repr.get('afs')
        self.assertIsNotNone(parent_cat)
        self.assertEqual(parent_cat, parent_prefix)
        self.assertEqual(label, 'Accommodation and food service')
