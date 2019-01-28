import mock
import copy

from core.tests.mocks import survey_definition_dict
from core.response_detail import SurveyDefinition, get_response_detail
from djangae.test import TestCase

result_data = {
    "Q102": {
        "values": [0],
        "choices_text": ['Creatives are based mainly on brand and product principles.'],
    },
    "Q103": {
        "values": [1.33],
        "choices_text": ['Coordinated across online channels without shared timeline.'],
    },
    "Q104": {
        "values": [4],
        "choices_text": ['Media and creative teams working hand in hand from planning to execution using collaborative tools such as a Creative Management Platform (CMP).'],
    },
    "Q128": {
        "values": [1.33, 1.33],
        "choices_text": ['Upper funnel targeting (e.g. to drive awareness).', 'Lower funnel targeting (e.g. to drive sales).'],
    },
}


class SurveyDefinitionTestCase(TestCase):
    def setUp(self):
        self.survey_definition = SurveyDefinition(survey_definition_dict)

    def test_map_question_type_not_considered(self):
        input_type = {
            "type": "TE",
            "selector": "FORM",
            "subSelector": None
        }
        t = SurveyDefinition.map_question_type(input_type)

        self.assertIsNone(t)

    def test_map_question_type_is_checkbox(self):
        input_type = {
            "type": "MC",
            "selector": "MAVR",
            "subSelector": "TX"
        }
        t = SurveyDefinition.map_question_type(input_type)

        self.assertEqual(t, 'checkbox')

    def test_map_question_type_is_radio(self):
        input_type = {
            "type": "MC",
            "selector": "SAVR",
            "subSelector": "TX"
        }
        t = SurveyDefinition.map_question_type(input_type)

        self.assertEqual(t, 'radio')

    def test_get_choice_definition(self):
        choice_id = 1
        input_choice = {
            "recode": "4",
            "description": "Creatives are based on insights from digital and non-digital channels, balanced with brand and product principles.",
            "choiceText": "Creatives are based on insights from digital and non-digital channels, balanced with brand and product principles.",
            "imageDescription": None,
            "variableName": None,
            "analyze": True,
            "scoring": [
                {
                    "category": "SC_577ByjK0PVdnw69",
                    "value": "4"
                }
            ]
        }

        choice_def = SurveyDefinition.get_choice_definition(choice_id, input_choice)

        self.assertEqual(choice_def, {
            'id': choice_id,
            'text': input_choice['choiceText'],
            'value': input_choice['recode'],
        })

    def test_get_question_definition(self):
        input_q_def = survey_definition_dict['questions']['QID102']

        choice_def = SurveyDefinition.get_question_definition(input_q_def)

        choice_1_text = "Creatives are based mainly on brand and product principles."
        choice_2_text = "Creatives are based mainly on insights from a specific digital channel and advanced analytics."

        self.assertEqual(choice_def, {
            "id": "Q102",
            "type": 'radio',
            "text": 'Which of the following best describes the extent to which your organisation uses data to inform creative development?',
            "choices_map": {
                choice_1_text: {
                    'id': '1',
                    'text': choice_1_text,
                    'value': '0',
                },
                choice_2_text: {
                    'id': '2',
                    'text': choice_2_text,
                    'value': '1',
                },

            },
            "choices": ["Creatives are based mainly on brand and product principles.", "Creatives are based mainly on insights from a specific digital channel and advanced analytics."],
        })

    def test_get_questions(self):
        questions = self.survey_definition.get_questions()
        self.assertIsInstance(questions, dict)
        self.assertIsInstance(questions['questions_by_dimension'], dict)
        self.assertIsInstance(questions['definitions'], dict)
        self.assertIsInstance(questions['dimensions'], list)

    def test_get_question_definition_sets_the_right_number_of_def(self):
        questions = self.survey_definition.get_questions()
        self.assertEqual(len(questions['definitions'].values()), 4)

    def test_get_question_definition_sets_the_right_dimensions(self):
        questions = self.survey_definition.get_questions()
        self.assertEqual(questions['dimensions'], [{
            'id': 'ads',
            'title': 'Assets and ads',
        }, {
            'id': 'audience',
            'title': 'Audience',
        }])

    def test_get_question_definition_sets_the_right_questions_for_dimensions(self):
        questions = self.survey_definition.get_questions()
        self.assertEqual(questions['questions_by_dimension']['ads'], ['Q102', 'Q103', 'Q104'])
        self.assertEqual(questions['questions_by_dimension']['audience'], ['Q128'])

    @mock.patch.object(SurveyDefinition, '_get_question', side_effect=[{'id': 'not_taken'}, {'id': 'not_taken'}, {'id': 'Q102'}, {'id': 'Q103'}, {'id': 'Q104'}, {'id': 'Q128'}])
    def test_get_question_definition_sets_the_right_questions_definitions(self, mock_get_question):
        questions = self.survey_definition.get_questions()

        self.assertEqual(questions['definitions'], {
            'Q102': {'id': 'Q102'},
            'Q103': {'id': 'Q103'},
            'Q104': {'id': 'Q104'},
            'Q128': {'id': 'Q128'}
        })


class GetSurveyDetailTestCase(TestCase):
    def test_get_response_detail(self):
        detail = get_response_detail(survey_definition_dict, result_data)

        Q102_choices_map = detail['definitions']['Q102']['choices_map']
        Q103_choices_map = detail['definitions']['Q103']['choices_map']
        Q104_choices_map = detail['definitions']['Q104']['choices_map']
        Q128_choices_map = detail['definitions']['Q128']['choices_map']

        self.assertTrue(Q102_choices_map['Creatives are based mainly on brand and product principles.']['selected'])
        self.assertFalse(Q102_choices_map['Creatives are based mainly on insights from a specific digital channel and advanced analytics.'].get('selected', False))
        self.assertTrue(Q103_choices_map['Coordinated across online channels without shared timeline.']['selected'])
        self.assertTrue(Q104_choices_map['Media and creative teams working hand in hand from planning to execution using collaborative tools such as a Creative Management Platform (CMP).']['selected'])
        self.assertTrue(Q128_choices_map['Upper funnel targeting (e.g. to drive awareness).']['selected'])
        self.assertTrue(Q128_choices_map['Lower funnel targeting (e.g. to drive sales).']['selected'])

    def test_get_response_detail_choice_not_in_def(self):
        data = copy.deepcopy(result_data)
        choice_text = 'Not in definition'
        data['Q102']['choices_text'] = [choice_text]
        detail = get_response_detail(survey_definition_dict, data)

        Q102 = detail['definitions']['Q102']

        for k, choice in Q102['choices_map'].iteritems():
            self.assertFalse(choice.get('selected', False))

        self.assertEqual(Q102['not_in_schema_text'], [choice_text])

    def test_get_response_detail_set_in_question_not_available_in_result(self):
        detail = get_response_detail(survey_definition_dict, result_data)
        for k, q in detail['definitions'].items():
            self.assertTrue(q['available'])

    def test_get_response_detail_available_not_set_in_result(self):
        data = copy.deepcopy(result_data)
        data.pop('Q102', None)
        detail = get_response_detail(survey_definition_dict, data)
        self.assertFalse(detail['definitions']['Q102'].get('available', False))
        self.assertTrue(detail['definitions']['Q103'].get('available', False))
        self.assertTrue(detail['definitions']['Q104'].get('available', False))
        self.assertTrue(detail['definitions']['Q128'].get('available', False))
