'''index views'''
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index_views(request):
    return HttpResponse("这是index中的index_views")

def getTemp_views(request):
    t = loader.get_template("1-template.html")
    html = t.render()
    return HttpResponse(html)

def render_views(request):
    return render(request,"1-template.html")

def var_views(request):
    name = "<水浒传>"
    author = "施耐庵"
    title = "105个男人和3个女人的故事"
    return render(request,"var.html",locals())

def fun(a,b):
    return a + b

class A(object):
    """docstring for A"""
    a = "A类中的a属性"
    def f(self):
        return "This is the method of A"
        
def varTemp_views(request):
    L = ['老舍','竹子请','莫言']
    t = ('冰心','韩寒','郭敬明')
    d = {"A":"Andrew","B":"BEYOND","C":"Control"}
    return render(request,"04_var.html",{
        "num":10086,
        "str":"中国移动",
        "list":L,
        "tup":t,
        "dict":d,
        "fun":fun(25,52),
        "A":A(),
        })

def index_views(request):
    return render(request,'05_index.html')

def login_views(request):
    if 'uname' in request.session:
        return HttpResponse('欢迎'+'uname')
    else:
        uname = request.POST['uname']
        upwd = request.POST['upwd']
        request.session['uname'] = uname
        request.session['upwd'] = upwd
        return HttpResponse('欢迎'+uname)

def login02_views(request):
    if request.method == "GET":
        if "name" in request.session:
            return HttpResponse("ok")
        else:
            #判断cookie
            if "name" in request.COOKIES:
                name = request.COOKIES["name"]
                request.session["name"] = name
                return HttpResponse('ok')
            else:
                return render(request,"07_login.html")
    else:
        #存session
        name = request.POST['name']
        pwd = request.POST['pwd']
        request.session["name"] = name
        request.session['pwd'] = pwd
        print("name:",name,"pwd:",pwd)

        return HttpResponse("ok")