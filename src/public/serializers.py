from core.models import Survey, SurveyResult
from rest_framework.serializers import ModelSerializer, CharField


class AdminSurveyResultSerializer(ModelSerializer):

    class Meta:
        model = SurveyResult
        fields = ('response_id', 'detail_link', 'report_link', 'started_at')


class AdminSurveyResultsSerializer(ModelSerializer):
    last_survey_result = AdminSurveyResultSerializer(read_only=True)
    country_name = CharField(source='get_country_display')
    industry_name = CharField(source='get_industry_display')
    last_survey_result_link = CharField(read_only=True)
    survey_results = AdminSurveyResultSerializer(many=True, read_only=True)

    class Meta:
        model = Survey
        fields = (
            'company_name',
            'industry',
            'industry_name',
            'country_name',
            'last_survey_result',
            'created_at',
            'last_survey_result_link',
            'survey_results',
            'link_sponsor',
            'link',
            'engagement_lead',
        )
