#coding=utf-8

import sys
import json
import requests 
import csv

#from PyQt5.QtWidgets import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from  mwidget import Ui_MainWidget

ServerURL = 'pacs.winning.com.cn/pat_test'

class MainWidget(QWidget):
    def __init__(self, parent=None, flags=0):
        QWidget.__init__(self)
    
        self.setFixedSize(220,350)
        
        self.ui = Ui_MainWidget()
        self.ui.setupUi(self)
        
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.ln_name.setFocus()
        
        self.ui.btn_gencode.clicked.connect(self.GenQRCode)
        self.ui.btn_import.clicked.connect(self.ImportFile)
        self.ui.btn_saveas.clicked.connect(self.SaveQRCode)
        self.ui.btn_back.clicked.connect(self.BackToMain)
        
        self.image = QImage()
        #self.GenCode("test")
       
    
    def init(self):
        pass
    
    def GenQRCode(self):
        # name no 不能为空
        if self.ui.ln_name.text() == '':
            QMessageBox.information(self,u'提示',u'姓名栏不能为空！')
            return
        if self.ui.ln_no.text() == '':
            QMessageBox.information(self,u'提示',u'工号不能为空！') 
            return
        
        person_info = {}
        person_info['name'] = unicode(self.ui.ln_name.text())
        person_info['employeeNo'] = unicode(self.ui.ln_no.text())
        person_info['department'] = unicode(self.ui.ln_dept.text())
        person_info['title'] = unicode(self.ui.ln_post.text())
        person_info['corporation'] = unicode(self.ui.ln_company.text())
        person_info['phone'] = unicode(self.ui.ln_telephone.text())
        person_info['cellPhone'] = unicode(self.ui.ln_mobile.text())
        person_info['email'] = unicode(self.ui.ln_email.text())
        person_info['site'] = unicode(self.ui.ln_site.text())
        person_info['address'] = unicode(self.ui.ln_addr.text())
        
        fails, uid = self.RegisterPersonInfo(person_info)
        if fails:
            QMessageBox.information(self,u'Error',fails)
            return
        elif uid:
            self.GenCode(uid)
            self.ShowQRCode()
        else:
            return
 
    def RegisterPersonInfo(self,info):
        fails = ''
        uid = ''
        try:
            #print info
            ret = requests.post('http://'+ServerURL+'/tools/employee/record', json=info)
            #print ret.content
            if ret.status_code == 200:
                data = json.loads(ret.content)
                if data.get('err'):
                    fails = data['err']
                elif data.get('id'):
                    uid = data['id']
            else:
                fails = str(ret.status_code)
        except Exception as e:
            fails = str(e.message)
            print str(e.args)

        return fails,uid

    def GenCode(self,uid):
        data = 'http://'+ServerURL+'/tools/static/query.html?id='+uid
        #print data
        
        from qrcode import QRCode
        from StringIO import StringIO
        gen = QRCode()
        gen.add_data(data)
        img = gen.make_image()
        io = StringIO()
        img.save(io)
        io.seek(0)
        
        #image = QImage()
        self.image.loadFromData(io.read())

    def ShowQRCode(self):
        newimg = self.image.scaled(QSize(180,350),Qt.KeepAspectRatio,Qt.SmoothTransformation)
        self.ui.lb_image.setPixmap(QPixmap.fromImage(newimg))           
        self.ui.stackedWidget.setCurrentIndex(1)        
    
    def ImportFile(self):
        filename = unicode(QFileDialog.getOpenFileName(self,u'打开','/','*.csv'))
        if filename != '':
            #print filename
            pathname = unicode(QFileInfo(filename).absolutePath())
            pathname = pathname+u'/BCard二维码'
            if not QDir().exists(pathname):
                QDir().mkdir(pathname)
            #print pathname
            try:
                csvfile = file(filename, 'r')
                reader = csv.reader(csvfile)
                reader.next()  # jump first line
                
                failsitem = []
                index = 1
                for line in reader:
                    
                    try:
                        index += 1
                        person_info = {}
                        person_info['name'] =  str(line[0]).decode('GB2312')
                        person_info['employeeNo'] =  str(line[1]).decode('GB2312')
                        person_info['department'] = str(line[2]).decode('GB2312')
                        person_info['title'] = str(line[3]).decode('GB2312')
                        person_info['corporation'] = str(line[4]).decode('GB2312')
                        person_info['phone'] = str(line[5]).decode('GB2312')
                        person_info['cellPhone'] = str(line[6]).decode('GB2312')
                        person_info['email'] = str(line[7]).decode('GB2312')
                        person_info['site'] = str(line[8]).decode('GB2312')
                        person_info['address'] = str(line[9]).decode('GB2312')
                        #print line[0],line[1]

                        if line[0] == '' or line[1] == '':
                            failsitem.append(index)
                            continue
                        
                        fails, uid = self.RegisterPersonInfo(person_info)
                        if fails:
                            print 'fails:'+fails
                            failsitem.append(index)
                            continue
                        
                        #print 'uid:'+uid
                        if uid != '':
                            self.GenCode(uid)
                            filename = pathname+'/'+ person_info['employeeNo']+'-'+person_info['name']+'.png'
                            #print filename
                            print self.image.save(filename)
                            
                    except Exception as e:
                        print e
                        failsitem.append(index)
                csvfile.close()
                
                QMessageBox.information(self, u'生成结束', u'二维码存放路径为:' + pathname)                
                
                if len(failsitem) != 0:
                    msg = u'共{0}条记录生成失败，失败条目为：{1}'.format(len(failsitem), str(failsitem))
                    QMessageBox.information(self, u'部分生成失败', msg)
                    
            except Exception as e:
                print e
            
        
    def SaveQRCode(self):       
        if self.image and not self.image.isNull():
            dflname = self.ui.ln_no.text()+'-'+self.ui.ln_name.text()+'.png'
            filename = QFileDialog.getSaveFileName(self,u'保存二维码','/'+dflname)
            if filename != '':
                self.image.save(filename)
    
    def BackToMain(self):
        self.ui.stackedWidget.setCurrentIndex(0)  

if __name__ == '__main__':
    app = QApplication(sys.argv)

    wgt = MainWidget()
    wgt.show()
    
    app.exec_()