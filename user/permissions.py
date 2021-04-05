from rest_framework.permissions import BasePermission


class AdministratorOnly(BasePermission):
    """ Administrator permission. """

    def has_permission(self, request, view):
        return request.user


class DeveloperOnly(BasePermission):
    pass