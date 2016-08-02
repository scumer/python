# -*- coding:utf-8 -*- 
def GenerateXml():
    import xml.dom.minidom
    impl = xml.dom.minidom.getDOMImplementation()
    dom = impl.createDocument(None, 'root', None)
    root = dom.documentElement  
    ReportInfo = dom.createElement('ReportInfo')
    root.appendChild(ReportInfo)

    nameE = []
    nameT = []
    nameE.append(dom.createElement('path'))
    nameT.append(dom.createTextNode('linux'))
    
    nameE.append(dom.createElement('a'))
    nameT.append(dom.createTextNode('1'))
    
    nameE.append(dom.createElement('cc'))
    nameT.append(dom.createTextNode('dd'))
    
    
    #nameE = dom.createElement('path')
    #nameT = dom.createTextNode('linux')

    #nameE[0].appendChild(nameT[0])
    #nameE[1].appendChild(nameT[1])
    ##nameE.setAttribute("value","aaaaaaaaaaa") #增加属性
    #ReportInfo.appendChild(nameE[0])
    #ReportInfo.appendChild(nameE[1])
    
    for i in range(0,len(nameE)):
        nameE[i].appendChild(nameT[i])
        ReportInfo.appendChild(nameE[i])


    return dom.toprettyxml(indent='  ', newl='\n',encoding='UTF-8')
    
    #f= open('new.xml', 'w')
    #dom.writexml(f, addindent='  ', newl='\n',encoding='UTF-8')
    #f.close()  

#strxml = GenerateXml()


def RegReportInfo():
    import xml.dom.minidom

    impl = xml.dom.minidom.getDOMImplementation()
    dom = impl.createDocument(None, 'root', None)
    root = dom.documentElement  
    ReportInfo = dom.createElement('Request')
    root.appendChild(ReportInfo)    
    
    impl_ret = xml.dom.minidom.getDOMImplementation()
    dom_ret = impl_ret.createDocument(None, 'root', None)
    root_ret = dom_ret.documentElement
    parameter = dom_ret.createElement('parameter')
    root_ret.appendChild(parameter)

    nameE = []
    nameT = []
    nameE.append(dom_ret.createElement('Confirm'))
    nameT.append(dom_ret.createTextNode('T')) 
    nameE.append(dom_ret.createElement('ErrorDesc'))  # ward
    nameT.append(dom_ret.createTextNode('error'))   
    for i in range(0,len(nameE)):
        nameE[i].appendChild(nameT[i])
        parameter.appendChild(nameE[i])     
    
    try:
        nameE = []
        nameT = [] 
        
        nameE.append(dom.createElement('BookCenterSID'))
        nameT.append(dom.createTextNode(None or 'aaaa'))
        
        nameE.append(dom.createElement('Brlx'))  # ward
        nameT.append(dom.createTextNode('1'))
        
        nameE.append(dom.createElement('CardNo'))
        nameT.append(dom.createTextNode('1'))
        
        nameE.append(dom.createElement('PatName'))  # MedicalCard->name
        nameT.append(dom.createTextNode('1'))
        
        nameE.append(dom.createElement('Sex'))
        nameT.append(dom.createTextNode('1'))
        
        nameE.append(dom.createElement('Phone'))
        nameT.append(dom.createTextNode('1'))
        
        nameE.append(dom.createElement('IDNum'))
        nameT.append(dom.createTextNode('1'))
        
        nameE.append(dom.createElement('HisApplyNo'))
        nameT.append(dom.createTextNode('1'))
        
        nameE.append(dom.createElement('ReportNo'))  # ReportID
        nameT.append(dom.createTextNode('ReportID'))
        
        nameE.append(dom.createElement('ReportType'))
        nameT.append(dom.createTextNode('1'))
        
        nameE.append(dom.createElement('ReportName'))  # studyitem
        nameT.append(dom.createTextNode('1'))
        
        nameE.append(dom.createElement('ReportDate'))
        nameT.append(dom.createTextNode('1'))
        
        nameE.append(dom.createElement('ReportDoctor'))
        nameT.append(dom.createTextNode(''))
        
        nameE.append(dom.createElement('HospitalName'))  # Hospital->hospitalCode->hospitalName
        nameT.append(dom.createTextNode('1'))
        
        nameE.append(dom.createElement('ReportDesc'))
        nameT.append(dom.createTextNode('1'))
        
        name_e.append(dom.createElement('CardType'))  # 1就诊卡 2医保卡
        name_t.append(dom.createTextNode('1'))        
        
        for i in range(0,len(nameE)):
            nameE[i].appendChild(nameT[i])
            ReportInfo.appendChild(nameE[i])                
    except Exception as e:
        print e.message,e.args
            
    
    
    return dom.toprettyxml(encoding='UTF-8',newl='',indent=''),dom_ret.toprettyxml(indent='  ', newl='\n',encoding='UTF-8')


