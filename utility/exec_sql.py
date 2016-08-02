# coding=utf-8

import requests
import HTMLParser
import xmltodict
import json


tcloud_conf = [
{'hosp': u'六院',       'addr':'http://101.231.40.242:7345'},
{'hosp': u'公利医院',   'addr':'http://180.166.22.190:30800'},
{'hosp': u'奉贤中心',   'addr':'http://222.72.133.188:8004'},
{'hosp': u'邵逸夫医院', 'addr':'http://121.43.186.154'},
{'hosp': u'同济医院',   'addr':'http://180.166.182.146:30025'},
{'hosp': u'嘉定中心',   'addr':'http://180.153.70.144:90'},
{'hosp': u'卢湾', 'addr':'http://180.168.156.226:30025'},
{'hosp': u'龙华医院',   'addr':'http://180.169.35.28:30025'},
{'hosp': u'珠海五院',   'addr':'http://113.106.107.210:30025'},
#{'hosp': u'江湾社区卫生服务中心', 'addr':'http://222.44.22.227:30026'},  # 铁通网络
]

# ws_path = '/PEM/service.asmx'

class WS_API():
  def __init__(self, url):
      # self.ws_url = url
      self.ws_url = url+'/PEM/service.asmx'

  def studycount_of_today(self):
      sql = 'select count(*) from pacs_study where studytime between \'{0}\' and \'{1}\''
      sql = sql.format(date.today(), date.today() + timedelta(1))
      result = self.exec_sql(sql)
      if result:
          return result.get('string', {}).get('NewDataSet', {}).get('DataList', {}).get('Column1', '0')

  def latest_studytime(self):
      sql = 'select top 1 studytime from pacs_study order by studytime desc'
      sql = sql.format(date.today(), date.today() + timedelta(1))
      result = self.exec_sql(sql)

      error = result.get('string', {}).get('#text', '') if result else ''

      # import json
      # print json.dumps(result, indent=2)
      studytime = ''
      if result:
          studytime = result.get('string', {}).get(
              'NewDataSet', {}).get('DataList', {}).get('studytime', '')
          studytime = studytime.replace('T', ' ')[:-6]
          # 2016-05-11T16:44:43+08:00
      return studytime, error

  def exec_sql(self, sql):
      header = {'Content-Disposition': 'form-data'}
      content = {'SQLString': sql}
      try:
          ret = requests.post(self.ws_url + '/psp_ExecuteSQL',
                              data=content, headers=header)
          if ret.status_code != 200:
              return None

          html_parser = HTMLParser.HTMLParser()
          result = html_parser.unescape(ret.text)
          # print result

          dresult = xmltodict.parse(result)
          return dresult
      except Exception, e:
          print e.message

      return None

ws = WS_API(tcloud_conf[0]['addr'])   # 六院
# ws = WS_API(tcloud_conf[1]['addr']) # 公利
# ws = WS_API(tcloud_conf[6]['addr'])   # 卢湾

result = ws.exec_sql('select * from pacs_volume')
# result = ws.exec_sql('select top 1 * from pacs_study order by studytime desc')
# print result

pat_info = result.get('string', {}).get('NewDataSet', {}).get('DataList', {}) if result else {}
print json.dumps(pat_info, indent=2, ensure_ascii=False) if pat_info else json.dumps(result, indent=2) if result else ''


# while True:
#   sql = raw_input("input sql statement:")
#   if sql:
#     result = ws.exec_sql(sql)
#     pat_info = result.get('string', {}).get('NewDataSet', {}).get('DataList', {}) if result else {}
#     print json.dumps(pat_info, indent=2, ensure_ascii=False) if pat_info else json.dumps(result, indent=2) if result else ''
