# coding=utf-8

import json
import requests

debug = -1
#139.196.167.219 测试
#139.196.168.120 平台
server_platform = '139.196.168.120'
server_test = '139.196.167.219'
server_local = '127.0.0.1'
server_yanyan = '139.196.57.2/pat_test'


#openid o0WQ1uE3CvBjh-8a9LFC45ximYEI
#PushType':'20', 'PatName':u'刘朝芳', 'SexName':'女', 'CityCode':'021', 'CardNo':'133009002463167'
#cnt = {'PushType':'10', 'PatName':u'刘朝芳', 'SexName':'女', 'CityCode':'021', 'CardNo':'133009002463167',
#cnt = {'PushType':'20', 'PatName':u'周建明', 'SexName':'男', 'CityCode':'021', 'CardNo':'K029420489',
#{'PushType':'20', 'PatName':u'夏其富', 'SexName':'男', 'CityCode':'021', 'CardNo':'K05115005',

cnt =  {'PushType':'20', 'PatName':u'刘朝芳', 'SexName':'女', 'CityCode':'021', 'CardNo':'133009002463167',
       'ApplyNo':'12345',
       'PushSign':'1',
       'Title':u'title',
       'QueuePre':u'平扫',
       'BookTime':'2016-03-15 11:11:11',
       'ExamName':'MR',
       'TipMsg':u'此处填写提示语句',
       'RegTime':'2016-03-15 11:11:11',
       'HospitalName':u'上海市第六人民医院',
       'QueueNo':u'平扫009',
       'CurQueueNo':'2',
       'TechNo':'12345',
       'ExamItems':'CT胸部平扫',
       'ExamTime':'2011-11-11',
       'LabelID':'A102615537',
       'CurWaitTime':'12',
       'HospitalCode':'425026521',
       'YYZYSX':u"""1、5Cu3001本设备具有强磁场，如装有心脏起搏器，或体内有金属或磁性物体植入史和早期妊娠的病人不能进行检查 ，请告知医师，以免发生意外。\n
       2、病人请勿穿戴任何有金属物的内衣，检查头、颈部的病人请在检查前日洗头，勿擦头油。 \n"""}
#{"PushType":"20","PatName":u"微信001","SexName":u"男",'CityCode':'021',"CardNo":"A20151227",
cnt2 = {"PushType":"25","PatName":u"微信001","SexName":u"男",'CityCode':'021',"CardNo":"A20151227",
    "AgeUnit":u"岁    ","ExamItems":"",
       "TechNo":"3408872","Age":"25","QueueNo":u"增强027",
       "RegTime":"2015/12/27","SubSysCode":"RIS_FS","CurWaitTime":u"30分钟",
       "CityCode":"021","BookTime":"","LabelID":"123456789A","Remark":"",
       "Title":u"市六医院放射科,微信001,25.00,岁    ,男,2015/12/27,3408872,,123456789A,6",
       u"TipMsg":"注意叫号屏及声音提示，过号请携带此叫号单重新取号。","ExamTime":"","ExamRoom":u"CT1号机房",
       "ExamName":"CT","ExamCode":"CT","WardOrReg":u"门诊","CurQueueNo":u"增强019","HospitalName":u"上海市第六人民医院","HospitalCode":""}


if debug == 1:
    ret = requests.post(r'http://medical-tech.winning.com.cn/platform/ris/message', json=(cnt))
    print ret.content
elif debug == 0:
    url = 'http://'+server_test+'/ris/message_notice?cnt=' + json.dumps(cnt)
    print url
    ret = requests.get(url)
    print ret.content    



inf = {"studyUID":"1.2.86.76547135.7.3626529.20160318104226",
       "PatName":"3354663/Wang Xiao Hui","PatID":"3705751","PatSex":"M","PatAge":"028Y",
       "AccessionNo":"3354663","HospCode":"470003265",
       "films":[{"studyUID":"1.2.86.76547135.7.3626529.20160318104226",
                 "seriesUID":"1.3.12.2.1107.5.1.4.51968.30000016031700073412500000177",
                 "objectUID":"1.3.12.2.1107.5.1.4.51968.30000016031623525646800011219"}]} 
