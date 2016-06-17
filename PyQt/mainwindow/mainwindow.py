# coding=utf-8


import sys
import image_qrc
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from toolbar import ToolBar
from colorswatch import *


#name,flags,area
g_set = (("Black", 0, Qt.LeftDockWidgetArea),
         ("White", 0, Qt.RightDockWidgetArea),
         ("Red", 0, Qt.TopDockWidgetArea),
         ("Green", 0, Qt.TopDockWidgetArea),
         ("Blue", 0, Qt.BottomDockWidgetArea),
         ("Yellow", 0, Qt.BottomDockWidgetArea))

class MainWindow(QMainWindow):
    def __init__(self, parent=None, flags=0):
        QMainWindow.__init__(self, parent)
        
        self.center = None
        self.toolbars = []
        self.dockWidgetMenu = None
        self.mainWindowMenu = None
        self.mapper = None
        self.extraDockWidgets = []
        self.createDockWidgetAction = None
        self.destroyDockWidgetMenu = None
    
        self.setObjectName('MainWindow')
        self.setWindowTitle('MainWindow')
        
        self.center = QTextEdit(self)
        #self.center.setReadOnly(True)
        self.center.setMinimumSize(400,205)
        self.setCentralWidget(self.center)
        
        self.setupToolBar()
        self.setupMenuBar()
        
        #self.setupDockWidgets(customSizeHints)
        self.setupDockWidgets()
        self.statusBar().showMessage('Status Bar')
        
        self.setWindowIcon(QIcon(QPixmap(':res/image/qt.png')))
           
    #@pyqtSlot()    
    def showEvent(self, event):        
        QMainWindow.showEvent(self, event)
        #QMainWindow.showEvent(event)  # error
        #QShowEvent()
        print 'call showEvent'
        pass
    
    @pyqtSlot()
    def actionTriggered(self, action):
        print ("action '%s' triggered"), action.text().toLocal8Bit().data()
        print action.text()
        print action.text().toLocal8Bit()
    
    @pyqtSlot(int)
    def setCorner(self,id):
        print id
         
    @pyqtSlot()
    def saveLayout(self):
        pass
         
    @pyqtSlot()
    def loadLayout(self):
        pass
 
    @pyqtSlot()
    def switchLayoutDirection(self):
        pass

    @pyqtSlot()
    def setDockOptions(self):
        pass
    
    @pyqtSlot()
    def createDockWidget(self):
        dialog = CreateDockWidgetDialog(self)
        ret = dialog.exec_()
        if ret == QDialog.Rejected:
            return
        
        dw = QDockWidget()
        dw.setObjectName(dialog.objectName())
        dw.setWindowTitle(dialog.objectName())
        dw.setWidget(QTextEdit())
        
        area = dialog.location()
        if area != Qt.NoDockWidgetArea:
            self.addDockWidget(area, dw)
        else:
            if not self.restoreDockWidget(dw):
                QMessageBox.warning(self, '', 'Failed to restore dock widget')
                #dw.deleteLater()
                return
        self.extraDockWidgets.append(dw)
        self.destroyDockWidgetMenu.setEnabled(True)
        self.destroyDockWidgetMenu.addAction(QAction(dialog.objectName(),self))
        
    
    @pyqtSlot(QAction)
    def destroyDockWidget(self,action):
        print action
     
    def setupToolBar(self):
        for i in range(3):
            tb = ToolBar('Tool Bar {0}'.format(i+1), self)
            self.toolbars.append(tb)
            self.addToolBar(tb)
 
    def setupMenuBar(self):
        #-----File Menu
        menu = self.menuBar().addMenu('&File') 
        
        action = menu.addAction('Save layout')
        self.connect(action, SIGNAL('triggered()'), self, SLOT('saveLayout()'))
        
        action = menu.addAction('Load layout')
        self.connect(action, SIGNAL('triggered()'), self, SLOT('loadLayout()'))        

        action = menu.addAction('Switch layout dir')
        self.connect(action, SIGNAL('triggered()'), self, SLOT('switchLayoutDirection()'))   
        
        menu.addSeparator()
        menu.addAction('&Quit', self, SLOT('close()'))
        
        #------Main Window Menu
        self.mainWindowMenu = self.menuBar().addMenu('Main Window')
        
        action = self.mainWindowMenu.addAction('Animated docks')
        action.setCheckable(True)
        action.setChecked(self.dockOptions() & self.AnimatedDocks)
        self.connect(action, SIGNAL('toggled(bool)'), self, SLOT('setDockOptions()'))
        
        action = self.mainWindowMenu.addAction('Allow nested docks')
        action.setCheckable(True)
        action.setChecked(self.dockOptions() & self.AllowNestedDocks)
        self.connect(action, SIGNAL('toggled(bool)'), self, SLOT('setDockOptions()'))
        
        action = self.mainWindowMenu.addAction('Allow tabbed docks')
        action.setCheckable(True)
        action.setChecked(self.dockOptions() & self.AllowTabbedDocks)
        self.connect(action, SIGNAL('toggled(bool)'), self, SLOT('setDockOptions()'))
        
        action = self.mainWindowMenu.addAction('Force tabbed docks')
        action.setCheckable(True)
        action.setChecked(self.dockOptions() & self.ForceTabbedDocks)
        self.connect(action, SIGNAL('toggled(bool)'), self, SLOT('setDockOptions()'))
        
        action = self.mainWindowMenu.addAction('Vertical tabs')
        action.setCheckable(True)
        action.setChecked(self.dockOptions() & self.VerticalTabs)
        self.connect(action, SIGNAL('toggled(bool)'), self, SLOT('setDockOptions()'))
        
        #-----Tool bars Menu
        toolBarMenu = self.menuBar().addMenu('Tool bars')
        toobar_count = len(self.toolbars)
        for i in range(toobar_count):
            toolBarMenu.addMenu(self.toolbars[i].menu)
            pass
            
        self.dockWidgetMenu = self.menuBar().addMenu('Dock Widgets')

    def setupDockWidgets(self):
        self.mapper = QSignalMapper(self)
        self.connect(self.mapper, SIGNAL('mapped(int)'), self, SLOT('setCorner(int)'))
        #self.mapper.mapped[int].connect(self.setCorner, Qt.QueuedConnection)
        
        corner_menu = self.dockWidgetMenu.addMenu('Top left')   
        group = QActionGroup(self)
        
        group.setExclusive(True)
        addAction(corner_menu,'top dock area', group, self.mapper, 0)
        addAction(corner_menu,'left dock area', group, self.mapper, 1)
        
        
        self.createDockWidgetAction = QAction('Add dock widget...', self)
        self.connect(self.createDockWidgetAction,SIGNAL('triggered()'),SLOT('createDockWidget()'))
        
        self.destroyDockWidgetMenu = QMenu('Destroy dock widget', self)
        self.destroyDockWidgetMenu.setEnabled(False)
        #self.connect(self.destroyDockWidgetMenu,SIGNAL('triggered(QAction)'), SLOT('destroyDockWidget(QAction)'))        
        self.destroyDockWidgetMenu.triggered[QAction].connect(self.destroyDockWidget, Qt.QueuedConnection)        
        
        self.dockWidgetMenu.addSeparator()
        
        global g_set
        setcount = len(g_set)
        for i in range(setcount):
            swatch = ColorSwatch(g_set[i][0], self, Qt.WindowFlags(g_set[i][1]))
            #swatch.setWindowIcon(QIcon(QPixmap(':res/image/qt.png')))
            if i%2 == 1:
                swatch.setWindowIcon(QIcon(QPixmap(':res/image/qt.png'))) #?????????
            if g_set[i][0] == 'Blue':
                titleBar = BlueTitleBar(swatch)
                swatch.setTitleBarWidget(titleBar)
                swatch.topLevelChanged[bool].connect(titleBar.updateMask, Qt.QueuedConnection)
                #swatch.featuresChanged[QDockWidget.DockWidgetFeatures].connect(titleBar.updateMask, Qt.QueuedConnection)
                self.connect(swatch, SIGNAL('topLevelChanged(bool)'), titleBar, SLOT('updateMask()'))
                self.connect(swatch, SIGNAL('featuresChanged(QDockWidget::DockWidgetFeatures)'), titleBar, SLOT('updateMask()'))
                
            self.addDockWidget(g_set[i][2], swatch)
            self.dockWidgetMenu.addMenu(swatch.menu)
                
                
                
        
        self.dockWidgetMenu.addAction(self.createDockWidgetAction)
        self.dockWidgetMenu.addMenu(self.destroyDockWidgetMenu)
        
