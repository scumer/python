# coding=utf-8

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from render_qt_text import * 

image = None
def genIcon(iconSize, str_, color):
    w = iconSize.width()
    h = iconSize.height()
    
    global image
    image = QImage(w,h,QImage.Format_ARGB32_Premultiplied)
    image.fill(0)
    
    p = QPainter(image)
    render_qt_text(p,w,h,color)
    
    return QPixmap.fromImage(image, Qt.DiffuseAlphaDither|Qt.DiffuseAlphaDither)

def genIcon_(iconSize, number, color):
    return genIcon(iconSize, number, color)

class ToolBar(QToolBar):
    def __init__(self, title, parent=None):
        QToolBar.__init__(self, title)
        
        self.spinbox = None
        self.spinboxAction = None
        
        self.orderAction = None
        self.randomizeAction = None
        self.addSpinBoxAction = None
        self.removeSpinBoxAction = None
        
        self.movableAction = None
        
        self.allowedAreasActions = None
        self.allowLeftAction = None
        self.allowRightAction = None
        self.allowTopAction = None
        self.allowBottomAction = None
        
        self.areaActions = None
        self.leftAction = None
        self.rightAction = None
        self.topAction = None
        self.bottomAction = None
        
        self.toolBarBreakAction = None
        
        self.menu = None
        self.tip = None
        
        self.spinbox = 0
        self.spinboxAction = 0
        self.tip = 0
        
        self.setWindowTitle(title)
        self.setObjectName(title)
        self.setIconSize(QSize(32,32))
        
        bg = QColor(self.palette().background().color())
        self.menu = QMenu('One', self)
        self.menu.setIcon(QIcon(genIcon(self.iconSize(),1,Qt.black)))
        self.menu.addAction(QIcon(genIcon(self.iconSize(),'A',Qt.blue)),"A")
        self.menu.addAction(QIcon(genIcon(self.iconSize(),'B',Qt.blue)),"B")
        self.menu.addAction(QIcon(genIcon(self.iconSize(),'C',Qt.blue)),"C")
        self.addAction(self.menu.menuAction())
        
        two = self.addAction(QIcon(genIcon(self.iconSize(),'2',Qt.white)),"Two")
        boldFont = QFont()
        boldFont.setBold(True)
        two.setFont(boldFont)
        
        #act = QAction(QIcon(genIcon(self.iconSize(),3,Qt.red)), 'three')
        self.addAction(QAction(QIcon(genIcon(self.iconSize(),3,Qt.red)), 'three', self))
        self.addAction(QAction(QIcon(genIcon(self.iconSize(),4,Qt.green)), 'Four', self))
        self.addAction(QAction(QIcon(genIcon(self.iconSize(),5,Qt.blue)), 'Five', self))
        self.addAction(QAction(QIcon(genIcon(self.iconSize(),6,Qt.yellow)), 'Six', self))
        
        
        self.connect(self.menu, SIGNAL('aboutToShow()'), self, SLOT('updateMenu()'))
        
        
        
    def enterEvent(self, event):
        pass
    
    def leaveEvent(self, event):
        pass
    
    def allow(self, area, ballow):
        pass
    
    def place(self, area, bplace):
        pass
    
    @pyqtSlot()
    def order(self):
        pass
    
    @pyqtSlot()
    def randomize(self):
        pass
    
    @pyqtSlot()
    def addSpinBox(self):
        pass
    
    @pyqtSlot()
    def removeSpinBox(self):
        pass        
    
    @pyqtSlot()
    def updateMenu(self):
        #print 'aboutToShow->updateMenu'
        pass
    
    @pyqtSlot()
    def insertToolBarBreak(self):
        pass        
    
    @pyqtSlot()
    def changeMovable(self, b):
        pass    
    
    @pyqtSlot()
    def allowLeft(self, b):
        pass 
    
    @pyqtSlot()
    def allowRight(self, b):
        pass 
    
    @pyqtSlot()
    def allowTop(self, b):
        pass 
    
    @pyqtSlot()
    def allowBottom(self, b):
        pass 
    
    @pyqtSlot()
    def placeLeft(self, b):
        pass 
    
    @pyqtSlot()
    def placeRight(self, b):
        pass 
    
    @pyqtSlot()
    def placeTop(self, b):
        pass 
    
    @pyqtSlot()
    def placeBottom(self, b):
        pass         