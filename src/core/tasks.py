import io
import json
import os
import zipfile

import requests

from core.models import Survey, SurveyResult
from django.conf import settings


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

    progress_status = 'in progress'
    request_check_progress = 0
    qualtrics_data = {}
    headers = {
        'content-type': 'application/json',
        'x-api-token': settings.QUALTRICS_API_TOKEN,
    }

    # Step 1: Creating Data Export
    data_export_payload = {
        'format': file_format,
        'surveyId': settings.QUALTRICS_SURVEY_ID,
    }

    if response_id:
        data_export_payload['lastResponseId'] = response_id

    download_request_response = requests.request(
        'POST',
        settings.RESPONSE_EXPORT_BASE_URL,
        json=data_export_payload,
        headers=headers
    )
    progress_id = download_request_response.json()['result']['id']

    # Step 2: Checking on Data Export Progress and waiting until export is ready
    while request_check_progress < 100 and progress_status is not 'complete':
        request_check_url = ''.join((settings.RESPONSE_EXPORT_BASE_URL, progress_id))
        request_check_response = requests.request('GET', request_check_url, headers=headers)
        request_check_progress = request_check_response.json()['result']['percentComplete']

    # Step 3: Downloading file
    request_download_url = ''.join((settings.RESPONSE_EXPORT_BASE_URL, progress_id, '/file'))
    request_download = requests.request('GET', request_download_url, headers=headers, stream=True)

    # Step 4: Unziping file
    with io.BytesIO() as in_memory_buffer:
        for chunk in request_download.iter_content(chunk_size=1024):
            in_memory_buffer.write(chunk)
        # it seems slightly overengineered to write `_unpack_zip` function to loop through a zip
        # file that should most likely cointain only one file (it will cointain more than one
        # file in case the number of responses is abouve 1M), however, looping through the zip
        # archive allow us to read file content anonymously.
        qualtrics_data = [response for response in _unpack_zip(in_memory_buffer)]
        qualtrics_data = qualtrics_data[0]

    return json.loads(qualtrics_data)


def _unpack_zip(in_memory_buffer):
    with zipfile.ZipFile(in_memory_buffer) as thezip:
        for zipinfo in thezip.infolist():
            with thezip.open(zipinfo) as thefile:
                yield thefile.read()
