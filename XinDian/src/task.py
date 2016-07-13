# coding=utf-8

import time,os,sys
import logging
import json
import signal
import multiprocessing as mp
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime

import requests
from sqlalchemy.orm import sessionmaker, aliased
from sqlalchemy import text

from dbmodel import PatientInfo as PatCard, XDReport, Image, Series, Study
from dbconnect import DBSession
from config import Configure

# proxies = {
#   'http': 'http://10.10.1.10:3128',
#   'https': 'http://10.10.1.10:1080',
# }

# requests.get('http://example.org', proxies=proxies)

# 解决打包成exe后每个multiprocessing.Process产生两个进程的问题,但好像还是多一个进程
try:
    # Python 3.4+
    if sys.platform.startswith('win'):
        import multiprocessing.popen_spawn_win32 as forking
    else:
        import multiprocessing.popen_fork as forking
except ImportError:
    import multiprocessing.forking as forking

if sys.platform.startswith('win'):
    # First define a modified version of Popen.
    class _Popen(forking.Popen):
        def __init__(self, *args, **kw):
            if hasattr(sys, 'frozen'):
                # We have to set original _MEIPASS2 value from sys._MEIPASS
                # to get --onefile mode working.
                os.putenv('_MEIPASS2', sys._MEIPASS)
            try:
                super(_Popen, self).__init__(*args, **kw)
            finally:
                if hasattr(sys, 'frozen'):
                    # On some platforms (e.g. AIX) 'os.unsetenv()' is not
                    # available. In those cases we cannot delete the variable
                    # but only set it to the empty string. The bootloader
                    # can handle this case.
                    if hasattr(os, 'unsetenv'):
                        os.unsetenv('_MEIPASS2')
                    else:
                        os.putenv('_MEIPASS2', '')

    # Second override 'Popen' class with our modified version.
    forking.Popen = _Popen


class BaseService(mp.Process):
    """
    需要实现do_work内容,完成具体的业务流程，
    需要实例赋值upload_url
    调用endloop停止work
    """

    def __init__(self, group=None, target=None, name=None,  *args, **kwargs):
        super(BaseService, self).__init__(group=group, target=target, name=name, args = args, kwargs = kwargs)  
        self.exit = mp.Event()

        self.dbsession = None
        self.pname = name
        self.conf = Configure()
        self.url_pfx = self.conf.get_default('Service', 'UploadURL', 'http://pacs.winning.com.cn/platform')
        self.url_path = ''
        
    def run(self):
        if not self.pname:
            self.pname = mp.current_process().name

        self.init_logger()
        self.dbsession =  DBSession().get_session()

        logging.info(self.pname + ' Starting')

        self.do_work()

        logging.info(self.pname + ' Exit')

    def endloop(self):
        logging.info(self.pname + ' Exiting')
        self.exit.set()

    def init_logger(self):
        if not os.path.exists('./log'):
            os.mkdir('./log')

        logfile = TimedRotatingFileHandler('./log/'+'t_'+self.pname+'.log', when='D', backupCount=5)
        formatter = logging.Formatter('[%(asctime)s P:%(process)-5d %(funcName)s:%(lineno)d %(levelname)5s] %(message)s', '%Y-%m-%d %H:%M:%S')
        logfile.setFormatter(formatter)
        logging.getLogger('').setLevel(logging.INFO)
        logging.getLogger('').addHandler(logfile) 

        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('[' + self.pname + '-%(levelname)5s] %(message)s')
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)

    def upload(self, data):
        try:
            logging.info('%s:%s',self.pname,json.dumps(data, ensure_ascii=False) if data else None)

            success = False
            errdesc = ''
            ret = requests.post(self.url_pfx+self.url_path, json=data, timeout=2)
            ret.raise_for_status()
            
            if ret.json() and ret.json().get('msg','') == 'OK':   # if ret.text and json.loads(ret.text).get('msg','') == 'OK':
                success = True
            else:
                logging.error(ret.text)
                # errdesc = 'upload failed'
            
        except Exception as e:
            logging.exception(e)
            # errdesc += e.message
        finally:
            # logging.error(errdesc) if errdesc else None
            return success    

    def do_work(self):
        raise NotImplementedError()       
        

