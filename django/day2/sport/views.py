'''这是sport应用的视图处理文件　'''
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_views(request):
    return HttpResponse("这是sport中的index_views")

def params_views(request):
    return render(request,'01_params.html')

def name_views(request):
    return HttpResponse("已成功到达name_views")

def name_arg_views(request,num):
    return HttpResponse("patament:"+num)