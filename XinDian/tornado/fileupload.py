# coding=utf-8

import requests
import json

url = 'http://127.0.0.1:9000/upload/film'
film_name = 'config.ini'
film_name = '280.dcm'

data = {'film':'val','a':'b'}

# ret = requests.post(url,data=json.dumps(data))
# ret = requests.post(url,data="{'film':'val','a':'b'}")
header = {'Content-Type':'multipart/form-data', }

files = {'filmdata':(film_name,open(film_name,'rb'),'application/octet-stream')}

# ret = requests.post(url,data=data, headers = header)
ret = requests.post(url,data=data,files=files)

# print ret.__dict__
print ret, ret.text