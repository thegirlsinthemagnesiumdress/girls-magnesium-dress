
def flatten_industries(categories, parent, result):
    """Given a dictionary of nested categories, it returns a
    flatten representation of it.

    :param categories: dictionary containing the initial categories.
    :param parent: string representing the initial root element, `None`
        if no specific parent element is needed.
    :param result: dictionary of starting elements, empty dictionary if no
        initial element are needed.

    :returns: dicitonary containing the flat reprensentation of `categories`.

    Example:
    CATEGORIES = OrderedDict([
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

    FLATTEN_REPR = flatten_industries(CATEGORIES, None, {})

    FLATTEN_REPR is the graph representation of CATEGORIES:
    FLATTEN_REPR = {
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
    if not categories:
        return
    for cat, data in categories.items():
        label, subcat = data
        result[cat] = (label, parent)
        flatten_industries(subcat, cat, result)
    return result
