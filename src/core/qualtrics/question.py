import re
import logging
from datetime import datetime, timedelta
from collections import defaultdict
from exceptions import InvalidResponseData

import numpy
from django.conf import settings

_question_key_regex = re.compile(r'^(?P<question_id>Q\d+(_\d+)*)(_--(?P<multi_answer_value>[.\d]+)-\d+)?$')
DEFAULT_WEIGHT = 1
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


_MULTI_MISSING_IN_SETTINGS = ("Some multi answer questions are defined in qualtrics but they haven't "
                              "been added to settings.MULTI_ANSWER_QUESTIONS. Questions ids: {}")

_MULTI_MISSING_IN_QUALTRICS = ("Some multi answer questions are defined in settings.MULTI_ANSWER_QUESTIONS but they "
                               "haven't been properly defined in QUALTRICS. Questions ids: {}")

_MISSING_IN_SETTINGS = ("Some questions are defined in qualtrics but they haven't been added to settings.DIMENSIONS."
                        "Questions ids: {}")

_IDS_NOT_IN_QUALTRICS = ("Some questions are defined in settings.DIMENSIONS but they haven't been properly "
                         "defined in QUALTRICS or (required) questions not been answered. Questions ids: {}")


def weighted_questions_average(questions_array):
    """[summary]

    Arguments:
        questions_array (q_id, q_value, q_weight) -- Question tuple with value and weights

    Returns:
        float -- weighted average.
    """
    values = map(lambda x: sum(x[1]), questions_array)
    weights = map(lambda x: x[2], questions_array)

    return numpy.average(values, weights=weights)


def match_question_key(key):
    match = _question_key_regex.search(key)

    return {
        'question_id': match.group('question_id') if match else None,
        'multi_answer_value': match.group('multi_answer_value') if match else None,
    }


def clean_survey_data(data):
    """A single response object is a dict with a lot of data we don't need.

    This function filters the dict keys to be only the questions set in settings.DIMENSION and transforms the untuitive
    structure of the multi select answers.

    Multi select answers have a key that looks like {question_id}_--{question_answer_value}-{answer_index}
    and value '1' or '0' [whether they are selected or not]
    We transform the data to have the key equal to the question_id and the value to be a list of question_answer_value

    Returns:
        Dict
    """
    single_answer_questions_dict, multi_answer_questions_dict = _get_questions_by_type(data)

    configured_multi_answer = set(settings.MULTI_ANSWER_QUESTIONS)
    multi_answer_from_survey = set(multi_answer_questions_dict.keys())
    # multi answer that are in data received but not in configured settings
    multi_missing_in_settings = multi_answer_from_survey - configured_multi_answer
    # multi answer that are in configured settings but not in data received
    multi_missing_in_qualtrics = configured_multi_answer - multi_answer_from_survey

    # Will need some rethinking if we have not required questions.
    if multi_missing_in_settings:
        logging.warn(_MULTI_MISSING_IN_SETTINGS.format(', '.join(multi_missing_in_settings)))

    if multi_missing_in_qualtrics:
        logging.warn(_MULTI_MISSING_IN_QUALTRICS.format(', '.join(multi_missing_in_qualtrics)))

    questions_dict = single_answer_questions_dict.copy()
    questions_dict.update(multi_answer_questions_dict)

    questions_from_survey = set(questions_dict.keys())
    # set of questions that are configured in settings.DIMENSIONS
    configured_questions = set([item for questions in settings.DIMENSIONS.values() for item in questions])
    # questions that are in survey data but not in configured settings
    missing_in_settings = questions_from_survey - configured_questions
    # questions that are in configured settings but are not in survey data or doesn't have an answer
    ids_not_in_qualtrics = configured_questions - questions_from_survey

    if missing_in_settings:
        logging.warn(_MISSING_IN_SETTINGS.format(', '.join(missing_in_settings)))

    if ids_not_in_qualtrics:
        raise InvalidResponseData(_IDS_NOT_IN_QUALTRICS.format(', '.join(ids_not_in_qualtrics)))

    # We ignore all the questions that are not configured in settings.DIMENSIONS
    for id in missing_in_settings:
        del questions_dict[id]

    return questions_dict


def _get_questions_by_type(data):
    single_answer = defaultdict(list)
    multi_answer = defaultdict(list)

    for question_key, question_value in data.iteritems():
        match = match_question_key(question_key)

        # is a single answer question
        if match['question_id'] and not match['multi_answer_value']:
            if question_value:
                single_answer[match['question_id']].append(question_value)
        # is a multi answer question
        elif match['question_id'] and match['multi_answer_value']:
            if question_value == '1':
                multi_answer[match['question_id']].append(match['multi_answer_value'])
            else:
                multi_answer[match['question_id']].append('0')

    return single_answer, multi_answer


def data_to_questions(survey_data):
    data = clean_survey_data(survey_data)

    def create_tuple(question_key, data):
        question_value = 0
        try:
            question_value = map(float, data.get(question_key))

        except ValueError:
            pass

        return (
            question_key,
            question_value,
            settings.WEIGHTS.get(question_key, DEFAULT_WEIGHT),
            get_question_dimension(question_key)
        )

    questions = map(lambda x: create_tuple(x, data), data)

    return questions


def get_question_dimension(question_id):
    for dimension_key, dimension_value in settings.DIMENSIONS.iteritems():
        if question_id in dimension_value:
            return dimension_key


def discard_scores(survey_data):
    """
    Returns `True` if survey data should be discarded from best practice.

    :param survey_data: dictionary object representing survey response data.
    :returns: `True` if time to give the `survey_data` answers took less than 5
    minutes, `False` otherwise
    """
    start_date = datetime.strptime(survey_data.get('StartDate'), DATE_FORMAT)
    end_date = datetime.strptime(survey_data.get('EndDate'), DATE_FORMAT)
    return end_date - start_date < timedelta(minutes=5)
