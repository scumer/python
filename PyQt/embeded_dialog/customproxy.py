# coding=utf-8

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class CustomProxy(QGraphicsProxyWidget):
    def __init__(self, parent=None, flags=0):
        QGraphicsProxyWidget.__init__(self, parent,flags)
        
        self.timeLine = None
        self.popupShown = 0
        self.currentPopup = None
        
        self.timeLine = QTimeLine(250, self)
        #self.connect(self.timeLine, SIGNAL('stateChanged()'),self, SLOT('stateChanged_()'))
        #self.connect(self.timeLine, SIGNAL('valueChanged(float)'),self, SLOT('updateStep(float)'))

        #self.connect(self.timeLine, SIGNAL('stateChanged'),self, SLOT('stateChanged_'))
        #self.connect(self.timeLine, SIGNAL('valueChanged'),self, SLOT('updateStep'))
        self.timeLine.valueChanged.connect(self.updateStep)
        self.timeLine.stateChanged.connect(self.stateChanged_)#, Qt.QueuedConnection)
        #QTimeLine.NotRunning
        
        #self.timeLine.valueChanged.connect(self.updateStep)
        #self.timeLine.stateChanged.connect(self.stateChanged)        
        
        #self.timeLine.start()

    
    def boundingRect(self):
        #print 'CustomProxy boundingRect'
        #return QGraphicsProxyWidget.boundingRect(self).adjusted(0,0,10,10) #???
        return QGraphicsProxyWidget.boundingRect(self)
    
    def paintWindowFrame(self, painter, option, widget=None):
        #color = QColor(0,0,0,64)
        
        #r = self.windowFrameRect()
        #right = QRectF(r.right(),r.top()+10,10,r.height())
        #bottom = QRectF(r.left()+10,r.bottom(), r.width(),10)
        #intersectsRight = right.intersects(option.exposedRect)
        #intersectsBottom = bottom.intersects(option.exposedRect)
        
        #if intersectsRight and intersectsBottom:
            #path = QPainterPath()
            #path.addRect(right)
            #path.addRect(bottom)
            #painter.setPen(Qt.NoPen)
            #painter.setBrush(color)
            #painter.drawPath(path)
        #elif intersectsBottom:
            #painter.fillRect(bottom, color)
        #elif intersectsRight:
            #painter.fillRect(right, color)
        
        QGraphicsProxyWidget.paintWindowFrame(self, painter, option, widget);
    
    def hoverEnterEvent(self, event):
        QGraphicsProxyWidget.hoverEnterEvent(self, event)
        self.scene().setActiveWindow(self)
        
        #print 'self.timeLine.currentValue:',self.timeLine.currentValue()
        if(self.timeLine.currentValue() != 1):
            self.zoomIn() #放大
 
    def hoverLeaveEvent(self, event):
        QGraphicsProxyWidget.hoverLeaveEvent(self, event)
        if not self.popupShown and (self.timeLine.direction() != QTimeLine.Backward or self.timeLine.currentValue() != 0):
            self.zoomOut()
     
    def sceneEventFilter(self, watched, event): ## ?作用？
        print '-'*20 + 'sceneEventFilter'
        print watched
        print watched.isWindow()
        print event.type()
        
        #if watched.isWindow() and (event.type() == QEvent.UngrabMouse or event.type() == QEvent.GrabMouse):
            #self.popupShown = watched.isVisible()
            #if not self.popupShown and not self.isUnderMouse():
                #self.zoomOut()
        return QGraphicsProxyWidget.sceneEventFilter(self, watched,event)

    def itemChange(self, change, value):
        #print 'itemChange'
        #if change == self.ItemChildAddedChange or change == self.ItemChildRemovedChange:
            #if change == self.ItemChildAddedChange:
                #self.currentPopup = value
                #self.currentPopup.setCacheMode(ItemCoordinateCache)
                #if self.scene():
                    #self.currentPopup.installSceneEventFilter(self)
            #elif self.scene():
                #self.currentPopup.removeSceneEventFilter(self)
                #self.currentPopup = None
        #elif self.currentPopup and change == self.ItemSceneHasChanged:
            #self.currentPopup.installSceneEventFilter(self)

        item = value
        try:
            if change == self.ItemChildAddedChange:
                item.installSceneEventFilter(self)
            else:
                item.removeSceneEventFilter(self)
        except:
            pass        
        
        return QGraphicsProxyWidget.itemChange(self, change, value);
    
    @pyqtSlot(float)
    def updateStep(self,value):
        r = self.boundingRect()
        #self.setTransform(QTransform()
                          #.translate(r.width()/2,r.height()/2)
                          #.rotate(value*30,Qt.XAxis)
                          #.rotate(value*10,Qt.YAxis)
                          #.rotate(value*5,Qt.ZAxis)
                          #.scale(1+1.5*value,1+1.5*value)
                          #.translate(-r.width()/2,-r.height()/2))
        
        self.setTransform(QTransform()
                          .translate(r.width()/2,r.height()/2)
                          .scale(1+1.3*value,1+1.3*value)
                          .translate(-r.width()/2,-r.height()/2))    
        #self.setCacheMode(self.DeviceCoordinateCache)

    
    @pyqtSlot(QTimeLine.State)
    def stateChanged_(self,value):
        #print 'stateChanged', value
        if value == QTimeLine.Running:
            if self.timeLine.direction() == QTimeLine.Forward:
                self.setCacheMode(self.ItemCoordinateCache)
        elif value == QTimeLine.NotRunning:
            if self.timeLine.direction() == QTimeLine.Backward:
                self.setCacheMode(self.DeviceCoordinateCache)
        pass

    
    @pyqtSlot()
    def zoomIn(self):
        if self.timeLine.direction() != QTimeLine.Forward:
            self.timeLine.setDirection(QTimeLine.Forward)
        if self.timeLine.state() == QTimeLine.NotRunning:
            self.timeLine.start()
    
    @pyqtSlot()
    def zoomOut(self):
        if self.timeLine.direction() != QTimeLine.Backward:
            self.timeLine.setDirection(QTimeLine.Backward)
        if self.timeLine.state() == QTimeLine.NotRunning:
            self.timeLine.start()   
            