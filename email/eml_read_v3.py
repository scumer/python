# coding=utf-8

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtOpenGL import *
import sys

from eml_read_v2 import *
dirname = r'F:\DOCS\salary'

class Window(QMainWindow):
    def __init__(self, parent=None, flags=Qt.Widget):
        super(Window,self).__init__(parent,flags)
        
        
        
        colname = []
        colcnt = []    
        get_salary(dirname,colname,colcnt)
        del colname[1:5]
        #for i in colname:
            #print '%s'%i,',',
        #print ''
        
        for col in colcnt:
            del col[1:5]
            #print colcnt[0]
                #for cnt in col:
                    #print '%s'%cnt,',',
                #print ''   
        rows = len(colname)
        columns = len(colcnt)
        table = QTableWidget(columns,rows)
        self.setCentralWidget(table)    
        
        titleBackground = QColor(Qt.lightGray)
        titleFont = table.font()
        titleFont.setBold(True)
        
        for i in range(len(colname)):
            #print colname[i]
            table.setItem(0, i, QTableWidgetItem(colname[i]))
            table.item(0, i).setBackgroundColor(titleBackground)
            #table.item(0, i).setFont(titleFont)
        
        for i in range(len(colcnt)):
            for j in range(len(colcnt[i])):
                table.setItem(i+1, j, QTableWidgetItem(colcnt[i][j]))
            
        #table.item(0,0).setBackgroundColor()
        self.showMaximized()
    
    
    
        


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    win = Window()
    win.show()
    qApp.exec_()