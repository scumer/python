# coding=utf-8
from __future__ import unicode_literals
import requests
import json


url = 'http://139.196.167.82/wechat'
url = 'http://127.0.0.1:6234/wechat?signature=d082b9911b051e73ffc69c9080ff25e2718fa0cf&timestamp=1464602899&nonce=835732096'
url = 'http://139.196.167.82/wechat'
url = 'http://127.0.0.1:6234'
url = 'http://139.196.167.82'

auth_token = 'WyI1NzRjZjZjOTE0YzEzNDBjYTY2ODljZmUiLCJkNDFkOGNkOThmMDBiMjA0ZTk4MDA5OThlY2Y4NDI3ZSJd.Ci6UNA.ipVFL5TBPoEsvOa1ziVr-y-1Ynw'
auth_token = 'WyI1NzRjZWJmNDZjNjI3MjFhNTQ2MWJiZmQiLCJkNDFkOGNkOThmMDBiMjA0ZTk4MDA5OThlY2Y4NDI3ZSJd.CjVXrQ.OHOC-5co9FQXUluYJ9uEgr8ZDC8' #feihui
auth_token = 'WyI1NzRjZWJmNDZjNjI3MjFhNTQ2MWJiZmQiLCJkNDFkOGNkOThmMDBiMjA0ZTk4MDA5OThlY2Y4NDI3ZSJd.CnIW0A.xl-V4sEJffsI2gijqIx_acBLap8' #feihui
# auth_token = 'WyI1NzRiZmYyNTZjNjI3MjA4NTBmOGQyZjYiLCJkNDFkOGNkOThmMDBiMjA0ZTk4MDA5OThlY2Y4NDI3ZSJd.Cni3AQ.HUSA4GzvUcHcagnpw9YmALrvLH8' #xuhui

header = {'Authentication':auth_token}

def repr_dict(d):
    return '{%s}' % ',\n'.join("'%s': '%s'" % pair for pair in d.iteritems())

def exec_api(api,data=None):
    try:
        ret = requests.get(url+api, json=data, headers=header)
        print '\napi:',api
        ret.raise_for_status()
        print json.dumps(ret.json(), ensure_ascii=False, indent=2) if ret.json() else 'No Json Result!'
    except Exception, e:
        print e

header = {'Authentication':auth_token}



#unbind
api = '/wechat/card/unbind'
query = {'citycode':'021', 'cardno':'123', 'name':u'解绑', 'sex':u'男'}

# ret = requests.post(url+api, json=query)
# print json.dumps(ret.json(), ensure_ascii=False, indent=2) if ret.json() else 'No Json Result!'


# ret = requests.post(url+api, data=query, headers=header)
# print '\napi:\n',api,'\n', ret, '\n' ,ret.text

# /api/card/query
api = '/api/card/query'
query={'query':{'cityCode':'021',},'skip': 40,'number': 50}
# exec_api(api,query)


api = '/api/card/user'
# exec_api(api)

api = '/api/report/card/user'

# /api//card/user
api = '/api/card/user'
# exec_api(api)


# /api/card/<string:id>
cardid = '55c0288ea47e73282221ff3e'  #Ris
api = '/api/card/'+cardid
# exec_api(api)


# /api/report/query
cardid = '55c0288ea47e73282221ff35' #Ris
api = '/api/report/query/'+cardid
# query={'card':cardid}
exec_api(api)


#/api/report/<cardid>

# cardid = '55938b28a47e733c4e1ad40e' #Us
api = '/api/report/query'
# query={'query':{'card':cardid}}
# exec_api(api,query)


#/api/report/<cardid>
cardid = '57046490d52c9e2e606bf516'

#/api/report/<cardid>
cardid = '57046490d52c9e2e606bf516'
# cardid = '55c02447a47e73282221fed6' #   feihui

api = '/api/report/query/' + cardid
# exec_api(api,query)



# /api/report/<reportid>

# reportid = '55938c04a47e733c4e1ad410' # US
api = '/api/report/'+reportid
# exec_api(api)

#/api/queue/query
cardid = '55c0288ea47e73282221ff3e' #Ris
api = '/api/queue/query'

query={'query':{'card':cardid}}

# query={'query':{'card':cardid}}


# query={'query':{'card':cardid}}
# exec_api(api, query)

#/api/queue/<queue_id>
queueid = '55bec9ada47e732ced6512d5' #Ris
api = '/api/queue/'+queueid
# exec_api(api, query)


#/api/queue/user
api = '/api/queue/user'
# exec_api(api, query)

#/api/film/
reportid = '55c02940a47e73282221ff52'
api = '/api/film/'+reportid
# exec_api(api, query)
# "objectUID": "1.3.6.1.4.1.19439.2.100001.100001.20150803102324.1012044", 
# "seriesUID": "1.2.840.1.4.1.194.1.100000000.20150803102408.1527", 
# "studyUID": "1.2.840.113619.2.334.3.2831199747.915.1437875346.418"


#/api/film/<reportid>/<studyUID>/<seriesUID>/<objectUID>
reportid = '55c02940a47e73282221ff52'
uid = {
"objectUID": "1.3.6.1.4.1.19439.2.100001.100001.20150803102324.1012044", 
"seriesUID": "1.2.840.1.4.1.194.1.100000000.20150803102408.1527", 
"studyUID": "1.2.840.113619.2.334.3.2831199747.915.1437875346.418"
}
api = '/api/film/{0}/{1}/{2}/{3}'.format(reportid,uid['studyUID'],uid['seriesUID'],uid['objectUID'])
# exec_api(api)



# /api/code/bar/<code>
code = '188888888'
api = '/api/code/bar/' + code
# /api/code/qr/study/<reportid>

#/api/report/png/<reportid>

# 第三方调用报告

HTTP_REFERER = ''

url = 'http://pacs.winning.com.cn/embedded/'
# url = 'http://pacs.winning.com.cn/embedded/lis/42500982800/Q17534710'


report_type = 'all'
report_type = 'lis'


# url = url + report_type+'/42500982800/Q17534710'
# # header = {'referer':'http://www.glhospital.com:8082'}
# header = {'referer':'http://shggwslczx.hm.guahao.com/'}
# ret = requests.get(url, headers=header)
# print ret
# # print ret.text

# import codecs
# file =codecs.open('report.html','w',"utf-8")
# file.write(ret.text, )
# file.close()






# hosp = '425016155'
# studyuid = '1.2.840.1.4.1.194.0.100000000.20151020151048.1747.10000.2624204'
# view_type = 'pc'
# url = 'http://pacs.winning.com.cn/pat_test'+'/tcloud/' + hosp + '/' +view_type+ '/' + studyuid
# url = 'http://pacs.winning.com.cn/tcloud/425016155/webview/1.2.840.113704.1.111.5132.1436470478.1'
# print url
# ret = requests.get(url)
# print ret
# print ret.text


hosp = '425016155'
studyuid = '1.2.840.1.4.1.194.0.100000000.20151020151048.1747.10000.2624204'
view_type = 'pc'
url = 'http://pacs.winning.com.cn/pat_test'+'/tcloud/' + hosp + '/' +view_type+ '/' + studyuid
url = 'http://pacs.winning.com.cn/tcloud/425016155/webview/1.2.840.113704.1.111.5132.1436470478.1'
print url
ret = requests.get(url)
print ret
print ret.text


