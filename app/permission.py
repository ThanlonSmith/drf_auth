class MyPermission1:
    def has_permission(self, request, view):
        # 超级用户可以访问
        if request.user.user_type != 3:
            return False
        return True


class MyPermission2:
    def has_permission(self, request, view):
        # 普通用户可以访问，超级用户不可以访问
        if request.user.user_type == 3:
            return False
        return True
