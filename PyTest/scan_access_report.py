#coding=utf-8

from qrcode import QRCode
from StringIO import StringIO
from Crypto.Cipher import AES
from wechatpy.crypto.pkcs7 import PKCS7Encoder
import base64
import json
from urllib import quote   
#fp.close()

def gen_qrcode_b(name, data):
    fp = open(name, 'w')
    #qr = qrcode.QRCode( version=1,  error_correction=level, box_size=1,border=1)
    gen = QRCode()
    gen.add_data(data)
    gen.make(fit=True)
    img = gen.make_image()
    io = StringIO()    
    img.save(fp)
    fp.close()

def gen_qrcode(img_file, data):
    print data
    gen = QRCode()
    gen.add_data(data)
    img = gen.make_image()
    img.save(img_file)
    

class EncryptConf(object):
    key = 'WinningSoftPACSFilmReportService'

    @classmethod
    def encrypt(cls, string):
        aes = AES.new(cls.key[:16], mode=AES.MODE_ECB)
        return base64.encodestring(aes.encrypt(PKCS7Encoder.encode(string)))

    @classmethod
    def decrypt(cls, string):
        aes = AES.new(cls.key[:16], mode=AES.MODE_ECB)
        return PKCS7Encoder.decode(aes.decrypt(base64.decodestring(string)))

str = '9X56TdK2c3T+0U/GhdXmkqCE6CXviMmybYVyx5vlU+I='
str= '7wzZeUb/qpIh1sFvNP7TJ6CE6CXviMmybYVyx5vlU+I='
print EncryptConf().decrypt(str)

cnt = {'ao':'15490620','cn':'01196113','cc':'0571','h':'425054397','n':u'高剑','s':u'男'}
cnt = {'ao':'15490620','cn':'D1661372XXX','cc':'021','h':'425054397','n':u'陆悠','s':u'女'}
data = EncryptConf().encrypt(json.dumps(cnt))
print data
# print EncryptConf().decrypt(data)
#url = 'http://192.168.3.3:801/scan/report?info='+quote(data)
url = 'http://vwraieoyhh.proxy.qqbrowser.cc/scan/report?info='+quote(data)
url = 'http://192.168.33.189:6234/scan/report?info='+quote(data)
# url = 'http://192.168.33.189:6234/scan/report?info='+(data)


print url
gen_qrcode('report.png',url)  


data = u'''BEGIN:VCARD
N:Gump;Forrest;;;
FN:Forrest Gump
ORG:Bubba Gump Shrimp Co.
TITLE:Shrimp Man
TEL;TYPE=work,voice;VALUE=uri:tel:+11115551212
TEL;TYPE=home,voice;VALUE=uri:tel:+14045551212
ADR;TYPE=work;LABEL="100 Waters Edge\nBaytown, LA 30314\nUnited States of A
 merica":;;100 Waters Edge;Baytown;LA;30314;United States of America
ADR;TYPE=home;LABEL="42 Plantation St.\nBaytown, LA 30314\nUnited States of
 America":;;42 Plantation St.;Baytown;LA;30314;United States of America
EMAIL:forrestgump@example.com
END:VCARD'''
# gen_qrcode('card.jpg',data)


