from rest_framework.views import APIView
from .models import User, UserToken
from django.http import JsonResponse
from utils.md5 import md5
from app.throttle import UserVisitThrottle, VisitThrottle


class AuthView(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = [VisitThrottle, ]

    def post(self, request, *args, **kwargs):
        self.dispatch
        ret = {'code': 1000, 'msg': None}
        try:
            # 需要以form-data的方式提交
            name = request._request.POST.get('name')
            pwd = request._request.POST.get('pwd')
            instance = User.objects.filter(name=name, pwd=pwd).first()  # User object (1)，
            print(type(instance))  # <class 'app.models.User'>，加不加all()结果一样
            print(instance)  # User object (1)，加不加all()结果一样
            if not instance:
                ret['code'] = 1001
                ret['msg'] = '用户名或密码错误'
            else:
                token = md5(name=name)
                UserToken.objects.update_or_create(user=instance, defaults={'token': token})
                ret['token'] = token
        except Exception as e:
            ret['code'] = 1001
            ret['msg'] = '请求异常'
        return JsonResponse(ret)


class OrderView(APIView):
    # 需要认证，使用自定义的Authenticate类来认证，已经在全局中做了认证
    # authentication_classes = [FirstAuthenticate, Authenticate, ]
    # 将权限类列表置为空，则不需要任何权限就可以访问
    # permission_classes = []

    def get(self, request, *args, **kwargs):
        # request.user
        # request.auth
        # print(request.user)  # User object (1)
        # print(request.auth)  # print(request.auth)#User object (1)
        """
        权限:
        if request.user.user_type != 3:
            return HttpResponse('无权访问')
        """
        self.dispatch
        order_dict = {
            1: {
                'name': "thanlon",
                'age': 24,
                'gender': '男',
            },
            2: {
                'name': "kiku",
                'age': 26,
                'gender': '女',
            },
        }
        # token = request._request.GET.get('token')
        ret = {'code': 1000, "msg": None, 'data': None}
        try:
            ret['data'] = order_dict
        except Exception as e:
            pass
        return JsonResponse(ret)
