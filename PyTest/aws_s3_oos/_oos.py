# coding=utf-8

import hashlib
import urllib
import hmac
import base64
import requests
from datetime import datetime

ak = 'CD5E0C8514658FD6A8B0'
sk = 'Sp/J9+KMxZYgLKwu4/Jeua4b2ScAAAFVFGWP1rH1'

ak = 'AKIAJRWHHEK76NKTORWQ'
sk = 'G/36E6c7bVaSWDnLtHvzudTRRoSVh5YPSZQ96RCf'

"""
客户端发送的消息头需要包含由SK、请求时间、请求类型等信息生成的鉴权信息
在进行鉴权之前，需要对桶名，对象名单独进行URLEncode编码，再生成鉴权信息

"""

# StringToSign = HTTP-Verb + "\n" + Content-MD5 + "\n" + Content-Type + "\n" + Date + "\n" + CanonicalizedHeaders + CanonicalizedResource



data = file('oos.txt').read()
m5 = hashlib.md5()   
m5.update(data)   
data_m5 = m5.digest()
data_b64m5 =  base64.b64encode(data_m5)

content_type = 'text/plain'
http_verb = 'PUT'

_date = datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')

x_amz_acl = 'x-amz-acl:public-write'
resource = '/xuhui-dicomimage2/uploadtest'

x_amz_date = 'x-amz-date:'+_date
string_to_sign = http_verb + '\n' +content_type+'\n' +data_b64m5+'\n' +_date +'\n'+ x_amz_acl + '\n' + resource #x_amz_acl + '\n' + 
print string_to_sign

signature =  hmac.new(sk.encode('utf-8'),string_to_sign.encode('utf-8'),hashlib.sha1).digest().encode('base64').rstrip()
# print signature


auth = 'AWS {0}:{1}'.format(ak, signature)
header = {'Authorization': auth, 'Date':_date, 'Content-Type':content_type}


url = 'http://s3.amazonaws.com'+resource
# ret = requests.put(url, headers = header, data=data)
# print ret
# print ret.text


def upload_file(url='http://xuhui-dicomimage2.s3.amazonaws.com',filename='test.dcm',bucket = 'xuhui-dicomimage2', key='dicom1'):
	"""
	PUT
	q10cSgtI/IjDlRfZqEWG5w==
	text/plain
	Sun, 12 Jun 2016 16:32:44 GMT
	/xuhui-dicomimage2/foobar
	"""
	verb = 'PUT'
	
	cnt_type = 'application/dicom'
	dt = datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
	rs = '/'+bucket+'/'+key
	
	# data = file(filename).read()
	fp = open(filename,'rb')
	data = fp.read()
	fp.close()
	m5 = hashlib.md5()   
	m5.update(data)   
	data_m5 = m5.digest()
	data_b64m5 =  base64.b64encode(data_m5)


	string_to_sign = '{_verb}\n{_data}\n{_type}\n{_date}\n{_resource}'.format(_verb=verb,_data=data_b64m5,_type=cnt_type, _date=dt, _resource=rs)
	# print string_to_sign

	signature =  hmac.new(sk.encode('utf-8'),string_to_sign.encode('utf-8'),hashlib.sha1).digest().encode('base64').rstrip()

	# auth = 'AWS {0}:{1}'.format(ak, signature)
	# header = {'Authorization': auth, 'Date':_date, 'Content-Type':cnt_type, 'Content-MD5': data_b64m5}
	# ret = requests.put(url+'/'+key, headers = header, data=data)
	# print ret,ret.text


# upload_file()


def get_all_buckets(url = 'http://s3.amazonaws.com'):
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


def download(url = 'http://xuhui-dicomimage2.s3.amazonaws.com/dicom1'):
	"""
	GET


	Tue, 21 Jun 2016 05:51:01 GMT

	:param url:
	:return:
	"""

	resource = '/xuhui-dicomimage2/dicom1'
	string_to_sign = 'GET' + '\n' +'\n' +'\n' +_date + '\n' + resource #x_amz_acl + '\n' +
	print string_to_sign
	signature =  hmac.new(sk.encode('utf-8'),string_to_sign.encode('utf-8'),hashlib.sha1).digest().encode('base64').rstrip()
	auth = 'AWS {0}:{1}'.format(ak, signature)
	header = {'Authorization': auth, 'Date':_date}
	ret = requests.get(url, headers = header, data=data)
	print ret
	# print ret.content
	fp = open('my_down_dcm.dcm','wb')
	fp.write(ret.content)
	fp.close()
download()