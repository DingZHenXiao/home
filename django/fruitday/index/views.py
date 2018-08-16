import json
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *

# Create your views here.
def login_views(request):
    if request.method == 'GET':
        #获取源地址
        url = request.META.get('HTTP_REFERER','/')
        resp = HttpResponseRedirect(url)
        if "id" in request.session and "uphone" in request.session:
            return HttpResponseRedirect(resp)
        else:
            if "id" in request.COOKIES and "uphone" in request.COOKIES:
                id = request.COOKIES['id']
                uphone = request.COOKIES['uphone']
                request.session['id'] = id
                request.session['uphone'] = uphone
                return HttpResponseRedirect(resp)
            else:
                # 创建　LoginForm 对象，再交给模板
                form = LoginForm()
                resp = render(request, 'login.html', locals())
                resp.set_cookie('url', url)
                return resp
    else:
        uphone = request.POST['uphone']
        upwd = request.POST['upwd']
        uList = Users.objects.filter(uphone=uphone, upwd=upwd)
        if uList:
            url = request.COOKIES.get('url','/')
            resp = HttpResponseRedirect(url)
            if 'url' in request.COOKIES:
                resp.delete_cookie('url')
            #存session
            request.session['id'] = uList[0].id
            request.session['uphone'] = uphone
            # 判断用户是否勾选上　记住密码
            if 'isSaved' in request.POST:
                # 分两次将　uphone 和　id 存进　cookie
                expires = 60 * 60 * 24 * 365
                resp.set_cookie('id', uList[0].id, expires)
                resp.set_cookie('uphone', uphone, expires)

            return resp
        else:
            form = LoginForm()
            return render(request, 'login.html', locals())


def register_views(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        # 接收提交的数据并注册回数据库
        uphone = request.POST['uphone']
        upwd = request.POST['upwd']
        uname = request.POST['uname']
        uemail = request.POST['uemail']

        # 验证手机号码是否已经存在
        uList = Users.objects.filter(uphone=uphone)
        if uList:
            # 手机号码已经存在，给出错误提示
            return render(request,
                          'register.html',
                          {'errMsg': '手机号码已经存在',
                           'uname': uname,
                           'uemail': uemail,
                           })

        dic = {
            'uphone': uphone,
            'upwd': upwd,
            'uname': uname,
            'uemail': uemail,
        }

        Users(**dic).save()
        return HttpResponse('注册成功')

def checkphone_views(request):
    #接收前端提交过来的数据－uphone
    uphone = request.GET["uphone"]
    print(len(uphone))
    #查询upone在数据表中是否存在
    u_list = Users.objects.filter(uphone=uphone)
    print(u_list)
    #如果存在响应:{"status":1},如果不存在则响应{"status":0}
    if u_list:
        s = 1
        msg = "手机已经被注册"
    else:
        if len(uphone) != 11:
            s = 1
            msg = '手机号不正确'
        else:
            s = 0
            msg = '通过'
    dic = {"status": s,"msg": msg}
    return HttpResponse(json.dumps(dic))

def index_views(request):
    #读取所有分类
    types = GoodsType.objects.all()
    # goods = types.goods_set.all()
    print(types)

    return render(request,"index.html",locals())

def all_type_goods_views(request):
    #大列表：准备承装所有的类型和商品
    all_list = []
    types = GoodsType.objects.all()
    print(types)
    #循环遍历types,得到每一个type以及对应的商品们
    for type in types:
        print(type)
        #将type序列化为json字符串
        type_json = json.dumps(type.to_dict())
        #获取type下的前１０个产品
        g_list = type.goods_set.order_by("id")[0:10]
        #将g_list序列化成为json字符串
        g_list_json = serializers.serialize('json',g_list)
        #创建一个字典，将type_json和g_list_json封装
        dic = {
            "type":type_json,
            "goods":g_list_json,
        }
        #将字典追加进all_list序列化
        all_list.append(dic)
    return HttpResponse(json.dumps(all_list))

def check_login_views(request):
    '''
    验证session中是否包含登录信息
    '''
    if "id" in request.session and 'uphone' in request.session:
        loginStatus = 1
        #通过session中的id获取uname
        id = request.session.get('id')
        uname = Users.objects.get(id=id).uname
        dic = {
            'loginStatus':loginStatus,
            'uname':uname,
        }
        return HttpResponse(json.dumps(dic))
    else:
        #session中没有登录信息
        #查询cookies是否有登录信息
        if 'id' in request.COOKIES and 'uphone' in request.COOKIES:
            user_id = request.COOKIES['id']
            uphone = request.COOKIES['uphone']
            #将user_id和uphone保存进session
            request.session['id'] = user_id
            request.session['uphone'] = uphone
            #查询uname的值，响应给客户端
            uname = Users.objects.get(id=user_id).uname
            loginStatus = 1
            dic = {
                'loginStatus': loginStatus,
                'uname': uname,
            }
            return HttpResponse(json.dumps(dic))
        else:
            #session和cookies中均没有登录信息
            dic={
                'loginStatus':0,
            }
            return HttpResponse(json.dumps(dic))

def logout_views(request):
    if 'id' in request.session and 'uphone' in request.session:
        del request.session['id']
        del request.session['uphone']
        #记录源地址
        url = request.META.get('HTTP_REFERER','/')
        resp = HttpResponseRedirect(url)
        #判断cookie中是否包含登录信息
        if 'id' in request.COOKIES and 'uphone' in request.COOKIES:
            resp.delete_cookie('id')
            resp.delete_cookie('uphone')
        return resp
    return HttpResponseRedirect('/')

def add_cart_views(request):
    #从session中获取用户ID
    user_id = request.session.get('id')
    #从请求中获取商品id
    good_id = request.POST['good_id']
    #购买数量默认为1
    good_count = 1
    #购买车中是否有相同的用户及商品,如果有的话，则更新数量,
    cart_list = CarInto.objects.filter(user_id=user_id,good_id=good_id)
    if cart_list:
        cartinfo = cart_list[0]
        cartinfo.ccount=cartinfo.ccount+good_count
        cartinfo.save()
        dic = {
            'status':1,
            'statusText':'更新数量成功'
        }
        return HttpResponse(json.dumps(dic))
    else:
        cartinfo = CarInto()
        cartinfo.good_id = good_id
        cartinfo.user_id = user_id
        cartinfo.ccount = good_count
        cartinfo.save()
        # 如果没有则将上述数据插入数据库
        dic = {
            "status":1,
            "statusText":'添加购物车成功'
        }
        return HttpResponse(json.dumps(dic))


