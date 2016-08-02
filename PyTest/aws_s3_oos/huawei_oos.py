# coding=utf-8

import hashlib
import urllib
import hmac
import base64
import requests
from datetime import datetime

ak = '43e9ab6b7d0bc4b5e609'
sk = '86ef19440d578b2dfd7a3e66701aad501dcd6e0c'

"""
客户端发送的消息头需要包含由SK、请求时间、请求类型等信息生成的鉴权信息
在进行鉴权之前，需要对桶名，对象名单独进行URLEncode编码，再生成鉴权信息

"""

# StringToSign = HTTP-Verb + "\n" + Content-MD5 + "\n" + Content-Type + "\n" + Date + "\n" + CanonicalizedHeaders + CanonicalizedResource



data = file('1.html').read()
data = ''
m5 = hashlib.md5()
m5.update(data)
data_m5 = m5.hexdigest()
data_b64m5 =  base64.b64encode(data_m5)
# data_b64m5 = ''
# print data_b64m5

content_type = 'text/plain'
http_verb = 'PUT'

_date = datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
# print _date

x_amz_acl = 'x-amz-acl:public-read-write'
resource = '/dicomimage2/'

x_amz_date = 'x-amz-date:'+_date
string_to_sign = http_verb + '\n' + '\n' +'\n' +_date +'\n'+ resource #x_amz_acl + '\n' +
# print string_to_sign

signature =  hmac.new(sk.encode('utf-8'),string_to_sign.encode('utf-8'),hashlib.sha1).digest().encode('base64').rstrip()
# print signature


auth = 'AWS {0}:{1}'.format(ak, signature)
header = {'Authorization': auth, 'Date':_date}


url = 'http://192.168.2.253:80' + resource
#ret = requests.put(url, headers = header)
#print ret,ret.text


def create_bucket(url='http://192.168.2.253:80',bucket='dicomimage2'):
	verb = 'PUT'
	cnt_type = ''
	data_b64m5 = ''
	dt = datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
	rs = '/'+bucket

	string_to_sign = '{_verb}\n{_data}\n{_type}\n{_date}\n{_resource}'.format(_verb=verb,_data=data_b64m5,_type=cnt_type, _date=dt, _resource=rs)
	print string_to_sign

	signature =  hmac.new(sk.encode('utf-8'),string_to_sign.encode('utf-8'),hashlib.sha1).digest().encode('base64').rstrip()

	auth = 'AWS {0}:{1}'.format(ak, signature)
	header = {'Authorization': auth, 'Date':_date}
	ret = requests.put(url+'/'+bucket, headers = header)
	print ret,ret.text


def create_bucket_DX(url='http://oos-fj.ctyunapi.cn',bucket='xuhui-dicomimage22'):
	verb = 'PUT'
	cnt_type = ''
	data_b64m5 = ''
	dt = datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
	dt = 'Wed, 06 Jul 2016 01:43:02 GMT'

	rs = '/'+bucket+'/'

	string_to_sign = '{_verb}\n{_data}\n{_type}\n{_date}\n{_resource}'.format(_verb=verb,_data=data_b64m5,_type=cnt_type, _date=dt, _resource=rs)
	print string_to_sign

	signature =  hmac.new(sk.encode('utf-8'),string_to_sign.encode('utf-8'),hashlib.sha1).digest().encode('base64').rstrip()

	auth = 'AWS {0}:{1}'.format(ak, signature)
	header = {'Authorization': auth, 'Date':dt}
	ret = requests.put('http://xuhui-dicomimage22.oos-fj.ctyunapi.cn', headers = header)
	print ret,ret.text

create_bucket_DX()


def get_all_buckets(url = 'http://192.168.2.253:80'):
	resource = '/'
	string_to_sign = 'GET' + '\n' +'\n' +'\n' +_date + '\n' + resource #x_amz_acl + '\n' + 
	print string_to_sign
	signature =  hmac.new(sk.encode('utf-8'),string_to_sign.encode('utf-8'),hashlib.sha1).digest().encode('base64').rstrip()
	auth = 'AWS {0}:{1}'.format(ak, signature)
	header = {'Authorization': auth, 'Date':_date}
	ret = requests.get(url, headers = header, data=data)
	print ret
	print ret.text

# get_all_buckets()




def upload_file(url='http://192.168.2.253:80',filename='oos.txt',resource = '/dicomimage2/uploadtest'):
	"""
	PUT
	q10cSgtI/IjDlRfZqEWG5w==
	text/plain
	Sun, 12 Jun 2016 16:32:44 GMT
	/xuhui-dicomimage2/foobar
	"""
	verb = 'PUT'
	
	cnt_type = 'text/plain'
	dt = datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
	rs = resource
	
	data = file(filename).read()
	m5 = hashlib.md5()   
	m5.update(data)   
	data_m5 = m5.digest()
	data_b64m5 =  base64.b64encode(data_m5)


	string_to_sign = '{_verb}\n{_data}\n{_type}\n{_date}\n{_resource}'.format(_verb=verb,_data=data_b64m5,_type=cnt_type, _date=dt, _resource=rs)
	print string_to_sign

	signature =  hmac.new(sk.encode('utf-8'),string_to_sign.encode('utf-8'),hashlib.sha1).digest().encode('base64').rstrip()

	auth = 'AWS {0}:{1}'.format(ak, signature)
	header = {'Authorization': auth, 'Date':_date, 'Content-Type':cnt_type, 'Content-MD5': data_b64m5}
	ret = requests.put(url+ resource, headers = header, data=data)
	print ret,ret.text

	
#upload_file()






