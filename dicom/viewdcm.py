# coding=utf-8

import sys
import numpy as np
from PyQt4.QtGui import *
from PyQt4.QtCore import *

#import gdcm
import dicom
from dicom.filereader import read_file
#from binascii import b2a_hex,a2b_hex

filename = r'E:\Project\Python\dicom\306.dcm'
filenameb = r'E:\Project\Python\dicom\qrcode.jpg'

class DCMWidget(QWidget):
    def __init__(self, parent=None, flags=Qt.Widget):
        super(DCMWidget,self).__init__(parent, flags)
        
        #self.painter = QPainter(self)        
        
        self.dcmdata = read_file(filename)
        self.row = self.dcmdata.Rows  # width
        self.column = self.dcmdata.Columns  # height
        self.modality = self.dcmdata.Modality
        
        self.slope = self.dcmdata.RescaleSlope
        self.interceprt = self.dcmdata.RescaleIntercept
        
        print 'Rows,Column:',self.row,self.column
        print 'Modality:',self.modality
        
        if type(self.dcmdata.WindowWidth) == dicom.multival.MultiValue:
            self.winw = self.dcmdata.WindowWidth[0] 
            self.winc = self.dcmdata.WindowCenter[0]
        else:
            self.winw = self.dcmdata.WindowWidth 
            self.winc = self.dcmdata.WindowCenter            
        
        print 'winw,winc:',self.winw,self.winc  
        print 'pixel array shape:',self.dcmdata.pixel_array.shape
        
        self.win_width = QApplication.desktop().width()
        self.win_height = QApplication.desktop().height()
        
        self.resize(800, 600)
        #self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        self.image = None
        self.pmin = None
        self.pmax = None
        
        #self.pix = QPixmap(filenameb)
        
        self.pixel_array_ori = self.dcmdata.pixel_array*self.slope+self.interceprt
        self.pixel_array_lut = self.get_LUT_value(self.pixel_array_ori,self.winw,self.winc)
        
        self.genImage()
  
    def paintEvent(self, e):
        #print 'paintEvent'
        
        painter = QPainter(self)
        
        #painter.translate(center)
         
        brush = QBrush(Qt.black)      
        painter.fillRect(self.rect(), brush)
        
        painter.setRenderHint(QPainter.SmoothPixmapTransform,True) # 双线性插值 not近邻取样
        #painter.scale(2,2)
        
        #painter.translate(-center)
        
        image = QImage()
        #image.scaled(100,100, Qt.KeepAspectRatio)

        image_center = QPoint(self.column / 2, self.row / 2) 
        win_center = QPoint(self.width()/2, self.height()/2)
        
        #painter.translate(win_center-image_center)
        
        target = QRect(0, 0, 100, 100)
        
        
        source = QRect(0, 0, self.row, self.column)
        #painter.drawPixmap(QPoint(),self.pix)
        #painter.drawImage(target, self.image, source)
        painter.drawImage(QPoint(), self.image)
        
        pass
     
    def get_LUT_value(self,data, window, level):
        """Apply the RGB Look-Up Table for the given data and window/level value."""
    
        # modified by x.h. 
        #data = np.array(data,dtype='int16')         
        cond_min = np.array([data <= (level - 0.5 - (window - 1.0) / 2)])
        cond_max = np.array([data >= (level - 0.5 + (window - 1.0) / 2)])
        cond_tot = np.logical_or.reduce([cond_min,cond_max], axis=0)#keepdims=True        
        cond_list = np.vstack([cond_min,cond_max,~cond_tot])
        
        self.pmin =  (level - 0.5 - (window - 1.0) / 2.0)
        self.pmax =  (level - 0.5 + (window - 1.0) / 2.0)

        return np.piecewise(data,
                            cond_list,
                            [0, 255, lambda data: (data-self.pmin)/float(self.pmax-self.pmin)*255.0])      
    def genImage(self):
        self.image = QImage(self.column, self.row,QImage.Format_RGB16)
        for i in range(self.column):
            for j in range(self.row):
                pv = int(self.pixel_array_lut[j][i])
                #print pv
                #pv = self.dcmdata.pixel_array[j][i]
                #print pv
                
                #pixel = self.dcmdata.pixel_array[j][i]
                #if pixel <= self.pmin:
                    #pixel = 0
                #elif pixel >= self.pmax:
                    #pixel = 255
                #else:
                    #pixel = g(pixel)
                    #if pixel > 255:
                        #print self.dcmdata.pixel_array[j][i],pixel
                #pv = int(pixel)
                #print pv
                gray = qRgb(pv,pv,pv)
                #gray = qGray(pv,pv,pv)
                self.image.setPixel(i,j,gray)        

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wgt = DCMWidget()
    wgt.show()
    app.exec_()
