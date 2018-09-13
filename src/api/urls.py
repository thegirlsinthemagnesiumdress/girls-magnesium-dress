from api.views import (
    CreateSurveyView,
    SurveyCompanyNameFromUIDView,
    SurveyResultsDetail,
    SurveyResultsIndustryDetail,
    SurveyDetailView,
)
from django.conf.urls import url


urlpatterns = [
    url(r'^survey$', CreateSurveyView.as_view(), name='create_survey'),
    url(r'^company-name$', SurveyCompanyNameFromUIDView.as_view(), name='company_name'),
    url(r'^report/result/(?P<sid>[0-9a-f]{32})/$', SurveyResultsDetail.as_view(), name='survey_result_report'),
    url(r'^report/company/(?P<sid>[0-9a-f]{32})/$', SurveyDetailView.as_view(), name='survey_report'),
    url(r'^report/industry/(?P<industry_name>\w+)/$', SurveyResultsIndustryDetail.as_view(), name='survey_industry'),
]
