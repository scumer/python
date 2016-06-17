# coding=utf-8

import requests

url = 'http://vwraieoyhh.proxy.qqbrowser.cc'
url = 'http://127.0.0.1:6234'
url = 'http://139.196.167.82'


def upload(url, data):
	ret = requests.post(url, json=data)     
	print url,ret,'\n',ret.text

queue1 =  {'PushType':'20', 'PatName':u'刘朝芳', 'SexName':'女', 'CityCode':'021', 'CardNo':'133009002463167'}
queue2 = {
"PatName":u"曹爱芳","CardNo":"D03290415","SexName":u"女",
"PushSign":u"1","PushType":"20","ExamName":u"普放","ExamRoom":u"1号拍片室","QueueNo":"H0265","QueuePre":"H","RegTime":"2016-06-05 00:00:00",
"ExamItems":u"腰椎正侧位","CurQueueNo":"H0159",
"HospitalName":u"上海市第六人民医院","HospitalCode":"425026521",
"AgeUnit":u"岁    ","ExamTime_1":"","TechNo":"2968954","Age":"17","YYZYSX":"","ApplyNo":"15669174",
"SubSysCode":"RIS_FS","CurWaitTime":"","CityCode":"021","BookTime":"","LabelID":"A102867720","AuditingTime":"","Remark":"",
"Title":u"市六医院放射科,陆悠,17.00,岁    ,女,2016/06/01,2968954,腰椎正侧位,A102867720,100",
"TipMsg":u"注意叫号屏及声音提示，过号请携带此叫号单重新取号。","ExamTime":"","ExamCode":"X","WardOrReg":u"门诊"}

queue3 = {
"PatName":u"许晓英","CardNo":"D21508617","SexName":u"女",
"PushSign":u"1","PushType":"20","ExamName":u"CT","ExamRoom":u"2号拍片室","QueueNo":"F0263","QueuePre":"F","RegTime":"2016-06-07 00:00:00",
"ExamItems":u"腰椎正侧位","CurQueueNo":"F0159",
"HospitalName":u"上海市第六人民医院","HospitalCode":"425026521",
"AgeUnit":u"岁    ","ExamTime_1":"","TechNo":"2968954","Age":"17","YYZYSX":"","ApplyNo":"15669174",
"SubSysCode":"RIS_FS","CurWaitTime":"","CityCode":"021","BookTime":"","LabelID":"A102867720","AuditingTime":"","Remark":"",
"Title":u"市六医院放射科,陆悠,17.00,岁    ,女,2016/06/01,2968954,腰椎正侧位,A102867720,100",
"TipMsg":u"注意叫号屏及声音提示，过号请携带此叫号单重新取号。","ExamTime":"","ExamCode":"X","WardOrReg":u"门诊"}



queue4 = {
"PatName":u"许俊生","CardNo":"133009002785802","SexName":u"男",
"PushSign":u"1","PushType":"20","ExamName":u"CT","ExamRoom":u"2号拍片室","QueueNo":"F0260","QueuePre":"F","RegTime":"2016-06-06 00:00:00",
"ExamItems":u"腰椎正侧位","CurQueueNo":"F0159",
"HospitalName":u"上海市第六人民医院","HospitalCode":"425026521",
"AgeUnit":u"岁    ","ExamTime_1":"","TechNo":"2968954","Age":"17","YYZYSX":"","ApplyNo":"15669174",
"SubSysCode":"RIS_FS","CurWaitTime":"","CityCode":"021","BookTime":"","LabelID":"A102867720","AuditingTime":"","Remark":"",
"Title":u"市六医院放射科,陆悠,17.00,岁    ,女,2016/06/01,2968954,腰椎正侧位,A102867720,100",
"TipMsg":u"注意叫号屏及声音提示，过号请携带此叫号单重新取号。","ExamTime":"","ExamCode":"X","WardOrReg":u"门诊"}

