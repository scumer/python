# coding=utf-8

import base64
from Crypto.Cipher import AES
from wechatpy.crypto.pkcs7 import PKCS7Encoder

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


print EncryptConf().decrypt('AkqaWSyrQWkeQBCtNIA9uT/BTgFXLaymmFoVhnjht9U=\n')