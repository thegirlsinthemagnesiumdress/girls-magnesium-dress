from core.models import Survey

weights = {
    'Q3': 2,
    'Q4': 0.5,
    'Q7': 0.3,
}

response_0_questions = [
    ('Q3', 2.0, 2, 'dimension_A'),
    ('Q4', 0.0, 0.5, 'dimension_A'),
    ('Q5_1', 2.0, 1, 'dimension_A'),
    ('Q5_2', 0.0, 1, 'dimension_A'),
    ('Q5_3', 3.0, 1, 'dimension_B'),
    ('Q6', 4.0, 1, 'dimension_B'),
    ('Q7', 2.0, 0.3, 'dimension_B'),
    ('Q8', 4.0, 1, 'dimension_C'),
    ('Q10', 0.0, 1, 'dimension_C'),
    ('Q11', 1.0, 1, 'dimension_C'),
    ('Q12', 2.0, 1, 'dimension_C'),
]

response_1_questions = [
    ('Q3', 1.0, 2, 'dimension_A'),
    ('Q4', 3.0, 0.5, 'dimension_A'),
    ('Q5_1', 1.0, 1, 'dimension_A'),
    ('Q5_2', 2.0, 1, 'dimension_A'),
    ('Q5_3', 4.0, 1, 'dimension_B'),
    ('Q6', 0.0, 1, 'dimension_B'),
    ('Q7', 1.0, 0.3, 'dimension_B'),
    ('Q8', 0.0, 1, 'dimension_C'),
    ('Q10', 0.0, 1, 'dimension_C'),
    ('Q11', 1.0, 1, 'dimension_C'),
    ('Q12', 0.0, 1, 'dimension_C'),
]


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
            'industry': 'A',
            'dmb': '0.5',
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
            'industry': 'A',
            'dmb': '0.5',
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
            'industry': 'B',
            'dmb': '0.5',
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
        }
    ]
}

dimensions = {
    'dimension_A': ['Q3', 'Q4', 'Q5_1', 'Q5_2'],
    'dimension_B': ['Q5_3', 'Q6', 'Q7'],
    'dimension_C': ['Q8', 'Q10', 'Q11', 'Q12'],
}

response_1_overall = 1.907407407

DMB = {
    'survey': {
        '1': {
            'overall': 1.5,
            'best_practice': 0,
            'category_overall': {
                'dimension_A': 1.388888889,  # 1.125,
            },
            'category_best_practice': {
                'dimension_A': 0,  # 1.75,
            },
        }
    }
}


def generate_surveys():
    companies_name = ['1', '2', '3']
    surveys = []

    for company_name in companies_name:
        s = Survey(company_name=company_name)
        s.save()
        surveys.append(s)

    return surveys


def get_mocked_results(all=True, uid=None):
    if all:
        return qualtrics_export
    else:
        index = len(qualtrics_export)
        qualtrics_data = qualtrics_export.get('responses')
        for idx, item in enumerate(qualtrics_data):
            if item.get('ResponseID') == uid:
                index = idx
                break
        return {'responses': qualtrics_data[index:]}