queueyy = {
"PatName":u"刘伟","CardNo":"133009002785985","SexName":u"男",
"PushSign":u"1","PushType":"20","ExamName":u"CT","ExamRoom":u"2号拍片室","QueueNo":"F0260","QueuePre":"F","RegTime":"2016-06-06 00:00:00",
"ExamItems":u"腰椎正侧位","CurQueueNo":"F0159",
"HospitalName":u"上海市第六人民医院","HospitalCode":"425026521",
"AgeUnit":u"岁    ","ExamTime_1":"","TechNo":"2968954","Age":"17","YYZYSX":"","ApplyNo":"15669174",
"SubSysCode":"RIS_FS","CurWaitTime":"","CityCode":"021","BookTime":"","LabelID":"A102867720","AuditingTime":"","Remark":"",
"Title":u"市六医院放射科,陆悠,17.00,岁    ,女,2016/06/01,2968954,腰椎正侧位,A102867720,100",
"TipMsg":u"注意叫号屏及声音提示，过号请携带此叫号单重新取号。","ExamTime":"","ExamCode":"X","WardOrReg":u"门诊"}


queuehui = {
"PatName":u"张国英","CardNo":"P0947276X","SexName":u"女",
"PushSign":u"1","PushType":"20","ExamName":u"CT","ExamRoom":u"2号拍片室","QueueNo":"F0260","QueuePre":"F","RegTime":"2016-06-09 00:00:00",
"ExamItems":u"腰椎正侧位","CurQueueNo":"F0159",
"HospitalName":u"上海市第六人民医院","HospitalCode":"425016155",
"AgeUnit":u"岁    ","ExamTime_1":"","TechNo":"2968954","Age":"17","YYZYSX":"","ApplyNo":"15669174",
"SubSysCode":"RIS_FS","CurWaitTime":"","CityCode":"021","BookTime":"","LabelID":"A1020000","AuditingTime":"","Remark":"",
"Title":u"市六医院放射科,陆悠,17.00,岁    ,女,2016/06/01,2968954,腰椎正侧位,A102867720,100",
"TipMsg":u"注意叫号屏及声音提示，过号请携带此叫号单重新取号。","ExamTime":"","ExamCode":"X","WardOrReg":u"门诊"}

# PushType_10 = {"AgeUnit":"岁    ","ExamTime_1":"","ExamItems":"","PushType":"10","PushSign":"0","TechNo":"2275955","Age":"81","YYZYSX":"","SexName":"男","QueueNo":"","RegTime":"2016-06-04 00:00:00","ApplyNo":"15669178","QueuePre":"","SubSysCode":"RIS_FS","CurWaitTime":"","CityCode":"021","BookTime":"2016-06-04 20:30～20:42","LabelID":"A102867721","AuditingTime":"","Remark":"","CardNo":"E01983389","PatName":"刘阿四","Title":"刘阿四,您的预约已成功，请仔细阅读预约回执单准时就诊。","TipMsg":"您的预约已成功，请仔细阅读预约回执单准时就诊。","ExamTime":"","ExamRoom":"MRI检查室3","ExamName":"MRI","ExamCode":"MRI","WardOrReg":"住院","CurQueueNo":"","HospitalName":"上海市第六人民医院","HospitalCode":"425026521"}
# PushType_22
# PushType_25
# PushType_50 
# PushType_0  
status_labels = {
    '0': u'取消',
    '10': u'登记',
    '20': u'分诊',
    '22': u'暂停',
    '25': u'检查完成',
    '50': u'报告完成'
}

# ret = requests.post(url+r'/platform/ris/message', json=(queue2))      
# print ret,'\n',ret.text 

# upload(url+'/platform/ris/message', queueyy)
# upload(url+'/platform/ris/message', queue3)

status = ['50','25','20']
status = ['25']
for stat in status:
	queuehui['PushType'] = stat
	# upload(url+'/platform/ris/message', queuehui)	



# RISReport、USReport、ESReport、LisReport、MicrobeReport (放射、超声、内镜、化验、微生物)

