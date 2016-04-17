# coding=utf-8
import email
from BeautifulSoup import BeautifulSoup

fp = open(u"工资条(1).eml", "r")
msg = email.message_from_file(fp) # 直接文件创建message对象，这个时候也会做初步的解码

##11,395.75元
#subject = msg.get("subject") # 取信件头里的subject,　也就是主题
##print subject
## 下面的三行代码只是为了解码象=?gbk?Q?=CF=E0=C6=AC?=这样的subject
#h = email.Header.Header(subject)
#dh = email.Header.decode_header(h)
#subject = dh[0][0]
#print "subject:", subject
#print "from: ", email.utils.parseaddr(msg.get("from"))[1] # 取from
#print "to: ", email.utils.parseaddr(msg.get("to"))[1] # 取to

#print msg.keys()

for par in msg.walk():
    #print par.__dict__
    #print help(par)
    #print par
    if not par.is_multipart(): # 这里要判断是否是multipart，是的话，#里面的数据是一个message 列表                              
        name = par.get_param("name") #如果是附件，这里就会取出附件的文件名
        if name:
            #有附件
            # 下面的三行代码只是为了解码象=?gbk?Q?=CF=E0=C6=AC.rar?=这样的文件名
            h = email.Header.Header(name)
            dh = email.Header.decode_header(h)
            fname = dh[0][0]
            print u'附件名:', fname
            data = par.get_payload(decode=True) #　解码出附件数据，然后存储到文件中
 
            try:
                f = open(fname, 'wb') #注意一定要用wb来打开文件，因为附件一般都是二进制文件
            except:
                print u'附件名有非法字符，自动换一个'
                f = open('aaaa', 'wb')
            f.write(data)
            f.close()
        else:
            #不是附件，是文本内容
            
            payload =  par.get_payload(decode=True) # 解码出文本内容，直接输出来就可以了。
            if (par.get_content_type() == 'text/html'):
                #payload
                soup = BeautifulSoup(''.join(payload))
                
                #print soup.prettify() 
                #print soup.table
                #soup.attrs()
                #print soup.findAll(name='p')
                for tab in soup.findAll(name='table'):
                    itemname = tab.findAll('tr')[0]
                    itemcnt = tab.findAll('tr')[1]
                    

                    #print unicode(cnt.p.span)
                    #item = ''
                    for s in itemname.findAll(name='span'):
                        if unicode(s.text) != '&nbsp;':
                            #item += unicode(s.text)
                            print unicode(s.text.strip()),
                    print ''        
                    for s in itemcnt.findAll(name='td'):
                        if unicode(s.text):
                            if unicode(s.text) != '&nbsp;':
                                #item += unicode(s.text)
                                print unicode(s.text.strip()),
                        else:
                            print '0',
                            
                    
                    
                    

                    
                    #if cnt.p:
                        ##print unicode(cnt.p.span)
                        #item = ''
                        #for s in cnt.p.findAll(name='span'):
                            #if unicode(s.text) != '&nbsp;':
                                #item += unicode(s.text)
                        #print item
                    #else:
                        #print 'NULL'

                    #for s in soup.findAll(name='span'):
                        #print unicode(s)
                
            
 
        #print '+'*60 # 用来区别各个部分的输出

fp.close()