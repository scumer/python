from qrcode import QRCode
from StringIO import StringIO
import os

zbar = r'"C:\Program Files (x86)\ZBar\bin\zbarimg.exe"'

cmd = zbar+ ' -q' + ' qrcode.jpg'
#print cmd

pipe = os.popen(cmd + ' 2>&1', 'r')
text = pipe.read()[8:]
#print text


def qrcode_data(filename):
    cmd = zbar+ ' -q ' + filename
    pipe = os.popen(cmd + ' 2>&1', 'r')
    text = pipe.read()[8:]
    pipe.close()
    
    return text

def all_data():
    list = os.listdir('.')
    for i in list:
        if i.split('.')[-1] == 'jpg':
            
            print i,' ',qrcode_data(i)
#all_data()

def gen_all_qr():        
    fp = open('data2.txt','r')    
    idx = 0
    while True:
        idx += 1
        rd = fp.readline()
        if rd == '':
            break      
        rd = rd.strip()
        if len(rd) == 0:
            continue
        
        #name,data = None
        ret = rd.split('   ')
        #print ret
        name = ret[0]
        data = ret[1]
        #str.split(self)
        print idx,' ',name,' ' ,data   
    fp.close()

gen_all_qr()

def gen_qrcode(filename,qrdata):
    
    fp = open(filename, 'w')
    
    #564be177d52c9e7a68b2c83d
    
    gen = QRCode()
    gen.add_data(qrdata)
    img = gen.make_image()
    io = StringIO()
    #img.save(io)
    img.save(fp)
    
    #img.show()
    #io.seek(0)
    #response = make_response(io.read())
    #response.headers['content-Type'] = 'image/jpeg'
   
    fp.close()
