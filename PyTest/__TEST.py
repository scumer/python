# coding=utf-8
from itertools import izip_longest
import json
import requests
import time
# import datetime
from datetime import datetime

from requests.exceptions import ConnectTimeout

# import logging
# from logging.handlers import TimedRotatingFileHandler as H, TimedRotatingFileHandler

# import sys

# logfile = TimedRotatingFileHandler('log.log', when='D', backupCount=5)
# formatter = logging.Formatter('[%(process)d %(asctime)s %(funcName)s() line:%(lineno)d %(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
# logfile.setFormatter(formatter)
# logging.getLogger('').setLevel(logging.INFO)
# logging.getLogger('').addHandler(logfile) 

# console = logging.StreamHandler()
# console.setLevel(logging.INFO)
# # formatter = logging.Formatter('[%(levelname)s]%(message)s')
# formatter = logging.Formatter('[%(asctime)s P:%(process)-5d %(funcName)s:%(lineno)d %(levelname)5s] %(message)s', '%Y-%m-%d %H:%M:%S')
# console.setFormatter(formatter)
# logging.getLogger('').addHandler(console)


def fun():
    logging.error('3')
    logging.info('info')
# logging.exception('3')
# fun()


# ret = requests.post('http://www.baidu.com')
# # print ret.request.headers
# try:
#     print ret.raise_for_status()
# except Exception, e:
#     print e.message

# print ret.text
# print ret.json().get('msg')

# if a = False:
#     print  a


# coding=utf-8
# import logging

# logger = logging.getLogger()
# hand = logging.FileHandler('my_log.txt')
# logger.addHandler(hand)
# formatter = logging.Formatter(u'[%(process)d %(asctime)s %(funcName)s() line:%(lineno)d %(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
# hand.setFormatter(formatter)

# logger.addHandler(logging.FileHandler('my_log.txt'))

# dd = {'a':u'中'}

# print json.dumps(dd, ensure_ascii=False)

# # logger.error(u'Pão')
# # # logger.error('São')
# logger.error('%s%s','a','b')
# # logger.error(d)




# import signal
# import os
# import time
# try:
#     def receive_signal(signum, stack):
#         print 'Received:', signum

#     # 注册信号处理程序
#     signal.signal(signal.SIGINT, receive_signal)
#     # signal.signal(signal.SIGUSR2, receive_signal)

#     # 打印这个进程的PID方便使用kill传递信号

#     print 'My PID is:', os.getpid()

#     # 等待信号，有信号发生时则调用信号处理程序
#     import multiprocessing as mp
#     while True:
#         time.sleep(1)
# except KeyboardInterrupt, e:
#     print 'exit'