class CreateDockWidgetDialog(QDialog):
    def __init__(self, parent=None, flags=0):
        QDialog.__init__(self)
        
        self.m_objectName = None
        self.m_location = None
        
        layout = QGridLayout(self)
        layout.addWidget(QLabel('Object name'),0,0)
        self.m_objectName = QLineEdit()
        layout.addWidget(self.m_objectName,0,1)
        
        layout.addWidget(QLabel("Location"),1,0)
        self.m_location = QComboBox()
        self.m_location.setEditable(False)
        self.m_location.addItem(self.tr("Top"))
        self.m_location.addItem(self.tr("Left"))
        self.m_location.addItem(self.tr("Right"))
        self.m_location.addItem(self.tr("Bottom"))
        self.m_location.addItem(self.tr("Restore"))  
        layout.addWidget(self.m_location,1,1)
        
        buttonLayout = QHBoxLayout()
        layout.addLayout(buttonLayout,2,0,1,2)
        buttonLayout.addStretch()
        
        cancelbtn = QPushButton('Cancel')
        self.connect(cancelbtn, SIGNAL('clicked()'),self, SLOT('reject()'))
        buttonLayout.addWidget(cancelbtn)
        okbtn = QPushButton('OK')
        self.connect(okbtn, SIGNAL('clicked()'),self, SLOT('accept()'))
        buttonLayout.addWidget(okbtn)   
        
        okbtn.setDefault(True)
         
    def objectName(self):
        return self.m_objectName.text()
    
    def location(self): 
        dict_location = {
        0:Qt.TopDockWidgetArea,
        1:Qt.LeftDockWidgetArea,
        2:Qt.RightDockWidgetArea,
        3:Qt.BottomDockWidgetArea,
        4:Qt.NoDockWidgetArea}
        
        return dict_location[self.m_location.currentIndex()]

def addAction(menu, text, group, mapper, id):
    first = True if group.actions() else False
    result = menu.addAction(text)
    result.setCheckable(True)
    result.setChecked(first)
    group.addAction(result)
    QObject.connect(result, SIGNAL('triggered()'), mapper, SLOT('map()'))
    mapper.setMapping(result, id)
    return result
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    mainwindow = MainWindow()
    mainwindow.show()
    
    #dlg = CreateDockWidgetDialog()
    #dlg.show()
    
    app.exec_()