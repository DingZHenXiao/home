'''index URL confinguration'''
from django.conf.urls import url,include
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^$', index_views),
]

urlpatterns += [
    url(r'^01_getTemp$',getTemp_views),
    url(r'^02_getTemp$',render_views),
    url(r'^03_var/$',var_views),
    url(r'^05_varTemp/$',varTemp_views),
    url(r'^06_index/$',index_views),
    url(r'^07_login/$',login_views),
    url(r'^08_login/$',login02_views),
]