class CardUpload(BaseService):
    """
    轮询RisInterfacePatientInfo表，上传病人卡信息到平台
    """
    def __init__(self, group=None, target=None, name=None, *args, **kwargs):
        super(CardUpload, self).__init__(group=group, target=target, name=name, *args, **kwargs)   
        self.url_path =  '/medical/card/upload'

    def do_work(self):
        while not self.exit.is_set():
            try:
                time.sleep(1)
                card = self.query_one_card()
                if not card:
                    continue

                card_id = card.id
                logging.info('run task id:%d'%card_id)

                card_state = card.CardState
                upload_state = False
                data = self.gen_card_info(card)
                if data:
                    upload_state = self.upload(data)
                self.update_card(card_id, card_state, upload_state)
            except KeyboardInterrupt:
                self.endloop()
            except Exception as e:
                # self.dbsession.rollback()
                logging.exception(e)

    def query_one_card(self):
        ret = self.dbsession.query(PatCard).filter(PatCard.CardState.in_([0,2])).limit(1).first() # 获取未处理或者处理失败一次的记录
        # print ret.__dict__ if ret else 'Query None'
        return ret

    def update_card(self, item_id, card_state=0, success=True):
        try:
            mtime = datetime.now()
            if success:
                self.dbsession.query(PatCard).filter(PatCard.id == item_id).update({"CardState": 1,'ModifyTime': mtime})
            else:
                card_state = 1 if card_state == 0 else card_state
                self.dbsession.query(PatCard).filter(PatCard.id == item_id, PatCard.CardState < 3).update({"CardState": card_state+1, 'ModifyTime': mtime})

            self.dbsession.commit()
        except Exception as e:
            self.dbsession.rollback()
            logging.exception(e)

    def gen_card_info(self, card):
        if not card:
            return None
        try:
            info = {}
            info['CityCode'] = card.CityCode
            info['HospitalCode'] = card.HospitalCode
            info['PatName'] = card.PatName
            info['Sex'] = card.Sex
            info['CardNo'] = card.CardNo
            info['Phone'] = card.Phone
            info['IDNum'] = card.IDNum
            info['PatNameSpell'] = card.PatNameSpell
            info['PatNameSpell'] = card.PatNameSpell
            return info
        except Exception as e:
            logging.exception(e)
            return None


class ReportUpload(BaseService):
    """
    轮询XDReport表，上传报告信息
    """
    def __init__(self, group=None, target=None, name=None, *args, **kwargs):
        super(ReportUpload, self).__init__(group=group, target=target, name=name, *args, **kwargs)   
        self.url_path = '/report/upload'

    def do_work(self):
        while not self.exit.is_set():
            try:
                time.sleep(1)

                report = self.query_one_report()
                if not report:
                    continue

                report_id = report.id
                logging.info('run task id:%d'%report_id)

                report_state = report.ReportState
                upload_state = False

                data = self.gen_report_info(report)
                if data:
                    upload_state = self.upload(data)

                self.update_report(report_id, report_state, upload_state)                    
            except KeyboardInterrupt:
                self.endloop()
            except Exception as e:
                logging.exception(e)

    def query_one_report(self):
        A = aliased(XDReport)
        B = aliased(PatCard)
        ret = self.dbsession.query(A,B).filter(A.CardNo==B.CardNo,A.PatName==B.PatName,A.ReportState.in_ ([0,2])).first() # 获取未处理或者处理失败一次的记录
        if ret and len(ret)==2:
            ret[0].HospitalCode = ret[1].HospitalCode
            ret[0].CityCode = ret[1].CityCode
            # print ret[0].__dict__ if ret[0] else 'Query None'
            return ret[0]
        return None

    def gen_report_info(self, report): 
        if not report:
            return None

        try:
            report_data = {}
            report_data['SubSysCode'] = 'RIS_FS'  # 将心电报告作为RIS放射报告处理

            # 卡信息
            report_data['CityCode'] = report.CityCode
            report_data['HospitalCode'] = report.HospitalCode
            report_data['CardNo'] = report.CardNo
            report_data['PatName'] = report.PatName
            report_data['Sex'] = report.Sex

            # 基本报告内容
            report_data['ApplyNo'] = report.ApplyNo
            report_data['LabelID'] = report.Studyuid # report.LabelID   为了第三方的胶片和报告关联，LabelID和TechNo使用Studyuid
            report_data['TechNo'] = report.Studyuid # report.TechNo
            report_data['Age'] = report.Age
            report_data['BirthDay'] = report.BirthDay
            report_data['ReportTime'] = str(report.ReportTime)
            report_data['ApplyDeptName'] = report.ApplyDeptName
            report_data['WardName'] = report.WardName
            report_data['BedNo'] = report.BedNo
            report_data['HospNo'] = report.HospNo
            report_data['VerifyDoctorName'] = report.VerifyDoctorName
            report_data['ReportDoctorName'] = report.ReportDoctorName
            report_data['StudyMethod'] = report.StudyItem
            report_data['StudyObservation'] = report.StudyObservation
            report_data['StudyResult'] = report.StudyResult
            report_data['StudyUID'] = report.Studyuid
            report_data['StudyItem'] = report.StudyItem
            report_data['AuditingTime'] = str(report.VerifyTime)
            report_data['WardOrReg'] = report.WardOrReg if hasattr(report, 'WardOrReg') else ''
            report_data['ReportDesc'] = report.InstName
            report_data['ExecTime'] = str(report.ExecTime)

            # 心电内容
            report_data['HR'] = report.HR
            report_data['PR'] = report.PR
            report_data['QT'] = report.QT
            report_data['QTC'] = report.QTC
            report_data['P'] = report.P
            report_data['T'] = report.T
            report_data['QRS'] = report.QRS
            report_data['QRSaxis'] = report.QRSaxis
            report_data['Paxis'] = report.Paxis
            report_data['Taxis'] = report.Taxis
            report_data['SV1'] = report.SV1
            report_data['RV5'] = report.RV5
            
            # logging.info(report_data)
            return report_data
        except Exception as e:
            logging.exception(e)
            return None

    def update_report(self, item_id, report_state=0, success=True):
        try:
            mtime = datetime.now()
            if success:
                self.dbsession.query(XDReport).filter(XDReport.id == item_id).update({"ReportState": 1,'ModifyTimeR': mtime})
            else:
                report_state = 1 if report_state == 0 else report_state
                self.dbsession.query(XDReport).filter(XDReport.id == item_id, XDReport.ReportState < 3).update({"ReportState": report_state+1,'ModifyTimeR': mtime})

            self.dbsession.commit()
        except Exception as e:
            self.dbsession.rollback()
            logging.exception(e)        
        

