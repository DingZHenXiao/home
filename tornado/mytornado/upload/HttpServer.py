#coding=utf-8

'''
name:Levi
功能：完成HTTPServer项目　
　　　　　httpserver部分
'''

from socket import *
import sys  
from threading import Thread 

#将httpserver具体内容封装为类
class HTTPServer(object):
    def __init__(self,app):
        self.sockfd = socket()
        self.sockfd.setsockopt\
        (SOL_SOCKET,SO_REUSEADDR,1)
        self.app = app 

    def bind(self,ip,port):
        self.ip = ip
        self.port = port
        self.sockfd.bind((ip,port))

    def serve_forever():
        self.sockfd.listen(10)
        print("listen to port %d ..." % self.port)
        while True:
            c,addr = self.sockfd.accept()
            print("connect from:",addr)
            handle_thread = Thread\
            (target=self.handle_client,agrgs=(c,))
            handle_thread.setDaemon(True)
            handle_thread.start()

    def handle_client(self,c):
        #接收浏览器的request
        request_data = c.recv(4096)
        request_lines = request_data.splitlines()
        #获取请求行GET / HTTP/1.1
        request_line = request_lines[0].decode("utf-8")
        print(request_line)
#创建httpserver对象，添加必要属性，启动服务程序
def main():
    #启动httpserver时从命令行直接输入使用的应用服务模块
    if len(sys.argv) < 2:
        sys.exit('''
            Run the server as:
            python3 HttpServer.py FrameWorkName:app
            '''
            )

    #提取模块和app名称
    module_name,app_name = sys.argv[1].split(":")

    #将当前目录加入环境变量
    sys.path.insert(1,'.')
    #导入模块生产模块对象
    m = __import__(module_name)
    #获取app对象
    app = getattr(m,app_name)

    #使app成为httpd的属性，处理具体请求事件
    httpd = HTTPServer(app)
    httpd.bind('0.0.0.0',8000)
    #启动服务器
    httpd.serve_forever()


if __name__ == "__main__":
    main()
