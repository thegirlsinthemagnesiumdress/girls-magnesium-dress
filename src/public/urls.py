from django.conf import settings
from django.conf.urls import url
from django.views.generic import TemplateView
from public.views import reports_admin, registration, report_static, index_static

urlpatterns = [
    url(r'^$', index_static, name="index"),
    url(r'^createsurvey/$', registration, name="registration"),
    url(r'^reports/$', reports_admin, name="reports"),
    url(r'^reports/(?P<sid>[\w]+)/$', report_static, name="report"),
]

handler404 = 'core.views.handler404'
handler500 = 'core.views.handler500'
