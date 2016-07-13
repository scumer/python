# coding=utf-8

import sys, os

import win32serviceutil
import win32service
import win32event
import winerror
import servicemanager

import multiprocessing as mp
from config import Configure
import THDataUP


app_path = os.path.dirname(sys.executable) if getattr(sys, 'frozen', False) else sys.path[0]
# print sys.path[0], os.path.dirname(sys.executable), getattr(sys, 'frozen', False)
os.chdir(app_path)
# print 'Svc Work Directory: '+os.getcwd()


class THDataUPService(win32serviceutil.ServiceFramework):
    """NT Service."""
    
    # _svc_name_ = service_name.replace(' ','')
    # _svc_display_name_ = service_name

    _svc_name_ = 'THDataUP'
    _svc_display_name_ = 'THDataUP'
    _svc_description_ = 'Part of Winning PACS+, Upload Patient Data To PACS+ Platform'

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)

    def SvcDoRun(self):
        THDataUP.Run()

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)     
        THDataUP.Stop()


if __name__ == '__main__':
    mp.freeze_support()
    if len(sys.argv) == 1:
        try:
            servicemanager.Initialize()
            servicemanager.PrepareToHostSingle(THDataUPService)
            servicemanager.StartServiceCtrlDispatcher()
        except win32service.error, details:
            if details[0] == winerror.ERROR_FAILED_SERVICE_CONTROLLER_CONNECT:
                win32serviceutil.usage()
    else:
        win32serviceutil.HandleCommandLine(THDataUPService)
    # win32serviceutil.HandleCommandLine(THDataUPService)
