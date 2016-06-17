# coding=utf-8


import sys
import image_qrc
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from render_qt_text import *

def bgColorForName(name):
    return QColor('#F1F1F1')

def fgColorForName(name):
    return QColor("#F8F8F8")

class ColorDock(QFrame):
    def __init__(self, name, parent=None, flags=0):
        QFrame.__init__(self)
        
        self.color = None
        self.szHint = None
        self.minSzHint = None
        
        font = self.font()
        font.setPointSize(8)
        self.setFont(font)
        
        self.szHint = QSize(-1,-1)
        self.minSzHint = QSize(125,75)
        
    def sizeHint(self):
        return self.szHint

    def minimumSizeHint(self):
        return self.minSzHint
    
    def setCustomSizeHint(self, size):
        self.szHint = size
        self.updateGeometry()
        
    
    def paintEvent(self, event):
        print 'ColorDock paintEvent'
        
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        p.fillRect(self.rect(), bgColorForName(self.color))
        p.save()
        
        render_qt_text(p, self.width(), self.height(), fgColorForName(self.color))        
        
        p.restore()
             
    @pyqtSlot()
    def changeSizeHints(self):
        print 'changeSizeHints'

def createSpinBox(value, parent, max=1000):
    result = QSpinBox(parent)
    result.setMinimum(-1)
    result.setMaximum(max)
    result.setValue(value)
    return result

class ColorSwatch(QDockWidget):
    def __init__(self, name, parent=None, flags=0):
        QDockWidget.__init__(self, name)
        
        self.menu = None
        
        self.setObjectName(name + ' Dock Widget')
        self.setWindowTitle(self.objectName() + ' Dock Widget')
        
        swatch = ColorDock(name, self)
        swatch.setFrameStyle(QFrame.Box | QFrame.Sunken)
        
        self.setWidget(swatch)
        
        self.closableAction = QAction('Closable', self)
        self.closableAction.setCheckable(True)
        
        self.menu = QMenu(name, self)
        self.menu.addAction(self.closableAction)
        
        if name == 'White' or name == 'white':
            print 'white'
            self.toggleViewAction().setShortcut(Qt.CTRL|Qt.Key_R)
        
    
    def resizeEvent(self, event):
        print 'resizeEvent'
        if isinstance(self.titleBarWidget(), BlueTitleBar):
            self.titleBarWidget().updateMask()  
            
        QDockWidget.resizeEvent(self, event)
        pass
    def contextMenuEvent(self, event):
        event.accept()
        self.menu.exec_(event.globalPos())
        pass

class BlueTitleBar(QWidget):
    def __init__(self, parent=None, flags=0):
        QWidget.__init__(self)
        
        self.centerPm = QPixmap(":res/image/titlebarCenter.png")
        self.rightPm = QPixmap(":res/image/titlebarRight.png")
        self.leftPm = QPixmap(":res/image/titlebarLeft.png")
        
          
    def sizeHint(self):
        return self.minimumSizeHint()
    
    def minimumSizeHint(self):
        dw = (self.parentWidget())
        assert(dw != None)
        
        result = QSize(self.leftPm.width()+self.rightPm.width(),self.centerPm.height())
        if dw.features() & QDockWidget.DockWidgetVerticalTitleBar:
            result.transpose()
        return result
    
    def paintEvent(self, event):
        painter = QPainter(self)
        rect = self.rect()
        
        dw = self.parentWidget()
        assert(dw != None)
        if dw.features() & QDockWidget.DockWidgetVerticalTitleBar:
            s = rect.size()
            s.transpose()
            rect.setSize(s)
            
            painter.translate(rect.left(), rect.top() + rect.width())
            painter.rotate(-90)
            painter.translate(-rect.left(), -rect.top())
        
        painter.drawPixmap(rect.topLeft(), self.leftPm)
        painter.drawPixmap(rect.topRight() - QPoint(self.rightPm.width() - 1, 0), self.rightPm)
        brush = QBrush(self.centerPm)
        painter.fillRect(rect.left() + self.leftPm.width(), 
                         rect.top(),
                         rect.width() - self.leftPm.width() - self.rightPm.width(),
                         self.centerPm.height(), 
                         brush)
        
    
    def mousePressEvent(self, event):
        pass
    
    @pyqtSlot()
    def updateMask(self):
        print 'updateMask'
        pass