# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'embeddedDialog.ui'
#
# Created: Mon Nov 30 10:26:53 2015
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.setEnabled(True)
        Dialog.resize(370, 215)
        Dialog.setWhatsThis(_fromUtf8(""))
        Dialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.formLayout = QtGui.QFormLayout(Dialog)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.layoutDirection = QtGui.QComboBox(Dialog)
        self.layoutDirection.setObjectName(_fromUtf8("layoutDirection"))
        self.layoutDirection.addItem(_fromUtf8(""))
        self.layoutDirection.addItem(_fromUtf8(""))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.layoutDirection)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.fontComboBox = QtGui.QFontComboBox(Dialog)
        self.fontComboBox.setObjectName(_fromUtf8("fontComboBox"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.fontComboBox)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.style = QtGui.QComboBox(Dialog)
        self.style.setObjectName(_fromUtf8("style"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.style)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.spacing = QtGui.QSlider(Dialog)
        self.spacing.setOrientation(QtCore.Qt.Horizontal)
        self.spacing.setObjectName(_fromUtf8("spacing"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.spacing)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Embeded Dialog", None))
        self.label.setText(_translate("Dialog", "Layout Direction:", None))
        self.layoutDirection.setItemText(0, _translate("Dialog", "Left", None))
        self.layoutDirection.setItemText(1, _translate("Dialog", "Right", None))
        self.label_2.setText(_translate("Dialog", "Select Font:", None))
        self.label_3.setText(_translate("Dialog", "Style:", None))
        self.label_4.setText(_translate("Dialog", "Layout spacing:", None))

