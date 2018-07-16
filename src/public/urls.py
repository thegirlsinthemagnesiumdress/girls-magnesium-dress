from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="public/index.html"), name="index"),
    url(r'^registration$', TemplateView.as_view(template_name="public/registration.html"), name="registration"),
    url(r'^reports/(?P<sid>[\w]+)$', TemplateView.as_view(template_name="public/report.html"), name="report"),
]
