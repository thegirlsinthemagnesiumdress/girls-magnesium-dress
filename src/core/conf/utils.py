from django.conf import settings


def map_industries(industries, parent, result):
    """Given a dictionary of nested industries, it returns a
    flatten representation of it.

    :param industries: dictionary containing the initial industries.
    :param parent: string representing the id of the parent element, `None`
        if no specific parent element is needed.
    :param result: dictionary of starting elements, empty dictionary if no
        initial element are needed.

    :returns: dicitonary containing the flat reprensentation of `industries`.

    Example:
    INDUSTRIES = OrderedDict([
        ('afs', ('Accommodation and food service', None)),
        ('aer', ('Arts, entertainment & recreation', None)),
        ('co', ('Construction', None)),
        ('edu', ('Education', OrderedDict([
            ('edu-fe', ('Further education', None)),
            ('edu-o', ('Other', None)),
            ('edu-pe', ('Primary education', None)),
            ('edu-se', ('Secondary education', None)),
        ]))),
    ])

    MAPPED_REPR = map_industries(INDUSTRIES, None, {})

    MAPPED_REPR is the graph representation of INDUSTRIES:
    MAPPED_REPR = {
        'aer': ('Arts, entertainment & recreation', None),
        'afs': ('Accommodation and food service', None),
        'co': ('Construction', None),
        'edu': ('Education', None),
        'edu-fe': ('Further education', 'edu'),
        'edu-o': ('Other', 'edu'),
        'edu-pe': ('Primary education', 'edu'),
        'edu-se': ('Secondary education', 'edu')
    }
    """
    if not industries:
        return
    for cat, data in industries.items():
        label, subcat = data
        result[cat] = (label, parent)
        map_industries(subcat, cat, result)
    return result


def flatten(industries, parent_label='', leaf_only=True):
    """Given a dictionary of nested industries, it returns a list of strings
    that combines nested industries in one label.

    :param industries: dictionary containing the initial industries.
    :param parent: string representing the parent label, ''
    if no specific parent element is needed.


    :returns: list of strings  flat reprensentation of `industries`.

    Example:
    INDUSTRIES = OrderedDict([
        ('afs', ('Accommodation and food service', None)),
        ('aer', ('Arts, entertainment & recreation', None)),
        ('co', ('Construction', None)),
        ('edu', ('Education', OrderedDict([
            ('edu-fe', ('Further education', None)),
            ('edu-o', ('Other', None)),
            ('edu-pe', ('Primary education', None)),
            ('edu-se', ('Secondary education', None)),
        ]))),
    ])

    FLATTENED_INDUSTRIES = flatten(INDUSTRIES)

    FLATTENED_INDUSTRIES is the list of industries labels.
    FLATTENED_INDUSTRIES = [
        ('afs', 'Arts, entertainment & recreation'),
        ('aer', 'Accommodation and food service'),
        ('co', 'Construction'),
        ('edu-fe', 'Education - Further education'),
        ('edu-o', 'Education - Other'),
        ('edu-pe', 'Education - Primary education'),
        ('edu-se', 'Education - Secondary education'),
    ]
    """
    result = []
    for key, val in industries.items():
        label, children = val
        if children:
            children_flat = flatten(children, label, leaf_only=leaf_only)
            result.extend(children_flat)

        if not leaf_only or not children:
            if parent_label:
                result.append((key, ' - '.join((parent_label, label))))
            else:
                result.append((key, label))

    return result


def get_tenant_key(slug):
    return settings.TENANTS_SLUG_TO_KEY[slug]


def get_tenant_slug(tenant):
    return settings.TENANTS[tenant]['slug']
