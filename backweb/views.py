from django.shortcuts import render
from django.http import HttpResponseRedirect

from backweb.filter import ArticleFilter
from backweb.models import User, Article
from rest_framework import mixins,viewsets

from backweb.serializer import BackWebSerializers


def login(request):
    if request.method == 'GET':
        return render(request,'backweb/login.html')

    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username)
        if user and user.password == password:
            request.session['user_id'] = user.id
            # 创建 session
            return HttpResponseRedirect('/api/backweb/index/')
        else:
            return render(request,'backweb/login.html',{'error':'用户名或密码错误!!'})

class ArticleView(viewsets.GenericViewSet,
                  mixins.DestroyModelMixin,
                  mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin):
    queryset = Article.objects.filter(is_delete=0)
    serializer_class = BackWebSerializers
    filter_class = ArticleFilter

    def perform_destroy(self,instance):
        # 修改删除数据
        instance.is_delete = 1
        instance.save()


def index(request):
    if request.method == 'GET':
        return render(request,'backweb/index.html')

def art(request):
    if request.method == 'GET':
        return render(request,'backweb/article.html')

def add_art(request):
    if request.method == 'GET':
        return render(request,'backweb/add_art.html')
    elif request.method == 'POST':
        pass