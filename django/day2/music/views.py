'''这是music应用的视图处理文件　'''
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_views(request):
    return HttpResponse("这是music的index_views")
