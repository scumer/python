# coding=utf-8
from app.model import *
import json
import traceback
import time
from flask import jsonify
from flask import current_app
#from app.model import
execfile('index_platform_test.wsgi')
from utility import makeQR
#['杨素芳','425016155','P22580773','女','021'],
#['张维银','425016155','143608300439612','男','021'],
pat = [
[u'杨素芳','425016155','P22580773',u'女','021'],
[u'张维银','425016155','143608300439612',u'男','021'],    
[u'储梅芳','425016155','P02367684',u'女','021'],
[u'荣增光','425016155','P0247288X',u'男','021'],
[u'戴影','425016155','P12353710',u'女','021'],
[u'黄荣毅','425016155','P08660363',u'男','021'],
[u'黄雅珍','425016155','143608300466898',u'女','021'],
[u'杨美玲','425016155','143608300466259',u'女','021'],
[u'徐金娣','425016155','P22553943',u'女','021'],
[u'彭贵友','425016155','143608300439722',u'男','021'],
[u'秦银女','425016155','P04432435',u'女','021'],
[u'朱锦成','425016155','5003273834',u'男','021'],
[u'马小妹','425016155','K01341697',u'女','021']
]

#card = MedicalCard.objects(cardNo='5002258288170919552975110144').first()

#makeQR.py -cc 123
#['-cc', '123']



for p in pat:
    print p[0]
    argv = ['-city',p[4],'-hosp',p[1],'-c',p[2],'-n',p[0],'-s',p[3],'-o',p[0]+'.jpg']
    print argv
    #makeQR.cmd_main(argv)
    
    bind = {
        'cc': p[4],
        'h': [1],
        'cn': p[2],
        'n': p[0],
        's': p[3]
    }
    makeQR.make_qr(makeQR.gen_bind_url_redirect(bind), p[0]+p[2]+'.jpg')    
    
#makeQR.cmd_main(argv)
