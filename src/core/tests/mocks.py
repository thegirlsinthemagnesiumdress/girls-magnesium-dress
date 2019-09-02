# coding=utf-8
# flake8: noqa

from django.utils import dateparse
from collections import OrderedDict
from django.utils.translation import ugettext_lazy as _


MOCKED_DIMENSIONS = {
    'ads': [
        'Q3',
        'Q8',
    ],
    'access': [
        'Q4',
        'Q10',
    ],
    'audience': [
        'Q5_1',
        'Q11',
    ],
    'automation': [
        'Q5_2'
    ],
    'attribution': [
        'Q5_3',
        'Q12',
    ],
    'organization': [
        'Q6',
        'Q7',
    ],
}

MOCKED_MULTI_ANSWER_QUESTIONS = [
    'Q13',
]

MOCKED_WEIGHTS = {
    'Q1': 2,
    'Q3': 3,
}

MOCKED_DIMENSIONS_WEIGHTS = {
    1: {
        'ads': 0.2,
        'automation': 0.4,
        'attribution': 0.0,
    }
}

MOCKED_DIMENSION_TITLES_TENANT_1 = {
    'dim1': 'Dimension 1',
    'dim2': 'Dimension 2'
}

MOCKED_DIMENSION_TITLES_TENANT_2 = {
    'dim11': 'Dimension 11',
    'dim22': 'Dimension 22'
}

MOCKED_CONTENT_DATA_TENANT_1 = {
    'levels': {},
    'levels_max': 1,
    'level_descriptions': {},
    'dimensions': [],
    'dimension_titles': MOCKED_DIMENSION_TITLES_TENANT_1,
    'dimension_header_descriptions': {},
    'dimension_level_description': {},
    'dimension_recommendations': {},
}


MOCKED_CONTENT_DATA_TENANT_2 = {
    'levels': {},
    'levels_max': 2,
    'level_descriptions': {},
    'dimensions': [],
    'dimension_titles': MOCKED_DIMENSION_TITLES_TENANT_2,
    'dimension_header_descriptions': {},
    'dimension_level_description': {},
    'dimension_recommendations': {},
}

qualtrics_export = {
    'responses': [
        {
            'Organization-sum': '0.0',
            'Organization-weightedAvg': '0.0',
            'Organization-weightedStdDev': '0.0',
            'sid': '1',
            'ResponseID': 'AAA',
            'Enter Embedded Data Field Name Here...': '',
            'sponsor': '',
            'company_name': 'new survey',
            'dmb': '0.5',
            'StartDate': '2018-07-31 14:16:06',
            'EndDate': '2018-07-31 15:18:56',
            'Q1_1_TEXT': '',
            'Q1_2_TEXT': '',
            'Q2_1_TEXT': '',
            'Q2_2_TEXT': '',

            'Q3': '2',
            'Q4': '0',
            'Q5_1': '2',

            'Q5_2': '0',
            'Q5_3': '3',
            'Q6': '4',
            'Q7': '2',

            'Q8': '4',
            'Q10': '0',
            'Q11': '1',
            'Q12': '2',
            'Finished': '1',
        },
        {
            'Organization-sum': '0.0',
            'Organization-weightedAvg': '0.0',
            'Organization-weightedStdDev': '0.0',
            'sid': '3',
            'ResponseID': 'AAB',
            'Enter Embedded Data Field Name Here...': '',
            'sponsor': '',
            'company_name': 'new survey',
            'dmb': '0.5',
            'StartDate': '2018-07-31 14:16:07',
            'EndDate': '2018-07-31 15:18:56',
            'Q1_1_TEXT': '',
            'Q1_2_TEXT': '',
            'Q2_1_TEXT': '',
            'Q2_2_TEXT': '',

            'Q3': '1',
            'Q4': '3',
            'Q5_1': '1',

            'Q5_2': '2',
            'Q5_3': '4',
            'Q6': '0',
            'Q7': '1',

            'Q8': '0',
            'Q10': '0',
            'Q11': '1',
            'Q12': '0',
            'Finished': '0',
        },
        {
            'Organization-sum': '0.0',
            'Organization-weightedAvg': '0.0',
            'Organization-weightedStdDev': '0.0',
            'sid': '2',
            'ResponseID': 'AAC',
            'Enter Embedded Data Field Name Here...': '',
            'sponsor': '',
            'company_name': 'new survey',
            'dmb': '0.5',
            'StartDate': '2018-07-31 14:16:08',
            'EndDate': '2018-07-31 15:18:56',
            'Q1_1_TEXT': '',
            'Q1_2_TEXT': '',
            'Q2_1_TEXT': '',
            'Q2_2_TEXT': '',

            'Q3': '1',
            'Q4': '1',
            'Q5_1': '1',

            'Q5_2': '0',
            'Q5_3': '2',
            'Q6': '0',
            'Q7': '1',

            'Q8': '0',
            'Q10': '0',
            'Q11': '1',
            'Q12': '4',
            'Finished': '1',
        },
        {
            'Organization-sum': '0.0',
            'Organization-weightedAvg': '0.0',
            'Organization-weightedStdDev': '0.0',
            'sid': '2',
            'ResponseID': 'AAD',
            'Enter Embedded Data Field Name Here...': '',
            'sponsor': '',
            'company_name': 'new survey test 4',
            'dmb': '0.5',
            'StartDate': '2018-07-31 14:16:09',
            'EndDate': '2018-07-31 15:18:56',
            'Q1_1_TEXT': '',
            'Q1_2_TEXT': '',
            'Q2_1_TEXT': '',
            'Q2_2_TEXT': '',

            'Q3': '1',
            'Q4': '1',
            'Q5_1': '1',

            'Q5_2': '0',
            'Q5_3': '2',
            'Q6': '0',
            'Q7': '1',

            'Q8': '0',
            'Q10': '0',
            'Q11': '1',
            'Q12': '4',
            'Finished': '1',
        }
    ],
}

