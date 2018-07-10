import requests
import zipfile
import os
import json
from core.models import Survey, Benchmark



QUALTRICS_API_TOKEN = 'bvoXoFk5XgJEM1BubkTFQKnXbl1vX6YycmZ5ecUe'
data_center = 'google.co1'
BASE_URL = 'https://{0}.qualtrics.com/API/v3/responseexports/'.format(data_center)



uid = 'SV_beH0HTFtnk4A5rD'
response_id = 'R_2aIxNgtAMk8Q360'


def get_results(uid):
    try:
        survey = Benchmark.objects.filter(sid=uid).latest('loaded_at')
        print("Found Survey already downloaded, download partial result")
        return download_results(survey.sid, survey.response_id)

    except Benchmark.DoesNotExist:
        try:
            print("Found new Survey, download all the results so far")
            survey = Survey.objects.get(uid=uid)
            return download_results(survey.uid)
        except Survey.DoesNotExist:
            print("Cannot find any survey {}".format(uid))
            return


def download_results(survey_id, response_id=None):
    # Setting user Parameters
    file_format = 'json'
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
        'surveyId': survey_id,
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
