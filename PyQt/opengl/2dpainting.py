# coding=utf-8

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtOpenGL import *
import sys

class GLWidget(QGLWidget):
    def __init__(self, helper, parent=None):
        super(GLWidget,self).__init__(QGLFormat(QGL.SampleBuffers),parent)
        self.helper = helper
        self.elapsed = 0   
        self.setFixedSize(200,200)
        self.setAutoFillBackground(True)
        
    @pyqtSlot()
    def animate(self):
        self.elapsed = (self.elapsed+self.sender().interval())%1000
        self.repaint()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        self.helper.paint(painter, event, self.elapsed)
        painter.end()

class Widget(QWidget):
    def __init__(self, helper, parent=None, flags=Qt.Widget):
        super(Widget,self).__init__(parent)
        self.helper = helper
        self.elapsed = 0
        self.setFixedSize(200,200)
        
    @pyqtSlot()
    def animate(self):
        self.elapsed = (self.elapsed+self.sender().interval())%1000
        self.repaint()
    
    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        self.helper.paint(painter, event, self.elapsed)
        painter.end()
    
class Helper(object):
    def __init__(self):
        self.background = None
        self.circleBrush = None
        self.background = None
        self.circlePen = None
        self.textPen = None
        self.textFont = QFont()
        
        gradient = QLinearGradient(QPointF(50,-20),QPointF(80,20))
        #gradient = QLinearGradient(QPointF(0,0),QPointF(100,100))
        gradient.setColorAt(0.0,Qt.white)
        gradient.setColorAt(1.0,QColor(0xa6, 0xce, 0x39))
        
        self.background = QBrush(QColor(64, 32, 64))
        
        self.circleBrush = QBrush(gradient)
        self.circlePen = QPen(Qt.black)
        self.circlePen.setWidth(2)
        
        self.textPen = QPen(Qt.white)
        self.textFont.setPixelSize(50)
        
    
    def paint(self, painter, event, elapsed):
        painter.fillRect(event.rect(), self.background)
        #painter.setBrush(self.circleBrush)
        painter.translate(100,100)
        
        painter.save()
        painter.setBrush(self.circleBrush)
        painter.setPen(self.circlePen)
        painter.rotate(elapsed*0.03)
        
        r = elapsed/1000.0
        n = 30
        for i in range(n):
            painter.rotate(30)
            radius = 0+120.0*((i+r)/n)
            circleRadius = 1+(i+r)/n*20
            painter.drawEllipse(QRectF(radius, -circleRadius,
                                        circleRadius*2, circleRadius*2))            
            
        painter.restore()
        
        painter.setPen(self.textPen)
        painter.setFont(self.textFont)
        painter.drawText(QRect(-50, -50, 100, 100), Qt.AlignCenter, "XO")
        #painter.drawRect(QRect(-50, -50, 100, 100))
        

class Window(QWidget):
    def __init__(self, parent=None, flags=Qt.Widget):
        super(Window,self).__init__(parent,flags)
        self._helper = Helper()
        self.elapsed = 0
        
        native = Widget(self._helper,self)
        openGL = GLWidget(self._helper,self)
        
        nativeLabel = QLabel('Native')
        nativeLabel.setAlignment(Qt.AlignHCenter)
        
        openGLLabel = QLabel('OpenGL')
        openGLLabel.setAlignment(Qt.AlignHCenter)
        
        layout = QGridLayout()
        layout.addWidget(native, 0, 0)
        layout.addWidget(openGL, 0, 1)
        layout.addWidget(nativeLabel, 1, 0)
        layout.addWidget(openGLLabel, 1, 1)
        self.setLayout(layout)
        
        timer = QTimer(self)
        #self.connect(timer, SIGNAL('timeout()'), self, SLOT('test()'))
        self.connect(timer, SIGNAL('timeout()'), openGL, SLOT('animate()'))
        self.connect(timer, SIGNAL('timeout()'), native, SLOT('animate()'))
        timer.start(50)

if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    win = Window()
    win.show()
    qApp.exec_()