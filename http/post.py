# coding=utf-8
import requests
from requests import exceptions

content = {
    "studyUID":"1.3.6.1.4.1.19439.0.108707908.20150616152659.17.14764522",
    "films":[
        {
            "studyUID":"1.3.6.1.4.1.19439.0.108707908.20150616152659.17.14764522",
            "seriesUID":"1.3.46.670589.30.1.6.1.966169198450.1434466000687.1",
            "objectUID":"1.3.46.670589.30.1.6.966169198450.1.2408.1434466002187"
        },
        {
            "studyUID":"1.3.6.1.4.1.19439.0.108707908.20150616152659.17.14764522",
            "seriesUID":"1.3.46.670589.30.1.6.1.966169198450.1434466001593.1",
            "objectUID":"1.3.46.670589.30.1.6.966169198450.1.2408.1434466003453"
        },
        {
            "studyUID":"1.3.6.1.4.1.19439.0.108707908.20150616152659.17.14764522",
            "seriesUID":"1.3.46.670589.30.1.6.1.966169198450.1434466002390.1",
            "objectUID":"1.3.46.670589.30.1.6.966169198450.1.2408.1434466005015"
        },
        {
            "studyUID":"1.3.6.1.4.1.19439.0.108707908.20150616152659.17.14764522",
            "seriesUID":"1.3.46.670589.30.1.6.1.966169198450.1434466003468.1",
            "objectUID":"1.3.46.670589.30.1.6.966169198450.1.2408.1434466005984"
        }        
    ]
}
import dicttoxml

import dict2xml


# url = r'http://101.231.40.242:7345/pem/service.asmx/psp_LoginEx'
url = r'http://180.166.22.190:30800//PEM/service.asmx/psp_LoginEx'
url = r'http://101.231.40.242:7345/pem/service.asmx/psp_LoginEx'
url = r'http://101.231.40.242:7345/pem/service.asmx/psp_ExecuteSQL'

header = {'Content-Disposition': 'form-data'}
# content = {'i_sUserName': '001', 'i_sPassword': '001'}
content = {'SQLString': 'select top 2 * from pacs_study where studyid=1'}

# ret = requests.post("http://pacs.winning.com.cn/xuhui/dingdang", json=content)
# ret = requests.post(url, files=content, headers=header)
ret = requests.post(url, data=content, headers=header)
print ret.content

import HTMLParser
html_parser = HTMLParser.HTMLParser()
print ret
#
print html_parser.unescape(ret.text)

# print unicode(ret.content)
# try:
#     ret = requests.get('http://github.com', timeout=0.001)
#     print ret.text
# except exceptions.ConnectionError, e:
#     print e.message

