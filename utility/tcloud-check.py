# coding=utf-8

from __future__ import unicode_literals
from datetime import date, timedelta
from progressbar import ProgressBar, SimpleProgress
import urllib
import socket
import requests
import time
import HTMLParser
import textwrap

from prettytable import PrettyTable 
import xmltodict

'''
测试各医院云影的网络状态是否正常、病人列表是否为空
'''

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

url_strip = lambda urlstr : urlstr.replace('http://','').strip('/ \t\r\n\\')
webservice_url = lambda url: 'http://'+url_strip(url)+'/PEM/service.asmx' if url_strip else None
tcloud_url = lambda url: 'http://'+url_strip(url)+'/tcloud/imageviewer.html' if url_strip else None

class WS_API():
    def __init__(self, url):
        self.ws_url = url

    def studycount_of_today(self):
        sql = 'select count(*) from pacs_study where studytime between \'{0}\' and \'{1}\''
        sql = sql.format(date.today(),date.today()+timedelta(1))
        result = self.exec_sql(sql)
        if result:
            return result.get('string', {}).get('NewDataSet',{}).get('DataList', {}).get('Column1', '0')
        return 0

    def studycount(self):
        sql = 'select count(*) from pacs_study'
        sql = sql.format(date.today(),date.today()+timedelta(1))
        result = self.exec_sql(sql)
        if result:
            return result.get('string', {}).get('NewDataSet',{}).get('DataList', {}).get('Column1', '0')
        return 0

    def latest_studytime(self):
        sql = 'select top 1 studytime from pacs_study order by studytime desc'
        sql = sql.format(date.today(),date.today()+timedelta(1))
        result = self.exec_sql(sql)

        
        error = result.get('string', {}).get('#text','') if result else ''

        # import json
        # print json.dumps(result, indent=2)
        studytime = ''
        if result:
            studytime = result.get('string', {}).get('NewDataSet',{}).get('DataList', {}).get('studytime', '')
            studytime = studytime.replace('T',' ')[:-6]
            # 2016-05-11T16:44:43+08:00
        return studytime, error

    def exec_sql(self, sql):
        header = {'Content-Disposition': 'form-data'}
        content = {'SQLString': sql}
        try:
            ret = requests.post(self.ws_url+'/psp_ExecuteSQL', data=content, headers=header)
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

def telnet(ip, port):  
    '''
    telnet 
    '''
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
    sk.settimeout(500)    
    try:    	
        if type(port) != int:
            port = int(port)
        # start = time.time()
        sk.connect((ip,port)) 
        sk.close()  
        # print time.time()-start
        return True  
    except Exception, e:    
        print e
        sk.close()
    return False


PROXIES = {
  "http": "http://127.0.0.1:8787",
  "https": "http://127.0.0.1:8787",
}

def web_check(url,timeout=2):
    try:
        errdesc = ''
        is_success = ''

        ret = requests.head(url, timeout=timeout) # , proxies=PROXIES
        if ret.status_code != 200:
            errdesc = 'Connect Error:'+str(ret.status_code)
    except ConnectTimeout:
        errdesc = 'Connect Timeout'
    except Exception as e:
        errdesc = 'Conncet Error:'+e.message
    finally:
        return True if not errdesc else False, errdesc


def url_parse(url):
    if url:
        url = url.replace('http://','')
        ret = url.split(':')
        ip = ret[0]
        port = ret[1] if len(ret)>1 else 80
        return ip, port
    return None, None

def main():
    # init table format
    table = PrettyTable([u'医院名称', u'网络状态', u'网络延迟', u'今日检查数量',u'历史检查数量',u'最近检查时间', u'云影地址', u'错误信息'],
        header=True)  
    table.align[u"医院名称"] = "l"    
    table.align[u"云影地址"] = "l"     
    table.align[u"错误信息"] = "l"     
    table.padding_width = 1
    
    #init progress
    pbar = ProgressBar(widgets=[SimpleProgress()], maxval=len(tcloud_conf)).start()
    index = 0
    

    for tcloud in tcloud_conf:
        index+=1
        pbar.update(index)
        
        name = tcloud.get('hosp','')
        count = 0 # study count
        count_of_all = 0
        network = u'×'
        errdesc = ''
        latest_time = ''
        time_tcloud = ''
        time_ws = ''

        addr = tcloud.get('addr','')
        tcloud = tcloud_url(addr)

        time_start = time.time()
        conn, errdesc = web_check(tcloud) 
        time_tcloud =  '%.3f' % (time.time()-time_start)

        if conn:
            network = u'√'

            # study count
            ws = webservice_url(addr)
            if ws:
                time_start = time.time()
                count = WS_API(ws).studycount_of_today()
                latest_time, errdesc =  WS_API(ws).latest_studytime()
                count_of_all =  WS_API(ws).studycount()
                time_ws =  '%.3f' % ((time.time()-time_start)/2.0)
        else:
            network = u'×'
        errdesc = textwrap.fill(errdesc,40)
        table.add_row([name, network, time_tcloud+'/'+ time_ws,count, count_of_all,latest_time,tcloud, errdesc])

    pbar.finish()

    tb_data = table.get_string()
    tb_len = tb_data.index('\n')
    title = u'PACS+各医院云影像当日服务状态'
    title_len = (len(title.encode('utf-8'))+len(title))/2
    if title_len<tb_len:
        title = (tb_len-title_len)/2*' '+title
    print '',
    print title
    print tb_data

if __name__ == '__main__':
    main()

    import os
    os.system('pause')

    
