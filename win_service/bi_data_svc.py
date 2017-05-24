# coding=utf-8

import sys, os

import win32serviceutil
import win32service
import win32event
import winerror
import servicemanager

import bi_data

os.chdir(os.path.dirname(sys.executable) if getattr(sys, 'frozen', False) else sys.path[0])
print 'Svc Work Directory: '+os.getcwd()

class WinService(win32serviceutil.ServiceFramework):
    """NT Service."""

    _svc_name_ = 'PACS4BI'
    _svc_display_name_ = 'PACS4BI'
    _svc_description_ = u'UPDATE BI PACS Data'

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

    def SvcDoRun(self):
        bi_data.start_task(self.hWaitStop)
        # win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)  # 通知SCM停止这个过程   
        win32event.SetEvent(self.hWaitStop)  # 设置事件
        # bi_data.stop_task()  
        


if __name__ == '__main__':
    if len(sys.argv) == 1:
        try:
            servicemanager.Initialize()
            servicemanager.PrepareToHostSingle(WinService)
            servicemanager.StartServiceCtrlDispatcher()
        except win32service.error, details:
            if details[0] == winerror.ERROR_FAILED_SERVICE_CONTROLLER_CONNECT:
                win32serviceutil.usage()
    else:
        win32serviceutil.HandleCommandLine(WinService)

