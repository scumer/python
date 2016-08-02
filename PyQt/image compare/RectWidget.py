# coding=utf-8

import sys
import time
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from enum import Enum

from unity import *

class RectWidget(QWidget):
    def __init__(self, parent=None, flags=Qt.Widget):
        super(RectWidget,self).__init__(parent, flags=flags)
        self.rect_ = QRect(300.0, 200.0, 80.0, 160.0)
        self.setGeometry(0,0,200,200)
        self.resize(self.rect_.size())
        #self.adjustSize()
        
        pal = QPalette()
        pal.setColor(QPalette.Background, Qt.transparent)
        self.setPalette(pal)     
        
        
        
    def sizeHint(self):
        #print 'sizeHint'
        return self.rect_.size()
    
    def paintEvent(self,event):
        painter = QPainter(self)
        
        pen = QPen()
        pen.setWidth(2)
        pen.setColor(Qt.black)        

        painter.setPen(pen)
        painter.drawRect(self.rect_)
        #painter.drawPixmap(0,0,QPixmap(r'E:\Project\Python\PyQt\qrcode.jpg'))
        self.setGeometry(self.rect_)
        self.updateGeometry()
        self.resize(self.rect_.size())
        
    def mouseMoveEvent(self,event):
        self.rect_.adjust(-7,-7,-7,-7)

        self.update()
        super(RectWidget,self).mouseMoveEvent(event)    
    
    def mousePressEvent(self,event):
        #self.rect.adjust(5,5,5,5)

        #self.update()
        #super(RectWidget,self).mousePressEvent(event)    
        pass