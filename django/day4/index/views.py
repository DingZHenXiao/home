'''index views'''
from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.db.models import F,Q


# Create your views here.
def parent_views(request):
    return render(request,"01_parent.html")

def child_views(request):
    return render(request,"02_child.html")

# def addauthor_views(request):
#     Author.objects.create(name="丁振晓",
#                           age=23,
#                           email="dzx101444079@163.com")
#     return HttpResponse("Add Author OK")

# def addauthor_views(request):
#     author = Author(name="费成龙",
#                           age=24,
#                           email="123456789@163.com")
#     author.save()
#     return HttpResponse("Add 'fei' OK")

def addauthor_views(request):
    # dic = {"name":"汪晓菲","age":21,"email":"9876543210@163.com"}
    # author = Author(**dic)
    # author.save()

    return HttpResponse("Add 'wang' OK")

def addpublisher_views(request):
    # name=models.CharField(max_length=30)
    # address=models.CharField(max_length=50)
    # city=models.CharField(max_length=20)
    # country=models.CharField(max_length=20)
    # website=models.URLField()
    publisher = Publisher(name="古龙",
        address="河南郑州",
        city="郑州",
        country="中国",
        website="gulong@163.com")
    publisher.save()

    Publisher.objects.create(name="金庸",
        address="河南平顶山",
        city="平顶山",
        website="12345667.com")
    return HttpResponse("ok")

def addbook_views(request):
    # title=models.CharField(max_length=20)
    # publicate_date=models.DateField()
    Book.objects.create(title="神雕侠侣",publicate_date="2018-05-06")
    dic = {"title":"射雕英雄传","publicate_date":"2015-02-16"}
    book = Book(**dic)
    book.save()
    return HttpResponse("OK")

def query_views(request):
    authors = Author.objects.filter(isActive=True)
    # print(author)

    return render(request,"table.html",locals())


    # authors = Author.objects.values("name","age")
    # print(authors)
    # for i in authors:
    #     print("姓名:",i['name'],"年龄:",i['age'])

    # authors = Author.objects.values_list("name","age").order_by("age")
    # for i in authors:
    #     print('姓名:'+i[0],'年龄:'+i[1])

    # authors = Author.objects.exclude(id=1)
    # for i in authors:
    #     print(i.name,i.age,i.email)

    #使用filter实现部分行的查询
    # authors = Author.objects.filter(id=1)
    # for x in authors:
    #     print(x.name,x.age)

    #使用filter()借助查询谓词进行查询
    # authors = Author.objects.filter(email__contains="0")
    # for i in authors:
    #     print(i.name,i.email)

    #使用get()查询一条数据
    # author = Author.objects.get(id=1)
    # print(author.name)

    #使用count()计数
    # authors = Author.objects.filter(id__gte=1).count()
    # print(authors)
    # authors = Author.objects.count()
    # print(authors)
    # return HttpResponse("OK")

def update_views(request):
    #单个修改
    au = Author.objects.get(id=1)
    au.name = "ding"
    au.save()
    #批量修改
    Author.objects.filter(id__gt=1).update(age=40)
    return HttpResponse("Update successfully")

def delauthor_views(request,id):
    au = Author.objects.get(id=id)
    au.isActive = False
    au.save()
    #请求的转发
    # return query_views(request)
    return HttpResponseRedirect("/06_query/")

def updateauthor_views(request,id):
    au = Author.objects.get(id=id)
    return render(request,"table2.html",locals())

def doF_views(request):
    Author.objects.all().update(age=F("age")+10)
    return HttpResponseRedirect("/06_query/")

def doQ_views(request):
    authors = Author.objects.filter(Q(id=1)|
        Q(age__gte=40))()
    return render(request,"table.html",
        {"au":authors})

def oto_views(request):
    # wife = Wife.objects.get(id=4)
    # author = wife.author
    author = Author.objects.get(id=1)
    wife = author.wife
    return render(request,"01_oto.html",
        locals())
def otm_views(request):
    # 正向查询
    book = Book.objects.get(id=1)
    publisher = book.publisher
    #反向查询
    pub = Publisher.objects.get(id=2)
    bookList = pub.book_set.all()
    return render(request,"03_otm.html",
        locals())

def mtm_views(request):
    #正向查询
    book = Book.objects.get(id=1)
    authorList = book.author.all()
    #反向查询
    author = Author.objects.get(id=2)
    bookList = author.book_set.all()
    return render(request,"04_mtm.html",
        locals())

def mtm1_views(request):
    #正向查询
    author = Author.objects.get(id=1)
    publisherList = author.publisher.all()
    #反向查询
    publisher = Publisher.objects.get(id=3)
    authorList = publisher.author_set.all()
    return render(request,"05_mtm.html",
        locals())

def manager_views(request):
    count = Author.objects.auCount()
    return HttpResponse(count)

def manager1_views(request,age):
    authorList = Author.objects.ltAge(age)
    return HttpResponse(authorList)

def manager2_views(request,keyword):
    bookList = Book.objects.title_count(keyword)
    return HttpResponse(bookList)

def update2_views(request):
    name = request.POST["name"]
    age = request.POST["age"]
    email = request.POST["email"]
    id = request.POST["id"]
    author = Author.objects.get(id=id)
    author.name = name
    author.age = age
    author.email = email
    author.save()
    return HttpResponse("ok")