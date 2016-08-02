# coding=utf-8

import sys
import time
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class ImageWidget(QGraphicsItem):
    def __init__(self, filename, parent=None,scene=None):
        super(ImageWidget,self).__init__(parent,scene)
        self.image = QImage(filename)
        
        self.imagew = self.image.width()
        self.imageh = self.image.height()
        self.imagesize = QSizeF(self.image.size())
        
        self.topLeft = QPointF(0,0)
        self.clipRect = None
        
        
        #self.setCacheMode(QGraphicsItem.DeviceCoordinateCache)
        
    
    def boundingRect(self):
        if self.clipRect:
            rectf = QRectF(self.clipRect)
            return rectf
        return QRectF(QPoint(0,0),self.imagesize).adjusted(-2,-2,4,4)

    
    def paint(self, painter, item, widget):
        #painter = QPainter()
        nimage = QImage()
        topleft = None
        if self.clipRect:
            nimage = self.image.copy(self.clipRect)
            topleft = QPoint(self.clipRect.topLeft())
        else:
            nimage = self.image
            topleft = QPoint(1,1)
        painter.drawImage(topleft, nimage)
        
    def setClipRect(self,rect):
        self.clipRect = rect
        self.prepareGeometryChange()

        
        