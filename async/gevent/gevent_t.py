#coding=utf-8

# import gevent

# import gevent.monkey
# gevent.monkey.patch_all()
# # gevent.monkey.patch_socket()

# def foo(i, a, b, c): 
#     print gevent.getcurrent(), i
#     # print('Running in foo' + str(i) + ' ' + str(a) + str(b) + str(c))
#     gevent.sleep(0)
#     # print('Explicit context switch to foo again')

# tasks = [ gevent.spawn(foo,i, 1, 2,3) for i in range(0,10)]
# gevent.joinall(tasks)

#----------------------------------------------------------------------------

# from gevent import monkey; monkey.patch_socket()
# import gevent

# def f(n):
#     for i in range(n):
#         print gevent.getcurrent(), i
#         gevent.sleep(0)  #主动切换协程 正式环境不需要

# g1 = gevent.spawn(f, 5)
# g2 = gevent.spawn(f, 5)
# g3 = gevent.spawn(f, 5)
# g1.join()
# g2.join()
# g3.join()


# from gevent import monkey; monkey.patch_all()
# import gevent
# import urllib2

# def f(url):
#     print('GET: %s' % url)
#     resp = urllib2.urlopen(url)
#     data = resp.read()
#     print('%d bytes received from %s.' % (len(data), url))

# gevent.joinall([
#         gevent.spawn(f, 'https://www.python.org/'),
#         gevent.spawn(f, 'https://www.yahoo.com/'),
#         gevent.spawn(f, 'https://github.com/'),
# ])

# file io
import gevent
from gevent import monkey; monkey.patch_all()
# from gevent.fileobject import FileObject
from gevent.fileobject import FileObjectThread
# from gevent.fileobject import FileObjectPosix

import datetime

def hi():
    while True:
        print datetime.datetime.now(), "Hello"
        gevent.sleep( 1 )

def w():
    print "writing..."
    s = "*"*(1024*1024*1024)
    f = open( "a.txt", "wb" )
    f = FileObjectThread(f, 'wb', close=False)
    f.write(s)
    f.close()
    print 'write done'

t1 = gevent.spawn(hi)
t2 = gevent.spawn(w)
ts = [t1,t2]
gevent.joinall( ts )