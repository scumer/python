# coding=utf-8

import win32serviceutil
import win32service
import win32event
import winerror
import servicemanager
import os,sys

class PyWinService(win32serviceutil.ServiceFramework):
    #_exe_name_ = 'PyWinService'
    _svc_name_ = 'PyWinService2'
    _svc_display_name_ = 'PyWinService2'
    _svc_description_ = 'svc description'
   
    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        #self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.run = True
    
    def SvcStop(self):
        # service stop
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        #win32event.SetEvent(self.hWaitStop)
        
        self.run = False
   
    def SvcDoRun(self):
        
        import logging
        from logging.handlers import TimedRotatingFileHandler
        formatting = '%(asctime)s:%(levelname)s:%(name)s:%(message)s'
        logfile = TimedRotatingFileHandler('PyWinService2.log', when='D', backupCount=3)
        logfile.setLevel(logging.INFO)
        formatter = logging.Formatter(formatting)
        logfile.setFormatter(formatter)
        #logging.getLogger('').setLevel(logging.INFO)
        logging.getLogger('').addHandler(logfile)
        
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        console.setLevel(logging.INFO)
        logging.getLogger('').addHandler(console)
        
        
        logging.getLogger('').setLevel(logging.INFO)
        
        while self.run:
            import time
            time.sleep(2)
            logging.info('PyWinService:'+time.ctime())

            
            
if __name__ == '__main__':
    if len(sys.argv) == 1:
        try:
            servicemanager.Initialize()
            servicemanager.PrepareToHostSingle(PyWinService)
            servicemanager.StartServiceCtrlDispatcher()
        except win32service.error as details:
            if details[0] == winerror.ERROR_FAILED_SERVICE_CONTROLLER_CONNECT:
                win32serviceutil.usage()
            print details
    else:
        win32serviceutil.HandleCommandLine(PyWinService)    
            
        
        
        