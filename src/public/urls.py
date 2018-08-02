from django.conf.urls import url
from django.views.generic import TemplateView
from public.views import report_view, reports_list, reports_admin

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="public/index.html"), name="index"),
    url(r'^registration$', TemplateView.as_view(template_name="public/registration.html"), name="registration"),
    url(r'^reports$', reports_list, name="reports"),
    url(r'^reports/(?P<sid>[\w]+)$', report_view, name="report"),
    url(r'^reports_admin$', reports_admin, name="reports_admin"),
]
