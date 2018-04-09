from django.conf.urls import url
from api.views import CreateSurveyView, SurveyCompanyNameFromUIDView


urlpatterns = [
    url(r'^survey$', CreateSurveyView.as_view(), name='create_survey'),
    url(r'^company-name$', SurveyCompanyNameFromUIDView.as_view(), name='company_name'),
]
