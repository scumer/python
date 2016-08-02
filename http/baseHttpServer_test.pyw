# -*- coding: utf-8 -*-
# import BaseHTTPServer
from BaseHTTPServer import HTTPServer,BaseHTTPRequestHandler
import urllib,io,shutil

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.process(2)
 
    def do_POST(self):
        # self.process(1)
        pass
 
    def process(self,type):
        content =""
        if type==1:#post方法，接收post参数
            datas = self.rfile.read(int(self.headers['content-length']))
            datas = urllib.unquote(datas).decode("utf-8", 'ignore')#指定编码方式
            datas = transDicts(datas)#将参数转换为字典
            if datas.has_key('data'):
                content = "data:"+datas['data']+"\r\n"
 
        if '?' in self.path:
            print 'cmd = GET'
            # query = urllib.splitquery(self.path)
            # action = query[0]
 
            # if query[1]:#接收get参数
            #     queryParams = {}
            #     for qp in query[1].split('&'):
            #         kv = qp.split('=')
            #         queryParams[kv[0]] = urllib.unquote(kv[1]).decode("utf-8", 'ignore')
            #         content+= kv[0]+':'+queryParams[kv[0]]+"\r\n"

            #指定返回编码
            enc="UTF-8"
            # content = content.encode(enc)
            retinfo = "ok"
            retinfo = retinfo.encode(enc)
            f = io.BytesIO()
            # f.write(content)
            f.write(retinfo)
            f.seek(0)
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=%s" % enc)
            self.send_header("Content-Length", str(len(retinfo)))
            self.end_headers()
            shutil.copyfileobj(f,self.wfile)

server = HTTPServer(('', 8001), MyRequestHandler)
print 'started httpserver...'
server.serve_forever()



"""
Post Get 区别
定时执行检测
测试脚本
"""