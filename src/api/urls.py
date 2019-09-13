from api.views import (
    CreateSurveyView,
    AddSurveyView,
    SurveyCompanyNameFromUIDView,
    SurveyResultsIndustryDetail,
    SurveyDetailView,
    SurveyResultDetailView,
    AdminSurveyListView,
    UpdateAccountIdView,
    AccountViewSet,
)
from django.conf.urls import url
from django.conf import settings


urlpatterns = [
    url(r'^survey$', CreateSurveyView.as_view(), name='create_survey'),
    url(r'^survey/(?P<sid>[0-9a-f]{32})/$', UpdateAccountIdView.as_view(), name='update_survey'),
    url(r'^survey/add/(?P<sid>[0-9a-f]{32})/$', AddSurveyView.as_view(), name='add_survey'),
    url(r'^company-name$', SurveyCompanyNameFromUIDView.as_view(), name='company_name'),
    url(r'^report/company/(?P<sid>[0-9a-f]{32})/$', SurveyDetailView.as_view(), name='survey_report'),
    url(r'^report/result/(?P<response_id>\w+)/$', SurveyResultDetailView.as_view(), name='survey_result_report'),
    url(r'^report/industry/(?P<industry>[\w&-]+)/$', SurveyResultsIndustryDetail.as_view(), name='survey_industry'),
    url(r'^(?P<tenant>{})/admin/surveys/$'.format(settings.ENABLED_TENANTS), AdminSurveyListView.as_view(), name='admin_surveys'),  # noqa
    url(r'^(?P<tenant>{})/admin/surveys/search$'.format(settings.ENABLED_TENANTS), AccountViewSet.as_view(), name='admin_surveys_search'),  # noqa
]
