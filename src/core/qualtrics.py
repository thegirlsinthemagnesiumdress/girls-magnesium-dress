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

dimensions = {
    'activation': ['Q35', 'Q36'],
    'audience': ['Q24', 'Q25'],
    'automation': ['Q26', 'Q27'],
    'ads': ['Q28', 'Q29'],
    'analysis': ['Q30', 'Q31'],
    'access': ['Q32', 'Q33'],
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
    qualtrics_data =  zipfile.ZipFile(tmp_file).read('{}.json'.format(surveyName))
    os.remove(tmp_file)
    return json.loads(qualtrics_data)

def string_to_number_or_zero(number):
    try:
        return float(number)
    except ValueError:
        return 0

def get_question_dimension(question_id):
    for dimensions_key, value in dimensions.iteritems():
        if question_id in value:
            return dimensions_key

def to_questions_array(response_data):
    question_key_regex = re.compile(r'^Q\d+(_\d+)?$')

    # filter results keys that are questions. Unfortunately we have to rely on property key names.
    questions_keys = filter(question_key_regex.search, response_data.keys())

    # filter out questions without a response.
    questions_keys_with_value = filter(lambda key: response_data.get(key), questions_keys)

    # create a tuple with an array of questions where an element is (key, value, weight).
    questions_key_value = map(lambda key: (key, string_to_number_or_zero(response_data.get(key)), weights.get(key, 1), get_question_dimension(key)), questions_keys_with_value)
    return questions_key_value

def weighted_questions_average(questions_array):
    """[summary]

    Arguments:
        questions_array (q_id, q_value, q_weight) -- Question tuple with value and weights

    Returns:
        float -- weighted average.
    """

    values = map(lambda x: x[1], questions_array)
    weights = map(lambda x: x[2], questions_array)
    # weighted_sum = numpy.dot(values, weights)
    # return weighted_sum / functools.reduce(lambda sum, w: sum + w, weights, 0)
    return numpy.average(values, weights=weights)

def get_responses_by_survey(qualtrics_data):
    """ Aggregates responses by company_id

    Arguments:
        data {dict} -- Qualtrics json dict.

    Returns:
        dict -- {
            survey_id: questions_array
         }
    """

    responses_by_survey = {}

    for response in data['responses']:
        survey_id = response.sid
        questions = to_questions_array(response)
        if responses_by_survey[survey_id]:
            responses_by_survey[survey_id].append(questions)
        else:
            responses_by_survey[survey_id] = [questions]
    return responses_by_survey

def calculate_benchmark(filtered_responses, by_dimension=False):
    """ Calculates benchmark on the responses filtered dataset

    Arguments:
        questions {list} -- Array of responses

    Keyword Arguments:
        by_dimension {bool} -- Whether or not return a dict with benchmark by dimension (default: {False})
    """

    if by_dimension:
        # Loop on a every single response.
        responses_benchmarks_by_dimension = {}
        for response in filtered_responses:
            # Create a dict where single response benchmarks aggregated by dimension.
            response_benchmarks_by_dimension = calculate_benchmark_by_dimension(response)

            for dimension in dimensions:
                benchmark = response_benchmarks_by_dimension.get(dimension, 0)
                if responses_benchmarks_by_dimension.get(dimension):
                    responses_benchmarks_by_dimension[dimension].append(benchmark)
                else:
                    responses_benchmarks_by_dimension[dimension] = [benchmark]

        benchmark_by_dimension = {}

        # Create a dict where responses benchmarks aggregated by dimension.
        for dimension in dimensions:
            benchmark_by_dimension[dimension] = numpy.average(responses_benchmarks_by_dimension[dimension])

        return benchmark_by_dimension

    benchmark_array = map(lambda response_questions: weighted_questions_average(response_questions), filtered_responses)
    return numpy.average(benchmark_array)

def calculate_benchmark_by_dimension(response):

    # Create a dict where single response questions are aggregated by dimension.
    questions_by_dimension = {}
    for question in response:
        dimension = question[3]
        if questions_by_dimension.get(dimension):
            questions_by_dimension[dimension].append(question)
        else:
            questions_by_dimension[dimension] = [question]

    # Create a dict where single response benchmarks aggregated by dimension.
    benchmark_by_dimension = {}
    for dimension, questions in questions_by_dimension.iteritems():
        benchmark_by_dimension[dimension] = weighted_questions_average(questions)

    return benchmark_by_dimension

def get_responses_by_field(qualtrics_data, field_name):
    """ Aggregates responses by field

    Arguments:
        qualtrics_data {dict} -- Qualtrics json dict.

    Returns:
        dict -- {
            field_value: [responses]
        }
    """

    responses_by_field = {}

    for response in qualtrics_data['responses']:
        field_value = response.get(field_name)
        response_questions = to_questions_array(response)
        if responses_by_field.get(field_value):
            responses_by_field[field_value].append(response_questions)
        else:
            responses_by_field[field_value] = [response_questions]
    return responses_by_field


