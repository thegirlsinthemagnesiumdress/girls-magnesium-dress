from core.models import Survey
from rest_framework.serializers import ModelSerializer


class SurveySerializer(ModelSerializer):
    class Meta:
        model = Survey
        fields = ('company_name', 'link', 'link_sponsor')


class SurveyCompanyNameSerializer(ModelSerializer):
    class Meta:
        model = Survey
        fields = ('company_name',)
