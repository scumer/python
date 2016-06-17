# -*- coding: utf-8 -*-

import urllib2  
import urllib  
import re 
import os

def geturl():
	page = 0
	page_end = 64
	while True:
		if page == page_end:
			break
		luoo_url = "http://www.luoo.net/tag/?p=" + str(page)
		page = page+1
		print "<%s>" % page
		
		# luoo_url = "http://www.luoo.net/music/"
		myResponse = urllib2.urlopen(luoo_url)
		myPage = myResponse.read()  
		myPage = myPage.decode("utf-8") 
		# print myPage

		#
		#re. 
		myItems = re.findall('<img src="(http://img2.luoo.net/pics/vol.*?640x452.jpg)" alt="(.*?)" class="cover rounded">',myPage,re.S)  
		print myItems
		# for item in myItems:
		# 	suffix = get_file_extension(unicode(item[0]))
		# 	name = unicode(item[1])
		# 	fullname = (name) + (suffix)
		# 	picreq = urllib2.urlopen(item[0])
		# 	picdata = picreq.read()  
		# 	save_file(fullname, picdata)

def save_file(file_name, data):
    if data == None:
        return

    path = 'pic'
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

'''»ñÈ¡ÎÄ¼þºó×ºÃû'''
def get_file_extension(file):  
    return os.path.splitext(file)[1]

geturl()