"""
inf = {"studyUID":"1.2.826.0.1.3680043.8.920.132.64.120160314131704",
       "PatName":"ChenChunSheng","PatID":"G01373884","PatSex":"M","PatAge":"077Y",
       "AccessionNo":"AN16031400640253","HospCode":"42501068500",
       "films":[{"studyUID":"1.2.826.0.1.3680043.8.920.132.64.120160314131704",
                 "seriesUID":"1.2.840.113619.2.55.3.2831161140.850.1457349289.128",
                 "objectUID":"1.2.840.113619.2.55.3.2831161140.850.1457349289.129.1"}]}
inf = {"studyUID":"1.2.826.0.1.3680043.8.920.132.762.120160311090547",
       "PatName":"XuPengQiang","PatID":"136401900131919","PatSex":"M","PatAge":"033Y",
       "AccessionNo":"AN16031107620033","HospCode":"42501068500",
       "films":[{"studyUID":"1.2.826.0.1.3680043.8.920.132.762.120160311090547",
                 "seriesUID":"1.2.392.200046.100.2.1.69132726935.160311094120.1",
                 "objectUID":"1.2.392.200046.100.2.1.69132726935.160311094120.1.1.2"}]} 
inf = {"studyUID":"1.2.826.0.1.3680043.8.920.132.64.120160311171500",
       "PatName":"LiShuJun","PatID":"7100195332","PatSex":"M","PatAge":"061Y",
       "AccessionNo":"AN16031100640461","HospCode":"42501068500",
       "films":[{"studyUID":"1.2.826.0.1.3680043.8.920.132.64.120160311171500",
                 "seriesUID":"1.3.12.2.1107.5.2.36.40752.2016031117463940710813099.0.0.0",
                 "objectUID":"1.3.12.2.1107.5.2.36.40752.2016031117465128302213115"}]}

inf = {"studyUID":"1.2.826.0.1.3680043.8.920.132.762.120160311090547",
       "PatName":"XiongHongZhen","PatID":"7100070076","PatSex":"F","PatAge":"064Y",
       "AccessionNo":"AN16031400640251",
       "HospCode":"42501068500",
       "films":[{"studyUID":"1.2.826.0.1.3680043.8.920.132.64.120160314131545",
                 "seriesUID":"1.2.840.113619.2.55.3.2831161140.850.1457349289.52",
                 "objectUID":"1.2.840.113619.2.55.3.2831161140.850.1457349289.53.12"}]}                  
inf = {"studyUID":"1.2.826.0.1.3680043.8.920.132.762.120160311090547",
       "PatName":"LiuPeiYue","PatID":"136401900131991","PatSex":"F","PatAge":"025Y",
       "AccessionNo":"AN16031207620014",
       "HospCode":"42501068500",
       "films":[{"studyUID":"1.2.826.0.1.3680043.8.920.132.762.120160312075512",
                 "seriesUID":"1.2.392.200046.100.2.1.69132726935.160312083049.1",
                 "objectUID":"1.2.392.200046.100.2.1.69132726935.160312083049.1.1.2"}]}    

inf = {"studyUID":"1.2.826.0.1.3680043.8.920.132.64.120160316114801",
       "PatName":"ChenWeiBi","PatID":"00004651","PatSex":"F","PatAge":"063Y",
       "AccessionNo":"AN16031600640225","HospCode":"42501068500",
       "films":[{"studyUID":"1.2.826.0.1.3680043.8.920.132.64.120160316114801",
                 "seriesUID":"1.3.46.670589.11.42555.5.0.2236.2016031611543011071",
                 "objectUID":"1.3.46.670589.11.42555.5.0.2236.2016031611544299074"}]} 
                 
"""
inf = {"studyUID":"1.2.840.113619.2.340.3.2831175791.268.1462838474.208","PatName":"XIXIANGTAI","PatID":"LH00025536","PatSex":"M","PatAge":"061Y","AccessionNo":"1000059981","HospCode":"42502634500","films":[{"studyUID":"1.2.840.113619.2.340.3.2831175791.268.1462838474.208","seriesUID":"1.2.840.1.19439.1.100000000.20160511123740.1253","objectUID":"1.2.840.2.1000001.1000001.20160511123740.1013931"},{"studyUID":"1.2.840.113619.2.340.3.2831175791.268.1462838474.208","seriesUID":"1.2.840.1.19439.1.100000000.20160511123740.1253","objectUID":"1.2.840.2.1000001.1000001.20160511123742.1026308"}]}

inf = {
  "HospCode": "425026521", 
  "PatAge": "064Y", 
  "PatID": "00003542", 
  "PatName": "PANWEIGUI", 
  "films": [
    {
      "objectUID": "1.2.840.2.1000001.1000001.20160616145707.1000041", 
      "seriesUID": "1.2.840.1.19439.1.100000000.20160307145339.1733", 
      "studyUID": "1.2.840.1.19439.0.100000000.20150421094558.1517.10000.62502"
    }, 
    {
      "objectUID": "1.2.840.2.1000001.1000001.20160616145709.1018467", 
      "seriesUID": "1.2.840.1.19439.1.100000000.20160307145339.1733", 
      "studyUID": "1.2.840.1.19439.0.100000000.20150421094558.1517.10000.62502"
    }, 
    {
      "objectUID": "1.2.840.2.1000001.1000001.20160616145711.1006334", 
      "seriesUID": "1.2.840.1.19439.1.100000000.20160307145339.1733", 
      "studyUID": "1.2.840.1.19439.0.100000000.20150421094558.1517.10000.62502"
    }
  ], 
  "PatSex": "M", 
  "AccessionNo": "", 
  "studyUID": "1.2.840.1.19439.0.100000000.20150421094558.1517.10000.62502"
}

server = r'http://medical-tech.winning.com.cn/platform/xuhui/dingdang'
# ret = requests.post(server, json=(inf))
# print ret,ret.text
#
#
# ret = requests.get(r'http://pacs.winning.com.cn/pat_test/signature?url=http://pacs.winning.com.cn/pat_test/')
# print ret.content


# url = r'http://180.166.22.190:30800//PEM/service.asmx/psp_LoginEx'
# url = r'http://pacs.winning.com.cn/pat_test/card/scanbind'
# # url = r'http://139.196.167.82:8080/card/scanbind'


# header = {'Content-Disposition': 'form-data'}
# content = {'userinput': '001', 'i_sPassword': '001'}
# # ret = requests.post("http://pacs.winning.com.cn/xuhui/dingdang", json=content)
# # ret = requests.post(url, files=content, headers=header)
# ret = requests.post(url, data=content)
# print type(ret.text)
# print json.loads(ret.text.encode('utf-8'))['msg']

