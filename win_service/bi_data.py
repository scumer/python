# coding=utf-8

"""
《调用前置机pacs-ws倒腾PACS影像数据到BI系统-邛崃版》

套路：
    定时执行 01:00点,

    删除昨天(或者指定时间段)的统计数据
    将昨天的统计数据(或者指定时间段)加到BI库
    执行存储过程更新数据

    日志记录操作状态

    定时执行...
"""


import logging
import os, sys
import time
import thread
from datetime import date, timedelta, datetime

import win32event
import requests
import HTMLParser
import xmltodict
import pymssql
import schedule

from config import Configure
from dbconnect import MSSQL

qionglai = {
'450850053':u'邛崃市夹关镇中心卫生院',
'450849271':u'邛崃市牟礼镇中心卫生院',
'450860884':u'邛崃市羊安镇中心卫生院',
'450860905':u'邛崃市社区卫生服务中心',
'450860921':u'邛崃市平乐镇中心卫生院',
'450850221':u'邛崃市天台山镇卫生院',
'450850387':u'邛崃市南宝山镇卫生院',
'450850029':u'邛崃市回龙镇卫生院',
'450850125':u'邛崃市卧龙镇卫生院',
'450850133':u'邛崃市火井镇卫生院',
'450850141':u'邛崃市冉义镇卫生院',
'45085015x':u'邛崃市大同乡卫生院',
'450850168':u'邛崃市临济镇卫生院',
'450850205':u'邛崃市高埂镇卫生院',
'45085023x':u'邛崃市高何镇卫生院',
'450850248':u'邛崃市孔明乡卫生院',
'450850272':u'邛崃市茶园乡卫生院',
'450850280':u'邛崃市宝林镇卫生院',
'450850301':u'邛崃市水口镇卫生院',
'45085031x':u'邛崃市道佐乡卫生院',
'450850328':u'邛崃市桑园镇卫生院',
'450850352':u'邛崃市前进镇卫生院',
'777478687':u'邛崃市固驿镇卫生院',
'450860761':u'邛崃市人民医院'}


wshandler = None


def init_logger():
    if not os.path.exists('./log'):
        os.mkdir('./log')

    from logging.handlers import TimedRotatingFileHandler, RotatingFileHandler
    # logfile = TimedRotatingFileHandler('./log/'+'main.log', when='D', backupCount=5)
    logfile = RotatingFileHandler('./log/'+'main.log', maxBytes=10*1024*1024, backupCount=10)
    formatter = logging.Formatter('[%(asctime)s %(funcName)s:%(lineno)d %(levelname)5s] %(message)s', '%Y-%m-%d %H:%M:%S')
    logfile.setFormatter(formatter)
    logging.getLogger('').setLevel(logging.INFO)
    logging.getLogger('').addHandler(logfile) 

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('[%(asctime)s-%(levelname)5s] %(message)s', '%H:%M:%S')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)


def init():
    init_logger()
    ws = Configure().get('Common', 'ws') + '/PEM/service.asmx'
    logging.info('ws addr:'+ws)
    global wshandler
    wshandler = WSHandler(ws)


class WSHandler():
    """
    """
    def __init__(self, url):
        self.ws_url = url

    def exec_sql(self, sql):
        header = {'Content-Disposition': 'form-data'}
        content = {'SQLString': sql}
        retry_times = 3

        while retry_times:
            try:
                ret = requests.post(self.ws_url+'/psp_ExecuteSQL', data=content, headers=header, timeout=3, verify=False)
                ret.raise_for_status()
                html_parser = HTMLParser.HTMLParser()
                result = html_parser.unescape(ret.text)
                
                dresult = xmltodict.parse(result)
                # print dresult
                return dresult
            except Exception, e:
                logging.exception(e)
                retry_times -= 1
            logging.warning('ws retry:'+str(retry_times))
            time.sleep(5)
        
        return None


