# -*- coding: utf-8 -*-

from xml.dom.minidom import parse
import xml.dom.minidom

import sys
import os

reload(sys)
sys.setdefaultencoding('utf-8')


source_fname = raw_input('xml file name:')
#print source_fname
#source_fname = "create_film.xml"

result_fname = os.path.splitext(source_fname)[0]
result_fname = result_fname + '.sql'

# 使用minidom解析器打开 XML 文档
DOMTree = xml.dom.minidom.parse(source_fname)

collection = DOMTree.documentElement
#if collection.hasAttribute("shelf"):
    #print "Root element : %s" % collection.getAttribute("shelf")

# 
#TraceData = collection.getElementsByTagName("TraceData")
#Events = collection.getElementsByTagName("Event")
Events = collection.getElementsByTagName("Column")

# 打印每部电影的详细信息
index = 0
result_cnt = ""
fp = open(result_fname, 'w')

for event in Events:
    columnid = ""
    
    if event.hasAttribute("id"):
        columnid = event.getAttribute("id")
        #print eventid,'####'
        
    # eventid =  event.parentNode.getAttribute('id')
    # if eventid != "10":
    #     continue
    
    if(columnid != "1"):
        continue
    index += 1
    print '[',index,']'    
    print event.childNodes[0].data
    
    #记录数据用于保存
    
    idx = '\n['
    idx += str(index)
    idx += ']\n'
    result_cnt += idx
    result_cnt += event.childNodes[0].data
    #print '--->',eventid
    
    #if event.hasAttribute("name"):
        #print event.getAttribute("name")
        
    #print event.previousSibling.data
     
    #Columns = collection.getElementsByTagName("Column")
    #for column in Columns:
        #columnid = column.getAttribute("id")
        #if columnid == "1":
            #print column.childNodes[0].data
            #index += 1
            #print '[',index,']'
            #print column.childNodes[0].data
    

#print result_cnt  
fp.write(result_cnt)
fp.close()