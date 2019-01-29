from core.models import Survey
from django.utils import dateparse

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

    ],
}


def generate_surveys():
    companies_name = ['1', '2', '3']
    surveys = []

    for company_name in companies_name:
        s = Survey(company_name=company_name, industry="re", country="it")
        s.save()
        surveys.append(s)

    return surveys


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
    return qualtrics_definition

qualtrics_definition = {
    "blocks": {},
    "comments": {},
    "creationDate": "2018-11-29T13:27:15Z",
    "embeddedData": [],
    "expiration": {},
    "exportColumnMap": {},
    "flow": [],
    "id": "SV_beH0HTFtnk4A5rD",
    "isActive": True,
    "lastModifiedDate": "2019-01-28T16:04:23Z",
    "loopAndMerge": {},
    "name": "DMB Survey - Staging",
    "organizationId": "google",
    "ownerId": "UR_eQjASeYvNZoXnPD",
    "questions": {
        "QID102": {
            "choices": {
                "1": {
                    "analyze": True,
                    "choiceText": "Creatives are based mainly on brand and product principles.",
                    "description": "Creatives are based mainly on brand and product principles.",
                    "imageDescription": None,
                    "recode": "0",
                    "scoring": [
                        {"category": "SC_577ByjK0PVdnw69", "value": "0"}
                    ],
                    "variableName": None
                },
                "2": {
                    "analyze": True,
                    "choiceText": "Creatives are based mainly on insights from a specific digital channel and advanced analytics.",
                    "description": "Creatives are based mainly on insights from a specific digital channel and advanced analytics.",
                    "imageDescription": None,
                    "recode": "1",
                    "scoring": [
                        {"category": "SC_577ByjK0PVdnw69", "value": "1"}
                    ],
                    "variableName": None
                },
                "3": {
                    "analyze": True,
                    "choiceText": "Creatives are based mainly on insights from all relevant digital channels and advanced analytics.",
                    "description": "Creatives are based mainly on insights from all relevant digital channels and advanced analytics.",
                    "imageDescription": None,
                    "recode": "2",
                    "scoring": [
                        {"category": "SC_577ByjK0PVdnw69", "value": "2"}
                    ],
                    "variableName": None
                },
                "4": {
                    "analyze": True,
                    "choiceText": "Creatives are based on insights from digital and non-digital channels, balanced with brand and product principles.",
                    "description": "Creatives are based on insights from digital and non-digital channels, balanced with brand and product principles.",
                    "imageDescription": None,
                    "recode": "4",
                    "scoring": [
                        {"category": "SC_577ByjK0PVdnw69", "value": "4"}
                    ],
                    "variableName": None}
            },
            "questionLabel": None,
            "questionName": "Q102",
            "questionText": "Which of the following best describes the extent to which your organisation uses data to inform creative development?",
            "questionType": {
                "selector": "SAVR",
                "subSelector": "TX",
                "type": "MC"
            },
            "validation": {
                "doesForceResponse": True
            }
        },
    },
    "responseCounts": {}
}
