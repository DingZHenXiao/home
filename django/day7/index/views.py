from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import *
from .models import *

# Create your views here.


def request_views(request):
    # print(dir(request))
    scheme = request.scheme
    body = request.body
    path = request.path
    method = request.method
    host = request.get_host()
    get = request.GET
    post = request.POST
    cookies = request.COOKIES
    # return HttpResponse("ok")
    return render(request, "01_request.html",
                  locals())


def get1_views(request):
    return render(request, '02_get.html')


def get2_views(request):
    uname = request.GET["uname"]
    upwd = request.GET["upwd"]
    isSaved = request.GET.get('isSaved', '')
    return HttpResponse("uname:"+uname+"\n" +
                        "upwd:"+upwd+"\n"+"isSaved"+isSaved)


def get4_views(request):
    uname = request.GET["uname"]
    upwd = request.GET["upwd"]
    isSaved = request.GET.get('isSaved', '')
    return HttpResponse("uname:"+uname+"\n" +
                        "upwd:"+upwd+"\n"+"isSaved"+isSaved)


def post_views(request):
    if request.method == "GET":
        return render(request, '03_post.html')
    else:
        uname = request.POST["uname"]
        upwd = request.POST["upwd"]
        return HttpResponse(uname+','+upwd)


def form_views(request):
    if request.method == "GET":
        form = RemarkForm()
        return render(request, "04_form.html", locals())
    else:
        form = RemarkForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = cd["subject"]
            email = cd["email"]
            message = cd["message"]

            print(subject)
            print(email)
            print(message)
        return HttpResponse("Get OK")


def register_views(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, "05_register.html", locals())
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            Users(**form.cleaned_data).save()
            return HttpResponse("save ok")

def login_views(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, '06_login.html', locals())
    else:
        uname = request.POST['uname']
        upwd = request.POST['upwd']
        uList = Users.objects.filter(uname=uname, upwd=upwd)
        if uList:
            return HttpResponse('登录成功')
        else:
            return HttpResponse('登录失败')

def widget2_views(request):
    form = WidForm2()
    return render(request,'07_wid.html',locals())

def addCookie1_views(request):
    resp = HttpResponse('添加cookie')
    resp.set_cookie('uname','naruto',60*60*24*365)
    return resp

def addCookie2_views(request):
    resp = render(request,'02_get.html')
    resp.set_cookie('cookie2','uzumaki',60*60*24)
    return resp

def getCookie_views(request):
    # print(request.COOKIES)
    uname = request.COOKIES['uname']
    return render(request,'08_cookies.html',locals())

def setSession_views(request):
    request.session['uname'] = 'ding'
    return HttpResponse('add session success')

def getSession_views(request):
    if 'uname' in request.session:
        return HttpResponse('欢迎'+request.session['uname'])
    else:
        return HttpResponse('对不起，没查询到您的信息')

def index_views(request):
    #从session中获取登录名称
    uname = request.session.get('uname','')
    return render(request,"09_index.html",locals())

def login18_views(request):
    if request.method == 'GET':
        return render(request,'10_login.html')
    else:
        uname = request.POST['uname']
        upwd = request.POST['upwd']
        if uname == 'ding' and upwd == '123456':
            request.session['uname'] = uname
            return HttpResponseRedirect('/16_index/')
        else:
            pass#登录失败

def logout_views(request):
    if 'uname' in request.session:
        del request.session['uname']
        return HttpResponseRedirect('/16_index/')