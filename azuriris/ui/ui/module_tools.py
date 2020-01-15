# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'module_tools.ui',
# licensing of 'module_tools.ui' applies.
#
# Created: Wed Jan 15 16:23:29 2020
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ModuleTools(object):
    def setupUi(self, ModuleTools):
        ModuleTools.setObjectName("ModuleTools")
        ModuleTools.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(ModuleTools)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(ModuleTools)
        self.tabWidget.setObjectName("tabWidget")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(ModuleTools)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(ModuleTools)

    def retranslateUi(self, ModuleTools):
        ModuleTools.setWindowTitle(QtWidgets.QApplication.translate("ModuleTools", "Form", None, -1))

