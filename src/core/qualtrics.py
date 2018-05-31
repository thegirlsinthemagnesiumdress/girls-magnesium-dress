import requests
import zipfile
import os
import re
import json
import functools
import numpy


weights = {
    'Q24': 2,
    'Q25': 1,
}

categories = {
    ''
}


def get_results():
    # Setting user Parameters
    apiToken = 'bvoXoFk5XgJEM1BubkTFQKnXbl1vX6YycmZ5ecUe'
    surveyId = 'SV_beH0HTFtnk4A5rD'
    fileFormat = 'json'
    dataCenter = 'google.co1'
    surveyName = 'TRev'

    # Setting static parameters
    progressStatus = 'in progress'
    baseUrl = 'https://{0}.qualtrics.com/API/v3/responseexports/'.format(dataCenter)
    headers = {
        'content-type': 'application/json',
        'x-api-token': apiToken,
        }
    tmp_file = 'core/tmp_results/results.zip'

    # Step 1: Creating Data Export
    requestCheckProgress = 0
    downloadRequestUrl = baseUrl
    downloadRequestPayload = json.dumps({'format': fileFormat, 'surveyId': surveyId})
    downloadRequestResponse = requests.request('POST', downloadRequestUrl, data=downloadRequestPayload, headers=headers)
    progressId = downloadRequestResponse.json()['result']['id']


    # Step 2: Checking on Data Export Progress and waiting until export is ready
    while requestCheckProgress < 100 and progressStatus is not 'complete':
        requestCheckUrl = baseUrl + progressId
        requestCheckResponse = requests.request('GET', requestCheckUrl, headers=headers)
        requestCheckProgress = requestCheckResponse.json()['result']['percentComplete']
        print 'Download is ' + str(requestCheckProgress) + ' complete'
        if requestCheckProgress == 100:
            surveyResponsesFile = requestCheckResponse.json()['result']['file']
            print 'File: ' + surveyResponsesFile

    # Step 3: Downloading file
    requestDownloadUrl = baseUrl + progressId + '/file'
    requestDownload = requests.request('GET', requestDownloadUrl, headers=headers, stream=True)

    # Step 4: Unziping file
    # TODO probably this should be saved to a static dir ?
    with open(tmp_file, 'wb') as f:
        for chunk in requestDownload.iter_content(chunk_size=1024):
            f.write(chunk)

    # zipfile.ZipFile('RequestFile.zip').extractall('SurveyResults')
    data =  zipfile.ZipFile(tmp_file).read('{}.json'.format(surveyName))
    os.remove(tmp_file)
    return json.loads(data)


def string_to_number_or_zero(number):
    try:
        return float(number)
    except ValueError:
        return 0

def to_questions_array(survey_results):
    question_key_regex = re.compile(r'^Q\d+(_\d+)?$')

    # filter results keys that are questions.
    questions_keys = filter(question_key_regex.search, survey_results.keys())

    # filter out questions without a response.
    questions_keys_with_value = filter(lambda key: survey_results.get(key), questions_keys)

    # create a tuple with an array of questions where an element is (key, value, weight).
    questions_key_value = map(lambda key: (key, string_to_number_or_zero(survey_results.get(key)), weights.get(key, 1)), questions_keys_with_value)
    return questions_key_value


def average(questions_array):
    values = map(lambda x: x[1], questions_array)
    weights = map(lambda x: x[2], questions_array)
    weighted_sum = numpy.dot(values, weights)
    return weighted_sum / functools.reduce(lambda sum, w: sum + w, weights, 0)
