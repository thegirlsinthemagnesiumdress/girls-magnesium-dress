from django.conf.urls import url
from django.views.generic import TemplateView

from views import create_survey


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="public/index.html"), name="index"),
    url(r'^survey/$', create_survey, name="create_survey")
]
