# coding=utf-8

import requests
import HTMLParser
import xmltodict
import json


class WS_API():
  def __init__(self, url):
      self.ws_url = url

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


def upload_film_info():
    studyuid = '1.3.6.1.4.1.19439.0.108707908.20160329084323.1493.15482055'
    inf =   {
    "HospCode": "9999", 
    "PatAge": '', 
    "PatName": "***", 
    "films": [
      {
        "objectUID": "1.3.6.1.4.1.19439.2.000001.066077080.0.20160622102805.001747", 
        "seriesUID": "1.3.6.1.4.1.19439.1.000001.066077080.0", 
        "studyUID": "1.3.6.1.4.1.19439.0.000001.066077080.0"
      }, 
      {
        "objectUID": "1.3.6.1.4.1.19439.2.000001.066077080.0.20160622102809.001760", 
        "seriesUID": "1.3.6.1.4.1.19439.1.000001.066077080.0", 
        "studyUID": "1.3.6.1.4.1.19439.0.000001.066077080.0"
      }, 
    ], 
    "PatSex": "F", 
    "AccessionNo": 'A10262222', 
    "studyUID": "1.3.6.1.4.1.19439.0.000001.066077080.0", 
    "PatID": "16-11632"
  }
    server = r'http://medical-tech.winning.com.cn/platform/xuhui/dingdang'
    ret = requests.post(server, json=(inf))
    print ret,ret.text


def upload_film_data(upload=False, **args):
    inf = [{
        "HospCode": args['HospCode'],
        "PatSex": args['PatSex'],
        "PatAge": args['PatAge'],
        "PatName": args['PatName'],
        "PatID": args['PatID'],
        "AccessionNo": args['AccessionNo'],
        "studyUID": args['studyUID'],
        "films": [args['films']] if type(args['films']) != list else args['films'],
    }]

    server = r'http://medical-tech.winning.com.cn/platform/xuhui/dingdang'
    print '>>>>>>>>>>upload data'
    print json.dumps(inf, indent=2)
    if upload:
        ret = requests.post(server, json=inf)
        print ret, ret.text


def query_pat_info(ws_url, studyuid, hospcode):
    ws = WS_API(ws_url)

    result = ws.exec_sql("select top 1 * from pacs_study where modality= 'CT' order by inserttime desc")
    # result = ws.exec_sql("select top 1 Sex as PatSex, Age as PatAge, PatName,PatID,AccessionNo,studyUID from pacs_study where patid='%s'" % '1940245')
    print '>>>>>>>>>latest study'
    print json.dumps(result, indent=2) if result else ''

    sql_pat_info = "select top 1 Sex as PatSex, Age as PatAge, PatName,PatID,AccessionNo,studyUID from pacs_study where studyuid='%s'" % studyuid
    # sql_pat_info = "select top 1 Sex as PatSex, Age as PatAge, PatName,PatID,AccessionNo,studyUID from pacs_study where patid='%s'" % '3423444'
    # sql_pat_info = "select top 1 Sex as PatSex, Age as PatAge, PatName,PatID,AccessionNo,studyUID from pacs_study where AccessionNo='%s'" % AccessionNo
    result = ws.exec_sql(sql_pat_info)
    pat_info = result.get('string', {}).get('NewDataSet', {}).get('DataList', {}) if result else {}
    print '>>>>>>>>>>patient info'
    print json.dumps(pat_info, indent=2) if pat_info else json.dumps(result, indent=2) if result else ''

    sql_film_uid = """
  SELECT C.imageuid as objectUID,B.seriesuid as seriesUID,A.studyuid as studyUID FROM pacs_study A,pacs_series B,pacs_image C
  WHERE studyuid='{studyuid}'
  AND B.studyid=A.studyid
  AND C.studyid=A.studyid
  AND C.SeriesID=B.SeriesID
  AND B.Modality like '%FILM%'
  """.format(studyuid=studyuid)

    result = ws.exec_sql(sql_film_uid)
    film_info = result.get('string', {}).get('NewDataSet', {}).get('DataList', {}) if result else {}
    film_info = {'films': film_info} if film_info else {}
    print '>>>>>>>>>>film info'
    print json.dumps(film_info, indent=2) if film_info else json.dumps(result, indent=2) if result else ''

    upload_data = {}
    if pat_info and film_info:
        upload_data.update(pat_info)
        upload_data.update(film_info)
        upload_data.update({'HospCode': hospcode})

    return upload_data


if __name__ == '__main__':
    # 六院
    hospital_code = '9999'
    url = 'http://101.231.40.242:7345/pem/service.asmx'
    studyuid = '1.3.6.1.4.1.19439.0.108707908.20160615084008.1750.15705743'
    studyuid = '1.3.6.1.4.1.19439.0.108707908.20160118074643.1697.15310500'

    # local test
    url = 'http://180.168.156.226:30025/PEM/service.asmx'
    # studyuid = '1.2.840.1.19439.0.100000000.20150421094558.1517.10000.62502'

    upload_data = query_pat_info(
        ws_url=url, studyuid=studyuid, hospcode=hospital_code)

    # if upload_data:
    #     upload_film_data(upload=False, **upload_data)
        # upload_film_info()

    # ws = WS_API(url)

    # result = ws.exec_sql('select top 1 * from pacs_study order by inserttime desc')
    # # result = ws.exec_sql("update pacs_study set HospName='医疗结构'")
    # print json.dumps(result, indent=2) if result else ''


