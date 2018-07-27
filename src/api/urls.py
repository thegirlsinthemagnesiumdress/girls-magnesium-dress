from django.conf.urls import url
from api.views import CreateSurveyView, SurveyCompanyNameFromUIDView, SurveyResultsDetail


urlpatterns = [
    url(r'^survey$', CreateSurveyView.as_view(), name='create_survey'),
    url(r'^company-name$', SurveyCompanyNameFromUIDView.as_view(), name='company_name'),
    url(r'^report/(?P<sid>[0-9a-f]{32})/$', SurveyResultsDetail.as_view(), name='survey_report'),
]
