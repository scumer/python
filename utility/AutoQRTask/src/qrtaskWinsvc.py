# coding=utf-8

import sys, os

import win32serviceutil
import win32service
import win32event
import winerror
import servicemanager

import multiprocessing as mp
import qrtask


app_path = os.path.dirname(sys.executable) if getattr(sys, 'frozen', False) else sys.path[0]
os.chdir(app_path)
# print 'Svc Work Directory: '+os.getcwd()


class QRTaskService(win32serviceutil.ServiceFramework):
    """NT Service."""

    _svc_name_ = 'QRTask'
    _svc_display_name_ = 'QRTask'
    _svc_description_ = 'auto query studyuid and insert into auqr task queue'

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)

    def SvcDoRun(self):
        qrtask.Start()

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)     
        qrtask.Stop()


if __name__ == '__main__':
    mp.freeze_support()
    if len(sys.argv) == 1:
        try:
            servicemanager.Initialize()
            servicemanager.PrepareToHostSingle(QRTaskService)
            servicemanager.StartServiceCtrlDispatcher()
        except win32service.error, details:
            if details[0] == winerror.ERROR_FAILED_SERVICE_CONTROLLER_CONNECT:
                win32serviceutil.usage()
    else:
        win32serviceutil.HandleCommandLine(QRTaskService)

