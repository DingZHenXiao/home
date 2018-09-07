import json
from random import randint

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

        if username=="ding" and pwd=="123":
            files = self.request.files
            if files:
                avatars = files.get("avatar")
                for avatar in avatars:
                    filename = avatar.get("filename")
                    content = avatar.get("body")
                    with open("../upload/{}".format(filename),
                              "wb") as f:
                        f.write(content)
                self.redirect("/blog?username={}&"
                              "filename={}".format(username,filename))
            else:
                self.redirect('/blog?username={}'.format(username))
        else:
            # print("登录失败")
            self.redirect("/?msg=0")
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
        msg = self.request.query
        print(msg,type(msg))
        if msg:
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


app = Application([
    ("/",IndexHandler),
    ("/login",LoginHandler),
    ("/blog",BlogHandler,{"date":"day2","subject":"response"}),
                ],
    template_path="templates",
    static_path="mystatics",
    ui_modules={'login_module':Login_module,
                'blog_head_module':Blog_head_module,
                'blog_body_module':Blog_body_module,
                },
)
server = HTTPServer(app)
server.listen(options.PORT)
IOLoop.current().start()