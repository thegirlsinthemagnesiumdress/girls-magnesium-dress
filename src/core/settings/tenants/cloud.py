# coding=utf-8
# flake8: noqa
from . import GOOGLE_SHEET_BASE_SURVEY_FIELDS, GOOGLE_SHEET_BASE_RESULT_FIELDS

# DIMENSIONS
DIMENSION_LEARN = 'learn'
DIMENSION_LEAD = 'lead'
DIMENSION_SCALE = 'scale'
DIMENSION_SECURE = 'secure'

# SUBDIMENSIONS
SUBDIMENSION_EXTERNAL_EXPERIENCE = 'external_experience'
SUBDIMENSION_UPSKILLING = 'upskilling'
SUBDIMENSION_TEAMWORK = 'teamwork'
SUBDIMENSION_SPONSORSHIP = 'sponsorship'
SUBDIMENSION_INFRASTRUCTURE_AS_CODE = 'infrastructure_as_code'
SUBDIMENSION_RESOURCE_MANAGEMENT = 'resource_management'
SUBDIMENSION_CI_CD = 'ci_cd'
SUBDIMENSION_ARCHITECTURE = 'architecture'
SUBDIMENSION_IDENTITY_AND_ACCESS_MANAGEMENT = 'identity_and_access_management'
SUBDIMENSION_DATA_MANAGEMENT = 'data_management'
SUBDIMENSION_ACCESS_MANAGEMENT = 'access_management'
SUBDIMENSION_IDENTITY_MANAGEMENT = 'identity_management'
SUBDIMENSION_NETWORKING = 'networking'


# LEVELS
LEVEL_0 = 0
LEVEL_1 = 1
LEVEL_2 = 2
LEVEL_3 = 3

# WEIGHTS
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


SUBDIMENSION_TITLES = {
    SUBDIMENSION_EXTERNAL_EXPERIENCE: 'External Experience',
    SUBDIMENSION_UPSKILLING: 'Upskilling',
    SUBDIMENSION_TEAMWORK: 'Teamwork',
    SUBDIMENSION_SPONSORSHIP: 'Sponsorship',
    SUBDIMENSION_INFRASTRUCTURE_AS_CODE: 'Infrastructure as Code',
    SUBDIMENSION_RESOURCE_MANAGEMENT: 'Resource Management',
    SUBDIMENSION_CI_CD: 'Continuous Integration and Delivery (CI/CD)',
    SUBDIMENSION_ARCHITECTURE: 'Architecture',
    SUBDIMENSION_IDENTITY_AND_ACCESS_MANAGEMENT: 'Identity and Access Management',
    SUBDIMENSION_DATA_MANAGEMENT: 'Data Management',
    SUBDIMENSION_IDENTITY_MANAGEMENT: 'Identity Management',
    SUBDIMENSION_ACCESS_MANAGEMENT: 'Access Management',
    SUBDIMENSION_NETWORKING: 'Networking',
}

SUBDIMENSION_ORDER = {
    DIMENSION_LEARN: [
        SUBDIMENSION_EXTERNAL_EXPERIENCE,
        SUBDIMENSION_UPSKILLING,
    ],
    DIMENSION_LEAD: [
        SUBDIMENSION_TEAMWORK,
        SUBDIMENSION_SPONSORSHIP,
    ],
    DIMENSION_SCALE: [
        SUBDIMENSION_INFRASTRUCTURE_AS_CODE,
        SUBDIMENSION_RESOURCE_MANAGEMENT,
        SUBDIMENSION_CI_CD,
        SUBDIMENSION_ARCHITECTURE,
    ],
    DIMENSION_SECURE:[
        SUBDIMENSION_IDENTITY_AND_ACCESS_MANAGEMENT,
        SUBDIMENSION_DATA_MANAGEMENT,
        SUBDIMENSION_ACCESS_MANAGEMENT,
        SUBDIMENSION_IDENTITY_MANAGEMENT,
        SUBDIMENSION_NETWORKING,
    ]
}