# LIS Report
lisreport = [{"CardNo":"P0947276X","HospNo":"9037539","PatName":"张国英","ImeCode":"XMH","Sex":"女","HospitalCode":"425016155","CityCode":"021","ApplyNo":"1009988500","JZLSH":"","WardOrReg":"住院","ExecTime":"2016-6-1 0:00:00","InstID":"10024","TechNo":"807","Txm":"994530311P","CureNo":"482470","Birthday":"","Age":"50岁","AgeUnit":"岁","Ward":"5085","WardName":"介入科","BedNo":"+1","ApplyDept":"0184","ApplyDeptName":"介入科普通","ApplyDocCode":"1431","ApplyDocName":"王征宇","ApplyTime":"2016-5-31 23:15:33","ClinicDesc":"咯血","Bglxcode":"3","Bglxname":"化学发光","Sample":"1","SampleName":"血清","SampleTime":"2016-6-1 5:13:40","ReceiveTime":"2016-6-1 7:51:21","ExecDeptCode":"","ExecDeptName":"","RegisterCode":"6236","RegisterName":"肖成超","RegisterTime":"2016-6-1 8:22:16","ExecDocCode":"6236","ExecDocName":"肖成超","VerifierCode":"2092","VerifierName":"李凤妹","VerifierTime":"2016-6-1 13:20:42","PubCode":"2187","PubName":"赵卫卫","PubTime":"2016-6-1 13:20:42","IDNum":"","Comment":"","Createtime":"2016-6-1 13:22:42","UpTime":"","Upflag":"0","Upcount":"0","faledreason":"","Result":[{"YLJGDM":"42505781100","ApplyNo":"1009988500","SerialNo":"171332025","ItemCode":"HBcAb.","ItemName":"乙肝核心抗体","ResultValue":"1.8700","ResultChar":"1.870阴性","Result":"1.870阴性","HighLowFlag":"","ReferenCerange":">1.000","Unit":"COI","Printorder":"6550","IsPanic":"0","MethodName":"","Createtime":"2016-6-1 13:22:42"},{"YLJGDM":"42505781100","ApplyNo":"1009988500","SerialNo":"171332024","ItemCode":"HBeAb.","ItemName":"乙肝E抗体","ResultValue":"1.6600","ResultChar":"1.660阴性","Result":"1.660阴性","HighLowFlag":"","ReferenCerange":">1.000","Unit":"COI","Printorder":"6540","IsPanic":"0","MethodName":"","Createtime":"2016-6-1 13:22:42"},{"YLJGDM":"42505781100","ApplyNo":"1009988500","SerialNo":"171332023","ItemCode":"HBeAg.","ItemName":"乙肝E抗原","ResultValue":"0.1210","ResultChar":"0.121阴性","Result":"0.121阴性","HighLowFlag":"","ReferenCerange":"0～1","Unit":"COI","Printorder":"6530","IsPanic":"0","MethodName":"","Createtime":"2016-6-1 13:22:42"},{"YLJGDM":"42505781100","ApplyNo":"1009988500","SerialNo":"171332022","ItemCode":"HBsAb.","ItemName":"乙肝表面抗体","ResultValue":"0.0000","ResultChar":"<2.00阴性","Result":"<2.00阴性","HighLowFlag":"","ReferenCerange":"0～10","Unit":"IU/ml","Printorder":"6520","IsPanic":"0","MethodName":"","Createtime":"2016-6-1 13:22:42"},{"YLJGDM":"42505781100","ApplyNo":"1009988500","SerialNo":"171332021","ItemCode":"HBsAg.","ItemName":"乙肝表面抗原","ResultValue":"0.3650","ResultChar":"0.365阴性","Result":"0.365阴性","HighLowFlag":"","ReferenCerange":"0～1","Unit":"COI","Printorder":"6510","IsPanic":"0","MethodName":"","Createtime":"2016-6-1 13:22:42"},{"YLJGDM":"42505781100","ApplyNo":"1009988500","SerialNo":"171332020","ItemCode":"HCV_","ItemName":"丙型肝炎病毒抗体","ResultValue":"0.0350","ResultChar":"0.035阴性","Result":"0.035阴性","HighLowFlag":"","ReferenCerange":"0～1","Unit":"COI","Printorder":"6570","IsPanic":"0","MethodName":"","Createtime":"2016-6-1 13:22:42"}],"Image":[]}]
# upload(url+'/platform/lis/report/upload', lisreport)

