import io
import json
import zipfile
from collections import defaultdict

from google.appengine.api import urlfetch

import numpy
from django.conf import settings


def _weighted_questions_average(questions_array):
    """[summary]

    Arguments:
        questions_array (q_id, q_value, q_weight) -- Question tuple with value and weights

    Returns:
        float -- weighted average.
    """
    values = map(lambda x: x[1], questions_array)
    weights = map(lambda x: x[2], questions_array)

    return numpy.average(values, weights=weights)


def calculate_group_benchmark(filtered_responses):
    """ Calculates benchmark on the responses filtered dataset

    Arguments:
        questions {list} -- Array of responses

    Keyword Arguments:
        filtered_responses {array} -- Array of tuple (q_id, q_value, q_weight)
    """
    # each element of the dictionary will be key: list of weighted average by dimension
    responses_benchmarks_by_dimension = defaultdict(list)

    # Loop on a every single response.
    for response in filtered_responses:
        # Create a dict where single response benchmarks aggregated by dimension.
        _, response_benchmarks_by_dimension = calculate_response_benchmark(response)

        for dimension in settings.DIMENSIONS:
            benchmark = response_benchmarks_by_dimension.get(dimension, 0)
            responses_benchmarks_by_dimension[dimension].append(benchmark)

    benchmark_by_dimension = {}

    # Create a dict where responses benchmarks aggregated by dimension.
    for dimension in settings.DIMENSIONS:
        benchmark_by_dimension[dimension] = numpy.average(responses_benchmarks_by_dimension[dimension])

    return numpy.average(benchmark_by_dimension.values()), benchmark_by_dimension


def calculate_response_benchmark(response_questions):

    # Create a dict where single response questions are aggregated by dimension.
    questions_by_dimension = defaultdict(list)

    for question in response_questions:
        questions_by_dimension[question[3]].append(question)

    # Create a dict where single response benchmarks aggregated by dimension.
    benchmark_by_dimension = {}
    for dimension, questions in questions_by_dimension.iteritems():
        benchmark_by_dimension[dimension] = _weighted_questions_average(questions)

    return numpy.average(benchmark_by_dimension.values()), benchmark_by_dimension


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

    download_request_response = urlfetch.fetch(
        method=urlfetch.POST,
        url=settings.RESPONSE_EXPORT_BASE_URL,
        deadline=settings.QUALTRICS_REQUEST_DEADLINE,
        payload=json.dumps(data_export_payload),
        headers=headers
    )

    progress_id = json.loads(download_request_response.content)['result']['id']

    # Step 2: Checking on Data Export Progress and waiting until export is ready
    while request_check_progress < 100 and progress_status is not 'complete':
        request_check_url = ''.join((settings.RESPONSE_EXPORT_BASE_URL, progress_id))
        request_check_response = urlfetch.fetch(
            method=urlfetch.GET,
            url=request_check_url,
            deadline=settings.QUALTRICS_REQUEST_DEADLINE,
            headers=headers)
        request_check_progress = json.loads(request_check_response.content)['result']['percentComplete']

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
        qualtrics_data = [response for response in _unpack_zip(in_memory_buffer)]
        qualtrics_data = qualtrics_data[0]

    return json.loads(qualtrics_data)


def _unpack_zip(in_memory_buffer):
    with zipfile.ZipFile(in_memory_buffer) as thezip:
        for zipinfo in thezip.infolist():
            with thezip.open(zipinfo) as thefile:
                yield thefile.read()
