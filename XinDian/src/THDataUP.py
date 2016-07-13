# utf-8

import os,sys
import logging
import signal
import multiprocessing as mp
from logging.handlers import TimedRotatingFileHandler

from task import CardUpload, ReportUpload, FilmUpload
from config import Configure

TaskQueue = []


def Run():
    # init main log
    if not os.path.exists('./log'):
        os.mkdir('./log')

    formatter = logging.Formatter('[%(asctime)s P:%(process)-5d %(funcName)s:%(lineno)d %(levelname)5s] %(message)s', '%Y-%m-%d %H:%M:%S')
    logfile = TimedRotatingFileHandler('./log/'+'THDataUpload.log', when='D', backupCount=5)
    logfile.setLevel(logging.INFO)
    logfile.setFormatter(formatter)
    logging.getLogger('').setLevel(logging.INFO)
    logging.getLogger('').addHandler(logfile)

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('[MAIN-%(levelname)5s] %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

    try:
        # init global request
        proxy = Configure().get_default('Service', 'Proxy', None)
        if proxy:
            os.environ["HTTP_PROXY"] = proxy
            os.environ["HTTPS_PROXY"] = proxy

        # init all task
        TaskQueue.append(CardUpload(name='CardUpload'))
        TaskQueue.append(ReportUpload(name='ReportUpload'))
        TaskQueue.append(FilmUpload(name='FilmUpload'))

        for task in TaskQueue:
            task.start()

        logging.info('Start All Task:'+','.join([t.pname for t in TaskQueue]))
        
        for task in TaskQueue:
            task.join()

        logging.info('Stop All Task')
    except Exception, e:
        logging.exception(e)
        raise e


def Stop():
    logging.info('Get Stop Signal')
    for task in TaskQueue:
        task.endloop()
        # task.terminate()
        task.join()


if __name__ == '__main__':
    mp.freeze_support()
    try:
        Run()
    except KeyboardInterrupt:
        Stop()
    
    


 


    
