#!/usr/bin/python3
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, parse_config_file, options
from tornado.web import Application, RequestHandler



class IndexHandler(RequestHandler):
    def get(self,*args,**kwargs):
        self.render('escape.html',result='')
    def post(self,*args,**kwargs):
        test = self.get_body_argument('test')
        #以下请求头为破解谷歌自动转义的安全设置
        # self.set_header('X-XSS-Protection',0)
        self.render('escape.html',result=test)

define('PORT',type=int,default=8888)
parse_config_file('../config/config')

app = Application([("/",IndexHandler),
                   ],template_path='templates',

                  )
server = HTTPServer(app)
server.listen(options.PORT)
IOLoop.current().start()