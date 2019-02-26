import copy
import re
from collections import defaultdict
from core.qualtrics.question import get_question_dimension
from django.conf import settings


class SurveyDefinition(object):
    def __init__(self, definition, dimensions):
        self.definition = definition
        self.dimensions = dimensions

    def get_questions(self):
        questions = {
            "questions_by_dimension": defaultdict(list),
            "definitions": {},
            "dimensions": [],
        }

        for block_id, block in self.definition['blocks'].items():
            for element in block['elements']:
                def_q_id = element['questionId']
                q_definition = self._get_question(def_q_id)
                q_id = q_definition['id']
                q_dimension = get_question_dimension(q_id, self.dimensions)

                if q_dimension:
                    questions['definitions'][q_id] = q_definition
                    questions['questions_by_dimension'][q_dimension].append(q_id)

                    dimension_obj = {
                        'id': q_dimension,
                        'title': settings.DIMENSION_TITLES.get(q_dimension),
                    }
                    if dimension_obj not in questions['dimensions']:
                        questions['dimensions'].append(dimension_obj)
        return questions

    def _get_question(self, q_id):
        q_definition = self.definition['questions'].get(q_id, None)
        return self.get_question_definition(q_definition)

    @classmethod
    def get_question_definition(cls, q_definition):
        q_type = SurveyDefinition.map_question_type(q_definition['questionType'])
        choices_map = {
            choice['choiceText']: cls.get_choice_definition(id, choice, q_type)
            for id, choice in q_definition['choices'].items()
        }

        # Since we don't get an array for choices but a map, we assume the indexes are ordered.
        ordered_choices = [choice for id, choice in choices_map.items()]
        ordered_choices.sort(key=lambda choice: float(choice['id']))

        return {
            "id": q_definition['questionName'],
            "type": q_type,
            "text": cls.remove_dimension_header(q_definition['questionText']).lstrip(),
            "choices_map": choices_map,
            "choices": [c['text'] for c in ordered_choices],
        }

    @classmethod
    def remove_dimension_header(cls, text):
        return re.sub('^<h2 class="dmb-dimension-header">.*</h2>', '', text)

    @classmethod
    def get_choice_definition(cls, choice_id, choice_definition, question_type):
        value = float(choice_definition.get('recode', 0))
        if question_type == 'checkbox':
            value = value / 100

        value = round(value, 2)
        return {
            "id": choice_id,
            "text": choice_definition['choiceText'],
            "value": value,
        }

    @classmethod
    def map_question_type(cls, question_type):
        # It's not a singly choice or multichoce question
        type_map = {
            "SAVR": "radio",  # single choice question type
            "MAVR": "checkbox",  # multiple choice question type
        }

        if question_type['type'] != "MC":
            return None

        return type_map.get(question_type['selector'], None)


def get_response_detail(definition, response_data, dimensions):
    survey_definition = SurveyDefinition(definition, dimensions)
    questions = survey_definition.get_questions()

    response_detail = copy.deepcopy(questions)

    for q_id, q_definition in response_detail['definitions'].items():
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
                elif choice_text:
                    q_definition['not_in_schema_text'].append(choice_text)

    return response_detail