SUBDIMENSION_DESCRIPTION = 'Epics are clearly defined, nonoverlapping workstreams tied back to the four themes of cloud maturity. You should design programs around the epics to help you solidify your maturity in any given phase, or take it to the next level. More information on the themes and epics of cloud maturity can be found in the <a class="h-c-inline-link" href="https://cloud.google.com/adoption-framework/">Google Cloud Adoption Framework</a> whitepaper.'


SUBDIMENSION_DESCRIPTIONS = {
    SUBDIMENSION_EXTERNAL_EXPERIENCE: 'Accelerating cloud adoption by applying best practices and other organizational lessons learned from day one, through experienced subject matter experts.',
    SUBDIMENSION_UPSKILLING: 'Investing in learning, so that the incumbent staff may combine their existing in-depth knowledge about the business and the current IT state with learnings about new best practices.',
    SUBDIMENSION_TEAMWORK: 'Building a team that lives and breathes behaviors and culture, which includes high collaboration and trust, so that cloud technology is utilized in the most optimal manner.',
    SUBDIMENSION_SPONSORSHIP: 'Passionately and continuously demonstrating executive support for the cloud adoption strategy, so that early adopters have a widely recognized mandate for change.',
    SUBDIMENSION_INFRASTRUCTURE_AS_CODE: 'Automating through code the configuration and provisioning of resources, so that human error is reduced, time is saved, and every step is fully documented.',
    SUBDIMENSION_RESOURCE_MANAGEMENT: 'Organizing, naming, and setting quotas of cloud resources in order to ensure a structured, consistent, and controlled environment.',
    SUBDIMENSION_CI_CD: 'Automating changes to the system through a CI/CD process pipeline, so that all changes can be tested, audited, and deployed with minimal interruption. ',
    SUBDIMENSION_ARCHITECTURE: 'Providing best practice recommendations and a forward-looking view of the appropriate cloud compute and storage choices. ',
    SUBDIMENSION_DATA_MANAGEMENT: 'Understanding and managing what data is being stored, where it originates from, how sensitive it is, and who is accessing it — for the purpose of keeping data safe, discoverable, and useful.',
    SUBDIMENSION_IDENTITY_MANAGEMENT: 'Reliably authenticating users’ or services’ identity and guarding against loss of credentials and attempts at impersonation.',
    SUBDIMENSION_ACCESS_MANAGEMENT: 'Ensuring that only the right people and services are authorized to perform the right actions on the right resources.',
    SUBDIMENSION_NETWORKING: 'Connecting and protecting services and the flow of data between them via logical boundaries, regardless of a service’s identity or permissions.',
}