#US Report
usreport = {"CardNo":"P0947276X","PatName":"张国英","Sex":"女","HospitalCode":"425016155","InsertTime":"2016-6-1 14:09:58","UpFlag":"0","StudyItem":"","TechNo":"","Age":"31岁","WardName":"","ApplyDrCode":"","StudyResult":"左卵巢旁囊块，请随访双侧卵巢多小囊改变，请结合临床","uploadCount":"0","PatNameSpell":"","HospNo":"2005163499","ReportSource":"","StudyObservation":"子宫前位,宫体长径42mm，厚32mm，宽45mm；形态规则，肌层回声均匀。内膜厚5mm，呈高回声，边界清晰。CDFI示血流信号正常分布。未见宫内节育器。双侧卵巢单个切面内见10个以上直径小于10mm的无回声区，呈“多囊改变”，卵巢髓质增多、回声增强。左卵巢旁见14×15×14mm无回声区,内部透声好，后方回声增强。CDFI示内部未见明显血流信号。","ConsultDrCode":"","ShareFlag":"0","ApplyFlag":"","ShareBeginDate":"","ApplyDeptName":"","ApplyNo":"3555540","modifyTime":"","ReportDoctorName":"王岚","SubSysCode":"RIS_CS","ConsultHospCode":"","VerifyDoctorName":"王岚","FinallyEditTime":"2016-6-1 14:07:05","IDNum":"","ImageStatus":"-1","ReportTime":"2016-6-1 14:07:05","ReportDesc":"阴超","CityCode":"021","LabelID":"","AuditingTime":"","StudyMethod":"","SerialNo":"79966","isAgainShare":"1","FailedReason":"","ShareEndDate":"","WardOrReg":"0","SendHttpStat":"","SendHttpJson":"","BedNo":"","StudyUID":""}
# upload(url+'/platform/report/upload', usreport)

#ES Report
esreport = {"CardNo":"P0947276X","PatName":"张国英","HospitalCode":"425016155","InsertTime":"2016-6-1 14:17:35","UpFlag":"0","StudyItem":"","TechNo":"201605002","Sex":"女","Age":"35岁","WardName":"","ApplyDrCode":"","StudyResult":"浅表性胃炎并糜烂随访","uploadCount":"0","PatNameSpell":"","HospNo":"20160000508481","ReportSource":"","StudyObservation":"食道：食管黏膜光滑柔软，血管纹理清晰，扩张度好，齿状线清晰。 贲门：粘膜光滑，未见异常。胃底：未见明显异常胃体：粘膜光滑，色泽潮红，未见溃疡及出血。胃角：弧度存在粘膜光滑柔软，蠕动可。胃窦：粘膜红白相间，以红为主，见散在斑片状糜烂，未见出血及溃疡，蠕动尚可，色泽淡红。幽门：呈圆形，开闭尚可，粘膜皱襞光滑，色泽淡红，未见出血及溃疡。十二指肠：未见明显异常","ConsultDrCode":"","ShareFlag":"0","ApplyFlag":"","ShareBeginDate":"","ApplyDeptName":"普内科普通","ApplyNo":"3065584","modifyTime":"","ReportDoctorName":"计为明","SubSysCode":"RIS_NJ","ConsultHospCode":"","VerifyDoctorName":"计为明","FinallyEditTime":"2016-6-1 14:15:13","IDNum":"","ImageStatus":"-1","ReportTime":"2016-6-1 14:15:13","ReportDesc":"胃镜","CityCode":"021","LabelID":"0001499060","AuditingTime":"","StudyMethod":"","SerialNo":"6081","isAgainShare":"1","FailedReason":"","ShareEndDate":"","WardOrReg":"0","SendHttpStat":"","SendHttpJson":"","BedNo":"","StudyUID":""}
# upload(url+'/platform/report/upload', esreport)