strxml,strxmlret = RegReportInfo()
#print strxml
strxml = u'<?xml version="1.0" encoding="UTF-8"?><root><Request><CardType>2</CardType><PatientType>3310</PatientType><CardNo>03210236</CardNo><LabelID></LabelID><PatName>刘欣</PatName><PatNameSpell>lx</PatNameSpell><IDNum>62020119840925951X</IDNum><HospNo></HospNo><Sex>1</Sex><BirthDay>1984-09-25</BirthDay><Age>34岁</Age><PhoneNum>19078304851</PhoneNum><ApplyDeptName>心胸外科</ApplyDeptName><WardName></WardName><BedNo></BedNo><WardOrReg>1</WardOrReg><ReportNo>5632f44bb53ce00e0c6a9d54</ReportNo><HospCode>454556666</HospCode><ReportDepart>心胸外科</ReportDepart><SubSysCode>LIS_SH</SubSysCode><ReportDesc>X-Ray</ReportDesc><StudyItem>X-Ray照射</StudyItem><TechNo>2334542322</TechNo><HisApplyNo>201510283454</HisApplyNo><ReportDoctorName>张雨</ReportDoctorName><ReportTime>2015-10-30 14:23:10</ReportTime><VerifyDoctorName>刘莉平</VerifyDoctorName><AuditingTime>2015-10-30 15:23:10</AuditingTime><StudyMethod>检查方法3</StudyMethod><StudyObservation>查检所见3</StudyObservation><StudyResult>检查结论3</StudyResult></Request></root>'


strxml = u'<?xml version="1.0" encoding="UTF-8"?><root><Request><CardType>1</CardType><PatientType></PatientType><WardOrReg>0</WardOrReg><CardNo>03210236</CardNo><PatName>王超</PatName><PatNameSpell></PatNameSpell><HospNo></HospNo><LabelID>0000039275</LabelID><BedNo></BedNo><WardName></WardName><Sex>1</Sex><PhoneNum>13020008002</PhoneNum><IDNum>370405198703210236</IDNum><HisApplyNo></HisApplyNo><ReportNo>5632f44bb53ce00e0c6a9d54</ReportNo><TechNo>3367409</TechNo><ReportType>普放</ReportType><StudyItem>腰椎正侧位</StudyItem><ReportTime>2015-10-28 10:09:06</ReportTime><ReportDoctorName>魏小二/易飞</ReportDoctorName><HospitalName>浙江省邵逸夫医院</HospitalName><HospCode>470003265</HospCode><ReportDesc>普放</ReportDesc><SubSysCode></SubSysCode><ReportDepart>骨科</ReportDepart><VerifyDoctorName>张霞</VerifyDoctorName><AuditingTime></AuditingTime><StudyMethod>正侧位X线摄片</StudyMethod><StudyObservation>腰椎序列光整，生理曲度存在，诸椎骨未见明显骨质异常，椎间隙无狭窄，附件未见明显异常，未见异常软组织影。</StudyObservation><StudyResult>腰椎轻度骨质疏松，部分椎小关节稍模糊，强直性脊柱炎不除外，请结合临床，建议必要时进一步检查。</StudyResult></Request></root>'


