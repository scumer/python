# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mwidget.ui'
#
# Created: Wed Mar 16 21:45:55 2016
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        MainWidget.setObjectName(_fromUtf8("MainWidget"))
        MainWidget.resize(231, 350)
        self.gridLayout_2 = QtGui.QGridLayout(MainWidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.stackedWidget = QtGui.QStackedWidget(MainWidget)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.gridLayout_3 = QtGui.QGridLayout(self.page)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_9 = QtGui.QLabel(self.page)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.page)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.page)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.ln_addr = QtGui.QLineEdit(self.page)
        self.ln_addr.setObjectName(_fromUtf8("ln_addr"))
        self.gridLayout.addWidget(self.ln_addr, 9, 1, 1, 1)
        self.ln_company = QtGui.QLineEdit(self.page)
        self.ln_company.setObjectName(_fromUtf8("ln_company"))
        self.gridLayout.addWidget(self.ln_company, 4, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.page)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.page)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.ln_site = QtGui.QLineEdit(self.page)
        self.ln_site.setObjectName(_fromUtf8("ln_site"))
        self.gridLayout.addWidget(self.ln_site, 8, 1, 1, 1)
        self.ln_dept = QtGui.QLineEdit(self.page)
        self.ln_dept.setObjectName(_fromUtf8("ln_dept"))
        self.gridLayout.addWidget(self.ln_dept, 2, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.page)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 9, 0, 1, 1)
        self.ln_post = QtGui.QLineEdit(self.page)
        self.ln_post.setObjectName(_fromUtf8("ln_post"))
        self.gridLayout.addWidget(self.ln_post, 3, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.page)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.ln_telephone = QtGui.QLineEdit(self.page)
        self.ln_telephone.setObjectName(_fromUtf8("ln_telephone"))
        self.gridLayout.addWidget(self.ln_telephone, 6, 1, 1, 1)
        self.ln_name = QtGui.QLineEdit(self.page)
        self.ln_name.setObjectName(_fromUtf8("ln_name"))
        self.gridLayout.addWidget(self.ln_name, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.page)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtGui.QLabel(self.page)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.page)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.ln_mobile = QtGui.QLineEdit(self.page)
        self.ln_mobile.setObjectName(_fromUtf8("ln_mobile"))
        self.gridLayout.addWidget(self.ln_mobile, 5, 1, 1, 1)
        self.ln_no = QtGui.QLineEdit(self.page)
        self.ln_no.setObjectName(_fromUtf8("ln_no"))
        self.gridLayout.addWidget(self.ln_no, 1, 1, 1, 1)
        self.ln_email = QtGui.QLineEdit(self.page)
        self.ln_email.setObjectName(_fromUtf8("ln_email"))
        self.gridLayout.addWidget(self.ln_email, 7, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 5, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 10, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btn_gencode = QtGui.QPushButton(self.page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_gencode.sizePolicy().hasHeightForWidth())
        self.btn_gencode.setSizePolicy(sizePolicy)
        self.btn_gencode.setMinimumSize(QtCore.QSize(20, 30))
        self.btn_gencode.setMaximumSize(QtCore.QSize(80, 30))
        self.btn_gencode.setObjectName(_fromUtf8("btn_gencode"))
        self.horizontalLayout.addWidget(self.btn_gencode)
        spacerItem2 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.btn_import = QtGui.QPushButton(self.page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_import.sizePolicy().hasHeightForWidth())
        self.btn_import.setSizePolicy(sizePolicy)
        self.btn_import.setMinimumSize(QtCore.QSize(20, 30))
        self.btn_import.setMaximumSize(QtCore.QSize(80, 30))
        self.btn_import.setObjectName(_fromUtf8("btn_import"))
        self.horizontalLayout.addWidget(self.btn_import)
        spacerItem3 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.page_2)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.lb_image = QtGui.QLabel(self.page_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_image.sizePolicy().hasHeightForWidth())
        self.lb_image.setSizePolicy(sizePolicy)
        self.lb_image.setText(_fromUtf8(""))
        self.lb_image.setObjectName(_fromUtf8("lb_image"))
        self.gridLayout_4.addWidget(self.lb_image, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem4 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.btn_back = QtGui.QPushButton(self.page_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_back.sizePolicy().hasHeightForWidth())
        self.btn_back.setSizePolicy(sizePolicy)
        self.btn_back.setMinimumSize(QtCore.QSize(20, 30))
        self.btn_back.setMaximumSize(QtCore.QSize(80, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("F:/图片/ICO/1458111253_ic_arrow_back_48px.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_back.setIcon(icon)
        self.btn_back.setObjectName(_fromUtf8("btn_back"))
        self.horizontalLayout_2.addWidget(self.btn_back)
        spacerItem5 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.btn_saveas = QtGui.QPushButton(self.page_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_saveas.sizePolicy().hasHeightForWidth())
        self.btn_saveas.setSizePolicy(sizePolicy)
        self.btn_saveas.setMinimumSize(QtCore.QSize(20, 30))
        self.btn_saveas.setMaximumSize(QtCore.QSize(80, 30))
        self.btn_saveas.setObjectName(_fromUtf8("btn_saveas"))
        self.horizontalLayout_2.addWidget(self.btn_saveas)
        spacerItem6 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout_2.addWidget(self.stackedWidget, 0, 1, 1, 1)

        self.retranslateUi(MainWidget)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWidget)
        MainWidget.setTabOrder(self.ln_name, self.ln_no)
        MainWidget.setTabOrder(self.ln_no, self.ln_dept)
        MainWidget.setTabOrder(self.ln_dept, self.ln_post)
        MainWidget.setTabOrder(self.ln_post, self.ln_company)
        MainWidget.setTabOrder(self.ln_company, self.ln_mobile)
        MainWidget.setTabOrder(self.ln_mobile, self.ln_telephone)
        MainWidget.setTabOrder(self.ln_telephone, self.ln_email)
        MainWidget.setTabOrder(self.ln_email, self.ln_site)
        MainWidget.setTabOrder(self.ln_site, self.ln_addr)
        MainWidget.setTabOrder(self.ln_addr, self.btn_gencode)
        MainWidget.setTabOrder(self.btn_gencode, self.btn_import)
        MainWidget.setTabOrder(self.btn_import, self.btn_back)
        MainWidget.setTabOrder(self.btn_back, self.btn_saveas)

    def retranslateUi(self, MainWidget):
        MainWidget.setWindowTitle(_translate("MainWidget", "BCard", None))
        self.label_9.setText(_translate("MainWidget", "官网主页", None))
        self.label_6.setText(_translate("MainWidget", "移动电话", None))
        self.label_7.setText(_translate("MainWidget", "固定电话", None))
        self.label_8.setText(_translate("MainWidget", "电子邮箱", None))
        self.label_5.setText(_translate("MainWidget", "公司名称", None))
        self.label_10.setText(_translate("MainWidget", "联系地址", None))
        self.label_3.setText(_translate("MainWidget", "部门", None))
        self.label_2.setText(_translate("MainWidget", "工号", None))
        self.label.setText(_translate("MainWidget", "姓名", None))
        self.label_4.setText(_translate("MainWidget", "职务", None))
        self.btn_gencode.setText(_translate("MainWidget", "生成二维码", None))
        self.btn_import.setText(_translate("MainWidget", "导入", None))
        self.btn_back.setText(_translate("MainWidget", "返回", None))
        self.btn_saveas.setText(_translate("MainWidget", "保存", None))

