import pymysql
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, parse_config_file, options
from tornado.web import Application, RequestHandler, UIModule

define("PORT",type=int,default='10086')
parse_config_file('../config/config')

class LoginHandler(RequestHandler):
    def get(self,*args,**kwargs):
        self.render('login.html')

    def post(self,*args,**kwargs):
        name = self.get_body_argument('username')
        pwd = self.get_body_argument('password')
        if name == 'ding' and pwd == '123456':
            self.redirect('/genecheck')
        else:
            self.redirect('/?msg=0')

class Login_module(UIModule):
    def render(self):
        resp = ''
        msg = self.request.query.split("=")[-1]
        if msg == '0':
            resp = '用户名或密码错误'
        return self.render_string('modules/login_module.html',
                                  result=resp)

class RegisterHandler(RequestHandler):
    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        pass

class GenecheckHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('genecheck.html')

    def post(self, *args, **kwargs):
        userId = self.get_body_argument('userId')
        self.redirect('genecheck?userId=%s'%userId)

class Genecheck_module(UIModule):
    def render(self, *args, **kwargs):
        userId = self.request.query.split("=")[-1]
        dic = {
            'host':'127.0.0.1',
            'user':'root',
            'password':'123456',
            'port':3306,
            'database':'genedb',
            'charset':'utf8',
        }
        conn = pymysql.connect(**dic)
        cursor = conn.cursor()
        sql = 'select username,info,gender from genetb where id = %s'
        params = (userId,)
        cursor.execute(sql, params)
        result = cursor.fetchone()
        print(result)
        gender = '先生'
        if result[2] == "woman":
            gender = "女士"
        return self.render_string(
            'modules/genecheck_module.html',
            name=result[0],
            result=result[1],
            gender=gender,
        )

app = Application([('/',LoginHandler),
                   ('/register',RegisterHandler),
                   ('/genecheck',GenecheckHandler),
                   ],
                  template_path='templates',
                  ui_modules={
                      'login_module':Login_module,
                      'genecheck_module':Genecheck_module,
                  },
                  )
server = HTTPServer(app)
server.listen(options.PORT)
IOLoop.current().start()
