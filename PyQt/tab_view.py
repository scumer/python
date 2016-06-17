# coding=utf-8

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PIL import ImageQt

import gdcm
import dicom
from dicom.filereader import read_file
from binascii import b2a_hex,a2b_hex



class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None, flags=0):
        QtGui.QMainWindow.__init__(self, parent)
        self.setWindowTitle(u'TabViewer')    
        #self.setGeometry(QtCore.QRect(480,640,600,400))
       
        openAct = QtGui.QAction('&Open', self)
        closeAct = QtGui.QAction('&Close', self)
        exitAct = QtGui.QAction('&Exit', self)
        
        fileMenu = self.menuBar().addMenu(self.tr("&File"))
        fileMenu.addAction(openAct)
        fileMenu.addAction(closeAct)
        fileMenu.addAction(exitAct)
        
        self.connect(openAct, QtCore.SIGNAL('triggered()'), self, QtCore.SLOT('action_open()'))
        
        self.dcm_read()
     
    open_files = None   
    
    @pyqtSlot()
    def action_open(self):
        open_files = QFileDialog.getOpenFileNames(self, self.tr('open selected tab files'),QDir.currentPath())
        for i in open_files:           
            print unicode(i)
        if open_files:
            image = QImage(open_files[0])
            label = QLabel()
            #label.setPixmap(QPixmap.fromImage(image))
            
    def dcm_read(self):
        filename = r'E:\Project\Python\PyQt\306-.dcm'
        label = QLabel()
 
    
        dcm = read_file(filename)
        row = dcm.Rows
        column = dcm.Columns
        ba = dcm.BitsAllocated
        bs = dcm.BitsStored
        bh = dcm.HighBit
        print row,column
        print ba,bs,bh
        buf = dcm.PixelData
        
        win_width = dcm.WindowWidth
        win_center = dcm.WindowCenter     
        print dcm.WindowWidth
        print dcm.WindowCenter         

        #image = QImage(buf,column,row, row*ba/8, QImage.Format_RGB16)
        
        ds = QDataStream(QByteArray(buf))
        
        pixel_arrar = dcm.pixel_array
        image = QImage(column,row,QImage.Format_RGB16)
        #imageqt_ = ImageQt.ImageQt(image)
        
        
        from dicom.contrib import pydicom_PIL
        image_array = pydicom_PIL.get_LUT_value(dcm.pixel_array, dcm.WindowWidth[0], dcm.WindowCenter[0])
        
       
        index = 0
        for i in range(row):
            for j in range(column):
                #pv = ds.readRawData(2)

                start = index*2
                stop = (index+1)*2
                pv = buf[start:stop]
                index += 1                
                
                #if pixel_arrar[i][j] > 255:
                    ##print b2a_hex(pv),
                    #print 'pixel:',pixel_arrar[i][j], #pixel_arrar[j][i],
                    #print  int(b2a_hex(pv[::-1]),16)

                #pv = int(b2a_hex(pv[::-1]),16)
                
                #pv = pixel_arrar[j][i]
                g = lambda x :  x * 299/1000 + x * 587/1000 + x * 114/1000
                pv = int(image_array[j][i])
                
                gray = qGray(int(pv),int(pv),int(pv))
                #gray = g(pv)
                
                
                
                #gray = qRgb(pv,pv,pv)
                #print pv,gray

                image.setPixel(i,j,pv)
                pass
        #image.scaled(800,800)
        
        pix = QPixmap.fromImage(image)
        
        #pix.scaled(800,800)
        label.setPixmap(pix)
        
    
        self.setCentralWidget(label)
        #label.adjustSize()
        label.showMaximized()
        #label.show()
      


if __name__ == '__main__':
    qApp = QtGui.QApplication(sys.argv)
    
    #main_window = MainWindow()
    #main_window.show()
    from dicom.contrib import pydicom_PIL
    import numpy as np
    filename = r'E:\Project\Python\PyQt\306.dcm'
    dataset = read_file(filename)

    print dataset.WindowWidth
    print dataset.WindowCenter    
    print dataset.BitsAllocated
    
    #dataset.WindowWidth = 250
    #dataset.WindowCenter = 40
    #dataset.pixel_array = np.array(dataset.pixel_array,dtype='int16')
    image = pydicom_PIL.get_LUT_value(dataset.pixel_array, dataset.WindowWidth[0], dataset.WindowCenter[0])
    print image.ndim,np.shape(image)
    print image.__array_interface__    
    
    
    #print np.array(np.array(dataset.pixel_array,dtype='int16')).__array_interface__  
    
    pydicom_PIL.show_PIL(dataset)


    qApp.exec_()