class FilmUpload(BaseService):
    """
    上传胶片信息
    """
    def __init__(self, group=None, target=None, name=None, *args, **kwargs):
        super(FilmUpload, self).__init__(group=group, target=target, name=name, *args, **kwargs)   
        self.url_path = '/xuhui/dingdang'

    def do_work(self):
        while not self.exit.is_set():
            try:
                time.sleep(1)

                item = self.query_one_item()
                if not item:
                    continue

                task_id = item[0].id
                logging.info('run task id:%d'%task_id)

                task_state = item[0].ImageState
                upload_state = False

                data = self.gen_item_info(item)
                if data:
                    upload_state = self.upload(data)

                self.update_task(task_id, task_state, upload_state)                    
            except KeyboardInterrupt:
                self.endloop()
            except Exception as e:
                logging.exception(e)

    def query_one_item(self, taskname=XDReport.__tablename__):
        try:
            return self.dbsession.execute('tsp_QueryFilmTask :taskname,:count',{'taskname':taskname,'count':3}).fetchall()

            # orm方式获取工作列表内容
            # RP = aliased(XDReport)
            # PC = aliased(PatCard)
            # ST = aliased(Study)
            # SE = aliased(Series)
            # IM = aliased(Image)

            # tmp = self.dbsession.query(RP.id,RP.Studyuid,SE.SeriesUID,IM.ImageUID,PC.HospitalCode).\
            # filter(RP.CardNo==PC.CardNo,RP.PatName==PC.PatName, RP.ReportState==1,RP.ImageState.in_([0,2]), 
            # RP.Studyuid==ST.StudyUID, ST.StudyID==SE.StudyID,ST.StudyID==IM.StudyID, IM.SeriesID==SE.SeriesID)   # XXX

            # if tmp:
            #     rid = min(tmp).id
            #     ret = self.dbsession.query(tmp.subquery()).filter(text("id=%d"%rid))
            #     for r in ret:
            #         print r.id

        except Exception, e:
            logging.exception(e)
            return None     

    def gen_item_info(self, item):
        if not item:
            return None
        assert isinstance(item, list)

        try:
            item_data = {'films':[]}
            item_data['studyUID'] = item[0].StudyUID
            item_data['PatName']  = item[0].PatName
            item_data['PatAge']   = item[0].Age
            item_data['PatSex']   = item[0].Sex
            item_data['PatID']    = item[0].TechNo
            item_data['HospCode'] = item[0].HospitalCode
            item_data['AccessionNo'] = item[0].LabelID

            for film in item:
                uid = {}
                uid['objectUID'] = film.ObjectUID
                uid['seriesUID'] = film.SeriesUID
                uid['studyUID'] = film.StudyUID
                print uid
                item_data['films'].append(uid)
            # logging.info(item_data)
            return item_data
        except Exception as e:
            logging.exception(e)
            return None

    def update_task(self, task_id, task_state=0, success=True):
        try:
            mtime = datetime.now()
            if success:
                self.dbsession.query(XDReport).filter(XDReport.id == task_id).update({"ImageState": 1,'ModifyTimeI': mtime})
            else:
                report_state = 1 if report_state == 0 else report_state
                self.dbsession.query(XDReport).filter(XDReport.id == task_id, XDReport.ReportState < 3).update({"ImageState": report_state+1,'ModifyTimeI': mtime})

            self.dbsession.commit()
        except Exception as e:
            self.dbsession.rollback()
            logging.exception(e)        


if __name__ == '__main__':
    mp.freeze_support()

    service_1 = CardUpload(name='CardUpload')
    service_1.start()
    service_2 = ReportUpload(name='ReportUpload')
    service_2.start()
    service_3 = FilmUpload(name='FilmUpload')
    service_3.start()
    
    try:
        service_1.join()
        service_2.join()
        service_3.join()
    except KeyboardInterrupt:
        pass
