# coding=utf-8
import os
import json
import urllib
import base64
import qrcode as qr
from Crypto.Cipher import AES
from wechatpy.crypto.pkcs7 import PKCS7Encoder

url_prefix = r'http://pacs.winning.com.cn/pat_test/scan/bind?card='
# url_prefix = r'http://pacs.winning.com.cn/pat_test/scan/bind?card='


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


def gen_bind_url_redirect(bind_info):
    return url_prefix + urllib.quote(EncryptConf.encrypt(json.dumps(bind_info)))

def make_qr(data, img_file):
    print data
    gen = qr.QRCode()
    gen.add_data(data)
    img = gen.make_image()
    img.save(img_file)


def gen_qrcode(pat):
    if not os.path.exists('./qrcode'):
        os.mkdir('qrcode')

    for p in pat:
        # print p[0],
        # argv = ['-city',p[4],'-hosp',p[1],'-c',p[2],'-n',p[0],'-s',p[3],'-o',p[0]+'.jpg']
        # print argv

        bind = {
            'cc': p[4],
            'h': p[1],
            'cn': p[2],
            'n': p[0],
            's': p[3]
        }
        print bind
        # print json.dumps(bind)
        make_qr(gen_bind_url_redirect(bind), u'./qrcode/{0}.jpg'.format(bind['n'] + bind['cn']))


pat = [
[u'杨素芳','425016155','P22580773',u'女','021'],
]

pat = [
[u'田旭东','425016155','143608300447902',u'男','021'],
]
'''
ex:
http://pacs.winning.com.cn/scan/bind?
card=LhXcWbmhZW/yCG4%2B1CmJTAPLc1a4f2jPP52QUmnbfwL6lmwIG6LVkSKGhVVHtTcEpELYzyuePIIy%0ApIsKmGYszmP0JkjIO5xj16vS4SxFJ48FzQeo1mRUGLRYGq3mUCSv%0A
card=LhXcWbmhZW/yCG4%2B1CmJTAmmKPbB8kYJOx7Zggj5942Zj%2BWHrN1i4%2B6BDY45kpBkX%2BN7nOp6aYRY%0AoTZeGHst7ZbLwQpT/XVXbdbL2guMpl4mwoR%2BN/5KkSDP1Q0WlA3juLlQX21mSOSUnPGh72lNf/l2%0AMgKDRt8h00DM3XQZCfw%3D%0A
'''
gen_qrcode(pat)

