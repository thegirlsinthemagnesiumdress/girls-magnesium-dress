from api.views import (
    CreateSurveyView,
    SurveyCompanyNameFromUIDView,
    SurveyResultsIndustryDetail,
    SurveyDetailView,
)
from django.conf.urls import url


urlpatterns = [
    url(r'^survey$', CreateSurveyView.as_view(), name='create_survey'),
    url(r'^company-name$', SurveyCompanyNameFromUIDView.as_view(), name='company_name'),
    url(r'^report/company/(?P<sid>[0-9a-f]{32})/$', SurveyDetailView.as_view(), name='survey_report'),
    url(r'^report/industry/(?P<industry>[\w-]+)/$', SurveyResultsIndustryDetail.as_view(), name='survey_industry'),
]
