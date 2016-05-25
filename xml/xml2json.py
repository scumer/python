# coding=utf-8

# from __future__ import unicode_literals
import xmltodict
import json

xmlstr = u'<?xml version="1.0" encoding="utf-8"?><root><Request><WardOrReg>0</WardOrReg><CardNo></CardNo><PatName>\u80e1\u7231\u82f1</PatName><PatNameSpell></PatNameSpell><HospNo></HospNo><LabelID></LabelID><BedNo></BedNo><WardName>\u5168\u79d1\u533b\u5b66</WardName><Sex>1</Sex><PhoneNum></PhoneNum><IDNum>330104195401042747</IDNum><ReportNo>571f45c4d52c9e0efddfe06c</ReportNo><TechNo>3409733</TechNo><ReportType></ReportType><StudyItem>\u51a0\u8109\u5e73\u626b+\u589e\u5f3a</StudyItem><ReportTime>2016-04-22 15:52:59</ReportTime><ReportDoctorName>\u80e1\u8d62\u5347</ReportDoctorName><HospitalName>\u6d59\u6c5f\u7701\u90b5\u9038\u592b\u533b\u9662</HospitalName><HospCode>470003265</HospCode><ReportDesc></ReportDesc><ReportDepart>\u5168\u79d1\u533b\u5b66</ReportDepart><VerifyDoctorName>\u697c\u6e05\u6e05</VerifyDoctorName><StudyMethod>CT</StudyMethod><StudyObservation>\u5e73\u626b\u65cb\u652f\u8fd1\u6bb5\u9499\u5316\u3002    \u589e\u5f3a\u540e\u8584\u5c42\u626b\u63cf\u5e76\u4e09\u7ef4\u91cd\u5efa\uff0c\u5404\u652f\u51a0\u8109\u663e\u793a\u826f\u597d\u3002\u5404\u652f\u51a0\u72b6\u52a8\u8109\u5168\u7a0b\u663e\u793a\uff0c\u5de6\u53f3\u51a0\u8109\u5f00\u53e3\u4f4d\u7f6e\u65e0\u6b8a\uff1b    \u5de6\u524d\u964d\u652f\u8fd1\u6bb5\u8f6f\u6591\u5757\uff0c\u76f8\u5e94\u7ba1\u8154\u8f7b\u5ea6\u53d8\u7a84\uff0c\u72ed\u7a84\u7ea630%\u3002    \u65cb\u652f\u8fd1\u6bb5\u9499\u5316\u6591\u5757\uff0c\u7ba1\u8154\u8f7b\u5ea6\u53d8\u7a84\u3002    \u4f59\u51a0\u8109\u7ba1\u58c1\u5149\u6ed1\uff0c\u7ba1\u8154\u5747\u5300\uff0c\u672a\u89c1\u660e\u663e\u6591\u5757\u5f62\u6210\u53ca\u7ba1\u8154\u72ed\u7a84\u3002\u5fc3\u810f\u53ca\u5404\u5927\u8840\u7ba1\u8d77\u59cb\u90e8\u5f62\u6001\u3001\u8d70\u884c\u672a\u89c1\u660e\u663e\u5f02\u5e38\u3002</StudyObservation><StudyResult>\u5de6\u524d\u964d\u652f\u8fd1\u6bb5\u8f6f\u6591\u5757\uff0c\u7ba1\u8154\u8f7b\u5ea6\u53d8\u7a84\u3002    \u65cb\u652f\u8fd1\u6bb5\u9499\u5316\u6591\u5757\u3002</StudyResult><Age>61\u5c81</Age><ApplyDeptName>\u5168\u79d1\u533b\u5b66</ApplyDeptName><CardType>1</CardType><PatientType>1</PatientType><BirthDay></BirthDay><AuditingTime></AuditingTime><SubSysCode></SubSysCode><HisApplyNo></HisApplyNo></Request></root>'

print xmlstr

convertedDict = xmltodict.parse(xmlstr)
print convertedDict
jsonstr = json.dumps(convertedDict, indent=2, ensure_ascii=False)
print "jsonstr=", jsonstr
