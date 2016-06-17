#coding = utf-8

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys


class Pixmap(QGraphicsWidget):
    clicked = pyqtSignal()
    
    def __init__(self, pix, parent=None, flags=Qt.Widget):
        #QGraphicsWidget.__init__(self)
        super(Pixmap, self).__init__(parent, flags)
        
        self.orig = pix
        self.p = pix
        
        #self.clicked = pyqtSignal()
    
    def paint(self, painter, item, widget=None):
        
        
        
        if 0:
            painter.drawPixmap(self.p.rect(), self.orig, self.orig.rect())
        elif 1:
            center = QPointF(self.p.width()/2.0, self.p.height()/2.0)
            #center = self.p.rect().center()
            #print 'rect:',self.p.rect()
            print 'center:',center
            painter.translate(center)
            factor = self.p.size().height()/200.0
            print factor
            painter.scale(factor, factor)
            painter.translate(-100,-100)
            
            painter.drawPixmap(QPointF(), self.orig)            
        else:
        #painter.drawPixmap(self.p.rect(), self.orig, self.orig.rect())
            painter.drawPixmap(QPointF(), self.p)
   
    def mousePressEvent(self, event):
        self.emit(SIGNAL("clicked()")) 
    
    def setGeometry(self, rect):
        #print '------------'
        QGraphicsWidget.setGeometry(self, rect)
        
        #print rect.size().width()
        # self.orig.size().width()
    
        if self.orig.size() == QSize(200,200):
            self.p = self.orig.scaled(rect.size().toSize())
        elif rect.size().width() > self.orig.size().width():
            self.p = self.orig.scaled(rect.size().toSize(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        else:
            self.p = self.orig
            
class GraphicsView(QGraphicsView):
    def __init__(self, scene, parent=None):
        QGraphicsView.__init__(self, scene, parent)
    
    def resizeEvent(self, event):
        self.fitInView(self.sceneRect(), Qt.KeepAspectRatio)


def createStates(objects, selectedRect, parent):
    for object_ in objects:
        state = QState(parent)
        state.assignProperty(object_, 'geometry', selectedRect)
        parent.addTransition(object_, SIGNAL('clicked()'), state)
    pass

def createAnimations(objects, machine):
    for object_ in objects:
        machine.addDefaultAnimation(QPropertyAnimation(object_, 'geometry'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    
    p1 = Pixmap(QPixmap(r'E:\Project\Python\PyQt\appchooser\1.jpg'), None)
    p2 = Pixmap(QPixmap(r'E:\Project\Python\PyQt\appchooser\2.jpg'), None)
    p3 = Pixmap(QPixmap(r'E:\Project\Python\PyQt\appchooser\3.jpg'),None)
    p4 = Pixmap(QPixmap(r'E:\Project\Python\PyQt\appchooser\4.jpg'),None)

    
    p1.setObjectName("p1")
    p2.setObjectName("p2")
    p3.setObjectName("p3")
    p4.setObjectName("p4")    
    
    p1.setGeometry(QRectF(  0.0,   0.0, 64.0, 64.0))
    p2.setGeometry(QRectF(236.0,   0.0, 64.0, 64.0))
    p3.setGeometry(QRectF(236.0, 236.0, 64.0, 64.0))
    p4.setGeometry(QRectF(  0.0, 236.0, 64.0, 64.0))
        
    scene = QGraphicsScene(0,0,300,300)
    #scene.setBackgroundBrush(Qt.white)
    scene.addItem(p1)
    scene.addItem(p2)
    scene.addItem(p3)
    scene.addItem(p4)
    
    window = GraphicsView(scene)
    window.setFrameStyle(0)
    #window.setAlignment(Qt.AlignLeft | Qt.AlignTop)
    #window.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    #window.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    
    machine = QStateMachine()
    machine.setGlobalRestorePolicy(QStateMachine.RestoreProperties)
    
    group = QState(machine)
    group.setObjectName('group')
    
    selectedRect = QRect(86, 86, 128, 128)
    
    idleState = QState(group)
    group.setInitialState(idleState)
    
    objects = None
    objects = [p1,p2,p3,p4]
    
    createStates(objects, selectedRect, group)
    createAnimations(objects, machine)
    
    machine.setInitialState(group)
    machine.start()
    
    window.resize(300,300)
    window.show()
    #window.showMaximized()
    
    app.exec_()
