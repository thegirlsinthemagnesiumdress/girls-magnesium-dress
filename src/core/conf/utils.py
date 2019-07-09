from django.conf import settings
from djangae import environment
import re

VERSION_RE = re.compile(r'^(?P<version>.*)(\-dot|\:\d+)')


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
                result.append((key, ' - '.join((str(parent_label), str(label)))))
            else:
                result.append((key, str(label)))

    return result


def get_tenant_key(slug):
    return settings.TENANTS_SLUG_TO_KEY[slug]


def get_tenant_slug(tenant):
    return settings.TENANTS[tenant]['slug']


def get_tenant_product_name(tenant):
    return settings.TENANTS[tenant]['PRODUCT_NAME']


def get_other_tenant_footers(current_tenant):
    """Returns a list of tenants slugs and their footer labels, excluding the `current_tentant`."""
    other_tenants = []
    tenant_conf = settings.TENANTS.get(current_tenant)

    if not tenant_conf or not tenant_conf['in_dmb_footer']:
        return other_tenants

    current_tenant_slug = get_tenant_slug(current_tenant)
    for tenant in settings.TENANTS.values():
        if tenant['in_dmb_footer'] and tenant['slug'] is not current_tenant_slug:
            other_tenants.append((tenant['footer_label'], tenant['slug']))
    return other_tenants


def version_info(domain):
    """Returns version to be set on Qualtrics, based on domain parameter.
    :param domain:
    :returns: Tuple of two element (version, is_nightly), where the first one is the version name
    which need to be set on Qualtrics, and the second element is a flag identifying a nightly version.
    `version` is `None` in case a version is not applicable (for instance in production),
    and `is_nightly` is gonna be `True` if `nightly` word is in `domain`, `False` otherwise.
    """

    version = None
    is_nightly = False
    is_development = environment.is_development_environment()
    # if it's local environment
    if is_development:
        version = 'localhost'
    # if it's staging environment
    elif "staging" in environment.application_id():
        version_match = VERSION_RE.search(domain)
        if version_match:
            version = version_match.group('version')
        else:
            version = 'staging'
        is_nightly = 'nightly' in version
    return (version, is_nightly, is_development)
