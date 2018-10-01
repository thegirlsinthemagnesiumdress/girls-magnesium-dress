from core.models import Survey, SurveyResult
from rest_framework.serializers import ModelSerializer, CharField, JSONField


class SurveySerializer(ModelSerializer):
    class Meta:
        model = Survey
        fields = ('company_name', 'link', 'link_sponsor', 'engagement_lead', 'industry', 'country')


class SurveyCompanyNameSerializer(ModelSerializer):
    class Meta:
        model = Survey
        fields = ('company_name',)


class SurveyResultSerializer(ModelSerializer):
    dmb_d = JSONField()
    class Meta:
        model = SurveyResult
        fields = ('response_id', 'dmb', 'dmb_d', 'loaded_at')


class SurveyWithResultSerializer(ModelSerializer):
    last_survey_result = SurveyResultSerializer(read_only=True)
    country_name = CharField(source='get_country_display')
    industry_name = CharField(source='get_industry_display')

    class Meta:
        model = Survey
        fields = (
            'company_name',
            'link',
            'link_sponsor',
            'engagement_lead',
            'industry',
            'industry_name',
            'country_name',
            'last_survey_result',
        )