def get_image_study_count(start_date='1900-01-01', end_date='2020-01-01'):
    zbmc_study = u'检查数量'
    zbdm_study = '200.001'

    zbmc_image = u'图像数量'
    zbdm_image = '200.002'

    time_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    query_sql = """select count(*) as studycount, Convert(varchar(10), studytime,112) as studydate, HospCode as hospcode , Modality as modaity, SUM(ImageCountInStudy) as imagecount 
                   from Pacs_Study 
                   where Modality='DX' and hospcode in ({}) and studytime between '{}' and '{}' 
                   group by Convert(varchar(10),studytime,112),HospCode,Modality""".format(str(qionglai.keys())[1:-1], start_date, end_date)

    logging.info('query_sql:'+query_sql)
     
    res = wshandler.exec_sql(query_sql)
    if not res:
        logging.warning('query none from webservice')

    res = res.get('string', {}).get('NewDataSet',{}).get('DataList', {})
    res = res if type(res) == list else [res]

    zb_study = []
    zb_image = []
    for r in res:
        hosp = r.get('hospcode')
        if  hosp:
            jgbm = sjjgdm = hosp
            ksdm = jbdm = hosp+'-DX'
            # add_sql += u"('{0}','{1}','{2}','{3}','{4}',{5},'{6}','{7}','{8}','{9}'),".format(jgbm,ksdm,r['studydate'],zbdm,zbmc,r['imagecount'],jbdm,sjjgdm,r['studydate'],time_now)
            zb_study.append((jgbm,ksdm,r['studydate'],zbdm_study,zbmc_study,r['studycount'],jbdm,sjjgdm,r['studydate'],time_now))
            zb_image.append((jgbm,ksdm,r['studydate'],zbdm_image,zbmc_image,r['imagecount'],jbdm,sjjgdm,r['studydate'],time_now))
    
    return zb_study, zb_image


def update_image_study_count(start_date='19000100', end_date='20300101'):
    logging.info('Time Span:[{}-{})'.format(start_date, end_date))

    del_sql = "delete from FACT_YLFW_MX_KSRB where zbdm in ('200.001', '200.002') and daykey >= %s and daykey < %s"
    zb_study, zb_image = get_image_study_count(start_date, end_date)
    logging.info(zb_study)
    logging.info(zb_image)

    add_sql = 'insert into FACT_YLFW_MX_KSRB (JGBM,KSDM,DAYKEY,ZBDM,ZBMC,ZBZ,JBDM,SJJBDM,SJDM,XT_XGRQ) values (%s,%s,%s,%s,%s,%d,%s,%s,%s,%s)'

    try:
        logging.info('start delete and insert data')
        # 删除指定日期时间段的数据，然后更新数据
        with pymssql.connect(**MSSQL().conn_info) as conn:
            with conn.cursor(as_dict=True) as cursor:
                cursor.execute(del_sql, (start_date, end_date))
                cursor.executemany(add_sql, zb_study+zb_image)
                conn.commit()
    except pymssql.Error as e:
        logging.exception(e)
    else:
        # 执行相应存储过程，更新数据
        try:
            logging.info('start proc USP_BI_BBSJ_HZ')
            MSSQL().ExecProc("USP_BI_BBSJ_HZ", ('<PARAS><JGBM>+86</JGBM></PARAS>',))
            MSSQL().ExecProc("USP_BI_BBSJ_SHJHZ", ('<PARAS><JGBM>+86</JGBM></PARAS>',))
        except pymssql.Error as e:
            logging.exception(e)


def update_bi_data():
    logging.info('start update_bi_data!')
    
    today = date.today()
    date_today = today.strftime('%Y%m%d')
    date_last = (today-timedelta(days=1)).strftime('%Y%m%d')

    try:
        update_image_study_count(start_date=date_last, end_date=date_today)
    except Exception as e:
        logging.exception(e)


def main(hWaitStop=None):
    init()
    logging.info('start_task')

    schedule.every().day.at("01:00").do(update_bi_data)
    while True:
        try:
            schedule.run_pending()
            stop = win32event.WaitForSingleObject(hWaitStop, 3000)
            if stop == win32event.WAIT_OBJECT_0:
                logging.info('stop_task')
                break
        except Exception as e:
            logging.exception(e)


def start_task(hWaitStop):
    main(hWaitStop)


if __name__ == '__main__':
    init()

    args = sys.argv[1:]
    if args:
        start_date = args[0]
        end_date = args[1] if len(args)>1 else '20300101'
        print "Time Span:[{0}-{1})".format(start_date, end_date)
        update_image_study_count(start_date=start_date, end_date=end_date)
    # main()
    # start_task()



"""
select Convert(varchar(10), studytime,112) as studydate, HospCode as hospcode , Modality, SUM(ImageCountInStudy) as imagecount
from Pacs_Study
where HospCode='450849271'
and Modality='DX'
group by Convert(varchar(10),studytime,112),HospCode,Modality
order by studydate

select count(*) as studycount, Convert(varchar(10), studytime,112) as studydate, HospCode as hospcode , Modality as modaity, SUM(ImageCountInStudy) as imagecount
from Pacs_Study
where HospCode='450849271'
and Modality='DX'
group by Convert(varchar(10),studytime,112),HospCode,Modality
"""