print strxml
import requests,json
from collections import OrderedDict


headers = {'Content-Type': 'application/json'}
regreport_data = {"serviceId":"eh.regReportInfoService","method":"regReportInfo","body":[strxml]}

dct = OrderedDict([('serviceId','eh.regReportInfoService'),('method','regReportInfo'),('body',[strxml])])

ret= None
ret = requests.post(url=r'http://121.43.182.18:8080/ehealth-base/*.jsonRequest',data=json.dumps(dct),headers=headers)

#print ret.status_code
#print ret.content

print 'ret',type(ret.content)
data = json.loads(ret.content)
#print data['body']

xml_body = data['body']

import xml.dom.minidom
try:    
    
    print type(xml_body)
    if type(xml_body) == unicode:
        xml_body = xml_body.encode('utf-8')
        print type(xml_body)
    
    body_dom = xml.dom.minidom.parseString(string=xml_body)
    confirm_elem = body_dom.getElementsByTagName('Confirm')
    confirm = confirm_elem[0].firstChild.data if confirm_elem[0].firstChild else None
    if confirm == 'T':
        print 'T'
    else:
        print 'F'
        err_elem = body_dom.getElementsByTagName('ErrorDesc')
        error_desc = err_elem[0].firstChild.data if err_elem[0].firstChild else ''
        print error_desc

except Exception as e:
    print 'exception:',e.args


#print json.dumps(regreport_data,indent=2)



#print regreport_data
#print sorted(dct.items(), key=lambda d: d[0],reverse=True)

#print dct
#print json.dumps(regreport_data,indent=3) 

#print str([strxml])



    #print json.loads(ret.content)['body']
    #print ret.headers
#print json.loads(ret.content)['msg']

#------------------------------------------------------------------------------------------------------------------
str1 = {"studyUID":"1.3.6.1.4.1.19439.0.108707908.20151028084329.1450.15102863",
 "PatName":u'王超',"PatID":"3367409","PatSex":"M","PatAge":"028Y","AccessionNo":"0000039275","HospCode":"470003265",
 "films":[{"studyUID":"1.3.6.1.4.1.19439.0.108707908.20151028084329.1450.15102863",
           "seriesUID":"1.3.46.670589.30.1.6.1.963334086946.1445997559453.1",
           "objectUID":"1.3.46.670589.30.1.6.963334086946.1.1324.1445997565265"},
          {"studyUID":"1.3.6.1.4.1.19439.0.108707908.20151028084329.1450.15102863",
           "seriesUID":"1.3.46.670589.30.1.6.1.963334086946.1445997559453.1",
           "objectUID":"1.3.46.670589.30.1.6.963334086946.1.1324.1445997570328"}
         ]}

str2 = {"studyUID":"1.3.6.1.4.1.19439.0.108707908.20151028092347.1503.15103275",
       "PatName":u'高剑',"PatID":"3367581","PatSex":"M","PatAge":"020Y","AccessionNo":"0000039276","HospCode":"470003265",
       "films":[{"studyUID":"1.3.6.1.4.1.19439.0.108707908.20151028092347.1503.15103275",
                 "seriesUID":"1.3.6.1.4.1.19439.1.100000000.20151028143020.1343",
                 "objectUID":"1.2.840.2.1000001.1000001.20151028143022.1015724"}
                ]}

#print json.dumps(str2,indent=2)
#ret = requests.post(url=r'http://139.196.167.219/xuhui/dingdang',data=json.dumps(str2))

##ret = requests.get(url=r'http://139.196.57.139:80/menu/myCheck/')
#print ret.status_code
#print ret.content


def fun(b):
    if b:
        print 'Y'
    else:
        print 'N'
        
v1 = True
v2 = False

fun(v1 and v2)


a = 1
a += 2
print a