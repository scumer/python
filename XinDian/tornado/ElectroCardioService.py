# coding=utf-8
import logging
import urllib
import json
import datetime
import time

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
import tornado.gen

from msdb import ParseODBCError, MSSQL

# from tornado.options import define, options
# define("port", default=9000, help="run on the given port", type=int)

ms = None

def InitLogger(logname = 'ElectroCardio.log', logLevel = logging.INFO):
    import logging, os
    from logging.handlers import TimedRotatingFileHandler

    if not os.path.exists('./log'):
        os.mkdir('./log')

    formatter = logging.Formatter('[%(asctime)s %(funcName)s() line:%(lineno)d %(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
    logfile = TimedRotatingFileHandler('./log/'+logname, when='D', backupCount=5)
    logfile.setLevel(logLevel)
    logfile.setFormatter(formatter)
    logging.getLogger('').setLevel(logging.INFO)
    logging.getLogger('').addHandler(logfile)  

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('[%(levelname)s]%(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)


class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        # query = self.get_argument('q')
        # print 'query:', '123'

        ms.ExecQuery('SELECT * FROM Pacs_image')
        ms.ExecQuery('SELECT * FROM Pacs_image')
        resList = ms.ExecQuery("SELECT AEID,AEName,AEType,AETitle,IP,Port FROM Pacs_AETitle WHERE AEType = 'X'")
        import time
        time.sleep(2)

        import json
        data = json.dumps(list(resList[0]))
        # print data

        # client = tornado.httpclient.AsyncHTTPClient()
        # self.write("Hello, world")
        self.write(data)
        self.finish()
        # client.fetch("http://search.twitter.com/search.json?" + \
        #         urllib.urlencode({"q": query, "result_type": "recent", "rpp": 100}),
        #         callback=self.on_response)

    def on_response(self, response):
        body = json.loads(response.body)
        result_count = len(body['results'])
        now = datetime.datetime.utcnow()
        raw_oldest_tweet_at = body['results'][-1]['created_at']
        oldest_tweet_at = datetime.datetime.strptime(raw_oldest_tweet_at,
                "%a, %d %b %Y %H:%M:%S +0000")
        seconds_diff = time.mktime(now.timetuple()) - \
                time.mktime(oldest_tweet_at.timetuple())
        tweets_per_second = float(result_count) / seconds_diff
        self.write("""
                    <div style="text-align: center">
                        <div style="font-size: 72px">%s</div>
                        <div style="font-size: 144px">%.02f</div>
                        <div style="font-size: 24px">tweets per second</div>
                    </div>""" % (self.get_argument('q'), tweets_per_second))
        self.finish()


class FilmUpload(tornado.web.RequestHandler):
    # @tornado.web.asynchronous
    # @tornado.gen.coroutine
     def post(self):
        # print self.get_argument(name='film')
        print self.request.headers.__dict__
        print 'request data:'
        # print self.request.body
        print self.request.arguments
        # print self.request.body_arguments
        # print self.request.files

        fileinfo = self.request.files
        # print  fileinfo

        filmdata = fileinfo['filmdata'][0].get('body', '')
        filmname = 'rcv-'+fileinfo['filmdata'][0].get('filename', '') 

        fp = open(filmname, 'wb')
        fp.write(filmdata)
        fp.close()


        # print fileinfo
        # print self.request


def RunSvc(port=9000, debug=True):
    global ms
    ms = MSSQL('Techsvr_DSN', 'xuhui', '')
    app = tornado.web.Application(handlers=
        [(r'/',IndexHandler),
        (r'/upload/film',FilmUpload),
        ],
        debug=debug)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()


def StopSvc():
    tornado.ioloop.IOLoop.instance().stop()


if __name__ == "__main__":
    InitLogger()
    try:
        RunSvc(port=9000, debug=True)
    except KeyboardInterrupt as e:
        StopSvc()