#!/usr/bin/python3
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, parse_config_file, options
from tornado.web import Application, RequestHandler


class IndexHandler(RequestHandler):
    def get(self,*args,**kwargs):
        self.write('<a href=/python>python</a><br>')
        self.write('<a href=/java>java</a>')
    def post(self,*args,**kwargs):
        pass

class PythonHandler(RequestHandler):
    def get(self, p1=None, p2=None, *args, **kwargs):
        self.write('hello python<br>')
        if p1:
            self.write("date"+p1+"<br>")
        if p2:
            self.write("subject:"+p2)

    def post(self, *args, **kwargs):
        pass

class JavaHandler(RequestHandler):
    def get(self, j1=None, j2=None, *args, **kwargs):
        self.write('hello java'+"<br>")
        if j1:
            self.write("date:"+j1+"<br>")
        if j2:
            self.write("subject:"+j2+"<br>")

    def post(self, *args, **kwargs):
        pass

define('PORT',type=int,default=8888)
parse_config_file('../config/config')

app = Application([("/",IndexHandler),
                   ('/python',PythonHandler),
                   ("/python/([0-9a-zA-Z]+)",PythonHandler),
                   ("/python/([0-9a-zA-Z]+)/([A-Za-z]+)",PythonHandler),
                   ('/java',JavaHandler),
                   ("/java/([0-9a-zA-Z]+)",JavaHandler),
                   ("/java/([0-9a-zA-Z]+)/([a-zA-Z]+)",JavaHandler),
                   ])
server = HTTPServer(app)
server.listen(options.PORT)
IOLoop.current().start()