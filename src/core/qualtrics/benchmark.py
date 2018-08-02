
from collections import defaultdict


import numpy
from core.qualtrics.question import weighted_questions_average
from django.conf import settings


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
        benchmark_by_dimension[dimension] = weighted_questions_average(questions)

    return numpy.average(benchmark_by_dimension.values()), benchmark_by_dimension


def calculate_dimension_benchmark(weighted_responses):
    """ Calculates benchmark on the weighted_responses dataset."""
    responses_benchmarks_by_dimension = defaultdict(list)

    for response in weighted_responses:

        for dimension in settings.DIMENSIONS:
            benchmark = response.get(dimension, 0)
            responses_benchmarks_by_dimension[dimension].append(benchmark)

    benchmark_by_dimension = {}

    for dimension in settings.DIMENSIONS:
        benchmark_by_dimension[dimension] = numpy.average(responses_benchmarks_by_dimension[dimension])

    return numpy.average(benchmark_by_dimension.values()), benchmark_by_dimension
