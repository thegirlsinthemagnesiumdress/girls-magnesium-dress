from core.models import Survey
from rest_framework import serializers


class SurveySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Survey
        fields = ('company_name', 'link', 'link_sponsor')
