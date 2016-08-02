# coding=utf-8


import requests

url = 'http://localhost:8000/wrap'
data = {'text':'abcdefg 1cb c+d+3', 'width':'10'}
ret = requests.post(url, data=data, headers = header)
print ret.status_code

print ret.text