#MicrobeReport
mbreport = [{"CardNo":"P0947276X","HospNo":"143608300502095","PatName":"张国英","HospitalCode":"425016155","CityCode":"021","ApplyNo":"193572401","JZLSH":"","WardOrReg":"门诊","ExecTime":"2016-06-01 00:00:00","InstID":"10007","TechNo":"76780","Txm":"68004387734P","CureNo":"143608300502095","ImeCode":"HCQ","Sex":"女","Birthday":"1986-09-02 00:00:00","Age":"30岁","AgeUnit":"岁","Ward":"","WardName":"","BedNo":"","ApplyDept":"3020100","ApplyDeptName":"产科门诊","ApplyDocCode":"01255","ApplyDocName":"董颖","ApplyTime":"2016-06-01","ClinicDesc":"确认妊娠","Bglxcode":"10","Bglxname":"微生物","Sample":"11","SampleName":"分泌物","SampleTime":"2016-06-01 08:49:18","ReceiveTime":"2016-06-01 09:12:19","ExecDeptCode":"6040000","ExecDeptName":"医学检验科","RegisterCode":"01074","RegisterName":"沈振华","RegisterTime":"2016-06-01 09:12:19","ExecDocCode":"01074","ExecDocName":"沈振华","VerifierCode":"06631","VerifierName":"姚肖岚","VerifierTime":"2016-06-01 10:53:11","PubCode":"06631","PubName":"姚肖岚","PubTime":"2016-06-01 10:53:13","IDNum":"352228198609023524","Comment":"","Createtime":"2016-06-01 10:54:48","UpTime":"","Upflag":"0","Upcount":"0","faledreason":"","OrgResult":[{"YLJGDM":"425016155","ApplyNo":"19357240","ResultType":"鉴定结果","MethodName":"","OrganismNo":"x14","OrganismName":"衣原体检查：阴性","Result":"衣原体检查：阴性","Quantity":"","Createtime":"2016-06-01 10:54:48","AntiResult":[]}]}]
# upload(url+'/platform/microbe/report/upload', mbreport)

#RISReport
risreport = {"CardNo":"P0947276X","PatName":u"张国英","Sex":u"女","HospitalCode":"425016155","ApplyNo":"154906201",
"BedNo":"","StudyUID":"1.3.6.1.4.1.19439.0.108707908.20160330150900.1413.15490620","InsertTime":"2016-3-30 16:52:02",
"UpFlag":"0","StudyItem":"胸部","TechNo":"3523361","Age":"39岁","WardName":"","StudyResult":"1.两肺纹理略增多，请结合临床。2.右上肺小钙化灶。",
"uploadCount":"0","PatNameSpell":"ZCL","HospNo":"20160000161215","ReportSource":"pa",
"StudyObservation":"   两肺野纹理略增多，右上肺可见斑点高密度影。两侧肺门影清晰，大小正常范围。两侧肋膈角锐利，两横膈光滑。纵隔影无增宽，心影未见明显异常。",
"ShareFlag":"0","ShareBeginDate":"","ApplyDeptName":"中医内科","modifyTime":"",
"ReportDoctorName":"魏小二/李菁","SubSysCode":"RIS_FS","VerifyDoctorName":"瞿楠","FinallyEditTime":"2016-3-30 16:51:30","IDNum":"","ImageStatus":"-1","ReportTime":"2016-3-30 16:27:34",
"ReportDesc":"普放","CityCode":"021","LabelID":"A102761210","AuditingTime":"2016-3-30 16:49:22","StudyMethod":"","isAgainShare":"1","FailedReason":"","ShareEndDate":"",
"WardOrReg":"0","SendHttpStat":"","SendHttpJson":""}

upload(url+'/platform/report/upload', risreport)

#film
film = {"studyUID":"1","PatName":u"中文","PatID":"1","PatSex":"F","PatAge":"039Y","AccessionNo":"1","HospCode":"425026521","films":[{"studyUID":"123","seriesUID":"1.3.6.1.4.1.19439.1.100000000.20160330162041.1110","objectUID":"1.2.840.2.1000001.1000001.20160330161914.1016118"}]}
upload(url+'/platform/xuhui/dingdang', data = film)

