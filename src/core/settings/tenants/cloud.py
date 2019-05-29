# coding=utf-8
# flake8: noqa
from . import GOOGLE_SHEET_BASE_SURVEY_FIELDS, GOOGLE_SHEET_BASE_RESULT_FIELDS

DIMENSION_LEARN = "learn"
DIMENSION_LEAD = "lead"
DIMENSION_SCALE = "scale"
DIMENSION_SECURE = "secure"

LEVEL_0 = 0
LEVEL_1 = 1
LEVEL_2 = 2
LEVEL_3 = 3

WEIGHTS = {}

DIMENSION_TITLES = {
    DIMENSION_LEARN: 'Learn',
    DIMENSION_LEAD: 'Lead',
    DIMENSION_SCALE: 'Scale',
    DIMENSION_SECURE: 'Secure',
}

DIMENSION_ORDER = [
    DIMENSION_LEARN,
    DIMENSION_LEAD,
    DIMENSION_SCALE,
    DIMENSION_SECURE,
]

DIMENSIONS = {
    DIMENSION_LEARN: [
        'Q1',
        'Q2',
        'Q3',
        'Q4',
        'Q5',
    ],
    DIMENSION_LEAD: [
        'Q6',
        'Q7',
        'Q8',
        'Q9',
        'Q10',
        'Q11',
    ],
    DIMENSION_SCALE: [
        'Q12',
        'Q13',
        'Q14',
        'Q15',
        'Q16',
        'Q17',
    ],
    DIMENSION_SECURE: [
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
    LEVEL_0: 'Nascent',
    LEVEL_1: 'Developing',
    LEVEL_2: 'Mature',
    LEVEL_3: 'Leading',
}

LEVELS_DESCRIPTIONS = {
    LEVEL_0: '',
    LEVEL_1: '',
    LEVEL_2: '',
    LEVEL_3: '',
}

REPORT_LEVEL_DESCRIPTIONS = {
    LEVEL_0: '',
    LEVEL_1: '',
    LEVEL_2: '',
    LEVEL_3: '',
}


INDUSTRY_AVG_DESCRIPTION = ''

INDUSTRY_BEST_DESCRIPTION = ''


DIMENSION_HEADER_DESCRIPTION = {
    DIMENSION_LEARN: '',
    DIMENSION_LEAD: '',
    DIMENSION_SCALE: '',
    DIMENSION_SECURE: '',
}


DIMENSION_LEVEL_DESCRIPTION = {
    DIMENSION_LEARN: {
        LEVEL_0: '',
        LEVEL_1: '',
        LEVEL_2: '',
        LEVEL_3: '',
    },
    DIMENSION_LEAD: {
        LEVEL_0: '',
        LEVEL_1: '',
        LEVEL_2: '',
        LEVEL_3: '',
    },
    DIMENSION_SCALE: {
        LEVEL_0: '',
        LEVEL_1: '',
        LEVEL_2: '',
        LEVEL_3: '',
    },
    DIMENSION_SECURE: {
        LEVEL_0: '',
        LEVEL_1: '',
        LEVEL_2: '',
        LEVEL_3: '',
    },
}


DATA_ACTIVATION_GUIDE_CTA = {
    'text': '',
    'link': '',
}


DIMENSION_LEVEL_RECOMMENDATIONS = {
    DIMENSION_LEARN: {
        LEVEL_0: [],
        LEVEL_1: [],
        LEVEL_2: [],
        LEVEL_3: [],
    },
    DIMENSION_LEAD: {
        LEVEL_0: [],
        LEVEL_1: [],
        LEVEL_2: [],
        LEVEL_3: [],
    },
    DIMENSION_SCALE: {
        LEVEL_0: [],
        LEVEL_1: [],
        LEVEL_2: [],
        LEVEL_3: [],
    },
    DIMENSION_SECURE: {
        LEVEL_0: [],
        LEVEL_1: [],
        LEVEL_2: [],
        LEVEL_3: [],
    },
}

DIMENSION_SIDEPANEL_HEADING = ''

DIMENSION_SIDEPANEL_DESCRIPTIONS = {
    DIMENSION_LEARN: '',
    DIMENSION_LEAD: '',
    DIMENSION_SCALE: '',
    DIMENSION_SECURE: '',
}


CONTENT_DATA = {
    'levels': LEVELS,
    'level_descriptions': LEVELS_DESCRIPTIONS,
    'report_level_descriptions': REPORT_LEVEL_DESCRIPTIONS,
    'dimensions': DIMENSION_ORDER,
    'dimension_labels': DIMENSION_TITLES,
    'dimension_headers_descriptions': DIMENSION_HEADER_DESCRIPTION,
    'dimension_level_description': DIMENSION_LEVEL_DESCRIPTION,
    'dimension_level_recommendations': DIMENSION_LEVEL_RECOMMENDATIONS,
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
