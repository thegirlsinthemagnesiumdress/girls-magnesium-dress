
from collections import defaultdict


import numpy
from core.qualtrics.question import weighted_questions_average


def calculate_group_benchmark_from_raw_responses(filtered_responses, dimensions):
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

        for dimension in dimensions:
            benchmark = response_benchmarks_by_dimension.get(dimension, 0)
            responses_benchmarks_by_dimension[dimension].append(benchmark)

    benchmark_by_dimension = {}

    # Create a dict where responses benchmarks aggregated by dimension.
    for dimension in dimensions:
        benchmark_by_dimension[dimension] = numpy.average(responses_benchmarks_by_dimension[dimension])

    return numpy.average(benchmark_by_dimension.values()), benchmark_by_dimension


def calculate_response_benchmark(response_questions, dimensions_weights=None):
    """Calcualte dmb (Digital Maturity Benchmark) and dmb_d (Digital Maturity Benchmark by dimension)
    for a list of `response_questions`.

    :param response_questions: a list of tuples that represent a question in the the for of:
                                response_questions = [
                                    ('Q1', [1.0], 1, 'dimension_A'),
                                    ('Q2', [3.0], 1, 'dimension_A'),
                                    ('Q3', [2.0], 2, 'dimension_A'),
                                    ('Q4', [1.0], 3, 'dimension_B'),
                                    ('Q5', [1.0, 2.0], 1, 'dimension_B'),
                                    ('Q6', [1.0], 3, 'dimension_C'),
                                ]
                                where each element of the list is:
                                    (question_key, list_of_values, question_weight, dimension)
    :param dimension_weights: an optional dictionaty that represent each dimension weight in
                            the form of:
                            dimensions_weights = {
                                'dimension_A': 0.3,
                                'dimension_B': 0.3,
                                'dimension_C': 0,
                            }

    :return: (dmb, dmb_d), where dmb is the simple average of `dmb_d` when `dimensions_weights`
        is not defined. In case `dimensions_weights` is defined, all dimensions with weight
        different from 0 will be taken into account. If the weight for a specific dimension is 0,
        then it will be excluded, and the related dimension will be forced to `None` in `dmb_d`
        return value.
    """

    # Create a dict where single response questions are aggregated by dimension.
    questions_by_dimension = defaultdict(list)
    excluded_dimensions = []

    # load all excluded dimensions
    if dimensions_weights:
        excluded_dimensions = [k for k, v in dimensions_weights.items() if v == 0]

    # create a dictionary of elements that are not in excluded dimensions
    for question in response_questions:
        if question[3] and question[3] not in excluded_dimensions:
            questions_by_dimension[question[3]].append(question)

    # Create a dict where single response benchmarks aggregated by dimension.
    benchmark_by_dimension = {}
    for dimension, questions in questions_by_dimension.iteritems():
        benchmark_by_dimension[dimension] = weighted_questions_average(questions)

    # in case dimensions_weights is defined, pair benchmark_by_dimension with the correct weight
    ordered_weights = None
    benchmark_by_dimension_values = []
    if dimensions_weights:
        ordered_weights = []
        for dim, val in benchmark_by_dimension.items():
            benchmark_by_dimension_values.append(val)
            ordered_weights.append(dimensions_weights[dim])
    else:
        benchmark_by_dimension_values = benchmark_by_dimension.values()

    dmb = numpy.average(benchmark_by_dimension_values, weights=ordered_weights)

    # insert back in the dimensions excluded
    for excluded_dim in excluded_dimensions:
        benchmark_by_dimension[excluded_dim] = None

    return dmb, benchmark_by_dimension


def _by_dimension(dmb_d_list, aggregated_function, dimensions):
    """
    Given a `dmb_d_list` and an `aggregated_function`, returns a dictionary
    where the `aggregated_function` is applied for each `settings.DIMENSION`
    """
    dmb_d_by_dimension = defaultdict(list)
    benchmark_by_dimension = {}

    for dmb_d in dmb_d_list:

        for dimension in dimensions:
            benchmark = dmb_d.get(dimension, None)
            if benchmark:
                dmb_d_by_dimension[dimension].append(benchmark)

    for dimension in dimensions:
        if dmb_d_by_dimension[dimension]:
            benchmark_by_dimension[dimension] = aggregated_function(dmb_d_by_dimension[dimension])
        else:
            benchmark_by_dimension[dimension] = None
    return benchmark_by_dimension


def calculate_dmb(dmb_values, aggregated_function):
    dmb_values = [value for value in dmb_values if value]
    return aggregated_function(dmb_values)


def calculate_group_benchmark(dmb_d_list, dimensions, dmb_values=None):
    """ Calculates benchmark on the dmb_d_list dataset."""
    benchmark_by_dimension = _by_dimension(dmb_d_list, numpy.average, dimensions)
    dmb = None
    if dmb_values is not None:
        # case for NEWS
        dmb = calculate_dmb(dmb_values, numpy.average)
    else:
        dmb = calculate_dmb(benchmark_by_dimension.values(), numpy.average)

    return dmb, benchmark_by_dimension


def calculate_best_practice(dmb_d_list, dimensions, dmb_values=None):
    """ Calculates best practice on the dmb_d_list dataset."""
    benchmark_by_dimension = _by_dimension(dmb_d_list, numpy.amax, dimensions)
    dmb = None
    if dmb_values is not None:
        # case for NEWS
        dmb = calculate_dmb(dmb_values, numpy.amax)
    else:
        dmb = calculate_dmb(benchmark_by_dimension.values(), numpy.average)

    return dmb, benchmark_by_dimension
