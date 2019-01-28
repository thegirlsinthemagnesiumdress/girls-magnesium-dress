from django.conf.urls import url
from public.views import reports_admin, registration, report_static, index_static, result_detail

urlpatterns = [
    url(r'^$', index_static, name="index"),
    url(r'^createsurvey/$', registration, name="registration"),
    url(r'^reports/$', reports_admin, name="reports"),
    url(r'^reports/(?P<sid>[\w]+)/$', report_static, name="report"),
    url(r'^result-detail/(?P<response_id>[\w]+)/$', result_detail, name="response-detail"),
]
