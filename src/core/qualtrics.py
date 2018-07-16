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


def calculate_group_benchmark(filtered_responses, by_dimension=False):
    """ Calculates benchmark on the responses filtered dataset

    Arguments:
        questions {list} -- Array of responses

    Keyword Arguments:
        by_dimension {bool} -- Whether or not return a dict with benchmark by dimension (default: {False})
    """

    # Loop on a every single response.
    responses_benchmarks_by_dimension = {}

    for response in filtered_responses:
        # Create a dict where single response benchmarks aggregated by dimension.
        _, response_benchmarks_by_dimension = calculate_response_benchmark(response)

        for dimension in settings.DIMENSIONS:
            benchmark = response_benchmarks_by_dimension.get(dimension, 0)
            if responses_benchmarks_by_dimension.get(dimension):
                responses_benchmarks_by_dimension[dimension].append(benchmark)
            else:
                responses_benchmarks_by_dimension[dimension] = [benchmark]

    benchmark_by_dimension = {}

    # Create a dict where responses benchmarks aggregated by dimension.
    for dimension in settings.DIMENSIONS:
        benchmark_by_dimension[dimension] = numpy.average(responses_benchmarks_by_dimension[dimension])

    return numpy.average(benchmark_by_dimension.values()), benchmark_by_dimension


def calculate_response_benchmark(response_questions):

    # Create a dict where single response questions are aggregated by dimension.
    questions_by_dimension = {}
    for question in response_questions:
        dimension = question[3]
        if questions_by_dimension.get(dimension):
            questions_by_dimension[dimension].append(question)
        else:
            questions_by_dimension[dimension] = [question]

    # Create a dict where single response benchmarks aggregated by dimension.
    benchmark_by_dimension = {}
    for dimension, questions in questions_by_dimension.iteritems():
        benchmark_by_dimension[dimension] = _weighted_questions_average(questions)

    return numpy.average(benchmark_by_dimension.values()), benchmark_by_dimension
