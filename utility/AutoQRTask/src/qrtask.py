# coding=utf-8

import os, sys
import time
import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime,timedelta

import gdcm

from dbmodel import MSSQL
from config import Configure

work_dir = lambda: os.path.dirname(sys.executable) if getattr(sys, 'frozen', False) else sys.path[0]
os.chdir(work_dir())

#########################
WORK_DATE = datetime.now()
RUN_TASK = True

QRSCP_CONFIG = { 
               'callingAE':Configure().get('QRSCP', 'CallingAE'), 
               'callAE':Configure().get('QRSCP', 'CalledAE'), 
               'port':int(Configure().get('QRSCP', 'Port')), 
               'host':Configure().get('QRSCP', 'Host')
               }

studyUIDTag = gdcm.Tag(0x0020,0x000D)
studyDateTag = gdcm.Tag(0x0008,0x0020)
#########################

def init_logger():
    if not os.path.exists('./log'):
        os.mkdir('./log')

    logfile = TimedRotatingFileHandler('./log/qrtask.log', when='D', backupCount=5)
    formatter = logging.Formatter('[%(asctime)s %(funcName)s:%(lineno)d %(levelname)5s] %(message)s', '%Y-%m-%d %H:%M:%S')
    logfile.setFormatter(formatter)
    logging.getLogger('').setLevel(logging.INFO)
    logging.getLogger('').addHandler(logfile) 

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('[%(levelname)s] %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)


def getQuery(kwargs):
    queryKeys = gdcm.DataSet()
    for key in kwargs:
        de = gdcm.DataElement()
        de.SetTag(key)
        de.SetByteValue(kwargs[key],gdcm.VL(len(kwargs[key])))
        queryKeys.Insert(de)

    # ePatientRootType,eStudyRootType   
    # ePatient,eStudy,eSeries,eImage 
    query = gdcm.CompositeNetworkFunctions_ConstructQuery(gdcm.eStudyRootType,gdcm.eStudy,queryKeys,False) 
    return query


def findSCU(studytime):
    query = getQuery(
        {
            studyDateTag:studytime
        })
    res = gdcm.DataSetArrayType()
    findok = gdcm.CompositeNetworkFunctions_CFind(QRSCP_CONFIG['host'],QRSCP_CONFIG['port'],query,res,QRSCP_CONFIG['callingAE'],QRSCP_CONFIG['callAE'])
    # print 'result len:', res.size()
    # for dataset in res:
    #     print dataset.GetDataElement(studyUIDTag)

    return findok, res


def getQueryDate():
    # 格式化检查起止日期
    curtime = datetime.now()
    timedlt = int(Configure().get_default('Service', 'TimeDelta', '1'))
    timespan = timedelta(days=timedlt)
    
    studydate_start = datetime.strftime(curtime-timespan, '%Y%m%d')
    # studydate_end = datetime.strftime(curtime, '%Y%m%d')

    return studydate_start


def Start():
    gdcm.Trace_DebugOn()
    gdcm.Trace_SetStreamToFile('./log/qrscu.log')
    init_logger()

    runtime = Configure().get('Service','runtime')

    logging.info(u'服务启动成功')

    while RUN_TASK:
        # 根据当前日期和WORK_DATE对比判断是否需要更新TaskState
        global WORK_DATE
        curtime = datetime.now()
        nowdate = datetime.strftime(curtime, '%Y%m%d')
        workdate = datetime.strftime(WORK_DATE, '%Y%m%d')
        if nowdate > workdate:
            Configure().set('Service','TaskState','0')
            # global WORK_DATE
            WORK_DATE = curtime
            logging.info('update work date')

        # 根据当前时间和配置的运行时间已经TaskState 判断是否执行本次任务
        taskstate = Configure().get('Service','TaskState')
        nowtime = datetime.strftime(curtime, '%H:%M:%S')
        if (nowtime < runtime) or taskstate != '0':
            time.sleep(60)
            continue

        logging.info(u'开始执行当天任务')

        # 开始查询
        try:
            studydate =getQueryDate()
            # studydate = '20101009-20120101'
            logging.info(u'查询检查日期:'+studydate)

            bok, res = findSCU(studydate)
            studylist = [] 
            if bok:
                for dataset in res:
                    studylist.append(str(dataset.GetDataElement(studyUIDTag).GetValue()))

                logging.info(u'C-Find查询成功！检查数量为:'+str(res.size()))
                logging.info(studylist) if len(studylist) < 20 else logging.info('\n{0}...{1}'.format(studylist[:20],studylist[-20:]))
                    
            else:
                logging.error(u'C-Find查询失败!')
                continue    
        except Exception, e:
            logging.exception(e)
            time.sleep(60)
            continue

        # 查询结果入库
        try:
            if studylist:
                MSSQL().ExecMany("INSERT INTO QrStudyUid (StudyUID) VALUES (%s)", studylist)
            Configure().set('Service','TaskState','1')
            logging.info(u'入库结束！今日任务结束！')
        except Exception, e:
            logging.info(u'入库失败！')
            logging.exception(e)

        time.sleep(60)
    logging.info(u'停止任务')
        

def Stop():
    global RUN_TASK
    RUN_TASK = False


if __name__ == "__main__":
    # gdcm.Trace_DebugOn()
    Start()
    # Stop()
    
