from django.test import TestCase
from public.serializers import AdminSurveyResultsSerializer
from core.tests.mommy_recepies import make_survey, make_survey_result
from django.utils import dateparse


class AdminSurveyResultsSerializerTests(TestCase):

    def test_serializer_return_correct_keys(self):
        survey = make_survey(sid="92345123451234512345123451234512")
        survey_result = make_survey_result(
            survey=survey,
            response_id='AAA',
            dmb=1.0,
            dmb_d='{}'
        )
        survey.last_survey_result = survey_result
        survey.save()

        serializer = AdminSurveyResultsSerializer(survey)

        self.assertSetEqual(
            set(serializer.data.keys()),
            set(['company_name',
                 'industry',
                 'industry_name',
                 'country_name',
                 'last_survey_result',
                 'created_at',
                 'last_survey_result_link',
                 'survey_results',
                 'link_sponsor',
                 'link',
                 'engagement_lead'])
        )

    def test_serializer_return_correct_serializerd_data(self):
        survey = make_survey(sid="92345123451234512345123451234512")
        survey_result = make_survey_result(
            survey=survey,
            response_id='AAA',
            dmb=1.0,
            dmb_d='{}'
        )
        survey.last_survey_result = survey_result
        survey.save()

        serializer = AdminSurveyResultsSerializer(survey)
        self.assertTrue(serializer.is_valid)
        self.assertEqual(serializer.data.get('company_name'), survey.company_name)
        self.assertIsNotNone(serializer.data.get('last_survey_result'))
        last_survey_result_serialized = serializer.data.get('last_survey_result')
        self.assertEqual(last_survey_result_serialized.get('report_link'), survey.last_survey_result.report_link)
        self.assertEqual(
            dateparse.parse_datetime(last_survey_result_serialized.get('started_at')),
            survey.last_survey_result.started_at
        )
