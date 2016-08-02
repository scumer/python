# -*- coding: utf-8 -*-

from BaseHTTPServer import HTTPServer,BaseHTTPRequestHandler
import urllib,io,shutil


class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.process(2)
 
    def do_POST(self):
        pass
 
    def process(self,type):
        if '?' in self.path:
            print 'GET Request'
            # MonitorService.CheckServiceStatus()
            #指定返回编码
            enc="UTF-8"
            retinfo = "ok"
            retinfo = retinfo.encode(enc)
            f = io.BytesIO()
            f.write(retinfo)
            f.seek(0)
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=%s" % enc)
            self.send_header("Content-Length", str(len(retinfo)))
            self.end_headers()
            shutil.copyfileobj(f,self.wfile)

try:
	server = HTTPServer(('', 8001), MyRequestHandler)
	print 'started httpserver...'
	server.serve_forever()
except KeyboardInterrupt, e:
	print 'Bye!'
	server.server_close()
