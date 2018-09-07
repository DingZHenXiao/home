#这sport应用的路由配置文件
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$',index_views),
    url(r'^01_params/$',params_views),
    url(r'^02_name/$',name_views,name="page2"),
    url(r'^03_name(\d{4})$',name_arg_views,name="page3"),
]