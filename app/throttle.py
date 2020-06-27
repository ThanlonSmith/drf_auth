import time
from rest_framework.throttling import BaseThrottle, SimpleRateThrottle

VISIT_RECORD = {}


# class VisitThrottle(BaseThrottle):
#     def __init__(self):
#         self.history = None
#         self.ctime = None
#
#     def allow_request(self, request, view):
#         """
#         设定10s之内只能访问10次
#         :param request:
#         :param view:
#         :return: True or False
#         返回值为True表示可以访问;返回值为False或None表示访问频率太高被限制
#         """
#         # 获取用户的ip地址,当前request(封装)中有的就取当前的request，如果没有就到_request中取
#         # remote_addr = request._request.META.get('REMOTE_ADDR')
#         remote_addr = self.get_ident(request)  # 调用父类的方法获取IP标识
#         print(remote_addr)  # 127.0.0.1
#         self.ctime = time.time()  # 1593151531.1494734
#         print(self.ctime)
#         if remote_addr not in VISIT_RECORD:
#             VISIT_RECORD[remote_addr] = [self.ctime]
#             return True
#         self.history = VISIT_RECORD.get(remote_addr)
#         while self.history and self.history[-1] < self.ctime - 10:
#             self.history.pop(-1)
#         if len(self.history) < 10:
#             self.history.insert(0, self.ctime)
#             return True
#         return False  # 写不写都可以,如果执行到这里说明不可访问的，返回False或None都可以表示不可以访问
#
#     def wait(self, *args, **kwargs):
#         """
#         设置距离下次可以请求的时间
#         :param args:
#         :param kwargs:
#         :return:默认返回None，表示使用默认
#         """
#         """
#         当请求被拒绝，会执行wait方法
#         """
#         ctime = time.time()
#         print(ctime)
#         print(self.history[-1])
#         """
#         return False
#         {
#           "detail": "Request was throttled. Expected available in 0 seconds."
#         }
#         """
#         return 60 - (ctime - self.history[-1])

class VisitThrottle(SimpleRateThrottle):
    # scope被当作key使用的，根据它到配置文件中取值
    scope = 'erics'

    def get_cache_key(self, request, view):
        """获取key"""
        return self.get_ident(request)


class UserVisitThrottle(SimpleRateThrottle):
    # scope被当作key使用的，根据它到配置文件中取值
    scope = 'user_erics'

    def get_cache_key(self, request, view):
        """获取key"""
        print(request)  # <rest_framework.request.Request object at 0x7f155c6b86d0>
        # 用户认证成功之后就会有request.user
        print(request.user)  # User object (1)
        print(request.user.name)  # thanlon
        return request.user.name
