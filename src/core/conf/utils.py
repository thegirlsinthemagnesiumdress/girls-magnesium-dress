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
    is_staging = False
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
        is_staging = True
        is_nightly = 'nightly' in version
    return (version, is_nightly, is_development, is_staging)


def get_tenant_level_ranges(levels, levels_max):
    """Returns an array or ranges for determining a scores level.

    Args:
        tenant (string): The tenant to generate level ranges for.

    Returns:
        [(number, number)]: An array of tuples representing the level ranges
    """
    level_ranges = []

    levels = sorted(levels.keys())
    for i in range(0, len(levels)):
        # If we are on the last level then the max is LEVELS_MAX
        if i == len(levels) - 1:
            level_ranges.append((levels[i], levels_max))
        else:
            level_ranges.append((levels[i], levels[i + 1]))

    return level_ranges


def get_level_key(level_ranges, score):
    """Gets the level key for level dictionaries based on the score.

    Args:
        level_ranges ([(number number)]): An array of ranges representing the level boundaries.
        score (number): The score for a dimension or overall.

    Returns:
        number: The key for dictionaries using level values (e.g. level descriptions).
    """
    # If the level is the max score then return the highest level (min of the final range).
    max_range = level_ranges[-1]
    if score >= max_range[1]:
        return max_range[0]
    # Otherwise loop through the ranges and find the range containing the score.
    for (level_min, level_max) in level_ranges:
        if level_min <= score < level_max:
            return level_min
    # Else return the minimum level.
    return level_ranges[0][0]


def get_next_level_key(level_ranges, score):
    """Gets the next levels' key for level dictionaries based on the score.

    Args:
        level_ranges ([(number number)]): An array of ranges representing the level boundaries.
        score (number): The score for a dimension or overall.

    Returns:
        number: The key for the next level for dictionaries using level values (e.g. level descriptions).
    """
    # If the level is the max score then return the highest level (min of the final range).
    max_range = level_ranges[-1]
    if score >= max_range[0]:
        return max_range[0]
    # Otherwise loop through the ranges and find the range containing the score.
    for (level_min, level_max) in level_ranges:
        if level_min <= score < level_max:
            return level_max
    # Else return the maximum of the lowest range.
    return level_ranges[0][1]


def in_top_level(level_ranges, score):
    """Checks if a score is in the top level.

    Args:
        level_ranges ([(number, number)]): The level ranges to test the score on.
        score (number): The raw score from qualtrics.

    Returns:
        boolean: True if the score is in the top level.
    """
    level = get_level_key(level_ranges, score)
    top_level = level_ranges[-1][0]
    return level >= top_level


def get_level_info(tenant, score, level_ranges=None):
    """Gets the current and next level's value, name, and description.

    Args:
        tenant (string): The tenant to pull level content from.
        score (number): The raw qualtrics result.
        level_ranges ([(number, number)], optional): Array of tuples for calculating scores' level
            should only be set for testing as is found in content data. Defaults to None.

    Returns:
        object: An object containing the value, name, and description of the current and next level.
    """
    content_data = settings.TENANTS[tenant]['CONTENT_DATA']
    # If level ranges have not been provided use the ones defined in the content data.
    if not level_ranges:
        level_ranges = content_data['level_ranges']
    level = get_level_key(level_ranges, score)
    next_level = get_next_level_key(level_ranges, score)
    # Form the level info object.
    return {
        "value": score,
        "inTopLevel": in_top_level(level_ranges, score),
        "levels": {
            "current": {
                "value": level,
                "name": content_data['levels'][level],
                "description": content_data['level_descriptions'][level],
            },
            "next": {
                "value": next_level,
                "name": content_data['levels'][next_level],
                "description": content_data['level_descriptions'][next_level],
            }
        }
    }


def get_dimension_level_info(tenant, dimension, score, level_ranges=None):
    """Gets the current and next dimension level's value, name, and description.

    Args:
        tenant (string): The tenant to pull level content from.
        dimension (string): The dimension to pull level content from.
        score (number): The raw qualtrics result.
        level_ranges ([(number, number)], optional): Array of tuples for calculating scores' level
                                                     should only be set for testing as is found in
                                                     content data. Defaults to None.

    Returns:
        object: An object containing the value, name, and description of the current and next dimension level.
    """
    content_data = settings.TENANTS[tenant]['CONTENT_DATA']
    # If level ranges have not been provided use the ones defined in the content data.
    if not level_ranges:
        level_ranges = content_data['level_ranges']
    level = get_level_key(level_ranges, score)
    next_level = get_next_level_key(level_ranges, score)
    # Form the level info object.
    return {
        "value": score,
        "inTopLevel": in_top_level(level_ranges, score),
        "levels": {
            "current": {
                "value": level,
                "name": content_data['levels'][level],
                "description": content_data['dimension_level_description'][dimension][level],
            },
            "next": {
                "value": next_level,
                "name": content_data['levels'][next_level],
                "description": content_data['dimension_level_description'][dimension][next_level],
            }
        }
    }


def get_detailed_survey_result_data(tenant, survey_result, level_ranges=None):
    """Gets data on the overall and dimension scores for a particular survey result.

    Args:
        tenant (string): The tenant to pull level content from.
        survey_result (core.models.SurveyResult): The survey result to gather data on.
        level_ranges ([(number, number)], optional): Array of tuples for calculating scores' level
                                                     should only be set for testing as is found in
                                                     content data. Defaults to None.

    Returns:
        object: An object containing level information about the overall and dimension scores,
                as well as if the score is in the top level and when the survey was taken.
                For use in the Admin's Account Details page.
    """
    content_data = settings.TENANTS[tenant]['CONTENT_DATA']
    # If level ranges have not been provided use the ones defined in the content data.
    if not level_ranges:
        level_ranges = content_data['level_ranges']
    # Construct the data object.
    survey_result_data = {
        "date": survey_result.loaded_at,
        "overall": get_level_info(tenant, survey_result.dmb, level_ranges),
        "dimensions": {dimension: get_dimension_level_info(tenant, dimension, value, level_ranges)
                       for dimension, value in survey_result.dmb_d.items()}
    }
    return survey_result_data


def get_account_detail_data(tenant, account, level_ranges=None):
    """Gets requied data for the account detail page.

    Args:
        tenant (string): The tenant to pull content from.
        account (Survey): The account to gather data and survey results from.
        level_ranges ([(number, number)], optional): Array of tuples for calculating scores' level
                                                     should only be set for testing as is found in
                                                     content data. Defaults to None.

    Returns:
        object, object, object: 3 Objects representing the account information, external survey
                                result data, and internal survey result data.
    """
    content_data = settings.TENANTS[tenant]['CONTENT_DATA']
    # If level ranges have not been provided use the ones defined in the content data.
    if not level_ranges:
        level_ranges = content_data['level_ranges']
    # Construct the account info object.
    account_info = {
        "id": account.account_id,
        "name": account.company_name,
        "country": settings.COUNTRIES[account.country],
        "industry": account.get_industry_display(),
    }
    # Construct the internal and external survey info arrays.
    external_surveys = [get_detailed_survey_result_data(tenant, survey_result, level_ranges)
                        for survey_result in account.survey_results.all()]
    internal_surveys = [get_detailed_survey_result_data(tenant, survey_result, level_ranges)
                        for survey_result in account.survey_results.all()]
    # Return the tuple of objects.
    return account_info, external_surveys, internal_surveys
