# coding=utf-8

from PyQt4.QtGui import * 
from PyQt4.QtCore import * 
import sys
from render_qt_text import * 

#import qrc
#from image_qrc import *
import image_qrc
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


app = QApplication(sys.argv)
label = QLabel()
pix = genIcon(label.size(), '1', Qt.blue)
#label.setPixmap(QPixmap(r'E:\Project\Python\PyQt\mainwindow\image\qt.png'))
#label.setPixmap(QPixmap(r':res/image/qt.png'))
label.setPixmap(pix)
label.show()

app.exec_()


