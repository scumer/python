# coding=utf-8

import sys, os
from ConfigParser import ConfigParser

import win32serviceutil
import win32service
import win32event
import winerror
import servicemanager
import os,sys

from ElectroCardioService import RunSvc, StopSvc, InitLogger


app_path = sys.path[0] if not getattr(sys, 'frozen', False) else os.path.dirname(sys.executable)
# print sys.path[0], os.path.dirname(sys.executable), getattr(sys, 'frozen', False)
os.chdir(app_path)
print 'SvcDoRun Directory: '+os.getcwd()

# read service config
config = ConfigParser(defaults={'name':'Winning ElectroCardio Service', 'port':'9000'})
config.read('./config.ini')
config.add_section('SERVICE') if not config.has_section('SERVICE') else None
service_name = config.get('SERVICE', 'name')
port = config.getint('SERVICE', 'port')


class ElectroCardioWinSvc(win32serviceutil.ServiceFramework):
    """NT Service."""

    _svc_name_ = service_name.replace(' ','')
    _svc_display_name_ = service_name
    _svc_description_ = 'Part of Winning PACS+, Handle Third Report and Medical Image'

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)

    def SvcDoRun(self):
        InitLogger()
        RunSvc(port=port, debug=False)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)     
        StopSvc()


if __name__ == '__main__':
     if len(sys.argv) == 1:
         try:
            servicemanager.Initialize()
            servicemanager.PrepareToHostSingle(ElectroCardioWinSvc)
            servicemanager.StartServiceCtrlDispatcher()
         except win32service.error, details:
             if details[0] == winerror.ERROR_FAILED_SERVICE_CONTROLLER_CONNECT:
                 win32serviceutil.usage()
     else:
         win32serviceutil.HandleCommandLine(ElectroCardioWinSvc)
    # win32serviceutil.HandleCommandLine(ElectroCardioWinSvc)
    
     