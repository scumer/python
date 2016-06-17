# coding=utf-8

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import embeddedDialog

class embededDlg(QDialog):
    def __init__(self, parent=None, flags=0):
        QDialog.__init__(self)
        
        self.ui = embeddedDialog.Ui_Dialog()
        self.ui.setupUi(self)
        
        self.ui.layoutDirection.setCurrentIndex(self.layoutDirection() != Qt.LeftToRight)
        
        flags = Qt.Dialog | Qt.WindowCloseButtonHint
        self.setWindowFlags(flags)
        
        #self.ui.style.setWindowFlags(Qt.WindowFlags(Qt.WindowContextHelpButtonHint))
        #self.resize(483, 139)
        self.adjustSize()
        
        #print self.style().objectName()
        for stylename in QStyleFactory.keys():
            self.ui.style.addItem(stylename)
            if self.style().objectName().toLower() == stylename.toLower():
                self.ui.style.setCurrentIndex(self.ui.style.count()-1)
        
        self.connect(self.ui.layoutDirection,SIGNAL('activated(int)'),
                     self, SLOT('layoutDirectionChanged(int)'))
        self.connect(self.ui.spacing,SIGNAL('valueChanged(int)'),
                     self, SLOT('spacingChanged(int)'))   
        self.connect(self.ui.fontComboBox,SIGNAL('currentFontChanged(QFont)'),
                     self, SLOT('fontChanged(QFont)'))   
        self.connect(self.ui.style,SIGNAL('activated(QString)'),
                     self, SLOT('styleChanged(QString)'))    
    
    @pyqtSlot(int)
    def layoutDirectionChanged(self,idx):
        self.setLayoutDirection(Qt.LeftToRight if idx==0 else Qt.RightToLeft)

    @pyqtSlot(int)
    def spacingChanged(self,idx):
        self.layout().setSpacing(idx)
        self.adjustSize()
    
    @pyqtSlot(QFont)
    def fontChanged(self,font):
        #print unicode(font.toString())
        self.setFont(font)
        pass
    
    @pyqtSlot(QString)
    def styleChanged(self,qstr):
        #print unicode(qstr)
        style = QStyleFactory.create(qstr)
        if style:
            setStyleHelper(self,style)


def setStyleHelper(widget, style):
    widget.setStyle(style)
    widget.setPalette(style.standardPalette())
    for child in widget.children():
        if (isinstance(child, QWidget)):
            setStyleHelper(child,style)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    dialog = embededDlg()
    dialog.show()
    
    app.exec_()