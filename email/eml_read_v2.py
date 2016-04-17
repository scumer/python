# coding=utf-8
import email
import re
import os
from BeautifulSoup import BeautifulSoup

dirname = r'F:\DOCS\salary'

pattren = re.compile(u'(.*)年(.*)月份.*结算日(.*)\）')
##11,395.75元 201511
def analysis_email(filename,colname,colcnt):
    fp = open(filename, "r")
    msg = email.message_from_file(fp) # 直接文件创建message对象，这个时候也会做初步的解码
    
    subject = msg.get("subject") # 取信件头里的subject,　也就是主题
    #print subject
    # 下面的三行代码只是为了解码象=?gbk?Q?=CF=E0=C6=AC?=这样的subject
    h = email.Header.Header(subject)
    dh = email.Header.decode_header(h)
    subject = dh[0][0]
    #print subject

    for par in msg.walk():
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
                    #print u'附件名有非法字符，自动换一个'
                    f = open('aaaa', 'wb')
                f.write(data)
                f.close()
            else:
                #不是附件，是文本内容
                payload =  par.get_payload(decode=True) # 解码出文本内容，直接输出来就可以了。
                if (par.get_content_type() == 'text/html'):
                    soup = BeautifulSoup(''.join(payload))
                    cnt = []
                    allp = soup.findAll(name='p')
                    for p in allp:
                        #print unicode(p.span.text)
                        if p.span.text[:2] == '20':
                            dateinfo = ''
                            for s in p.findAll(name='span'):
                                if unicode(s.text):
                                    if unicode(s.text) != '&nbsp;':
                                        #item += unicode(s.text)
                                        #print unicode(s.text.strip()),
                                        dateinfo += (s.text.strip()) 
                                        
                            #print dateinfo
                            
                            match = pattren.match(dateinfo)
                            if match:
                                g = match.groups()
                                if len(g) != 3:
                                    print 'date info analysis error!'
                                    return
                                dateinfo = ('%s.%02d(%s)')%(g[0],int(g[1]),g[2])
                                #print dateinfo
                                cnt.append(dateinfo)

                            #
                            #print dateinfo                            
                    
                    for tab in soup.findAll(name='table'):
                        itemname = tab.findAll('tr')[0]
                        itemcnt = tab.findAll('tr')[1]
                        if not colname:
                            colname.append(u'结算日期')
                            for s in itemname.findAll(name='span'):
                                if unicode(s.text):
                                    if unicode(s.text) != '&nbsp;':
                                        #item += unicode(s.text)
                                        #print unicode(s.text.strip()),
                                        colname.append(s.text.strip())
                        #print ''   
                        
                        for s in itemcnt.findAll(name='td'):
                            if unicode(s.text):
                                if unicode(s.text) != '&nbsp;':
                                    #item += unicode(s.text)
                                    #print unicode(s.text.strip()),
                                    cnt.append(s.text.strip())
                            else:
                                #print '0',
                                cnt.append(0)
                        #print ''
                        colcnt.append(cnt)
                        

    fp.close()
    



def get_salary(path,colname,colcnt):
    dirlist = os.listdir(path)
    for fname in dirlist:
        fname = os.path.join(path,fname)
        analysis_email(fname, colname, colcnt)

if __name__ == '__main__':
    colname = []
    colcnt = []    
    get_salary(dirname,colname,colcnt)
    
    fp = file('salary.csv','wb')
    #analysis_email(u'工资条(2).eml',colname,colcnt)
    del colname[1:5]
    itemname = ''
    for i in colname:
        itemname += i+',' 
        print '%s'%i,',',
    print ''
    fp.write(itemname.encode('utf-8')[:-1]+'\r\n')
    
    for col in colcnt:
        del col[1:5]
        itemcnt = ''
        for cnt in col:
            itemcnt += '%s'%cnt+',' 
            print '%s'%cnt,',',
        print ''
        fp.write(itemcnt.encode('utf-8')[:-1]+'\r\n')
        #fp.writelines(sequence_of_strings)
    fp.close()


#analysis_email(u'eml_read.py')