import io
import logging
import json
import zipfile
from exceptions import FetchResultException
import random
from datetime import datetime, timedelta

from google.appengine.api import urlfetch

from django.conf import settings


def fetch_results(file_format='json', started_after=None, text=False):
    """Fetch results from Quatrics API.

        :raises: `core.qualtrics.exceptions.FetchResultException` if
            any of the steps to generate and retrieve the data export
            fails
        :returns: dictionary of survey responses in the following format:
            {
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
                        'Q1_1_TEXT': '',
                        'Q1_2_TEXT': '',
                        'Q2_1_TEXT': '',
                        'Q2_2_TEXT': '',

                        'Q3': '2',
                        'Q4': '0',
                        'Q5_1': '2',
                    },
                    ...
                ]
            }
    """
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
        'seenUnansweredRecode': '0',
        'endDate': (datetime.now() + timedelta(days=random.randint(1, 1000))).strftime('%Y-%m-%dT%H:%M:%SZ'),
    }

    if started_after:
        data_export_payload['startDate'] = started_after.isoformat()

    if text:
        data_export_payload['useLabels'] = True

    logging.info("Sending request to Qualtrics Export API with payload {}".format(data_export_payload))
    download_request_response = urlfetch.fetch(
        method=urlfetch.POST,
        url=settings.RESPONSE_EXPORT_BASE_URL,
        deadline=settings.QUALTRICS_REQUEST_DEADLINE,
        payload=json.dumps(data_export_payload),
        headers=headers
    )

    try:
        export_generation_response = json.loads(download_request_response.content)
        progress_id = export_generation_response['result']['id']
    except KeyError:
        raise FetchResultException(export_generation_response)

    # Step 2: Checking on Data Export Progress and waiting until export is ready
    while request_check_progress < 100 and progress_status is not 'complete':
        request_check_url = ''.join((settings.RESPONSE_EXPORT_BASE_URL, progress_id))
        request_check_response = urlfetch.fetch(
            method=urlfetch.GET,
            url=request_check_url,
            deadline=settings.QUALTRICS_REQUEST_DEADLINE,
            headers=headers)
        progress_response = json.loads(request_check_response.content)
        try:
            request_check_progress = progress_response['result']['percentComplete']
        except KeyError:
            raise FetchResultException(progress_response)

    # Step 3: Downloading file
    request_download_url = ''.join((settings.RESPONSE_EXPORT_BASE_URL, progress_id, '/file'))

    request_download = urlfetch.fetch(
        method='GET',
        url=request_download_url,
        headers=headers,
        deadline=settings.QUALTRICS_REQUEST_DEADLINE
    )

    # Step 4: Unziping file
    with io.BytesIO() as in_memory_buffer:
        in_memory_buffer.write(request_download.content)

        # it seems slightly overengineered to write `_unpack_zip` function to loop through a zip
        # file that should most likely cointain only one file (it will cointain more than one
        # file in case the number of responses is abouve 1M), however, looping through the zip
        # archive allow us to read file content anonymously.
        try:
            qualtrics_data = [response for response in _unpack_zip(in_memory_buffer)]
            qualtrics_data = qualtrics_data[0]

        except zipfile.BadZipfile as e:
            raise FetchResultException(json.loads(request_download.content))
    return json.loads(qualtrics_data)


def _unpack_zip(in_memory_buffer):
    with zipfile.ZipFile(in_memory_buffer) as thezip:
        for zipinfo in thezip.infolist():
            with thezip.open(zipinfo) as thefile:
                yield thefile.read()
