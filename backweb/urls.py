"""
author:何凯
date:
"""
from django.conf.urls import url
from rest_framework.routers import SimpleRouter
from backweb import views


router = SimpleRouter()
router.register('art',views.ArticleView)
urlpatterns = [
    url(r'^login/',views.login),
    url(r'^index/',views.index),
    url(r'^article/',views.art),
    url(r'^add_art/',views.add_art),
    ]

urlpatterns += router.urls