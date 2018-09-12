from django.conf import settings
from django.conf.urls import url
from django.views.generic import TemplateView
from public.views import report_view, reports_admin, registration

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="public/index.html"), name="index"),
    url(r'^registration$', registration, name="registration"),
    url(r'^reports$', reports_admin, name="reports"),
    url(r'^reports/(?P<sid>[\w]+)$', report_view, name="report"),
    # Don't merge with this, it's just for testing
    url(r'^report-static$', TemplateView.as_view(template_name="public/report-static.html"), name="report-static"),
]
