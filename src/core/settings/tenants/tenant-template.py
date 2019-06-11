# coding=utf-8
# flake8: noqa
from . import GOOGLE_SHEET_BASE_SURVEY_FIELDS, GOOGLE_SHEET_BASE_RESULT_FIELDS

# DIMENSIONS
DIMENSION_1 = '<dimension_id>'
DIMENSION_2 = '<dimension_id>'
DIMENSION_3 = '<dimension_id>'
DIMENSION_4 = '<dimension_id>'

# LEVELS
LEVEL_0 = 0
LEVEL_1 = 1
LEVEL_2 = 2
LEVEL_3 = 3
LEVELS_MAX = 4

# WEIGHTS
WEIGHTS = {
    'Q1': 1,
    'Q2': 1,
    'Q3': 1,
    'Q4': 1,
    'Q5': 1,
    'Q6': 1,
    'Q7': 1,
    'Q8': 1,
    'Q9': 1,
    'Q10': 1,
    'Q11': 1,
    'Q12': 1,
    'Q13': 1,
    'Q14': 1,
    'Q15': 1,
    'Q16': 1,
    'Q17': 1,
    'Q18': 1,
    'Q19': 1,
    'Q20': 1,
    'Q21': 1,
    'Q22': 1,
    'Q23': 1,
    'Q24': 1,
    'Q25': 1,
}

DIMENSION_TITLES = {
    DIMENSION_1: 'Dimension 1',
    DIMENSION_2: 'Dimension 2',
    DIMENSION_3: 'Dimension 3',
    DIMENSION_4: 'Dimension 4',
}

DIMENSION_ORDER = [
    DIMENSION_1,
    DIMENSION_2,
    DIMENSION_3,
    DIMENSION_4,
]

DIMENSIONS = {
    DIMENSION_1: [
        'Q1',
        'Q2',
        'Q3',
        'Q4',
        'Q5',
    ],
    DIMENSION_2: [
        'Q6',
        'Q7',
        'Q8',
        'Q9',
        'Q10',
        'Q11',
    ],
    DIMENSION_3: [
        'Q12',
        'Q13',
        'Q14',
        'Q15',
        'Q16',
        'Q17',
    ],
    DIMENSION_4: [
        'Q18',
        'Q19',
        'Q20',
        'Q21',
        'Q22',
        'Q23',
        'Q24',
        'Q25',
    ],
}

MULTI_ANSWER_QUESTIONS = []


LEVELS = {
    LEVEL_0: 'Level 0',
    LEVEL_1: 'Level 1',
    LEVEL_2: 'Level 2',
    LEVEL_3: 'Level 3',
}

LEVELS_DESCRIPTIONS = {
    LEVEL_0: 'Level 0 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
    LEVEL_1: 'Level 1 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
    LEVEL_2: 'Level 2 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
    LEVEL_3: 'Level 3 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
}

REPORT_LEVEL_DESCRIPTIONS = {
    LEVEL_0: 'Level 0 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
    LEVEL_1: 'Level 1 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
    LEVEL_2: 'Level 2 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
    LEVEL_3: 'Level 3 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
}


INDUSTRY_AVG_DESCRIPTION = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'

INDUSTRY_BEST_DESCRIPTION = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'


DIMENSION_HEADER_DESCRIPTION = {
    DIMENSION_1: 'Dimension 1 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
    DIMENSION_2: 'Dimension 2 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
    DIMENSION_3: 'Dimension 3 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
    DIMENSION_4: 'Dimension 4 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
}


