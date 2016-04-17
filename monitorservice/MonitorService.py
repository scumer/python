#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：TA服务监控(服务状态，磁盘状态)
"""
import os
import ConfigParser
import logging
import sys
import base64
import socket
import time
import sched
import threading
import urllib,io,shutil
from threading import Timer
from logging.handlers import RotatingFileHandler
from BaseHTTPServer import HTTPServer,BaseHTTPRequestHandler

import gdcm
import pyodbc
import odbc_
# import sqlmod_


#==============================================================================
# Globals
#==============================================================================
LOGFILENAME                = 'MonitorService.log'
DB_MONITORINFO_TABLE       = 'Pacs_MonitorInfo'
DICOM_SERVICE_NEED_MONITOR = ['StorageNet', 'QRSCP', 'Worklist']
_logger          = None
_winpacs         = None
_worklistport    = 5000
_httpport        = 8000
_timer           = 60*60  #1小时
#==============================================================================
# 配置文件相关
#==============================================================================
CFG_FILE_NAME         = 'MonitorService.ini'
DB_CFG_FILENAME       = 'DBConnect.ini'

CFG_COMMON_SECTION    = 'Monitor'
CFG_COMMON_VOLUMENAME = 'VolumeName'

CFG_DB_SECTION        = 'ODBC'
# CFG_DB_SERVERNAME   = 'Server'
CFG_DB_DSN            = 'DSN'  
CFG_DB_USERNAME       = 'DBUser'
CFG_DB_PASSWORD       = 'DBPassword'
# CFG_DB_DATABASE       = 'DataBase'

CFG_LOG_SECTION       = 'Log'
CFG_LOG_PATH          = 'Path'
CFG_LOG_LEVEL         = 'Level'

def service_init():
    curModulePath = GetAppPath()

    config = ConfigParser.ConfigParser()
    cfgFileName = os.path.join(curModulePath, CFG_FILE_NAME)
    config.read(cfgFileName)

    """
    日志配置
    """
    logPath = curModulePath
    logLevel = logging.INFO
    try:
        if config.has_section(CFG_LOG_SECTION):
            if config.has_option(CFG_LOG_SECTION, CFG_LOG_PATH):
                logPath = config.get(CFG_LOG_SECTION, CFG_LOG_PATH)
            if config.has_option(CFG_LOG_SECTION, CFG_LOG_LEVEL):
                logLevel = config.getint(CFG_LOG_SECTION, CFG_LOG_LEVEL)
    except Exception, e:
        pass

    if logPath == '':
        logPath = curModulePath
    if not os.path.exists(logPath):
        os.makedirs(logPath)
    logName = os.path.join(logPath, LOGFILENAME)

    global _logger
    _logger = CreateLogger(logName, logLevel)

    """
    读取WorkList服务端口
    """
    try:
        if config.has_section('Worklist'): 
            if config.has_option('Worklist', 'port'):               
                port = config.getint('Worklist', 'port')
                global _worklistport
                _worklistport = port
    except Exception, e:
        _logger.error(str(e))   
  
    """
    读取http服务端口
    """
    try:
        if config.has_section('Http'): 
            if config.has_option('Http', 'port'):               
                port = config.getint('Http', 'port')
                global _httpport
                _httpport = port
    except Exception, e:
        _logger.error(str(e)) 

    """
    读取监控执行间隔时间
    """
    try:
        if config.has_section('Timer'): 
            if config.has_option('Timer', 'interval'):               
                time = config.getfloat('Timer', 'interval')
                global _timer
                _timer = time*60
    except Exception, e:
        _logger.error(str(e)) 
    
    """
    数据库初始化
    """
    try:
        config = ConfigParser.ConfigParser()
        cfgFileName = os.path.join(curModulePath, DB_CFG_FILENAME)
        if not os.path.exists(cfgFileName):
            _logger.error("DB ini file:%s doesn't exist!" % (cfgFileName))
            return False
        config.read(cfgFileName)
        DSN      = config.get(CFG_DB_SECTION, CFG_DB_DSN)
        UserName = config.get(CFG_DB_SECTION, CFG_DB_USERNAME)
        PassWord = config.get(CFG_DB_SECTION, CFG_DB_PASSWORD)
        # DataBase = config.get(CFG_DB_SECTION, CFG_DB_DATABASE)
        PassWord = base64.b64decode(PassWord)

        global _winpacs
        _winpacs = odbc_.MSSQL(DSN, UserName, PassWord)
    except Exception, e:
        _logger.exception('Init DataBase Error!')
        return False
    
def GetDiskInfo(VolumeName):
    if VolumeName == '' or VolumeName == None:
        return ''
    _logger.info('DiskName:%s' % (VolumeName))

    try:
        diskinfo = {}
        if os.name == 'nt': #windows
            import win32api
            info = win32api.GetDiskFreeSpaceEx(VolumeName)
            free  = info[0]/1024/1024/1024
            total = info[1]/1024/1024/1024
            diskinfo =  {'total':total,'free':free}
        else:   #'posix'
            hddinfo = os.statvfs(VolumeName)
            total   = hddinfo.f_frsize * hddinfo.f_blocks
            free    = hddinfo.f_frsize * hddinfo.f_bavail
            diskinfo = {'total':total/1024/1024/1024,'free':free/1024/1024/1024}
       
        servicetype = 1
        hostname = socket.gethostname()
        localIP = GetLocalIP()
        
        #根据服务器hostname ip hosttype等确认是要插入新数据还是update数据
        sqlstr = "SELECT * FROM %s WHERE Host='%s' AND IP='%s' AND HostType=%d" % (DB_MONITORINFO_TABLE, hostname, localIP, servicetype)
        resList = _winpacs.ExecQuery(sqlstr)
        if resList:     #查询结果不为空，update数据
            sqlstr = "UPDATE %s SET SpaceTotal=%d, SpaceLeft=%d, HttpPort=%d WHERE Host='%s' AND IP='%s' AND HostType=%d" % (DB_MONITORINFO_TABLE, diskinfo['total'], diskinfo['free'], _httpport, hostname, localIP, servicetype)
            _winpacs.ExecNonQuery(sqlstr) 
        else:           #insert数据
            sqlstr = "INSERT INTO %s (Host, IP, HostType, SpaceTotal, SpaceLeft, HttpPort)VALUES('%s', '%s', %d, %d, %d, %d)" % (DB_MONITORINFO_TABLE, hostname, localIP, servicetype, diskinfo['total'], diskinfo['free'], _httpport)          
            _winpacs.ExecNonQuery(sqlstr) 

    except Exception as e:
        _logger.error(e)
        return None

def CheckTAService(hostName, portNo, aetitle='GDCMSCU', call='ANY-SCP'):
    ret = False
    try:
        cecho = gdcm.CompositeNetworkFunctions()
        ret   = cecho.CEcho(hostName, portNo, aetitle, call)
    except Exception, e:
        _logger.error(e.message)
        return False
    return ret

def CreateLogger(filename = 'tmp.log', logLevel = logging.ERROR):
    logger    = logging.getLogger()
    # handler   = logging.FileHandler(filename)
    # formatter = logging.Formatter('[%(asctime)s %(funcName)s() line:%(lineno)d %(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S') 
    
    # handler.setFormatter(formatter)
    # logger.addHandler(handler)
    # logger.setLevel(logLevel)
    Rthandler = RotatingFileHandler(filename, maxBytes=10*1024*1024,backupCount=5) #每个文件最大为10M，最多备份5个文件
    formatter = logging.Formatter('[%(asctime)s %(funcName)s() line:%(lineno)d %(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
    Rthandler.setFormatter(formatter)
    logger.addHandler(Rthandler)
    logger.setLevel(5)

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('[%(levelname)s]%(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    return logger 

def GetAppPath():
    app_path  = ''
    if getattr(sys, 'frozen', False):
        app_path  = os.path.dirname(sys.executable)
    else:
        app_path  = sys.path[0]
    return app_path

def GetLocalIP():
    if os.name == 'nt': #windows
        hostname = socket.gethostname()
        localIP = socket.gethostbyname(hostname)
    else:
        import fcntl
        import struct 
        ifname = 'eth0'
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        localIP = socket.inet_ntoa(fcntl.ioctl(s.fileno(),0x8915,struct.pack('256s', ifname[:15]))[20:24])
    return localIP  

def CheckServiceStatus():
    """
    根据hostname和servicename检测服务状态，并将检测结果写入数据库
    """
    hostname = socket.gethostname()
    localIP = GetLocalIP()
    #获取本机服务列表
    sqlstr = "SELECT module FROM PACS_TA6_Service WHERE host='%s'" % (hostname)
    resList = _winpacs.ExecQuery(sqlstr)
    servicelist = []
    for ret in resList:
        for module in ret:
            servicelist.append(str(module))
    servicelist = list((set(servicelist)))
    _logger.info('Dicom Service (Get From DB) In This Host:'+str(servicelist))

    for servicename in DICOM_SERVICE_NEED_MONITOR:
        # if servicename in DICOM_SERVICE_NEED_MONITOR:
            try:
                port = None
                if servicename == 'Worklist': # Worklist 不存在数据库中，单独处理
                    port = _worklistport
                    aetitle = 'ANY-SCP'
                else:
                    #get portNo
                    sqlgetport =  "SELECT property_value FROM PACS_TA6_Service WHERE host = '%s' AND module = '%s' AND property_name = 'Port'" % (hostname, servicename)
                    resList =_winpacs.ExecQuery(sqlgetport)
                    if not resList:
                        _logger.warn("Get Host:%s Service:%s PortNo Failed! Maybe Service Doesnt Exist in this Host" % (hostname, servicename))
                        # continue
                    else:
                        port = int(resList[0][0])

                    # get AETitle
                    sqlgetcall =  "SELECT property_value FROM PACS_TA6_Service WHERE host = '%s' AND module = '%s' AND property_name = 'AETitle'" % (hostname, servicename)
                    resList =_winpacs.ExecQuery(sqlgetcall)
                    if not resList:
                        aetitle = 'ANY-SCP'
                        _logger.warn("Get Host:%s Service:%s AETitle Failed! Maybe Service Doesnt Exist in this Host" % (hostname, servicename))
                        # continue
                    else:
                        aetitle = str(resList[0][0])

                if port and aetitle:
                    ret = CheckTAService(hostname, port, 'GDCMSCU', aetitle)
                    if not ret:
                        servicestatus = 0 # 0：服务挂了 1：服务正常
                        _logger.warn("C-Echo Service:%s Port:%s Failed!" % (servicename, port))
                    else:
                        servicestatus = 1
                else:
                    servicestatus = 0
                     
                servicetype = 1 #服务器类型 1：DICOM服务器（Net QR WL） 2：存储服务器 
                #根据服务器hostname ip hosttype等确认是要插入新数据还是update数据
                sqlstr = "SELECT * FROM %s WHERE Host='%s' AND IP='%s' AND HostType=%d AND DicomSvrType='%s'" % (DB_MONITORINFO_TABLE, hostname, localIP, servicetype, servicename)
                resList = _winpacs.ExecQuery(sqlstr)
                if resList:     #查询结果不为空，update数据
                    # UPDATE Pacs_MonitorInfo SET SpaceTotal=101,SpaceLeft=8 WHERE DicomSvrType='ne' OR  DicomSvrType='s'
                    sqlstr = "UPDATE %s SET DicomServiceStatus=%d, HttpPort=%d WHERE Host='%s' AND IP='%s' AND HostType=%d AND DicomSvrType='%s'" % (DB_MONITORINFO_TABLE, servicestatus, _httpport, hostname, localIP, servicetype, servicename)
                    _winpacs.ExecNonQuery(sqlstr) 

                else:          #insert数据
                    sqlstr = "INSERT INTO %s (Host, IP, HostType, DicomSvrType, DicomServiceStatus, HttpPort)VALUES('%s', '%s', %d, '%s', %d, %d)" % (DB_MONITORINFO_TABLE, hostname, localIP, servicetype, servicename, servicestatus, _httpport)
                    _winpacs.ExecNonQuery(sqlstr) 

            except Exception, e:
                _logger.exception('')

def doCheck():
    if _mutex.locked():
        return
    _mutex.acquire()
    # print '<pid>:',threading.current_thread()
    CheckServiceStatus()
    GetDiskInfo(GetAppPath())
    _mutex.release()

def TimerTask():
    doCheck()
    # print time.strftime('%H:%M:%S',time.localtime(time.time()))
    Timer(_timer, TimerTask).start() #Timer一次性定时
    # Timer(1, TimerTask).start() #Timer一次性定时

def SchedTask():
    print 'pid:', os.getpid(), threading.current_thread()
    CheckServiceStatus()
    GetDiskInfo(GetAppPath())
    # print time.strftime('%H:%M:%S',time.localtime(time.time()))
    schedule = sched.scheduler(time.time, time.sleep)
    schedule.enter(5, 0, SchedTask,())
    schedule.run()

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.process(2)
 
    def do_POST(self):
        pass
 
    def process(self,type):
        # if '?' in self.path:
        # 接收到GET请求后立即执行监控监控动作
        doCheck()

        #指定返回编码
        enc="UTF-8"
        retinfo = "ok"  # 返回信息
        retinfo = retinfo.encode(enc)
        f = io.BytesIO()
        f.write(retinfo)
        f.seek(0)
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=%s" % enc)
        self.send_header("Content-Length", str(len(retinfo)))
        self.end_headers()
        shutil.copyfileobj(f,self.wfile)

def main():
    try:
        if service_init() == False:
            _logger.error('service_init() Failed.')
            return
        global _mutex
        _mutex = threading.Lock()
        TimerTask()
        # SchedTask()

        #start http server
        server = HTTPServer(('', _httpport), MyRequestHandler)
        print 'started httpserver...'
        server.serve_forever()
    
    except KeyboardInterrupt:
        print 'Bye!'
        server.server_close()
        os._exit(0)
    except Exception, e:
        if _logger:
            _logger.exception('')
        else:
            fname = os.path.join(GetAppPath(), LOGFILENAME)
            logger = CreateLogger(fname)
            logger.exception('')

if __name__ == "__main__":
    main()