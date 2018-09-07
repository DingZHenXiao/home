"""index URL Configuration
"""
from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^01_request',request_views),
    url(r'^02_get/$',get1_views),
    url(r'^03_get/',get2_views),
    url(r'^04_get/$',get4_views),
    url(r'^05_post/$',post_views),
    url(r'^06_form/$',form_views),
    url(r'^07_register/$',register_views),
    url(r'^08_login/$',login_views),
    # url(r'^09_widget1/$',widget1_views),
    url(r'^10_widget2/$',widget2_views),
    url(r'^11_addCookie1/$',addCookie1_views),
    url(r'^12_addCookie2/$',addCookie2_views),
    url(r'^13_getCookie/$',getCookie_views),
    url(r'^14_setSession/$',setSession_views),
    url(r'^15_getSession/$',getSession_views),
    url(r'^16_index/$',index_views),
    url(r'^17_logout/$',logout_views),
    url(r'^18_login/$',login18_views),


]
