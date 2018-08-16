''' ajax01/index/views.py '''
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import json
from django.core import serializers

# Create your views here.
def xmlhttp_views(request):
    return render(request,'01_xmlhttp.html')

def request01_views(request):
    return HttpResponse('这是异步请求的数据')

def params_views(request):
    return render(request,"02_params.html")

def request02_views(request):
    #接收请求提交的参数-name
    uname = request.GET['name']
    return HttpResponse('欢迎:'+uname)

def post_views(request):
    #先获取csrf的验证码的值
    csrftoken = request.COOKIES['csrftoken']
    return render(request,'03_post.html',locals())

def request03_views(request):
    name = request.POST['name']
    return HttpResponse('欢迎:'+name)

def form_views(request):
    return render(request,"04_form.html")

def request04_views(request):
    uname = request.POST['uname']
    upwd = request.POST['upwd']
    return HttpResponse(uname+':'+upwd)

def checkname_views(request):
    return render(request,'05_checkname.html')

def request05_views(request):
    uname = request.POST['uname']
    uList = Users.objects.filter(uname=uname)
    if uList:
        return HttpResponse('no')
    else:
        return HttpResponse('ok')

def request06_views(request):
    # uList = ['张三丰','张无忌','张翠山']
    # jsonList = json.dumps(uList)
    # print(jsonList)

    # uTup = ('漩涡鸣人','UzumakiNaruto','KakaShi')
    # jsonUtup = json.dumps(uTup)

    # uDic = {
    #     'name':'sangFeng.zhang',
    #     'age':30,
    #     'gender':'M'
    # }
    # jsonDic = json.dumps(uDic)

    uList = [
        {
        'name':'sangFeng.zhang',
        'age':30,
        'gender':'M'
        },
        {
        'name':'丁振晓',
        'age':28,
        'gender':'M'
        },
    ]
    jsonList = json.dumps(uList)
    print(jsonList)

    # users = Users.objects.all()
    # jsonusers = serializers.serialize('json',users)

    # user = Users.objects.filter(id=1)
    # print(user)
    # jsonuser = serializers.serialize('json',user)

    # user = Users.objects.get(id=1)
    # print(user.to_dic())
    # json_user = json.dumps(user.to_dic())
    return HttpResponse(jsonList)

def json_views(request):
    return render(request,"06_json.html")

def json07_views(request):
    return render(request,"07_json.html")

def request07_views(request):
    uList = Users.objects.all()
    json = serializers.serialize("json",uList)
    return HttpResponse(json)

def request08_views(request):
    # return HttpResponse("动态加载的数据!")
    json = serializers.serialize("json",Users.objects.all())
    return HttpResponse(json)

def request09_views(request):
    uname = request.GET["uname"]
    json = serializers.serialize("json",Users.objects.filter(uname__contains=uname))
    return HttpResponse(json)

def filter_views(request):
    ulist = Users.objects.filter(id=1)
    print(ulist)
    for i in ulist:
        print(i)

    print("######################")
    ulist = serializers.serialize('json',ulist)
    print(ulist)

    return HttpResponse('ulist')