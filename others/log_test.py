#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
import string
import sys
import os
import time
from logging.handlers import RotatingFileHandler
# logger = None


def init():
	logname = 'log_test.log'
	logname = os.path.join(GetAppPath(), logname)
	logging.basicConfig(level=logging.DEBUG,
                format='[%(asctime)s %(filename)s %(funcName)s line:%(lineno)d %(levelname)s] %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S',
                filename=logname,
                )

def GetDiskInfo():
	global logger
	logger  = logging.getLogger()
	logname = 'log_test.log'
	logname = os.path.join(GetAppPath(), logname)
	handler = logging.FileHandler(logname)
	formatter = logging.Formatter('[%(asctime)s %(funcName)s() line:%(lineno)d %(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S') 


	handler.setFormatter(formatter)
	logger.addHandler(handler)
	logger.setLevel("DEBU")
	logger.error("This is an errwwwwwwwwsdor message")
	logger.info("This is info")
	pass

def GetAppPath():
	app_path  = ''
	if getattr(sys, 'frozen', False):
		appl_path  = os.path.dirname(sys.executable)
	else:
		app_path  = os.path.dirname(__file__)
	return app_path 

# init()
#GetDiskInfo()



class Log:
	"""封装logging模块"""
	def __init__(self, filename):
		#super(ClassName, self).__init__()
		self.filename = filename
		self.logger   = logging.getLogger()
		self.handler  = logging.FileHandler(self.filename)
		formatter     = logging.Formatter('[%(asctime)s %(funcName)s() line:%(lineno)d %(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S') 
		
		self.handler.setFormatter(formatter)
		self.logger.addHandler(self.handler)
		self.logger.setLevel(logging.DEBUG)
	def error(self, record):
		self.logger.error(record)


def CreateLogger(filename = 'tmp.log', logLevel = logging.ERROR):
	logger    = logging.getLogger()
	# handler   = logging.FileHandler(sys.stdout)
	# formatter = logging.Formatter('[%(asctime)s %(funcName)s() line:%(lineno)d %(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S') 
	
	# handler.setFormatter(formatter)
	# logger.addHandler(handler)
	# logger.setLevel(5)

	#定义一个RotatingFileHandler，最多备份5个日志文件，每个日志文件最大10M
	Rthandler = RotatingFileHandler(filename, maxBytes=10*1024,backupCount=2)
	formatter = logging.Formatter('[%(asctime)s %(funcName)s() line:%(lineno)d %(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
	Rthandler.setFormatter(formatter)

	logger.addHandler(Rthandler)
	logger.setLevel(5)
	return logger

logger = CreateLogger('log_test.log')
logger.info(time.strftime('%H:%M:%S',time.localtime(time.time())))
while True:
	logger.info(time.strftime('%H:%M:%S',time.localtime(time.time())))
	pass