from qrcode import QRCode
from StringIO import StringIO


#fp = open('qrcode.jpg', 'w')

##564be177d52c9e7a68b2c83d

#gen = QRCode()
#gen.add_data('http://139.196.57.2/report?id=566cd5dbd52c9e5df6ac4f68')
#img = gen.make_image()
#io = StringIO()
##img.save(io)
#img.save(fp)
##io.seek(0)
##response = make_response(io.read())
##response.headers['content-Type'] = 'image/jpeg'

#fp.close()

def gen_qrcode(name, data):
    fp = open(name, 'w')
    gen = QRCode()
    gen.add_data(data)
    img = gen.make_image()
    io = StringIO()    
    img.save(fp)
    fp.close()
    

qrdata = {'CT_DWM':'http://139.196.167.219/report_show?id=562c77de43b1bd581d70c239',
          'CT_HGF':'http://139.196.167.219/report_show?id=562c328a43b1bd581d70c007',
          'MR_YHJ':'http://139.196.167.219/report_show?id=562d8c9043b1bd581d70c80b'}

#for key in qrdata.keys():
    #print key,' ',qrdata[key]
    #gen_qrcode('Pat_'+key+'.jpg',qrdata[key])
    
gen_qrcode('zxm.jpg','http://pacs.winning.com.cn/pat_test/recorddemo/record?reportid=55c027dba47e73282221ff29')    