"""ding URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from .views import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^first/$',first_views),
    url(r'^0207/$',birthday_views),
    #正则表达式子组传参
    url(r'^admin/(\d{2})/(\d{4})/$',arg1_views),
    url(r'^run/(\d{4})/(\d{2})/$',run_arg2_views),
    #使用字典传参
    url(r'^show/$',show_views,{"arg1":"02","arg2":"07"})
]
