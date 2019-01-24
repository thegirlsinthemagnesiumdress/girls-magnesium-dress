from core.models import Survey
from django.utils import dateparse
from collections import OrderedDict
from core.conf.utils import flatten_industries


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
])

INDUSTRIES = flatten_industries(HIERARCHICAL_INDUSTRIES, None, {})


def generate_surveys():
    companies_name = ['1', '2', '3']
    surveys = []

    for company_name in companies_name:
        s = Survey(company_name=company_name, industry="re", country="it")
        s.save()
        surveys.append(s)

    return surveys


def get_mocked_results(started_after=None):
    if not started_after:
        return qualtrics_export
    else:
        index = len(qualtrics_export)
        qualtrics_data = qualtrics_export.get('responses')
        for idx, item in enumerate(qualtrics_data):
            if dateparse.parse_datetime(item.get('StartDate')) > started_after:
                index = idx
                break
        return {'responses': qualtrics_data[index:]}


def get_mocked_results_unfished(started_after=None):
    unfinished_res = [result for result in get_mocked_results(started_after=started_after)['responses']
                      if result['Finished'] == '0']
    return {'responses': unfinished_res}
