# coding=utf-8

import sys
import time
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from enum import Enum

from RectWidget import *
from RectItem import *
from ImageWidget import *

filename = r'E:\Project\Python\PyQt\qrcode.jpg'
filenameB = r'E:\Project\Python\PyQt\IP.png'

class Window(QMainWindow):
    def __init__(self, parent=None, flags=Qt.Widget):
        super(Window,self).__init__(parent,flags)
        
        self.sceneA = QGraphicsScene(self)
        self.sceneA.setSceneRect(0,0,500,500)
        self.sceneA.setBackgroundBrush(Qt.gray)
        self.sceneB = QGraphicsScene(self)
        self.sceneB.setSceneRect(0,0,500,500)
        
        #rect = RectWidget()        
        rectitem = RectItem()
        
        rectitemB = RectItem()
        rectitemB.setAcceptedMouseButtons(Qt.NoButton)
        rectitemC = RectItem()
        imageWidget = ImageWidget(filename)
        imageWidgetB = ImageWidget(filename)
        
        rectitem.setImageItem(imageWidgetB)
        
        #self.sceneA.addItem(imageWidget)
        self.sceneA.addItem(rectitem)
        
        self.sceneB.addItem(imageWidgetB)
        self.sceneB.addItem(rectitemB)
        
        rectitem.setBuddyItem(rectitemB)
        
        #imageWidget.setZValue(1)
        #print rectitem.zValue()
        #print imageWidget.zValue()
        #self.sceneA.addItem(rectitemC)
        #self.sceneB.addWidget(rect)
        
        self.viewA = QGraphicsView(self.sceneA)
        #self.viewA.centerOn(0,0)
        #self.viewA.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.viewB = QGraphicsView(self.sceneB)
        #self.viewA.setAttribute(Qt.WA_OpaquePaintEvent)
        #self.viewA.setAttribute(Qt.WA_NoSystemBackground)
        #self.viewA.viewport().setAttribute(Qt.WA_)
        #self.viewA.viewport().setAttribute(Qt.WA_NoSystemBackground)        
        
        hlayout = QHBoxLayout()
        hlayout.addWidget(self.viewA)
        hlayout.addWidget(self.viewB)
        
        self.widget = QWidget()
        self.widget.setLayout(hlayout)
        self.setCentralWidget(self.widget)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()