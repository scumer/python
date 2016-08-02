# -*- coding:utf-8 -*-

from xml.dom import minidom , Node

strxml= r'<?xml version="1.0" encoding="UTF-8"?><root><Request><CardType>2</CardType><PatientType>3310</PatientType><CardNo>03210236</CardNo><LabelID></LabelID><PatName>刘欣</PatName><PatNameSpell>lx</PatNameSpell><IDNum>62020119840925951X</IDNum><HospNo></HospNo><Sex>1</Sex><BirthDay>1984-09-25</BirthDay><Age>34岁</Age><PhoneNum>19078304851</PhoneNum><ApplyDeptName>心胸外科</ApplyDeptName><WardName></WardName><BedNo></BedNo><WardOrReg>1</WardOrReg><ReportNo>5632f44bb53ce00e0c6a9d54</ReportNo><HospCode>454556666</HospCode><ReportDepart>心胸外科</ReportDepart><SubSysCode>LIS_SH</SubSysCode><ReportDesc>X-Ray</ReportDesc><StudyItem>X-Ray照射</StudyItem><TechNo>2334542322</TechNo><HisApplyNo>201510283454</HisApplyNo><ReportDoctorName>张雨</ReportDoctorName><ReportTime>2015-10-30 14:23:10</ReportTime><VerifyDoctorName>刘莉平</VerifyDoctorName><AuditingTime>2015-10-30 15:23:10</AuditingTime><StudyMethod>检查方法3</StudyMethod><StudyObservation>查检所见3</StudyObservation><StudyResult>检查结论3</StudyResult></Request></root>'


strxml = '<?xml version="1.0" encoding="UTF-8"?><root><parameter><Confirm>T</Confirm><ErrorDesc/></parameter></root>'

dom = minidom.parseString(string=strxml)

print dom.toprettyxml(indent='  ', newl='\n')

ctag = dom.getElementsByTagName('Confirm')
print ctag[0].firstChild.data
etag = dom.getElementsByTagName('ErrorDesc')
if etag:
    print '0000'
    print etag[0].firstChild



