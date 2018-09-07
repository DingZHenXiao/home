from django.http import HttpResponse
def first_views(request):
    return HttpResponse("我的第一个django程序")

def birthday_views(request):
    return HttpResponse("生日快乐")

def arg1_views(request,arg1,arg2):
    return HttpResponse("参数传递:" + arg1 + " " + arg2)

def run_arg2_views(request,arg1,arg2):
    return HttpResponse(arg1+" "+arg2)

def show_views(request,arg1,arg2):
    return HttpResponse(arg1+" "+arg2)