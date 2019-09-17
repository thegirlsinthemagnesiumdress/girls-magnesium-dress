from rest_framework.permissions import BasePermission
from django.conf import settings


class IsSurveyAdminRequired(BasePermission):
    def has_permission(self, request, view):
        return request.user.email.endswith(settings.SURVEY_ADMIN_AUTHORIZED_DOMAINS)
