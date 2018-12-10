"""
author:何凯
date:
"""
from django.utils.deprecation import MiddlewareMixin
from backweb.models import User
from django.http import HttpResponseRedirect


class LoginStatusMiddleware(MiddlewareMixin):
    
    def process_request(self,request):
        # 如果为前端页面，不进行session判断
        if 'web' in request.path or 'login' in request.path:
            return None

        user_id = request.session.get('user_id')
        # 取得session
        if user_id:
            # 已经登陆
            user= User.object.get(pk=user_id)
            request.user = user
            # 将该用户返回给request；
            # 个人博客中没什么用，因为只有一个用户
            return None
        # 未登录
        return HttpResponseRedirect('/web/login/')

    def process_response(self,request,response):
        return response