DIMENSIONS = {
    DIMENSION_LEARN: [
        'Q7',
        'Q8',
        'Q9',
        'Q10',
        'Q11',
    ],
    DIMENSION_LEAD: [
        'Q13',
        'Q14',
        'Q15',
        'Q16',
        'Q17',
        'Q18',
    ],
    DIMENSION_SCALE: [
        'Q20',
        'Q21',
        'Q22',
        'Q23',
        'Q24',
        'Q25',
    ],
    DIMENSION_SECURE: [
        'Q27',
        'Q28',
        'Q29',
        'Q30',
        'Q31',
        'Q32',
        'Q33',
        'Q34',
    ],
    SUBDIMENSION_EXTERNAL_EXPERIENCE: [
        'Q7',
        'Q11',
    ],
    SUBDIMENSION_UPSKILLING: [
        'Q8',
        'Q9',
        'Q10',
    ],
    SUBDIMENSION_TEAMWORK: [
        'Q13',
        'Q15',
        'Q16',
        'Q18',
    ],
    SUBDIMENSION_SPONSORSHIP: [
        'Q14',
        'Q17',
    ],
    SUBDIMENSION_INFRASTRUCTURE_AS_CODE: [
        'Q20',
    ],
    SUBDIMENSION_RESOURCE_MANAGEMENT: [
        'Q21',
        'Q22',
    ],
    SUBDIMENSION_CI_CD: [
        'Q23',
        'Q24',
    ],
    SUBDIMENSION_ARCHITECTURE: [
        'Q25'
    ],
    SUBDIMENSION_DATA_MANAGEMENT: [
        'Q27',
        'Q29',
        'Q33',
    ],
    SUBDIMENSION_IDENTITY_AND_ACCESS_MANAGEMENT: [
        'Q28',
        'Q30',
    ],
    SUBDIMENSION_ACCESS_MANAGEMENT: [
        'Q32',
    ],
    SUBDIMENSION_IDENTITY_MANAGEMENT: [
        'Q31',
    ],
    SUBDIMENSION_NETWORKING: [
        'Q34',
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
    LEVEL_0: 'LEVEL 0 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
    LEVEL_1: 'LEVEL 1 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
    LEVEL_2: 'LEVEL 2 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
    LEVEL_3: 'LEVEL 3 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
}

REPORT_LEVEL_DESCRIPTIONS = {
    LEVEL_0: 'LEVEL 0 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
    LEVEL_1: 'LEVEL 1 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
    LEVEL_2: 'LEVEL 2 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
    LEVEL_3: 'LEVEL 3 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
}


INDUSTRY_AVG_DESCRIPTION = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'

INDUSTRY_BEST_DESCRIPTION = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'


DIMENSION_HEADER_DESCRIPTION = {
    DIMENSION_LEARN: 'LEARN - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
    DIMENSION_LEAD: 'LEAD - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
    DIMENSION_SCALE: 'SCALE - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
    DIMENSION_SECURE: 'SECURE - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
}


DIMENSION_LEVEL_DESCRIPTION = {
    DIMENSION_LEARN: {
        LEVEL_0: 'LEVEL 0 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        LEVEL_1: 'LEVEL 1 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        LEVEL_2: 'LEVEL 2 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        LEVEL_3: 'LEVEL 3 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
    },
    DIMENSION_LEAD: {
        LEVEL_0: 'LEVEL 0 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        LEVEL_1: 'LEVEL 1 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        LEVEL_2: 'LEVEL 2 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        LEVEL_3: 'LEVEL 3 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
    },
    DIMENSION_SCALE: {
        LEVEL_0: 'LEVEL 0 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        LEVEL_1: 'LEVEL 1 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        LEVEL_2: 'LEVEL 2 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        LEVEL_3: 'LEVEL 3 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
    },
    DIMENSION_SECURE: {
        LEVEL_0: 'LEVEL 0 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        LEVEL_1: 'LEVEL 1 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        LEVEL_2: 'LEVEL 2 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        LEVEL_3: 'LEVEL 3 - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
    },
}


# DATA_ACTIVATION_GUIDE_CTA = {
#     'text': '',
#     'link': '',
# }


DIMENSION_LEVEL_RECOMMENDATIONS = {
    DIMENSION_LEARN: {
        LEVEL_0: [
            {
                'header': 'LEARN - Level 0 - Recommendation 1',
                'text': 'LEARN - Level 0 - Recommendation 1 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'LEARN - Level 0 - Recommendation 2',
                'text': 'LEARN - Level 0 - Recommendation 2 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'LEARN - Level 0 - Recommendation 3',
                'text': 'LEARN - Level 0 - Recommendation 3 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'LEARN - Level 0 - Recommendation 4',
                'text': 'LEARN - Level 0 - Recommendation 4 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
        ],
        LEVEL_1: [
            {
                'header': 'LEARN - Level 1 - Recommendation 1',
                'text': 'LEARN - Level 1 - Recommendation 1 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'LEARN - Level 1 - Recommendation 2',
                'text': 'LEARN - Level 1 - Recommendation 2 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'LEARN - Level 1 - Recommendation 3',
                'text': 'LEARN - Level 1 - Recommendation 3 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'LEARN - Level 1 - Recommendation 4',
                'text': 'LEARN - Level 1 - Recommendation 4 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
        ],
        LEVEL_2: [
            {
                'header': 'LEARN - Level 2 - Recommendation 1',
                'text': 'LEARN - Level 2 - Recommendation 1 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'LEARN - Level 2 - Recommendation 2',
                'text': 'LEARN - Level 2 - Recommendation 2 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'LEARN - Level 2 - Recommendation 3',
                'text': 'LEARN - Level 2 - Recommendation 3 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'LEARN - Level 2 - Recommendation 4',
                'text': 'LEARN - Level 2 - Recommendation 4 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
        ],
        LEVEL_3: [
            {
                'header': 'LEARN - Level 3 - Recommendation 1',
                'text': 'LEARN - Level 3 - Recommendation 1 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'LEARN - Level 3 - Recommendation 2',
                'text': 'LEARN - Level 3 - Recommendation 2 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'LEARN - Level 3 - Recommendation 3',
                'text': 'LEARN - Level 3 - Recommendation 3 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'LEARN - Level 3 - Recommendation 4',
                'text': 'LEARN - Level 3 - Recommendation 4 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
        ],
    },
    DIMENSION_LEAD: {
        LEVEL_0: [
            {
                'header': 'LEAD - Level 0 - Recommendation 1',
                'text': 'LEAD - Level 0 - Recommendation 1 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'LEAD - Level 0 - Recommendation 2',
                'text': 'LEAD - Level 0 - Recommendation 2 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'LEAD - Level 0 - Recommendation 3',
                'text': 'LEAD - Level 0 - Recommendation 3 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'LEAD - Level 0 - Recommendation 4',
                'text': 'LEAD - Level 0 - Recommendation 4 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
        ],
        LEVEL_1: [
            {
                'header': 'LEAD - Level 1 - Recommendation 1',
                'text': 'LEAD - Level 1 - Recommendation 1 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'LEAD - Level 1 - Recommendation 2',
                'text': 'LEAD - Level 1 - Recommendation 2 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'LEAD - Level 1 - Recommendation 3',
                'text': 'LEAD - Level 1 - Recommendation 3 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'LEAD - Level 1 - Recommendation 4',
                'text': 'LEAD - Level 1 - Recommendation 4 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
        ],
        LEVEL_2: [
            {
                'header': 'LEAD - Level 2 - Recommendation 1',
                'text': 'LEAD - Level 2 - Recommendation 1 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'LEAD - Level 2 - Recommendation 2',
                'text': 'LEAD - Level 2 - Recommendation 2 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'LEAD - Level 2 - Recommendation 3',
                'text': 'LEAD - Level 2 - Recommendation 3 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'LEAD - Level 2 - Recommendation 4',
                'text': 'LEAD - Level 2 - Recommendation 4 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
        ],
        LEVEL_3: [
            {
                'header': 'LEAD - Level 3 - Recommendation 1',
                'text': 'LEAD - Level 3 - Recommendation 1 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'LEAD - Level 3 - Recommendation 2',
                'text': 'LEAD - Level 3 - Recommendation 2 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'LEAD - Level 3 - Recommendation 3',
                'text': 'LEAD - Level 3 - Recommendation 3 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'LEAD - Level 3 - Recommendation 4',
                'text': 'LEAD - Level 3 - Recommendation 4 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
        ],
    },
    DIMENSION_SCALE: {
        LEVEL_0: [
            {
                'header': 'SECURE - Level 0 - Recommendation 1',
                'text': 'SECURE - Level 0 - Recommendation 1 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'SECURE - Level 0 - Recommendation 2',
                'text': 'SECURE - Level 0 - Recommendation 2 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'SECURE - Level 0 - Recommendation 3',
                'text': 'SECURE - Level 0 - Recommendation 3 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'SECURE - Level 0 - Recommendation 4',
                'text': 'SECURE - Level 0 - Recommendation 4 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
        ],
        LEVEL_1: [
            {
                'header': 'SECURE - Level 1 - Recommendation 1',
                'text': 'SECURE - Level 1 - Recommendation 1 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'SECURE - Level 1 - Recommendation 2',
                'text': 'SECURE - Level 1 - Recommendation 2 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'SECURE - Level 1 - Recommendation 3',
                'text': 'SECURE - Level 1 - Recommendation 3 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'SECURE - Level 1 - Recommendation 4',
                'text': 'SECURE - Level 1 - Recommendation 4 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
        ],
        LEVEL_2: [
            {
                'header': 'SECURE - Level 2 - Recommendation 1',
                'text': 'SECURE - Level 2 - Recommendation 1 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'SECURE - Level 2 - Recommendation 2',
                'text': 'SECURE - Level 2 - Recommendation 2 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'SECURE - Level 2 - Recommendation 3',
                'text': 'SECURE - Level 2 - Recommendation 3 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'SECURE - Level 2 - Recommendation 4',
                'text': 'SECURE - Level 2 - Recommendation 4 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
        ],
        LEVEL_3: [
            {
                'header': 'SECURE - Level 3 - Recommendation 1',
                'text': 'SECURE - Level 3 - Recommendation 1 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'SECURE - Level 3 - Recommendation 2',
                'text': 'SECURE - Level 3 - Recommendation 2 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'SECURE - Level 3 - Recommendation 3',
                'text': 'SECURE - Level 3 - Recommendation 3 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'SECURE - Level 3 - Recommendation 4',
                'text': 'SECURE - Level 3 - Recommendation 4 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
        ],
    },
    DIMENSION_SECURE: {
        LEVEL_0: [
            {
                'header': 'SECURE - Level 0 - Recommendation 1',
                'text': 'SECURE - Level 0 - Recommendation 1 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'SECURE - Level 0 - Recommendation 2',
                'text': 'SECURE - Level 0 - Recommendation 2 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'SECURE - Level 0 - Recommendation 3',
                'text': 'SECURE - Level 0 - Recommendation 3 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'SECURE - Level 0 - Recommendation 4',
                'text': 'SECURE - Level 0 - Recommendation 4 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
        ],
        LEVEL_1: [
            {
                'header': 'SECURE - Level 1 - Recommendation 1',
                'text': 'SECURE - Level 1 - Recommendation 1 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'SECURE - Level 1 - Recommendation 2',
                'text': 'SECURE - Level 1 - Recommendation 2 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'SECURE - Level 1 - Recommendation 3',
                'text': 'SECURE - Level 1 - Recommendation 3 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'SECURE - Level 1 - Recommendation 4',
                'text': 'SECURE - Level 1 - Recommendation 4 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
        ],
        LEVEL_2: [
            {
                'header': 'SECURE - Level 2 - Recommendation 1',
                'text': 'SECURE - Level 2 - Recommendation 1 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'SECURE - Level 2 - Recommendation 2',
                'text': 'SECURE - Level 2 - Recommendation 2 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'SECURE - Level 2 - Recommendation 3',
                'text': 'SECURE - Level 2 - Recommendation 3 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'SECURE - Level 2 - Recommendation 4',
                'text': 'SECURE - Level 2 - Recommendation 4 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
        ],
        LEVEL_3: [
            {
                'header': 'SECURE - Level 3 - Recommendation 1',
                'text': 'SECURE - Level 3 - Recommendation 1 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'SECURE - Level 3 - Recommendation 2',
                'text': 'SECURE - Level 3 - Recommendation 2 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'SECURE - Level 3 - Recommendation 3',
                'text': 'SECURE - Level 3 - Recommendation 3 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            {
                'header': 'SECURE - Level 3 - Recommendation 4',
                'text': 'SECURE - Level 3 - Recommendation 4 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
        ],
    },
}

DIMENSION_SIDEPANEL_HEADING = 'DIMENSIONS - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'

DIMENSION_SIDEPANEL_DESCRIPTIONS = {
    DIMENSION_LEARN: 'LEARN - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
    DIMENSION_LEAD: 'LEAD - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
    DIMENSION_SCALE: 'SCALE - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
    DIMENSION_SECURE: 'SECURE - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
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
    'subdimensions': SUBDIMENSION_ORDER,
    'subdimension_description': SUBDIMENSION_DESCRIPTION,
    'subdimension_labels': SUBDIMENSION_TITLES,
    'subdimension_descriptions': SUBDIMENSION_DESCRIPTIONS,
}

#####  GOOGLE SHEETS EXPORT TENANT CUSTOMIZATION #####
GOOGLE_SHEET_EXPORT_SURVEY_FIELDS = GOOGLE_SHEET_BASE_SURVEY_FIELDS.copy()
GOOGLE_SHEET_EXPORT_RESULT_FIELDS = GOOGLE_SHEET_BASE_RESULT_FIELDS.copy()
GOOGLE_SHEET_EXPORT_RESULT_FIELDS.update(DIMENSION_TITLES)
#####  END OF GOOGLE SHEETS EXPORT TENANT CUSTOMIZATION #####
