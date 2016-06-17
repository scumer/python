import sys
import time
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from enum import Enum


class RectItem(QObject,QGraphicsItem):
    shapeChanged = pyqtSignal()
    
    def __init__(self, mode=0,parent=None, scene=None):
        QGraphicsItem.__init__(self,parent)
        QObject.__init__(self,parent)
        #super(RectItem,self).__init__(parent,scene)
        self.emit(SIGNAL("shapeChanged()")) 
        
class Pixmap(QGraphicsWidget):
    clicked = pyqtSignal()
    
    def __init__(self, pix, parent=None, flags=Qt.Widget):
        #QGraphicsWidget.__init__(self)
        super(Pixmap, self).__init__(parent, flags)
        self.emit(SIGNAL("clicked()")) 
        
class GraphicsScene(QGraphicsScene):
    shapeChanged = pyqtSignal()
    def __init__(self, parent=None):
        super(GraphicsScene,self).__init__(parent)
        self.emit(SIGNAL("shapeChanged()")) 
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = RectItem()
    
    b = Pixmap('0')
    
    c = GraphicsScene()
    app.exec_()