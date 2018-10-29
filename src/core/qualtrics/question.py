import re
import logging
from datetime import datetime, timedelta
from collections import defaultdict

import numpy
from django.conf import settings

# _question_key_regex = re.compile(r'(?P<question_id>^Q\d+(_\d+)?)')
# _question_key_regex = re.compile(r'(?P<question_id>^Q\d+(_\d+)?)(.*)')
_question_key_regex = re.compile(r'^(?P<question_id>Q\d+(_\d+)*)(_--(?P<multi_answer_value>[.\d]+)-\d+)?$')
DEFAULT_WEIGHT = 1
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


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


def match_question_key(key):
    match = _question_key_regex.search(key)

    return {
        'question_id': match.group('question_id') if match else None,
        'multi_answer_value': match.group('multi_answer_value') if match else None,
    }


def clean_survey_data(data):
    """A single response object is a dict with a lot of data we don't need.
    This function filters the dict keys to be only the questions and transforms the untuitive structure
    of the multi select answers.

    Multi select answers have a key that looks like {question_id}_--{question_answer_value}-{answer_index}
    and value '1' or '0' [whether they are selected or not]
    We transform the data to have the key equal to the question_id and the value to be a list of question_answer_value

    Returns:
        Dict
    """
    single_answer_questions_dict = {}
    multi_answer_questions_dict = defaultdict(list)

    for k, v in data.iteritems():
        match = match_question_key(k)

        # is a single answer question
        if match['question_id'] and not match['multi_answer_value']:
            single_answer_questions_dict[match['question_id']] = v
        # is a multi answer question
        elif match['question_id'] and match['multi_answer_value']:
            if match['multi_answer_value'] != '0':
                multi_answer_questions_dict[match['question_id']].append(match['multi_answer_value'])

    if sorted(single_answer_questions_dict.keys()) != sorted(settings.MULTI_ANSWER_QUESTION):
        logging.error("Multi answer questions mismatch. It's either we're missing some question in settings or some of the questions are not properly configured on qualtrics")

    questions_dict = single_answer_questions_dict.copy()
    questions_dict.update(multi_answer_questions_dict)

    return questions_dict


def data_to_questions(survey_data):
    data = clean_survey_data(survey_data)

    # filter out questions without a response.
    question_keys_with_value = filter(lambda key: data.get(key), data)

    # print('multiselect_question_keys_with_value', multiselect_question_keys_with_value)

    def create_tuple(question_key, data):
        question_value = 0
        try:
            value = data.get(question_key)
            if isinstance(value, (list,)):
                question_value = map(float, value)
            else:
                question_value = float(value)

        except ValueError:
            pass

        return (
            question_key,
            question_value,
            settings.WEIGHTS.get(question_key, DEFAULT_WEIGHT),
            get_question_dimension(question_key)
        )

    questions_key_value = map(lambda x: create_tuple(x, data), question_keys_with_value)

    return questions_key_value


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
