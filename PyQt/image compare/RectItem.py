# coding=utf-8

import sys
import time
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from enum import Enum

from unity import *
from RectWidget import *


class RectItem(QGraphicsItem):
    
    shapeChanged = pyqtSignal()
    
    def __init__(self, mode=0,parent=None, scene=None):
        super(RectItem,self).__init__(parent,scene)
        self.setAcceptHoverEvents(True)
        #self.setAcce
        self.rect = QRect(300.0, 200.0, 80.0, 160.0)
        
        self.act_btn = None
        self.act_state = None
        
        self.buddyItem = None
        self.imageItem = None
        #self.
        self.penWidth = 2
        
        
    def boundingRect(self):
        #print self.rect
        adval = self.penWidth+5
        return QRectF(self.rect.adjusted(-adval,-adval,adval,adval))
        #return QRectF(0,0,400,400)

    #def shape(self):
        #path = QPainterPath()
        #path.addRect(self.rect)
        #return path
    def hoverMoveEvent(self, event):
        pos = event.pos()
        state = ComputePointStateInRect(pos, self.rect, 5)  
        
        if state == PosState.Inside:
            self.setCursor(Qt.SizeAllCursor)
        elif state == PosState.P0 or state== PosState.P3:
            self.setCursor(Qt.SizeFDiagCursor)
        elif state == PosState.P1 or state== PosState.P2:
            self.setCursor(Qt.SizeBDiagCursor) 
        elif state == PosState.E0 or state == PosState.E2:
            self.setCursor(Qt.SizeHorCursor)
        elif state == PosState.E1 or state == PosState.E3:
            self.setCursor(Qt.SizeVerCursor)
        
        super(RectItem,self).hoverMoveEvent(event)
    
    def hoverLeaveEvent(self, event):
        self.setCursor(Qt.ArrowCursor)
        super(RectItem,self).hoverLeaveEvent(event)
    
    def mousePressEvent(self,event):
        self.act_btn = event.button()
        if self.act_btn == Qt.LeftButton:
            pos = event.pos()
            #print pos
            self.act_state = ComputePointStateInRect(pos, self.rect, 5)
            #print self.act_state
        
        #super(RectItem,self).mousePressEvent(event)  # error????
        
    def mouseMoveEvent(self,event):
        #event = QGraphicsSceneMouseEvent()
        if (self.act_btn==Qt.LeftButton) and self.act_state:
            pos = event.pos()
            lastPos = event.lastPos()
            deltPos = pos - lastPos
            dx = deltPos.x()
            dy = deltPos.y()  
            #print dx,dy
            new_rect = None
            
            if self.act_state == PosState.Inside:
                new_rect = self.rect.adjusted(dx,dy,dx,dy)
            elif self.act_state == PosState.P0:
                new_rect = self.rect.adjusted(dx,dy,0,0)
            elif self.act_state == PosState.P1:
                new_rect = self.rect.adjusted(0,dy,dx,0)  
            elif self.act_state == PosState.P2:
                new_rect = self.rect.adjusted(dx,0,0,dy)  
            elif self.act_state == PosState.P3:
                new_rect = self.rect.adjusted(0,0,dx,dy)
            elif self.act_state == PosState.E0:
                new_rect = self.rect.adjusted(dx,0,0,0) 
            elif self.act_state == PosState.E1:
                new_rect = self.rect.adjusted(0,dy,0,0) 
            elif self.act_state == PosState.E2:
                new_rect = self.rect.adjusted(0,0,dx,0) 
            elif self.act_state == PosState.E3:
                new_rect = self.rect.adjusted(0,0,0,dy)   
                
            if new_rect:
                self.rect = new_rect
                self.prepareGeometryChange()
            #else:
                #print 'new_rect invalid'
                #self.emit(SIGNAL('shapeChanged'))
                #self.emit(SIGNAL("clicked()")) 
            #self.rect.adjust(-7,-7,-7,-7)
            #self.prepareGeometryChange()
        #self.update()
        super(RectItem,self).mouseMoveEvent(event)

    def mouseReleaseEvent(self,event):  
        self.act_btn = None
        self.act_state = None
        super(RectItem,self).mouseReleaseEvent(event)

    def paint(self, painter, item, widget):
        #print self.pos().x()
        
        brush = QBrush()
        #brush.setColor(QColor(0,0,0,0))
        #brush.setStyle(Qt.NoBrush)
        #painter.setBrush(brush)
        
        pen = QPen()
        pen.setWidth(self.penWidth)
        pen.setColor(Qt.red)
        #pen.setStyle(Qt.DotLine)
        
        painter.setPen(pen)
        
        #painter.setRenderHints(QPainter.Antialiasing, True)
        painter.drawRect(self.rect)  
        painter.fillRect(self.rect,brush)
        
        
        
        painter.drawText(self.rect.topLeft(),'1'),
        #self.scene().update()
        if self.buddyItem:
            self.buddyItem.updateRect(self.rect)
        if self.imageItem:
            self.imageItem.setClipRect(QRect(self.rect))
        
    def updateRect(self,rect):
        self.rect = rect
        if rect:
            self.rect = rect
            self.prepareGeometryChange()
    
    def setBuddyItem(self,item):
        self.buddyItem = item
        
    def setImageItem(self, item):
        self.imageItem = item
    
        
