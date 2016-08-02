# coding=utf-8

import json
import requests

debug = 1
#139.196.167.219 测试
#139.196.168.120 平台
server_platform = '139.196.168.120'
server_test = '139.196.167.219'
server_local = '127.0.0.1'
server_yanyan = '139.196.57.2/pat_test'

cnt = {'name':'test','employeeNo':'1234'}
if debug == 1:
    ret = requests.post('http://'+server_yanyan+'/tools/employee/record', json=(cnt))
    print ret.content
elif debug == 0:
    url = 'http://'+server_test+'/ris/message_notice?cnt=' + json.dumps(cnt)
    print url
    ret = requests.get(url)
    print ret.content    
