# coding=utf-8
# flake8: noqa
from django.utils.translation import gettext_lazy as _

DIMENSION_ADS = 'ads'
DIMENSION_ACCESS = 'access'
DIMENSION_AUDIENCE = 'audience'
DIMENSION_ATTRIBUTION = 'attribution'
DIMENSION_AUTOMATION = 'automation'
DIMENSION_ORGANIZATION = 'organization'

LEVEL_0 = 0
LEVEL_1 = 1
LEVEL_2 = 2
LEVEL_3 = 3
LEVELS_MAX = 4

WEIGHTS = {}

DIMENSION_TITLES = {
    DIMENSION_ADS: _('Assets and ads'),
    DIMENSION_ACCESS: _('Access'),
    DIMENSION_AUDIENCE: _('Audience'),
    DIMENSION_ATTRIBUTION: _('Attribution'),
    DIMENSION_AUTOMATION: _('Automation'),
    DIMENSION_ORGANIZATION: _('Organisation'),
}

DIMENSION_ORDER = [
    DIMENSION_AUDIENCE,
    DIMENSION_ADS,
    DIMENSION_ACCESS,
    DIMENSION_ATTRIBUTION,
    DIMENSION_AUTOMATION,
    DIMENSION_ORGANIZATION,
]

DIMENSIONS = {
    DIMENSION_AUDIENCE: [
        'Q7',
        'Q8',
        'Q9',
    ],
    DIMENSION_ADS: [
        'Q11',
        'Q12',
        'Q13',
        'Q14',
    ],
    DIMENSION_ACCESS: [
        'Q16',
        'Q17',
        'Q18',
        'Q19',
    ],
    DIMENSION_ATTRIBUTION: [
        'Q21',
        'Q22',
        'Q23',
        'Q24',
        'Q25',
        'Q26',
    ],
    DIMENSION_AUTOMATION: [
        'Q28',
        'Q29',
        'Q30',
        'Q31',
        'Q32',
        'Q33',
        'Q34',
    ],
    DIMENSION_ORGANIZATION: [
        'Q36',
        'Q37',
        'Q38',
        'Q39',
    ],
}
