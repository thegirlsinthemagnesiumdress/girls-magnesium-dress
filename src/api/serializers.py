from core.models import Survey, SurveyResult, User
from rest_framework.serializers import ModelSerializer, CharField, JSONField, ValidationError
from django.conf import settings


class SurveySerializer(ModelSerializer):

    class Meta:
        model = Survey
        fields = (
            'account_id',
            'company_name',
            'link',
            'link_sponsor',
            'engagement_lead',
            'creator',
            'industry',
            'country',
            'tenant',
            'slug',
            'sid',
        )

    def validate(self, data):
        """
        Check that an industry belongs to valid tenant's industry list.
        """
        tenant_conf = settings.TENANTS.get(data.get('tenant'))
        if tenant_conf:
            industries = tenant_conf['INDUSTRIES']
            if data['industry'] not in industries:
                raise ValidationError("Industry does not belong to a set of valid industrues for this tenant")
        return data


class SurveySidSerializer(ModelSerializer):

    class Meta:
        model = Survey
        fields = (
            'sid',
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


class AdminSurveyResultsSerializer(ModelSerializer):
    last_survey_result = SurveyResultSerializer(read_only=True)
    last_internal_result = SurveyResultSerializer(read_only=True)
    country_name = CharField(source='get_country_display')
    industry_name = CharField(source='get_parent_industry_display')

    class Meta:
        model = Survey
        fields = (
            'sid',
            'account_id',
            'company_name',
            'industry_name',
            'country_name',
            'last_survey_result',
            'last_internal_result',
            'created_at',
        )


class SurveyCreatorSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('ldap',)


class SearchSurveySerializer(ModelSerializer):
    country_name = CharField(source='get_country_display')
    industry_name = CharField(source='get_industry_display')
    creator = SurveyCreatorSerializer(read_only=True)

    class Meta:
        model = Survey
        fields = (
            'sid',
            'account_id',
            'company_name',
            'industry_name',
            'country_name',
            'creator',
        )
