from django.conf.urls import url, include
from . import views
from api.views import SurveyViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'survey', SurveyViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
