import copy
import json
from django.conf import settings
from collections import defaultdict
from core.qualtrics.question import get_question_dimension


class SurveyDefinition(object):
    def __init__(self, definition):
        self.definition = definition

    def get_questions(self):
        questions = {
            "questions_by_dimension": defaultdict(list),
            "definitions": {},
            "dimensions": [],
        }

        for block_id, block in self.definition['blocks'].iteritems():
            for element in block['elements']:
                def_q_id = element['questionId']
                q_definition = self._get_question(def_q_id)
                q_id = q_definition['id']
                q_dimension = get_question_dimension(q_id)

                if q_dimension:
                    questions['definitions'][q_id] = q_definition
                    questions['questions_by_dimension'][q_dimension].append(q_id)

                    if q_dimension not in questions['dimensions']:
                        questions['dimensions'].append(q_dimension)
        return questions

    def _get_question(self, q_id):
        q_definition = self.definition['questions'].get(q_id, None)
        return self.get_question_definition(q_definition)

    @classmethod
    def get_question_definition(cls, q_definition):

        choices_map = {choice['choiceText']: SurveyDefinition.get_choice_definition(id, choice) for id, choice in q_definition['choices'].iteritems()}
        # Since we don't get an array for choices but a map, we assume the indexes are ordered.
        ordered_choices = [choice for id, choice in choices_map.iteritems()]
        ordered_choices.sort(key=lambda choice: float(choice['id']))

        return {
            "id": q_definition['questionName'],
            "type": SurveyDefinition.map_question_type(q_definition['questionType']),
            "text": q_definition['questionText'],
            "choices_map": choices_map,
            "choices": [c['text'] for c in ordered_choices],
        }

    @classmethod
    def get_choice_definition(cls, choice_id, choice_definition):
        return {
            "id": choice_id,
            "text": choice_definition['choiceText'],
            "value": choice_definition.get('recode', None),
        }

    @classmethod
    def map_question_type(cls, question_type):
        # It's not a singly choice or multichoce question
        type_map = {
            "SAVR": "SC",  # single choice question type
            "MAVR": "MC",  # multiple choice question type
        }

        if question_type['type'] != "MC":
            return None

        return type_map.get(question_type['selector'], None)


def get_response_detail(definition, response_data):
    survey_definition = SurveyDefinition(definition)
    questions = survey_definition.get_questions()

    response_detail = copy.deepcopy(questions)

    for q_id, q_definition in response_detail['definitions'].iteritems():
        # Array containing a list of choice texts that are not anymore in the schema.
        q_definition['not_in_schema_text'] = []

        # Result has data for the questions
        question_data = response_data.get(q_id)
        if question_data:
            q_definition['available'] = True
            for choice_text in question_data['choices_text']:
                choice_map = q_definition['choices_map'].get(choice_text, False)
                if choice_map:
                    q_definition['choices_map'][choice_text]['selected'] = True
                else:
                    q_definition['not_in_schema_text'].append(choice_text)

    return response_detail
