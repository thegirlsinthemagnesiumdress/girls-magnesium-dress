import json
import os
import zipfile

import requests

from core.models import Survey, SurveyResult


QUALTRICS_API_TOKEN = 'bvoXoFk5XgJEM1BubkTFQKnXbl1vX6YycmZ5ecUe'
data_center = 'google.co1'
BASE_URL = 'https://{0}.qualtrics.com/API/v3/responseexports/'.format(data_center)



qualtrics_survey_id = 'SV_beH0HTFtnk4A5rD'
response_id = 'R_2aIxNgtAMk8Q360'


def get_results():
    try:
        survey_result = SurveyResult.objects.latest('loaded_at')
        print("Found Survey already downloaded, download partial result")
        results = download_results(survey_result.response_id)
    except SurveyResult.DoesNotExist:
        print("Found new Survey, download all the results so far")
        results = download_results()
    finally:
        _create_survey_result(results.get('responses'))


def _create_survey_result(results_data):
    """Create `SurveyResult` given a list of `result_data`.

    :param survey: `core.SurveyResult` which `results_data` refers to
    :param results_data: dictionary containing the downloaded response
        from Qualtrics API.
    """
    for data in results_data:
        survey = Survey.objects.filter(sid=data.get('sid')).first()
        SurveyResult.objects.create(
            survey=survey,
            response_id=data.get('ResponseID'),
            data=data,
        )


def download_results(response_id=None, file_format='json'):
    # Setting user Parameters
    survey_name = 'TRev'

    # Setting static parameters
    progress_status = 'in progress'
    headers = {
        'content-type': 'application/json',
        'x-api-token': QUALTRICS_API_TOKEN,
    }
    tmp_file = 'src/core/tmp_results/results.zip'

    # Step 1: Creating Data Export
    request_check_progress = 0
    data_export_payload = {
        'format': file_format,
        'surveyId': qualtrics_survey_id,
    }

    if response_id:
        data_export_payload['lastResponseId'] = response_id

    download_request_payload = json.dumps(data_export_payload)
    download_request_response = requests.request(
        'POST',
        BASE_URL,
        data=download_request_payload,
        headers=headers
    )
    progress_id = download_request_response.json()['result']['id']

    # Step 2: Checking on Data Export Progress and waiting until export is ready
    while request_check_progress < 100 and progress_status is not 'complete':
        request_check_url = BASE_URL + progress_id
        request_check_response = requests.request('GET', request_check_url, headers=headers)
        request_check_progress = request_check_response.json()['result']['percentComplete']
        print 'Download is ' + str(request_check_progress) + ' complete'
        if request_check_progress == 100:
            survey_responses_file = request_check_response.json()['result']['file']
            print 'File: ' + survey_responses_file

    # Step 3: Downloading file
    request_download_url = BASE_URL + progress_id + '/file'
    request_download = requests.request('GET', request_download_url, headers=headers, stream=True)

    # Step 4: Unziping file
    # TODO probably this should be saved to a static dir ?
    with open(tmp_file, 'wb') as f:
        for chunk in request_download.iter_content(chunk_size=1024):
            f.write(chunk)

    # zipfile.ZipFile('RequestFile.zip').extractall('SurveyResults')
    qualtrics_data = zipfile.ZipFile(tmp_file).read('{}.json'.format(survey_name))
    os.remove(tmp_file)
    return json.loads(qualtrics_data)