HIERARCHICAL_INDUSTRIES = OrderedDict([
    ('ic', ('Information and Communication', OrderedDict([
        ('ic-bnpj', ('Books, news, periodicals, journals', None)),
        ('ic-o', ('Other', None)),
        ('ic-s', ('Software', None)),
        ('ic-trmvm', ('TV, radio, movies, video, music', None)),
        ('ic-t', ('Telecommunications', None)),
    ]))),
    ('co', ('Construction', None)),
    ('edu', ('Education', OrderedDict([
        ('edu-fe', ('Further education', None)),
        ('edu-o', ('Other', None)),
        ('edu-pe', ('Primary education', None)),
        ('edu-se', ('Secondary education', None)),
    ]))),
    ('fi', ('Financial and Insurance', OrderedDict([
        ('fi-b', ('Banking', None)),
        ('fi-i', ('Insurance', None)),
        ('fi-o', ('Other', None)),
    ]))),
    ('re', (('Real estate'), None)),
])

INDUSTRIES = {
    'co': ('Construction', None),
    'edu': ('Education', None),
    'edu-fe': ('Further education', 'edu'),
    'edu-o': ('Other', 'edu'),
    'edu-pe': ('Primary education', 'edu'),
    'edu-se': ('Secondary education', 'edu'),
    'ic': ('Information and Communication', None),
    'ic-bnpj': ('Books, news, periodicals, journals', 'ic'),
    'ic-o': ('Other', 'ic'),
    'ic-s': ('Software', 'ic'),
    'ic-t': ('Telecommunications', 'ic'),
    'ic-trmvm': ('TV, radio, movies, video, music', 'ic'),
    'fi': ('Financial and Insurance', None),
    'fi-b': ('Banking', 'fi'),
    'fi-i': ('Insurance', 'fi'),
    'fi-o': ('Other', 'fi'),
    're': ('Real estate', None),
}


HIERARCHICAL_INDUSTRIES_UNICODE = OrderedDict([
    ('ic', (_(u'Información y comunicación'), OrderedDict([
        ('ic-bnpj', (_(u'Libros, noticias, periódicos y revistas'), None)),
        ('ic-o', (_(u'Other'), None)),
    ]))),
])

INDUSTRIES_UNICODE = {
    'ic': (_(u'Información y comunicación'), None),
    'ic-bnpj': (_(u'Libros, noticias, periódicos y revistas'), 'ic'),
    'ic-o': (_(u'Other'), 'ic'),
}



MOCKED_GOOGLE_SHEET_BASE_SURVEY_FIELDS = {
    'company_name': 'Company Name',
    'country': 'Country',
    'industry': 'Industry',
    'created_at': 'Creation Date',
    'link': 'Report link',
}
MOCKED_GOOGLE_SHEET_BASE_RESULT_FIELDS = {
    'dmb': 'Overall DMB',
    'excluded_from_best_practice': 'Excluded from Benchmark',
}

GOOGLE_SHEET_EXPORT_SURVEY_FIELDS_TENANT_1 = MOCKED_GOOGLE_SHEET_BASE_SURVEY_FIELDS.copy()
GOOGLE_SHEET_EXPORT_RESULT_FIELDS_TENANT_1 = MOCKED_GOOGLE_SHEET_BASE_RESULT_FIELDS.copy()
GOOGLE_SHEET_EXPORT_RESULT_FIELDS_TENANT_1.update(MOCKED_DIMENSION_TITLES_TENANT_1)

GOOGLE_SHEET_EXPORT_SURVEY_FIELDS_TENANT_2 = MOCKED_GOOGLE_SHEET_BASE_SURVEY_FIELDS.copy()
GOOGLE_SHEET_EXPORT_RESULT_FIELDS_TENANT_2 = MOCKED_GOOGLE_SHEET_BASE_RESULT_FIELDS.copy()
GOOGLE_SHEET_EXPORT_RESULT_FIELDS_TENANT_2.update(MOCKED_DIMENSION_TITLES_TENANT_2)


