'''这是music应用的路由配置文件'''
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$',index_views),
]