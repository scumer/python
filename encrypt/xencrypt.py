# coding=utf-8

import os
import json
import urllib
import base64
import qrcode as qr
from Crypto.Cipher import AES
from wechatpy.crypto.pkcs7 import PKCS7Encoder

url_prefix = r'http://pacs.winning.com.cn/scan/bind?card='

key = 'WinningSoftPACSFilmReportService'
aes = AES.new(key[:16], mode=AES.MODE_ECB)
print PKCS7Encoder.encode('')
print base64.encodestring(aes.encrypt(PKCS7Encoder.encode('123')))


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

    @classmethod
    def encryptEx(cls, string):
        aes = AES.new(cls.key[:16], mode=AES.MODE_ECB)
        return base64.urlsafe_b64encode(aes.encrypt(PKCS7Encoder.encode(string)))

    @classmethod
    def decryptEx(cls, string):
        aes = AES.new(cls.key[:16], mode=AES.MODE_ECB)
        return PKCS7Encoder.urlsafe_b64decode(aes.decrypt(base64.decodestring(string)))

# print EncryptConf.encrypt('xuhui')
# print EncryptConf.decrypt('QELSR9Y+awWD1xQwdh0uJYHLHELppUpQ7Zxq0aqKnj8=')

bind_info = {'cc': '021', 'h': '42502634500', 's': u'\u7537', 'cn': '133012001177680', 'n': u'\u5e2d\u7965\u592a'}
# print urllib.quote(EncryptConf.encrypt(json.dumps(bind_info)))
# print EncryptConf.encrypt(json.dumps(bind_info))

# print urllib.quote(EncryptConf.encryptEx(json.dumps(bind_info)))
# print EncryptConf.encryptEx(json.dumps(bind_info))