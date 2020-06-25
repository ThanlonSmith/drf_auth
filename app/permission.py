from rest_framework.permissions import BasePermission


class MyPermission1(BasePermission):
    message = '必须是超级用户才可以访问'

    def has_permission(self, request, view):
        # 超级用户可以访问
        if request.user.user_type != 3:
            return False
        return True


class MyPermission2(BasePermission):
    def has_permission(self, request, view):
        # 普通用户可以访问，超级用户不可以访问
        if request.user.user_type == 3:
            return False
        return True
