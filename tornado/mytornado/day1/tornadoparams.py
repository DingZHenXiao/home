from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, parse_config_file, options
from tornado.web import Application, RequestHandler

define("PORT",type=int,default=8888)
parse_config_file("../config/config")


class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        html = "<form action='/login' method=post \
                enctype=multipart/form-data>"\
               "用户名:"\
               "<input type='text' name='username'><br>"\
               "密  码:"\
               "&nbsp;&nbsp;&nbsp;"\
               "<input type='password' name='pwd'><br>"\
               "<input type='file' name='avatar'><br>" \
               "<input type='file' name='avatar'><br>" \
               "<input type='submit' value='登录'>" \
               "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" \
               "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" \
               "<input type='reset' value='重置'>"\
               "</form>"
        self.write(html)

        msg = self.get_query_argument("msg",None)
        if msg:
            self.write(msg)


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
            self.redirect("/?msg=用户名或密码有误")


class BlogHandler(RequestHandler):
    def get(self, *args, **kwargs):
        username = self.get_query_argument("username",None)
        filename = self.get_query_arguments("filename",None)
        if username and filename:
            self.write("Welcom: "+username+"上传了文件")
        else:
            self.write("Welcom {} to Blog".format(username))
            # myhead = self.request.headers.get("myhead",None)
            # print(myhead)
    def post(self, *args, **kwargs):
        pass


app = Application([
    ("/",IndexHandler),
    ("/login",LoginHandler),
    ("/blog",BlogHandler),
                ])
server = HTTPServer(app)
server.listen(options.PORT)
IOLoop.current().start()