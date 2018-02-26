from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'company/(?P<company_id>\d+)', views.company, name='company_api')
]
