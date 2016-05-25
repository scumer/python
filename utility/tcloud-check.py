﻿# coding=utf-8

from __future__ import unicode_literals
from datetime import date, timedelta
from progressbar import ProgressBar, SimpleProgress
import urllib
import socket
import requests
import time
import HTMLParser

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
{'hosp': u'卢湾个渣渣', 'addr':'http://180.168.156.226:30025'},
{'hosp': u'龙华医院',   'addr':'http://180.169.35.28:30025'},
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

    def latest_studytime(self):
        sql = 'select top 1 studytime from pacs_study order by studytime desc'
        sql = sql.format(date.today(),date.today()+timedelta(1))
        result = self.exec_sql(sql)
        # import json
        # print json.dumps(result, indent=2)
        if result:
            studytime = result.get('string', {}).get('NewDataSet',{}).get('DataList', {}).get('studytime', '')
            studytime = studytime.replace('T',' ')[:-6]
            # 2016-05-11T16:44:43+08:00
            return studytime

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
    table = PrettyTable([u'医院名称', u'网络状态', u'今日检查数量',u'最近检查时间', u'云影地址', u'错误信息'],
        header=True)  
    table.align[u"医院名称"] = "l"    
    table.align[u"云影地址"] = "l"     
    table.padding_width = 1
    
    #init progress
    pbar = ProgressBar(widgets=[SimpleProgress()], maxval=len(tcloud_conf)).start()
    index = 0
    

    for tcloud in tcloud_conf:
        index+=1
        pbar.update(index)
        
        name = tcloud.get('hosp','')
        count = 0 # study count
        network = u'×'
        errdesc = ''
        latest_time = ''

        addr = tcloud.get('addr','')
        tcloud = tcloud_url(addr)

        ip, port = url_parse(addr)
        
        if telnet(ip, port):
            network = u'√'

            # study count
            ws = webservice_url(addr)
            if ws:
                # count = study_count_of_today(ws)
                count = WS_API(ws).studycount_of_today()
                latest_time =  WS_API(ws).latest_studytime()
        else:
            network = u'×'

        table.add_row([name, network, count, latest_time,tcloud, errdesc])

    pbar.finish()
    # print table.__unicode__()

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

    
