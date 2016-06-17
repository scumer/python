# -*- coding: utf-8 -*-

import urllib2  
import urllib  
import re 
import os

def geturl():
	page = 0
	page_end = 64
	# while True:
		# if page == page_end:
		# 	break
	luoo_url = "http://www.5.cn/magazine/1968/2834/index.html?from=timeline&isappinstalled=0"
	page = page+1
	# print "<%s>" % page
	
	# luoo_url = "http://www.luoo.net/music/"
	myResponse = urllib2.urlopen(luoo_url)
	myPage = myResponse.read()  
	myPage = myPage.decode("utf-8") 
	# print myPage

	#
	#re. 
	myItems = re.findall('src="(http://img.800.cn/20140928/(.*?).jpg)"></div></div>',myPage,re.S)  

	for item in myItems:
		suffix = get_file_extension(unicode(item[0]))
		name = unicode(item[1])
		fullname = (name) + (suffix)
		# print item
		print fullname
		picreq = urllib2.urlopen(item[0])
		picdata = picreq.read()  
		save_file(fullname, picdata)

def save_file(file_name, data):
    if data == None:
        return

    path = 'magazine_image'
    if not os.path.exists(path):
    	os.mkdir(path)
    # if(not path.endswith("/")):
    #     path=path+"/"
    # file=open(path+file_name, "wb")
    file_name = os.path.join(path, file_name)
    if not os.path.exists(file_name):
		file=open(file_name, "wb")
		file.write(data)
		file.flush()
		file.close()

# '''»ñÈ¡ÎÄ¼þºó×ºÃû'''
def get_file_extension(file):  
    return os.path.splitext(file)[1]

geturl()