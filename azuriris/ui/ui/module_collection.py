# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'module_collection.ui',
# licensing of 'module_collection.ui' applies.
#
# Created: Tue Oct 29 11:38:16 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ModuleCollection(object):
    def setupUi(self, ModuleCollection):
        ModuleCollection.setObjectName("ModuleCollection")
        ModuleCollection.resize(400, 300)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(ModuleCollection)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.shipTableView = QtWidgets.QTableView(ModuleCollection)
        self.shipTableView.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.shipTableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.shipTableView.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.shipTableView.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.shipTableView.setSortingEnabled(True)
        self.shipTableView.setObjectName("shipTableView")
        self.shipTableView.verticalHeader().setDefaultSectionSize(50)
        self.shipTableView.verticalHeader().setMinimumSectionSize(50)
        self.verticalLayout_2.addWidget(self.shipTableView)

        self.retranslateUi(ModuleCollection)
        QtCore.QMetaObject.connectSlotsByName(ModuleCollection)

    def retranslateUi(self, ModuleCollection):
        ModuleCollection.setWindowTitle(QtWidgets.QApplication.translate("ModuleCollection", "Form", None, -1))