MOCKED_TENANTS = {
    'tenant1': {
        'key': 'tenant1',
        'label': 'Tenant 1 label',
        'slug': 'tenant1-slug',
        'in_dmb_footer': True,
        'footer_label': 'Tenant 1 Footer Label',
        'QUALTRICS_SURVEY_ID': 'SV_bexxxxxxxx',
        'EMAIL_TO': 'Q97_4_TEXT',
        'EMAIL_BCC': 'Q97_5_TEXT',
        'DIMENSIONS': MOCKED_DIMENSIONS,
        'MULTI_ANSWER_QUESTIONS': MOCKED_MULTI_ANSWER_QUESTIONS,
        'WEIGHTS': MOCKED_WEIGHTS,
        'CONTENT_DATA': MOCKED_CONTENT_DATA_TENANT_1,
        'EXCLUDED_TIME_THRESHOLD': 5,
        'HIERARCHICAL_INDUSTRIES': HIERARCHICAL_INDUSTRIES,
        'INDUSTRIES': INDUSTRIES,
        'i18n': True,
        'GOOGLE_SHEET_EXPORT_SURVEY_FIELDS': GOOGLE_SHEET_EXPORT_SURVEY_FIELDS_TENANT_1,
        'GOOGLE_SHEET_EXPORT_RESULT_FIELDS': GOOGLE_SHEET_EXPORT_RESULT_FIELDS_TENANT_1,
        'PRODUCT_NAME': "Digital Maturity Benchmark",
    },
    'tenant2': {
        'key': 'tenant2',
        'label': 'Tenant 2 label',
        'slug': 'tenant2-slug',
        'in_dmb_footer': True,
        'footer_label': 'Tenant 2 Footer Label',
        'QUALTRICS_SURVEY_ID': 'SV_aaxxxxxxxx',
        'EMAIL_TO': 'Q97_4_TEXT',
        'EMAIL_BCC': 'Q97_5_TEXT',
        'DIMENSIONS': MOCKED_DIMENSIONS,
        'MULTI_ANSWER_QUESTIONS': MOCKED_MULTI_ANSWER_QUESTIONS,
        'WEIGHTS': MOCKED_WEIGHTS,
        'DIMENSIONS_WEIGHTS_QUESTION_ID': 'Q4',
        'DIMENSIONS_WEIGHTS': MOCKED_DIMENSIONS_WEIGHTS,
        'CONTENT_DATA': MOCKED_CONTENT_DATA_TENANT_2,
        'FORCED_INDUSTRY': 'ic-bnpj',
        'EXCLUDED_TIME_THRESHOLD': 5,
        'HIERARCHICAL_INDUSTRIES': HIERARCHICAL_INDUSTRIES,
        'INDUSTRIES': INDUSTRIES,
        'i18n': False,
        'GOOGLE_SHEET_EXPORT_SURVEY_FIELDS': GOOGLE_SHEET_EXPORT_SURVEY_FIELDS_TENANT_2,
        'GOOGLE_SHEET_EXPORT_RESULT_FIELDS': GOOGLE_SHEET_EXPORT_RESULT_FIELDS_TENANT_2,
        'PRODUCT_NAME': "Digital Maturity Benchmark",
    },
    'tenant3': {
        'key': 'tenant3',
        'label': 'Tenant 3 label',
        'slug': 'tenant3-slug',
        'in_dmb_footer': False,
        'footer_label': 'Tenant 3 Footer Label',
        'QUALTRICS_SURVEY_ID': 'SV_bbxxxxxxxx',
        'EMAIL_TO': 'Q97_4_TEXT',
        'EMAIL_BCC': 'Q97_5_TEXT',
        'DIMENSIONS': MOCKED_DIMENSIONS,
        'MULTI_ANSWER_QUESTIONS': MOCKED_MULTI_ANSWER_QUESTIONS,
        'WEIGHTS': MOCKED_WEIGHTS,
        'DIMENSIONS_WEIGHTS_QUESTION_ID': None,
        'DIMENSIONS_WEIGHTS': MOCKED_DIMENSIONS_WEIGHTS[1],
        'FORCED_INDUSTRY': 'ic-bnpj',
        'EXCLUDED_TIME_THRESHOLD': 5,
        'i18n': True,
        'PRODUCT_NAME': "Digital Maturity Benchmark",
        'HIERARCHICAL_INDUSTRIES': HIERARCHICAL_INDUSTRIES_UNICODE,
        'INDUSTRIES': INDUSTRIES_UNICODE,
    }
}
MOCKED_I18N_TENANTS = '|'.join([v['slug'] for k, v in MOCKED_TENANTS.items() if v['i18n']])
MOCKED_NOT_I18N_TENANTS = '|'.join([v['slug'] for k, v in MOCKED_TENANTS.items() if not v['i18n']])

MOCKED_TENANTS_SLUG_TO_KEY = {v['slug']: k for k, v in MOCKED_TENANTS.items()}

