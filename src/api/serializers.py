from core.models import Survey, SurveyResult
from rest_framework.serializers import ModelSerializer


class SurveySerializer(ModelSerializer):
    class Meta:
        model = Survey
        fields = ('company_name', 'link', 'link_sponsor', 'engagement_lead', 'industry', 'country')


class SurveyCompanyNameSerializer(ModelSerializer):
    class Meta:
        model = Survey
        fields = ('company_name',)


class SurveyResultSerializer(ModelSerializer):
    class Meta:
        model = SurveyResult
        fields = ('response_id', 'dmb', 'dmb_d')
