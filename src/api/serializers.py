from core.models import Survey, SurveyResult
from rest_framework.serializers import ModelSerializer, CharField, JSONField


class SurveySerializer(ModelSerializer):

    class Meta:
        model = Survey
        fields = (
            'account_id',
            'company_name',
            'link',
            'link_sponsor',
            'engagement_lead',
            'industry',
            'country',
            'tenant',
        )


class SurveyAccountIdSerializer(ModelSerializer):

    class Meta:
        model = Survey
        fields = (
            'account_id',
        )


class SurveyCompanyNameSerializer(ModelSerializer):
    class Meta:
        model = Survey
        fields = ('company_name',)


class SurveyResultSerializer(ModelSerializer):
    dmb_d = JSONField()

    class Meta:
        model = SurveyResult
        fields = ('response_id', 'dmb', 'dmb_d', 'started_at')


class SurveyWithResultSerializer(ModelSerializer):
    survey_result = SurveyResultSerializer(read_only=True)
    country_name = CharField(source='get_country_display')
    industry_name = CharField(source='get_industry_display')

    class Meta:
        model = Survey
        fields = (
            'company_name',
            'industry',
            'industry_name',
            'country_name',
            'survey_result',
            'created_at',
            'tenant',
        )


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
            'account_id',
            'sid',
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
