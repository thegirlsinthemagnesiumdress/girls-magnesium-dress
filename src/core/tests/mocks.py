from core.models import Survey


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
            'Q160': '0',
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
            'Q160': '0',
            'dmb': '0.5',
            'StartDate': '2018-07-31 14:16:06',
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
            'Q160': '1',
            'dmb': '0.5',
            'StartDate': '2018-07-31 14:16:06',
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
        }
    ]
}


def generate_surveys():
    companies_name = ['1', '2', '3']
    surveys = []

    for company_name in companies_name:
        s = Survey(company_name=company_name)
        s.save()
        surveys.append(s)

    return surveys


def get_mocked_results(response_id=None):
    if not response_id:
        return qualtrics_export
    else:
        index = len(qualtrics_export)
        qualtrics_data = qualtrics_export.get('responses')
        for idx, item in enumerate(qualtrics_data):
            if item.get('ResponseID') == response_id:
                index = idx
                break
        return {'responses': qualtrics_data[index:]}
