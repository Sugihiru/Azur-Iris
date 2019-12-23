# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\module_research.ui',
# licensing of '.\module_research.ui' applies.
#
# Created: Mon Dec 23 14:40:22 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ModuleResearch(object):
    def setupUi(self, ModuleResearch):
        ModuleResearch.setObjectName("ModuleResearch")
        ModuleResearch.resize(400, 300)
        self.gridLayout_2 = QtWidgets.QGridLayout(ModuleResearch)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(ModuleResearch)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 380, 280))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(ModuleResearch)
        QtCore.QMetaObject.connectSlotsByName(ModuleResearch)

    def retranslateUi(self, ModuleResearch):
        ModuleResearch.setWindowTitle(QtWidgets.QApplication.translate("ModuleResearch", "Form", None, -1))

