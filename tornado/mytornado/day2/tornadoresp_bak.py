import json

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, parse_config_file, options
from tornado.web import Application, RequestHandler

define("PORT", type=int, default=8888)
parse_config_file("../config/config")


class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('login.html')

        msg = self.get_query_argument("msg", None)
        if msg:
            self.write(msg)


class LoginHandler(RequestHandler):
    def post(self, *args, **kwargs):
        username = self.get_body_argument("username")
        pwd = self.get_body_argument("pwd")

        if username == "ding" and pwd == "123":
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
                              "filename={}".format(username, filename))
            else:
                self.redirect('/blog?username={}'.format(username))
        else:
            # print("登录失败")
            self.redirect("/?msg=用户名或密码有误")

    def get(self, *args, **kwargs):
        pass


class BlogHandler(RequestHandler):
    def set_default_headers(self):
        # self.set_header("Content-Type","application/json; ")
        print("调用set_default_headers方法")

    def initialize(self, date, subject):
        self.date = date
        self.subject = subject

    def on_finish(self):
        print("调用on_finish方法")

    def get(self, *args, **kwargs):
        print("接收到的参数是" + self.date)
        print("接收到的参数是" + self.subject)
        username = self.get_query_argument("username", None)
        filename = self.get_query_arguments("filename", None)
        if username and filename:
            self.write("Welcom: " + username + "上传了文件")
        else:
            # resp = {
            #     "key1":"value1",
            #     "key2":"value2",
            # }
            # json_str = json.dumps(resp)
            # self.set_status(888,"define status_code")
            self.write("Welcom to Blog")
            # self.write(json_str)
            # self.write(resp)
            # myhead = self.request.headers.get("myhead",None)
            # print(myhead)
            # self.send_error(500)

    def write_error(self, status_code, **kwargs):
        if status_code == 200:
            self.write("<span style=color:red;font-weight:bold;"
                       "font-size:36px;>这是一个极其严重的错误！</span>")
        else:
            super().write_error(status_code, **kwargs)

    def post(self, *args, **kwargs):
        pass


app = Application([
    ("/", IndexHandler),
    ("/login", LoginHandler),
    ("/blog", BlogHandler, {"date": "day2", "subject": "response"}),
], template_path="templates")
server = HTTPServer(app)
server.listen(options.PORT)
IOLoop.current().start()