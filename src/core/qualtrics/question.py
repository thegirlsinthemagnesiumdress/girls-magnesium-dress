import re

import numpy
from django.conf import settings


_question_key_regex = re.compile(r'^Q\d+(_\d+)?$')
DEFAULT_WEIGHT = 1


def weighted_questions_average(questions_array):
    """[summary]

    Arguments:
        questions_array (q_id, q_value, q_weight) -- Question tuple with value and weights

    Returns:
        float -- weighted average.
    """
    values = map(lambda x: x[1], questions_array)
    weights = map(lambda x: x[2], questions_array)

    return numpy.average(values, weights=weights)


def data_to_questions(survey_data):
    # filter results keys that are questions. Unfortunately we have to rely on property key names.
    questions_keys = filter(_question_key_regex.search, survey_data.keys())

    # filter out questions without a response.
    questions_keys_with_value = filter(lambda key: survey_data.get(key), questions_keys)

    def create_tuple(question_key):
        question_value = 0
        try:
            question_value = float(survey_data.get(question_key))
        except ValueError:
            pass

        return (
            question_key,
            question_value,
            settings.WEIGHTS.get(question_key, DEFAULT_WEIGHT),
            get_question_dimension(question_key)
        )

    questions_key_value = map(create_tuple, questions_keys_with_value)
    return questions_key_value


def get_question_dimension(question_id):
    for dimension_key, dimension_value in settings.DIMENSIONS.iteritems():
        if question_id in dimension_value:
            return dimension_key
