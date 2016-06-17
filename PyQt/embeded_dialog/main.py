# coding=utf-8

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from embededdialogs import *
from customproxy import * 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    scene = QGraphicsScene()
    #scene.setStickyFocus(True)
    
    gridSize = 5
    
    for x in range(gridSize):
        for y in range(gridSize):
            proxy = CustomProxy(None, Qt.Window)
            #proxy = QGraphicsProxyWidget(None, Qt.Window)
            proxy.setWidget(embededDlg())
            
            rect = proxy.boundingRect()
            
            proxy.setPos(x*rect.width()*1.05,y*rect.height()*1.05)
            proxy.setCacheMode(QGraphicsItem.DeviceCoordinateCache)
            
            scene.addItem(proxy)
            
    
    scene.setSceneRect(scene.itemsBoundingRect())
    
    view = QGraphicsView(scene)
    view.scale(0.7,0.7)

    view.setRenderHints(view.renderHints() | QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
    view.setBackgroundBrush(QBrush(QPixmap(r'E:\Project\Python\PyQt\embeded_dialog\No-Ones-Laughing-3.jpg')))
    view.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
    view.show()
    view.setWindowTitle("Embedded")
    
    #scene = QGraphicsScene()
    #scene.addText('hhhh')
    #view = QGraphicsView(scene)
    #view.show()
    
    app.exec_()
            
            