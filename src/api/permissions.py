from rest_framework import permissions
class ApiPermissions (permissions.BasePermission):
    """
    Qualtrics users should not be able to access any endpoint.
    Single viewsets could overwrite this.
    """

    def has_permission(self, request, view):
        return not request.user.is_qualtrics
