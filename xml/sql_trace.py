# -*- coding: utf-8 -*-

from xml.dom.minidom import parse
import xml.dom.minidom

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 使用minidom解析器打开 XML 文档
#DOMTree = xml.dom.minidom.parse("print_film.xml")
DOMTree = xml.dom.minidom.parse("create_film.xml")
collection = DOMTree.documentElement
#if collection.hasAttribute("shelf"):
    #print "Root element : %s" % collection.getAttribute("shelf")

# 在集合中获取所有电影
#TraceData = collection.getElementsByTagName("TraceData")
#Events = collection.getElementsByTagName("Event")

Events = collection.getElementsByTagName("Column")
#TrueEvents = collection.getElementsByTagName("Event")
#print Events

# 打印每部电影的详细信息
index = 0
for event in Events:
    columnid = ""
    
    if event.hasAttribute("id"):
        columnid = event.getAttribute("id")
        #print eventid,'####'
        
    eventid =  event.parentNode.getAttribute('id')
    if eventid != "10":
        continue
    
    if(columnid != "1"):
        continue
    index += 1
    print '[',index,']'    
    print event.childNodes[0].data
    #print '--->',eventid
    
    #if event.hasAttribute("name"):
        #print event.getAttribute("name")
        
    #print event.previousSibling.data
    

    
    
    #Columns = collection.getElementsByTagName("Column")
    #for column in Columns:
        #columnid = column.getAttribute("id")
        #if columnid == "1":
            ##print column.childNodes[0].data
            #index += 1
            #print '[',index,']'
            #print column.childNodes[0].data
    
    
    
    #type = event.getElementsByTagName('Column')
    #print "Type: %s" % type.childNodes[0].data
    #format = movie.getElementsByTagName('format')[0]
    #print "Format: %s" % format.childNodes[0].data
    #rating = movie.getElementsByTagName('rating')[0]
    #print "Rating: %s" % rating.childNodes[0].data
    #description = movie.getElementsByTagName('description')[0]
    #print "Description: %s" % description.childNodes[0].data