DIMENSION_LEVEL_DESCRIPTION = {
    DIMENSION_1: {
        LEVEL_0: 'Level 0 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        LEVEL_1: 'Level 1 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        LEVEL_2: 'Level 2 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        LEVEL_3: 'Level 3 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
    },
    DIMENSION_2: {
        LEVEL_0: 'Level 0 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        LEVEL_1: 'Level 1 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        LEVEL_2: 'Level 2 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        LEVEL_3: 'Level 3 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
    },
    DIMENSION_3: {
        LEVEL_0: 'Level 0 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        LEVEL_1: 'Level 1 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        LEVEL_2: 'Level 2 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        LEVEL_3: 'Level 3 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
    },
    DIMENSION_4: {
        LEVEL_0: 'Level 0 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        LEVEL_1: 'Level 1 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        LEVEL_2: 'Level 2 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        LEVEL_3: 'Level 3 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
    },
}


# DATA_ACTIVATION_GUIDE_CTA = {
#     'text': '',
#     'link': '',
# }


DIMENSION_RECOMMENDATIONS = {
    DIMENSION_1: {
        LEVEL_0: [
            {
                'header': 'Dimension 1 - Level 0 - Recommendation 1',
                'text': 'Dimension 1 - Level 0 - Recommendation 1 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 1 - Level 0 - Recommendation 2',
                'text': 'Dimension 1 - Level 0 - Recommendation 2 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 1 - Level 0 - Recommendation 3',
                'text': 'Dimension 1 - Level 0 - Recommendation 3 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 1 - Level 0 - Recommendation 4',
                'text': 'Dimension 1 - Level 0 - Recommendation 4 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
        ],
        LEVEL_1: [
            {
                'header': 'Dimension 1 - Level 1 - Recommendation 1',
                'text': 'Dimension 1 - Level 1 - Recommendation 1 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 1 - Level 1 - Recommendation 2',
                'text': 'Dimension 1 - Level 1 - Recommendation 2 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 1 - Level 1 - Recommendation 3',
                'text': 'Dimension 1 - Level 1 - Recommendation 3 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 1 - Level 1 - Recommendation 4',
                'text': 'Dimension 1 - Level 1 - Recommendation 4 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
        ],
        LEVEL_2: [
            {
                'header': 'Dimension 1 - Level 2 - Recommendation 1',
                'text': 'Dimension 1 - Level 2 - Recommendation 1 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 1 - Level 2 - Recommendation 2',
                'text': 'Dimension 1 - Level 2 - Recommendation 2 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 1 - Level 2 - Recommendation 3',
                'text': 'Dimension 1 - Level 2 - Recommendation 3 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 1 - Level 2 - Recommendation 4',
                'text': 'Dimension 1 - Level 2 - Recommendation 4 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
        ],
        LEVEL_3: [
            {
                'header': 'Dimension 1 - Level 3 - Recommendation 1',
                'text': 'Dimension 1 - Level 3 - Recommendation 1 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 1 - Level 3 - Recommendation 2',
                'text': 'Dimension 1 - Level 3 - Recommendation 2 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 1 - Level 3 - Recommendation 3',
                'text': 'Dimension 1 - Level 3 - Recommendation 3 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 1 - Level 3 - Recommendation 4',
                'text': 'Dimension 1 - Level 3 - Recommendation 4 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
        ],
    },
    DIMENSION_2: {
        LEVEL_0: [
            {
                'header': 'Dimension 2 - Level 0 - Recommendation 1',
                'text': 'Dimension 2 - Level 0 - Recommendation 1 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 2 - Level 0 - Recommendation 2',
                'text': 'Dimension 2 - Level 0 - Recommendation 2 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 2 - Level 0 - Recommendation 3',
                'text': 'Dimension 2 - Level 0 - Recommendation 3 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 2 - Level 0 - Recommendation 4',
                'text': 'Dimension 2 - Level 0 - Recommendation 4 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
        ],
        LEVEL_1: [
            {
                'header': 'Dimension 2 - Level 1 - Recommendation 1',
                'text': 'Dimension 2 - Level 1 - Recommendation 1 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 2 - Level 1 - Recommendation 2',
                'text': 'Dimension 2 - Level 1 - Recommendation 2 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 2 - Level 1 - Recommendation 3',
                'text': 'Dimension 2 - Level 1 - Recommendation 3 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 2 - Level 1 - Recommendation 4',
                'text': 'Dimension 2 - Level 1 - Recommendation 4 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
        ],
        LEVEL_2: [
            {
                'header': 'Dimension 2 - Level 2 - Recommendation 1',
                'text': 'Dimension 2 - Level 2 - Recommendation 1 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 2 - Level 2 - Recommendation 2',
                'text': 'Dimension 2 - Level 2 - Recommendation 2 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 2 - Level 2 - Recommendation 3',
                'text': 'Dimension 2 - Level 2 - Recommendation 3 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 2 - Level 2 - Recommendation 4',
                'text': 'Dimension 2 - Level 2 - Recommendation 4 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
        ],
        LEVEL_3: [
            {
                'header': 'Dimension 2 - Level 3 - Recommendation 1',
                'text': 'Dimension 2 - Level 3 - Recommendation 1 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 2 - Level 3 - Recommendation 2',
                'text': 'Dimension 2 - Level 3 - Recommendation 2 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 2 - Level 3 - Recommendation 3',
                'text': 'Dimension 2 - Level 3 - Recommendation 3 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 2 - Level 3 - Recommendation 4',
                'text': 'Dimension 2 - Level 3 - Recommendation 4 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
        ],
    },
    DIMENSION_3: {
        LEVEL_0: [
            {
                'header': 'Dimension 4 - Level 0 - Recommendation 1',
                'text': 'Dimension 4 - Level 0 - Recommendation 1 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 4 - Level 0 - Recommendation 2',
                'text': 'Dimension 4 - Level 0 - Recommendation 2 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 4 - Level 0 - Recommendation 3',
                'text': 'Dimension 4 - Level 0 - Recommendation 3 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 4 - Level 0 - Recommendation 4',
                'text': 'Dimension 4 - Level 0 - Recommendation 4 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
        ],
        LEVEL_1: [
            {
                'header': 'Dimension 4 - Level 1 - Recommendation 1',
                'text': 'Dimension 4 - Level 1 - Recommendation 1 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 4 - Level 1 - Recommendation 2',
                'text': 'Dimension 4 - Level 1 - Recommendation 2 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 4 - Level 1 - Recommendation 3',
                'text': 'Dimension 4 - Level 1 - Recommendation 3 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 4 - Level 1 - Recommendation 4',
                'text': 'Dimension 4 - Level 1 - Recommendation 4 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
        ],
        LEVEL_2: [
            {
                'header': 'Dimension 4 - Level 2 - Recommendation 1',
                'text': 'Dimension 4 - Level 2 - Recommendation 1 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 4 - Level 2 - Recommendation 2',
                'text': 'Dimension 4 - Level 2 - Recommendation 2 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 4 - Level 2 - Recommendation 3',
                'text': 'Dimension 4 - Level 2 - Recommendation 3 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 4 - Level 2 - Recommendation 4',
                'text': 'Dimension 4 - Level 2 - Recommendation 4 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
        ],
        LEVEL_3: [
            {
                'header': 'Dimension 4 - Level 3 - Recommendation 1',
                'text': 'Dimension 4 - Level 3 - Recommendation 1 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 4 - Level 3 - Recommendation 2',
                'text': 'Dimension 4 - Level 3 - Recommendation 2 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 4 - Level 3 - Recommendation 3',
                'text': 'Dimension 4 - Level 3 - Recommendation 3 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 4 - Level 3 - Recommendation 4',
                'text': 'Dimension 4 - Level 3 - Recommendation 4 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
        ],
    },
    DIMENSION_4: {
        LEVEL_0: [
            {
                'header': 'Dimension 4 - Level 0 - Recommendation 1',
                'text': 'Dimension 4 - Level 0 - Recommendation 1 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 4 - Level 0 - Recommendation 2',
                'text': 'Dimension 4 - Level 0 - Recommendation 2 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 4 - Level 0 - Recommendation 3',
                'text': 'Dimension 4 - Level 0 - Recommendation 3 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 4 - Level 0 - Recommendation 4',
                'text': 'Dimension 4 - Level 0 - Recommendation 4 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
        ],
        LEVEL_1: [
            {
                'header': 'Dimension 4 - Level 1 - Recommendation 1',
                'text': 'Dimension 4 - Level 1 - Recommendation 1 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 4 - Level 1 - Recommendation 2',
                'text': 'Dimension 4 - Level 1 - Recommendation 2 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 4 - Level 1 - Recommendation 3',
                'text': 'Dimension 4 - Level 1 - Recommendation 3 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 4 - Level 1 - Recommendation 4',
                'text': 'Dimension 4 - Level 1 - Recommendation 4 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
        ],
        LEVEL_2: [
            {
                'header': 'Dimension 4 - Level 2 - Recommendation 1',
                'text': 'Dimension 4 - Level 2 - Recommendation 1 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 4 - Level 2 - Recommendation 2',
                'text': 'Dimension 4 - Level 2 - Recommendation 2 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 4 - Level 2 - Recommendation 3',
                'text': 'Dimension 4 - Level 2 - Recommendation 3 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 4 - Level 2 - Recommendation 4',
                'text': 'Dimension 4 - Level 2 - Recommendation 4 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
        ],
        LEVEL_3: [
            {
                'header': 'Dimension 4 - Level 3 - Recommendation 1',
                'text': 'Dimension 4 - Level 3 - Recommendation 1 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 4 - Level 3 - Recommendation 2',
                'text': 'Dimension 4 - Level 3 - Recommendation 2 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 4 - Level 3 - Recommendation 3',
                'text': 'Dimension 4 - Level 3 - Recommendation 3 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'Dimension 4 - Level 3 - Recommendation 4',
                'text': 'Dimension 4 - Level 3 - Recommendation 4 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
        ],
    },
}

DIMENSION_SIDEPANEL_HEADING = 'Dimensions - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'

DIMENSION_SIDEPANEL_DESCRIPTIONS = {
    DIMENSION_1: 'Dimension 1 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
    DIMENSION_2: 'Dimension 2 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
    DIMENSION_3: 'Dimension 3 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
    DIMENSION_4: 'Dimension 4 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
}


CONTENT_DATA = {
    'levels': LEVELS,
    'level_descriptions': LEVELS_DESCRIPTIONS,
    'report_level_descriptions': REPORT_LEVEL_DESCRIPTIONS,
    'dimensions': DIMENSION_ORDER,
    'dimension_labels': DIMENSION_TITLES,
    'dimension_headers_descriptions': DIMENSION_HEADER_DESCRIPTION,
    'dimension_level_description': DIMENSION_LEVEL_DESCRIPTION,
    'dimension_recommendations': DIMENSION_RECOMMENDATIONS,
    'industry_avg_description': INDUSTRY_AVG_DESCRIPTION,
    'industry_best_description': INDUSTRY_BEST_DESCRIPTION,
    'dimension_sidepanel_heading': DIMENSION_SIDEPANEL_HEADING,
    'dimension_sidepanel_descriptions': DIMENSION_SIDEPANEL_DESCRIPTIONS,
}

#####  GOOGLE SHEETS EXPORT TENANT CUSTOMIZATION #####
GOOGLE_SHEET_EXPORT_SURVEY_FIELDS = GOOGLE_SHEET_BASE_SURVEY_FIELDS.copy()
GOOGLE_SHEET_EXPORT_RESULT_FIELDS = GOOGLE_SHEET_BASE_RESULT_FIELDS.copy()
GOOGLE_SHEET_EXPORT_RESULT_FIELDS.update(DIMENSION_TITLES)
#####  END OF GOOGLE SHEETS EXPORT TENANT CUSTOMIZATION #####
