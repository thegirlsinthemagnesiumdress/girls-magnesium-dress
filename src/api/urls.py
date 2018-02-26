from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'company/$', views.company, name='company_api')
]
