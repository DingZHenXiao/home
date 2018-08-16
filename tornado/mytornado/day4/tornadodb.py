import json
from random import randint
import pymysql
import time
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, parse_config_file, options
from tornado.web import Application, RequestHandler, UIModule

define("PORT",type=int,default=8888)
parse_config_file("../config/config")


class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('login.html')

class LoginHandler(RequestHandler):
    def post(self, *args, **kwargs):
        username = self.get_body_argument("username")
        pwd = self.get_body_argument("pwd")
        #建立连接
        mysettings = {
            'user':'root',
            'host':'localhost',
            'password':'123456',
            'port':3306,
            'database':'blogdb',
            'charset':'utf8',
        }
        connection = pymysql.connect(**mysettings)
        # #获取游标对象
        cursor = connection.cursor()
        # #发送sql指令
        sql = "select count(*) from tb_user " \
              "where user_name = %s and user_password = %s"
        params = (username, pwd)
        cursor.execute(sql,params)
        result = cursor.fetchone()
        if result[0]:
            print(result)
            self.redirect("/blog")
        else:
            self.redirect("/?args=1")

    def get(self, *args, **kwargs):
        pass


class BlogHandler(RequestHandler):
    def set_default_headers(self):
        # self.set_header("Content-Type","application/json; ")
        print("调用set_default_headers方法")

    def initialize(self,date,subject):
        self.date = date
        self.subject = subject

    def on_finish(self):
        print("调用on_finish方法")

    def get(self, *args, **kwargs):
        self.render("blog.html")
    
    def write_error(self, status_code, **kwargs):
        if status_code == 200:
            self.write("<span style=color:red;font-weight:bold;"
                       "font-size:36px;>这是一个极其严重的错误！</span>")
        else:
            super().write_error(status_code, **kwargs)

    def post(self, *args, **kwargs):
        pass


class Login_module(UIModule):
    def render(self, *args, **kwargs):
        res = ''
        args = self.request.query
        print(args)
        if args:
            res = '用户名或密码错误'
        return self.render_string(
            "module/login_module.html",result=res)

class Blog_head_module(UIModule):
    def render(self, *args, **kwargs):
        return self.render_string(
            "module/blog_head_module.html")


class Blog_body_module(UIModule):
    def render(self, *args, **kwargs):
        return self.render_string(
            'module/blog_body_module.html',
            a=8888,b=19999,
            blogs=[
                {
                    "author":"ding",
                    'title':'news',
                    'subject':'CHINA',
                    'content': '感冒好难受',
                    'conmment': 0,
                    'avatar': "",
                },
                {
                    "author": "wang",
                    'title': 'sport',
                    'subject': 'USA',
                    'content': '吾本将心向明月,奈何明月照沟渠.',
                    'conmment': 10000,
                    'avatar':"/static/images/a.jpg"
                },
                {
                    "author": "wang-hui-ning",
                    'title': '',
                    'subject': 'JAPAN',
                    'content': '人生若只如初见,何事秋风悲画扇.',
                    'conmment': 41654640,
                    'avatar': "",
                },
            ])

class RegisterHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('register.html')

    def post(self, *args, **kwargs):
        username = self.get_body_argument('username')
        password = self.get_body_argument("pwd")
        city = self.get_body_argument("city")
        print(username,password,city)
        if username and password:
            dic = {
                'host': '127.0.0.1',
                'user': 'root',
                'password': '123456',
                'port': 3306,
                'database': 'blogdb',
                'charset': 'utf8'
            }
            conn = pymysql.connect(**dic)
            cursor = conn.cursor()
            sql = 'select count(*) from tb_user where user_name = %s and user_password = %s'
            params = (username,password)
            cursor.execute(sql,params)
            result = cursor.fetchone()
            print(result)
            if result[0]:
                return self.redirect("/register?args=2")

            if self.request.files:
               file = self.request.files["avatar"]
               filename = str(time.time())+file[0]["filename"]
               filebody = file[0]["body"]
               print(filename)
               avatar = filename
               with open('mystatics/images/filename','wb') as f:
                   f.write(filebody)
            else:
               print("未上传头像")
           #数据库初始化

            sql = 'insert into tb_user(' \
                 'user_name,user_password,' \
                 'user_avatar,' \
                 'user_city) values(%s,%s,%s,%s)'
            params = (username,password,avatar,city)
            try:
               cursor.execute(sql,params)
               conn.commit()
               print("insert ok")
            except Exception as e:
               print(e)
               conn.rollback()
               print('rollback done')
            self.redirect("/")

        else:
            self.redirect("/register?args=1")

class Register_module(UIModule):
    def render(self, *args, **kwargs):
        resp = ''
        args = self.request.query
        args = args.split("=")
        print(args)
        if args[-1] == '1':
            resp = '用户名或密码不能为空!'
        if args[-1] == '2':
            resp = "用户名重复"
        return self.render_string('module/register_module.html',
                                  result=resp)


app = Application([
    ("/",IndexHandler),
    ("/login",LoginHandler),
    ("/blog",BlogHandler,{"date":"day2","subject":"response"}),
    ("/register",RegisterHandler),
                ],
    template_path="templates",
    static_path="mystatics",
    ui_modules={'login_module':Login_module,
                'blog_head_module':Blog_head_module,
                'blog_body_module':Blog_body_module,
                'register_module':Register_module,
                },
)
server = HTTPServer(app)
server.listen(options.PORT)
IOLoop.current().start()