qualtrics_text_export = {
    'responses': [
        {
            'Organization-sum': '0.0',
            'Organization-weightedAvg': '0.0',
            'Organization-weightedStdDev': '0.0',
            'sid': '1',
            'ResponseID': 'AAA',
            'Enter Embedded Data Field Name Here...': '',
            'sponsor': '',
            'company_name': 'new survey',
            'dmb': '0.5',
            'StartDate': '2018-07-31 14:16:06',
            'EndDate': '2018-07-31 15:18:56',
            'Q3': 'Some text for answer Q3',
            'Q4': 'Some text for answer Q4',
            'Q5_1': 'Some text for answer Q5_1',
            'Q5_2': 'Some text for answer Q5_2',
            'Q5_3': 'Some text for answer Q5_3',
            'Q6': 'Some text for answer Q6',
            'Q7': 'Some text for answer Q7',
            'Q8': 'Some text for answer Q8',
            'Q10': 'Some text for answer Q10',
            'Q11': 'Some text for answer Q11',
            'Q12': 'Some text for answer Q12',
            'Finished': '1',
        },
        {
            'Organization-sum': '0.0',
            'Organization-weightedAvg': '0.0',
            'Organization-weightedStdDev': '0.0',
            'sid': '3',
            'ResponseID': 'AAB',
            'Enter Embedded Data Field Name Here...': '',
            'sponsor': '',
            'company_name': 'new survey',
            'dmb': '0.5',
            'StartDate': '2018-07-31 14:16:07',
            'EndDate': '2018-07-31 15:18:56',
            'Q3': 'Some text for answer Q3',
            'Q4': 'Some text for answer Q4',
            'Q5_1': 'Some text for answer Q5_1',
            'Q5_2': 'Some text for answer Q5_2',
            'Q5_3': 'Some text for answer Q5_3',
            'Q6': 'Some text for answer Q6',
            'Q7': 'Some text for answer Q7',
            'Q8': 'Some text for answer Q8',
            'Q10': 'Some text for answer Q10',
            'Q11': 'Some text for answer Q11',
            'Q12': 'Some text for answer Q12',
            'Finished': '0',
        },
        {
            'Organization-sum': '0.0',
            'Organization-weightedAvg': '0.0',
            'Organization-weightedStdDev': '0.0',
            'sid': '2',
            'ResponseID': 'AAC',
            'Enter Embedded Data Field Name Here...': '',
            'sponsor': '',
            'company_name': 'new survey',
            'dmb': '0.5',
            'StartDate': '2018-07-31 14:16:08',
            'EndDate': '2018-07-31 15:18:56',
            'Q3': 'Some text for answer Q3',
            'Q4': 'Some text for answer Q4',
            'Q5_1': 'Some text for answer Q5_1',
            'Q5_2': 'Some text for answer Q5_2',
            'Q5_3': 'Some text for answer Q5_3',
            'Q6': 'Some text for answer Q6',
            'Q7': 'Some text for answer Q7',
            'Q8': 'Some text for answer Q8',
            'Q10': 'Some text for answer Q10',
            'Q11': 'Some text for answer Q11',
            'Q12': 'Some text for answer Q12',
            'Finished': '1',
        },
        {
            'Organization-sum': '0.0',
            'Organization-weightedAvg': '0.0',
            'Organization-weightedStdDev': '0.0',
            'sid': '2',
            'ResponseID': 'AAD',
            'Enter Embedded Data Field Name Here...': '',
            'sponsor': '',
            'company_name': 'new survey test 4',
            'dmb': '0.5',
            'StartDate': '2018-07-31 14:16:09',
            'EndDate': '2018-07-31 15:18:56',
            'Q3': 'Some text for answer Q3',
            'Q4': 'Some text for answer Q4',
            'Q5_1': 'Some text for answer Q5_1',
            'Q5_2': 'Some text for answer Q5_2',
            'Q5_3': 'Some text for answer Q5_3',
            'Q6': 'Some text for answer Q6',
            'Q7': 'Some text for answer Q7',
            'Q8': 'Some text for answer Q8',
            'Q10': 'Some text for answer Q10',
            'Q11': 'Some text for answer Q11',
            'Q12': 'Some text for answer Q12',
            'Finished': '1',
        }
    ]
}


