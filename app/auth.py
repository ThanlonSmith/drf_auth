from rest_framework.views import exceptions
from .models import UserToken
from rest_framework.authentication import BaseAuthentication, BasicAuthentication, SessionAuthentication, \
    TokenAuthentication, RemoteUserAuthentication


class FirstAuthenticate:
    def authenticate(self, request):
        pass

    def authenticate_header(self, request):
        pass


class Authenticate:
    def authenticate(self, request):
        token = request._request.GET.get('token')
        print(token)
        token_obj = UserToken.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed('用户认证失败！')
        # 在rest framework内部会将整个两个字段赋值给request,共后续操作使用
        return (token_obj.user, token_obj)  # （request.user,request.auth）

    def authenticate_header(self, request):
        pass
