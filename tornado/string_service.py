import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

import textwrap

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class ReverseHandler(tornado.web.RequestHandler):
	"""docstring for ReverseHandler"""
	def get(self, input):
		self.write(input[::-1])


class WrapHandler(tornado.web.RequestHandler):
	def post(self):
		text = self.get_argument('text','')
		width = self.get_argument('width', '40')
		self.write(textwrap.fill(text,int(width)))


def make_app():
	return tornado.web.Application(handlers=
		[(r'/reverse/(\w+)',ReverseHandler),
		(r'/wrap',WrapHandler)])

if __name__ == '__main__':
	tornado.options.parse_command_line()
	app = make_app()
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)

	try:
		tornado.ioloop.IOLoop.instance().start()
	except KeyboardInterrupt:
		tornado.ioloop.IOLoop.instance().stop()