survey_definition_dict = {
    "id": "SV_beH0HTFtnk4A5rD",
    "name": "DMB Survey - Staging",
    "ownerId": "UR_eQjASeYvNZoXnPD",
    "organizationId": "google",
    "isActive": True,
    "creationDate": "2018-11-29T13:27:15Z",
    "lastModifiedDate": "2018-12-11T17:22:31Z",
    "expiration": {
        "startDate": None,
        "endDate": None
    },
    "questions": {
        "QID97": {
            "questionType": {
                "type": "TE",
                "selector": "FORM",
                "subSelector": None
            },
            "questionText": "Where should we send your results once you've finished?",
            "questionLabel": None,
            "validation": {
                "doesForceResponse": False,
                "type": "CustomValidation"
            },
            "questionName": "Q97",
            "choices": {
                "4": {
                    "description": "Enter your email address (required)",
                    "choiceText": "Enter your email address (required)",
                    "imageDescription": None,
                    "variableName": None,
                    "analyze": True
                },
                "5": {
                    "description": "Who else should be emailed the report? (optional)",
                    "choiceText": "Who else should be emailed the report? (optional)",
                    "imageDescription": None,
                    "variableName": None,
                    "analyze": True
                }
            }
        },
        "QID173": {
            "questionType": {
                "type": "MC",
                "selector": "MAVR",
                "subSelector": "TX"
            },
            "questionText": "Privacy policy\n<p class=\"dmb-privacy__description h-c-copy\">\nYou’ll need to agree to the use of your responses so we can create the report for you.\n</p>\n\n            <a class=\"dmb-button dmb-button--secondary dmb-button--external\"           href=\"https://policies.google.com/privacy\"\n            target=\"_blank\"> <svg class=\"dmb-button__icon h-c-icon h-c-icon--18px\" role=\"img\" viewbox=\"0 0 24 24\"><path d=\"M20 12l-1.41-1.41L13 16.17V4h-2v12.17l-5.58-5.59L4 12l8 8 8-8z\"></path></svg> <span class=\"dmb-button__text\">View statement</span> </a> \n            </button>",
            "questionLabel": None,
            "validation": {
                "doesForceResponse": False,
                "type": "CustomValidation"
            },
            "questionName": "Q173",
            "choices": {
                "1": {
                    "recode": "1",
                    "description": "Agree to our privacy statement",
                    "choiceText": "Agree to our privacy statement",
                    "imageDescription": None,
                    "variableName": None,
                    "analyze": True
                }
            }
        },
        "QID102": {
            "questionType": {
                "type": "MC",
                "selector": "SAVR",
                "subSelector": "TX"
            },
            "questionText": "<h2 class=\"dmb-dimension-header\">Assets &amp; Ads</h2>\nWhich of the following best describes the extent to which your organisation uses data to inform creative development?",
            "questionLabel": None,
            "validation": {
                "doesForceResponse": True
            },
            "questionName": "Q102",
            "choices": {
                "1": {
                    "recode": "0",
                    "description": "Creatives are based mainly on brand and product principles.",
                    "choiceText": "Creatives are based mainly on brand and product principles.",
                    "imageDescription": None,
                    "variableName": None,
                    "analyze": True,
                    "scoring": [
                        {
                            "category": "SC_577ByjK0PVdnw69",
                            "value": "0"
                        }
                    ]
                },
                "2": {
                    "recode": "1",
                    "description": "Creatives are based mainly on insights from a specific digital channel and advanced analytics.",
                    "choiceText": "Creatives are based mainly on insights from a specific digital channel and advanced analytics.",
                    "imageDescription": None,
                    "variableName": None,
                    "analyze": True,
                    "scoring": [
                        {
                            "category": "SC_577ByjK0PVdnw69",
                            "value": "1"
                        }
                    ]
                },
            }
        },
        "QID103": {
            "questionType": {
                "type": "MC",
                "selector": "SAVR",
                "subSelector": "TX"
            },
            "questionText": "How would you describe the connection between your communication channels?",
            "questionLabel": None,
            "validation": {
                "doesForceResponse": True
            },
            "questionName": "Q103",
            "choices": {
                "1": {
                    "recode": "0",
                    "description": "Run largely independently by channel (e.g. display, search, social, email etc.)",
                    "choiceText": "Run largely independently by channel (e.g. display, search, social, email etc.)",
                    "imageDescription": None,
                    "variableName": None,
                    "analyze": True,
                    "scoring": [
                        {
                            "category": "SC_577ByjK0PVdnw69",
                            "value": "0"
                        }
                    ]
                },
                "2": {
                    "recode": "1.33",
                    "description": "Coordinated across online channels without shared timeline.",
                    "choiceText": "Coordinated across online channels without shared timeline.",
                    "imageDescription": None,
                    "variableName": None,
                    "analyze": True,
                    "scoring": [
                        {
                            "category": "SC_577ByjK0PVdnw69",
                            "value": "1.33"
                        }
                    ]
                },
                "3": {
                    "recode": "2.67",
                    "description": "Coordinated and across online channels with shared timeline.",
                    "choiceText": "Coordinated and across online channels with shared timeline.",
                    "imageDescription": None,
                    "variableName": None,
                    "analyze": True,
                    "scoring": [
                        {
                            "category": "SC_577ByjK0PVdnw69",
                            "value": "2.67"
                        }
                    ]
                },
                "4": {
                    "recode": "4",
                    "description": "Coordinated across online and offline channels with shared timeline.",
                    "choiceText": "Coordinated across online and offline channels with shared timeline.",
                    "imageDescription": None,
                    "variableName": None,
                    "analyze": True,
                    "scoring": [
                        {
                            "category": "SC_577ByjK0PVdnw69",
                            "value": "4"
                        }
                    ]
                }
            }
        },
        "QID104": {
            "questionType": {
                "type": "MC",
                "selector": "SAVR",
                "subSelector": "TX"
            },
            "questionText": "How do your media buying and creative origination teams collaborate?",
            "questionLabel": None,
            "validation": {
                "doesForceResponse": True
            },
            "questionName": "Q104",
            "choices": {
                "1": {
                    "recode": "0",
                    "description": "Little or no collaboration, separate or siloed creative processes with separate toolsets in place.",
                    "choiceText": "Little or no collaboration, separate or siloed creative processes with separate toolsets in place.",
                    "imageDescription": None,
                    "variableName": None,
                    "analyze": True,
                    "scoring": [
                        {
                            "category": "SC_577ByjK0PVdnw69",
                            "value": "0"
                        }
                    ]
                },
                "2": {
                    "recode": "1.33",
                    "description": "Some formalised media and creative collaboration, separate toolsets in place.",
                    "choiceText": "Some formalised media and creative collaboration, separate toolsets in place.",
                    "imageDescription": None,
                    "variableName": None,
                    "analyze": True,
                    "scoring": [
                        {
                            "category": "SC_577ByjK0PVdnw69",
                            "value": "1.33"
                        }
                    ]
                },
                "3": {
                    "recode": "2.67",
                    "description": "Media and creative teams working in conjunction using shared project management tools.",
                    "choiceText": "Media and creative teams working in conjunction using shared project management tools.",
                    "imageDescription": None,
                    "variableName": None,
                    "analyze": True,
                    "scoring": [
                        {
                            "category": "SC_577ByjK0PVdnw69",
                            "value": "2.67"
                        }
                    ]
                },
                "4": {
                    "recode": "4",
                    "description": "Media and creative teams working hand in hand from planning to execution using collaborative tools such as a Creative Management Platform (CMP).",
                    "choiceText": "Media and creative teams working hand in hand from planning to execution using collaborative tools such as a Creative Management Platform (CMP).",
                    "imageDescription": None,
                    "variableName": None,
                    "analyze": True,
                    "scoring": [
                        {
                            "category": "SC_577ByjK0PVdnw69",
                            "value": "4"
                        }
                    ]
                }
            }
        },
        "QID128": {
            "questionType": {
                "type": "MC",
                "selector": "MAVR",
                "subSelector": "TX"
            },
            "questionText": "Which of the following targeting methods do you use?  (Select all that apply)",
            "questionLabel": None,
            "validation": {
                "doesForceResponse": True
            },
            "questionName": "Q128",
            "choices": {
                "1": {
                    "recode": "133.1",
                    "description": "Upper funnel targeting (e.g. to drive awareness).",
                    "choiceText": "Upper funnel targeting (e.g. to drive awareness).",
                    "imageDescription": None,
                    "variableName": None,
                    "analyze": True,
                    "scoring": [
                        {
                            "category": "SC_577ByjK0PVdnw69",
                            "value": "1.33"
                        }
                    ]
                },
                "2": {
                    "recode": "133.2",
                    "description": "'Lower funnel targeting (e.g. to drive sales).'",
                    "choiceText": "Lower funnel targeting (e.g. to drive sales).",
                    "imageDescription": None,
                    "variableName": None,
                    "analyze": True,
                    "scoring": [
                        {
                            "category": "SC_577ByjK0PVdnw69",
                            "value": "1.33"
                        }
                    ]
                },
                "3": {
                    "recode": "133.3",
                    "description": "Mid funnel targeting (e.g. to drive consideration).",
                    "choiceText": "Mid funnel targeting (e.g. to drive consideration).",
                    "imageDescription": None,
                    "variableName": None,
                    "analyze": True,
                    "scoring": [
                        {
                            "category": "SC_577ByjK0PVdnw69",
                            "value": "1.33"
                        }
                    ]
                }
            }
        },
        "QID235": {
            "questionLabel": None,
            "questionName": "Q235",
            "questionText": "<h2 class=\"dmb-dimension-header h-c-headline h-c-headline--two\">\n  <img class=\"dmb-dimension-header__icon dmb-u-m-b-s\" src=\"${e://Field/static_url}/img/retail/dimensions/user-engagement.svg\">\n  User interface and navigation optimization\n</h2>\n\nPlease select the maturity level that most accurately describes your organisation's ability to support user interface and navigation optimisation:",
            "questionType": {
                "selector": "SAVR",
                "subSelector": "TX",
                "type": "MC"
            },
            "validation": {
                "doesForceResponse": True
            },
            "choices": {
                "1": {
                    "analyze": True,
                    "choiceText": "Limited Segmentation: All users are analysed in broad segments. \n<br />\n<br />\nLimited UX / UI Focus: UX / UI, messaging, and layout are not regularly updated.\n",
                    "description": "Limited Segmentation: All users are analysed in broad segments. \n<br />\n<br />\nLimited UX / UI Focus: UX / UI, messaging, and layout are not regularly updated.\n",
                    "imageDescription": None,
                    "recode": "1",
                    "scoring": [
                        {
                        "category": "SC_577ByjK0PVdnw69",
                        "value": "0"
                        }
                    ],
                    "variableName": None
                },
                "3": {
                    "analyze": True,
                    "choiceText": "Detailed Segmentation: Segments are based on personal and behavioral characteristics.\n<br />\n<br />\nAdvanced UX / UI: Personalization techniques are used at the segment level to enable customers to reach their baskets in fewer clicks, although load speed is a major consideration.\n<br />\n<br />\nAdvanced Analytics: Customer data is captured, monitored, and analyzed quickly and effectively to drive business decisions.\n",
                    "description": "Detailed Segmentation: Segments are based on personal and behavioral characteristics.\n<br />\n<br />\nAdvanced UX / UI: Personalization techniques are used at the segment level to enable customers to reach their baskets in fewer clicks, although load speed is a major consideration.\n<br />\n<br />\nAdvanced Analytics: Customer data is captured, monitored, and analyzed quickly and effectively to drive business decisions.\n",
                    "imageDescription": None,
                    "recode": "3",
                    "scoring": [
                        {
                        "category": "SC_577ByjK0PVdnw69",
                        "value": "2.67"
                        }
                    ],
                    "variableName": None
                },
                "4": {
                    "analyze": True,
                    "choiceText": "Dynamic Segmentation: The UX / UI can respond to a customer’s in-session behavior as he or she exhibits different segment characteristics.\n<br />\n<br />\nDynamic UX / UI: Sophisticated personalization techniques are used to tailor the customer’s experience in near real-time.\n<br />\n<br />\nAutomated Analytics: Customer data is captured, monitored, and analyzed in near real-time and decisions are automated.",
                    "description": "Dynamic Segmentation: The UX / UI can respond to a customer’s in-session behavior as he or she exhibits different segment characteristics.\n<br />\n<br />\nDynamic UX / UI: Sophisticated personalization techniques are used to tailor the customer’s experience in near real-time.\n<br />\n<br />\nAutomated Analytics: Customer data is captured, monitored, and analyzed in near real-time and decisions are automated.",
                    "imageDescription": None,
                    "recode": "4",
                    "scoring": [
                        {
                        "category": "SC_577ByjK0PVdnw69",
                        "value": "4"
                        }
                    ],
                    "variableName": None
                },
                "5": {
                    "analyze": True,
                    "choiceText": "Basic Segmentation: Uses standard characteristics (e.g., gender, geography) for segmentation.\n<br />\n<br />\nBasic UX / UI: Basic user understanding is used to design the look and feel of the online experience.\n<br />\n<br />\nBasic Analytics: Ability to synthesize customer information and observations into actionable insights.\n",
                    "description": "Basic Segmentation: Uses standard characteristics (e.g., gender, geography) for segmentation.\n<br />\n<br />\nBasic UX / UI: Basic user understanding is used to design the look and feel of the online experience.\n<br />\n<br />\nBasic Analytics: Ability to synthesize customer information and observations into actionable insights.\n",
                    "imageDescription": None,
                    "recode": "2",
                    "variableName": None
                }
            },
        }
    },
    "exportColumnMap": {
        "Q97_4_TEXT": {
            "question": "QID97",
            "choice": "QID97.choices.4"
        },
        "Q97_5_TEXT": {
            "question": "QID97",
            "choice": "QID97.choices.5"
        },
        "Q173_1": {
            "question": "QID173",
            "choice": "QID173.choices.1"
        },
        "Q102": {
            "question": "QID102"
        },
        "Q103": {
            "question": "QID103"
        },
        "Q104": {
            "question": "QID104"
        },
        "Q128_133.1": {
            "question": "QID128",
            "choice": "QID128.choices.1"
        },
        "Q128_133.2": {
            "question": "QID128",
            "choice": "QID128.choices.2"
        },
        "Q128_133.3": {
            "question": "QID128",
            "choice": "QID128.choices.3"
        },
    },
    "blocks": {
        "BL_4OcGZZcRLl0cRYp": {
            "description": "User Details",
            "elements": [
                {
                    "type": "Question",
                    "questionId": "QID97"
                },
                {
                    "type": "Question",
                    "questionId": "QID173"
                }
            ]
        },
        "BL_d4IXvKmLwWF9lo9": {
            "description": "Real questions",
            "elements": [
                {
                    "type": "Question",
                    "questionId": "QID102"
                },
                {
                    "type": "Question",
                    "questionId": "QID103"
                },
                {
                    "type": "Question",
                    "questionId": "QID104"
                },
                {
                    "type": "Question",
                    "questionId": "QID128"
                },
                {
                    "type": "Question",
                    "questionId": "QID235"
                },
            ]
        }
    },
    "flow": [
        {
            "type": "EmbeddedData"
        },
        {
            "type": "WebService"
        },
        {
            "id": "BL_4OcGZZcRLl0cRYp",
            "type": "Block"
        },
        {
            "id": "BL_d4IXvKmLwWF9lo9",
            "type": "Block"
        },
        {
            "type": "EmbeddedData"
        },
        {
            "type": "EndSurvey"
        }
    ],
    "embeddedData": [
        {
            "name": "sid"
        },
        {
            "name": "Enter Embedded Data Field Name Here..."
        },
        {
            "name": "sponsor"
        },
        {
            "name": "company_name",
            "type": "Custom"
        },
        {
            "name": "dmb",
            "defaultValue": "${gr://SC_577ByjK0PVdnw69/WeightedMean}"
        }
    ],
    "comments": {
        "QID3": {
            "commentList": [
                {
                    "userId": "UR_eQjASeYvNZoXnPD",
                    "message": "Hero element",
                    "timestamp": 1519214611
                }
            ]
        }
    },
    "loopAndMerge": {},
    "responseCounts": {
        "auditable": 256,
        "generated": 0,
        "deleted": 104
    }
}


