from rest_framework import permissions


class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        if (request.user.role == 1 or request.user.is_superuser) and request.user.is_active:
            return True


class IsWaiter(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.role == 2 and request.user.is_active:
            return True


class IsCook(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.role == 3 and request.user.is_active:
            return True


class CanGetListUser(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'list' and (request.user.is_admin or request.user.is_superuser):
            return True
