# coding=utf-8


import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None, flags=0):
        self.widget = None
        self.topFiller = None
        self.infoLabel = None
        self.bottomFiller = None
        self.vbox_layout = None
    
        self.cutAct = None
        self.copyAct = None
        self.pasteAct = None 
        
        self.newAct = None
        self.exitAct = None
        
        self.undoAct = None
        self.boldAct = None
        self.italicAct = None
        
        self.aboutAct = None
        self.aboutQtAct = None
        
        self.leftAlignAct = None
        self.rightAlignAct = None

        QMainWindow.__init__(self, parent)
        
        widget = QWidget()
        self.setCentralWidget(widget)
        
        self.topFiller = QWidget()
        self.topFiller.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        self.infoLabel = QLabel('<li>Choose a menu option,<br> or right-click to '
                           'invoke a context menu</li>')
        
        self.infoLabel.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        self.infoLabel.setAlignment(Qt.AlignCenter)
        
        self.radiobtn = QRadioButton(self)
        self.radiobtn.setCheckable(False)
        
        self.tlabel = QLabel("1")
        self.tlabel.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        self.tlabel.setAlignment(Qt.AlignCenter)        
        rect = QRect(0,0,50,50)
        region = QRegion(rect,QRegion.Ellipse)
        self.tlabel.setMask(region)

        
        self.bottomFiller = QWidget()
        self.bottomFiller.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        vbox_layout = QVBoxLayout()
        vbox_layout.setMargin(5)
        vbox_layout.addWidget(self.topFiller)
        vbox_layout.addWidget(self.infoLabel)
        vbox_layout.addWidget(self.tlabel)
        vbox_layout.addWidget(self.bottomFiller)
        widget.setLayout(vbox_layout)
        
        self.createActions()
        self.createMenus()
        
        msg = self.tr("A context menu is available by right-clicking")
        self.statusBar().showMessage(msg)
        
        self.setWindowTitle('Menus')
        self.setMinimumSize(60,60)
        self.resize(480, 320)
        

    
    def createActions(self):
        self.newAct = QAction(self.tr('&New'), self)
        self.newAct.setShortcut(QKeySequence.New)
        self.newAct.setStatusTip('tip new file')
        self.connect(self.newAct, SIGNAL('triggered()'), self, SLOT('newFile()'))
        
        self.exitAct = QAction('E&xit', self)
        self.exitAct.setShortcut(QKeySequence.Close)
        self.connect(self.exitAct, SIGNAL('triggered()'), self, SLOT('close()'))
        
        self.undoAct = QAction('&Undo', self)
        self.undoAct.setShortcut(QKeySequence.Undo)
        
        self.boldAct = QAction('&Bold', self)
        boldFont = self.boldAct.font()
        boldFont.setBold(True)
        self.boldAct.setFont(boldFont)
        
        self.aboutAct = QAction('About &Qt',self)
        self.aboutAct.setStatusTip('tip about')
        self.connect(self.aboutAct, SIGNAL('triggered()'), qApp, SLOT('aboutQt()'))
        
        self.leftAlignAct = QAction('Left', self)
        self.leftAlignAct.setCheckable(True)
        self.leftAlignAct.setShortcut('Ctrl+L')
        
        self.rightAlignAct = QAction('Right', self)
        self.rightAlignAct.setCheckable(True)
        self.rightAlignAct.setShortcut('Ctrl+R')
        
        alignmentGroup  = QActionGroup(self)
        alignmentGroup.addAction(self.leftAlignAct)
        alignmentGroup.addAction(self.rightAlignAct)
        self.leftAlignAct.setChecked(True)
        
        
        self.cutAct = QAction('Cut', self)
           
    def createMenus(self):
        fileMenu = self.menuBar().addMenu(self.tr('&File'))
        fileMenu.addAction(self.newAct)
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAct)
        
        editMenu = self.menuBar().addMenu('&Edit')
        editMenu.addAction(self.undoAct)
        fileMenu.addSeparator()
        editMenu.addAction(self.cutAct)
        fileMenu.addSeparator()
        
        formatMenu = editMenu.addMenu('&Format')
        formatMenu.addAction(self.boldAct)
        formatMenu.addSeparator().setText('Se Alignment')
        formatMenu.addAction(self.leftAlignAct)
        formatMenu.addAction(self.rightAlignAct)
        
        helpMenu = self.menuBar().addMenu('&Help')
        helpMenu.addAction(self.aboutAct)
        
        tb = QToolBar(u'Test')
        #tb.setIconSize(QSize(100,100 ))
        self.addToolBar(Qt.TopToolBarArea, tb)
        ac = QAction('Test',self)
        tb.addAction(ac)
        tb.addSeparator()
        tb.setMovable(False)
        
    
    def contextMenuEvent(self, event):
        menu = QMenu(self)
        menu.addAction(self.cutAct)
        #menu.addAction(self.copyAct)
        #menu.addAction(self.pasteAct)     
        menu.exec_(event.globalPos())
        
    @pyqtSlot()
    def newFile(self):
        self.infoLabel.setText(self.tr("Invoked <b>File|New</b>"))
        
    @pyqtSlot()
    def undo(self):
        self.infoLabel.setText(self.tr("Invoked <b>Edit|Undo</b>"))
        
    @pyqtSlot()
    def cut(self):
        self.infoLabel.setText(self.tr("Invoked <b>Edit|Cut</b>")) 
    
    @pyqtSlot()
    def bold(self):
        self.infoLabel.setText(self.tr("Invoked <b>Edit|Format|Bold</b>"))     
        
    @pyqtSlot()
    def leftAlign(self):
        self.infoLabel.setText(self.tr("Invoked <b>Edit|Format|leftAlign</b>")) 
    
    @pyqtSlot()
    def about(self):
        QMessageBox.about(self, 'About Menu', "The <b>Menu</b> example shows how to create menu-bar menus and context menus.")
        
    @pyqtSlot()
    def aboutQt(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    mainwindow = MainWindow()
    mainwindow.show()
    
    app.exec_()