survey_def_no_choices_page_break_dict = {
    "id": "SV_beH0HTFtnk4A5rD",
    "name": "DMB Survey - Staging",
    "ownerId": "UR_eQjASeYvNZoXnPD",
    "organizationId": "google",
    "isActive": True,
    "creationDate": "2018-11-29T13:27:15Z",
    "lastModifiedDate": "2018-12-11T17:22:31Z",
    "expiration": {
        "startDate": None,
        "endDate": None
    },
    "questions": {
        "QID102": {
            "questionType": {
                "type": "MC",
                "selector": "SAVR",
                "subSelector": "TX"
            },
            "questionText": "<h2 class=\"dmb-dimension-header\">Assets &amp; Ads</h2>\nWhich of the following best describes the extent to which your organisation uses data to inform creative development?",
            "questionLabel": None,
            "validation": {
                "doesForceResponse": True
            },
            "questionName": "Q102",
            "choices": {
                "1": {
                    "recode": "0",
                    "description": "Creatives are based mainly on brand and product principles.",
                    "choiceText": "Creatives are based mainly on brand and product principles.",
                    "imageDescription": None,
                    "variableName": None,
                    "analyze": True,
                    "scoring": [
                        {
                            "category": "SC_577ByjK0PVdnw69",
                            "value": "0"
                        }
                    ]
                },
                "2": {
                    "recode": "1",
                    "description": "Creatives are based mainly on insights from a specific digital channel and advanced analytics.",
                    "choiceText": "Creatives are based mainly on insights from a specific digital channel and advanced analytics.",
                    "imageDescription": None,
                    "variableName": None,
                    "analyze": True,
                    "scoring": [
                        {
                            "category": "SC_577ByjK0PVdnw69",
                            "value": "1"
                        }
                    ]
                },
            }
        },
        "QID267": {
            "questionLabel": None,
            "questionName": "Q39",
            "questionText": "<div></div>",
            "questionType": {
                "selector": "TB",
                "subSelector": None,
                "type": "DB"
            },
            "validation": {
                "doesForceResponse": False
            }
        },

    },
    "exportColumnMap": {
        "Q97_4_TEXT": {
            "question": "QID97",
            "choice": "QID97.choices.4"
        },
        "Q97_5_TEXT": {
            "question": "QID97",
            "choice": "QID97.choices.5"
        },
        "Q173_1": {
            "question": "QID173",
            "choice": "QID173.choices.1"
        },
        "Q102": {
            "question": "QID102"
        },
        "Q103": {
            "question": "QID103"
        },
        "Q104": {
            "question": "QID104"
        },
        "Q128_133.1": {
            "question": "QID128",
            "choice": "QID128.choices.1"
        },
        "Q128_133.2": {
            "question": "QID128",
            "choice": "QID128.choices.2"
        },
        "Q128_133.3": {
            "question": "QID128",
            "choice": "QID128.choices.3"
        },
        "Q235": {
            "question": "QID235"
        }
    },
    "blocks": {
        "BL_4OcGZZcRLl0cRYp": {
            "description": "User Details",
            "elements": [
                {
                    "type": "Question",
                    "questionId": "QID102"
                },
                {
                    "type": "Question",
                    "questionId": "QID267"
                },
                {
                    "type": "PageBreak"
                },
            ]
        }
    },
    "flow": [
        {
            "type": "EmbeddedData"
        },
        {
            "type": "WebService"
        },
        {
            "id": "BL_4OcGZZcRLl0cRYp",
            "type": "Block"
        },
        {
            "id": "BL_d4IXvKmLwWF9lo9",
            "type": "Block"
        },
        {
            "type": "EmbeddedData"
        },
        {
            "type": "EndSurvey"
        }
    ],
    "embeddedData": [
        {
            "name": "sid"
        },
        {
            "name": "Enter Embedded Data Field Name Here..."
        },
        {
            "name": "sponsor"
        },
        {
            "name": "company_name",
            "type": "Custom"
        },
        {
            "name": "dmb",
            "defaultValue": "${gr://SC_577ByjK0PVdnw69/WeightedMean}"
        }
    ],
    "comments": {
        "QID3": {
            "commentList": [
                {
                    "userId": "UR_eQjASeYvNZoXnPD",
                    "message": "Hero element",
                    "timestamp": 1519214611
                }
            ]
        }
    },
    "loopAndMerge": {},
    "responseCounts": {
        "auditable": 256,
        "generated": 0,
        "deleted": 104
    }
}


qualtrics_definition = {
    'result': survey_definition_dict
}


def get_mocked_results(started_after=None, text=False):
    qualtrics_data = qualtrics_export.get('responses')
    copied = [el for el in qualtrics_data]
    if text:
        copied = [el for el in qualtrics_text_export.get('responses')]

    if started_after:
        index = len(qualtrics_data)
        for idx, item in enumerate(qualtrics_data):
            if dateparse.parse_datetime(item.get('StartDate')) > started_after:
                index = idx
                break
        copied = [el for el in qualtrics_data[index:]]

    return {'responses': copied}


def get_mocked_results_unfished(started_after=None, text=False):
    unfinished_res = [result for result in get_mocked_results(started_after=started_after, text=text)['responses']
                      if result['Finished'] == '0']
    return {'responses': unfinished_res}


def get_survey_definition():
    return survey_definition_dict
