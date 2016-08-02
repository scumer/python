# -*- coding: utf-8 -*-

import urllib

try:
	proxy = r'127.0.0.1:8087'
	proxyConfig = 'http://%s:%s@%s' % ('anonymous', 'password', proxy)
	url = "http://movie.douban.com/photos/photo/2178960079/#title-anchor"
	# page = urllib.urlopen(url, proxies={'http':proxyConfig})
	page = urllib.urlopen(url)

	# print page.readlines()
	print page.read()
	# print page.readline()
	print "status:", page.getcode() #200请求成功,404
	# print "url:", page.geturl() 
	# print "head_info:\n",  page.info()  
except IOError, e:
	print e


	
 