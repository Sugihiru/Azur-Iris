# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'module_collection.ui',
# licensing of 'module_collection.ui' applies.
#
# Created: Tue Oct 29 12:32:30 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ModuleCollection(object):
    def setupUi(self, ModuleCollection):
        ModuleCollection.setObjectName("ModuleCollection")
        ModuleCollection.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(ModuleCollection)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(ModuleCollection)
        self.tabWidget.setObjectName("tabWidget")
        self.collectionTab = QtWidgets.QWidget()
        self.collectionTab.setObjectName("collectionTab")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.collectionTab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.shipTableView = QtWidgets.QTableView(self.collectionTab)
        self.shipTableView.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.shipTableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.shipTableView.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.shipTableView.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.shipTableView.setSortingEnabled(True)
        self.shipTableView.setObjectName("shipTableView")
        self.shipTableView.verticalHeader().setDefaultSectionSize(50)
        self.shipTableView.verticalHeader().setMinimumSectionSize(50)
        self.horizontalLayout_2.addWidget(self.shipTableView)
        self.tabWidget.addTab(self.collectionTab, "")
        self.retrofitTab = QtWidgets.QWidget()
        self.retrofitTab.setObjectName("retrofitTab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.retrofitTab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.retrofitTableView = QtWidgets.QTableView(self.retrofitTab)
        self.retrofitTableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.retrofitTableView.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.retrofitTableView.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.retrofitTableView.setSortingEnabled(True)
        self.retrofitTableView.setObjectName("retrofitTableView")
        self.horizontalLayout.addWidget(self.retrofitTableView)
        self.tabWidget.addTab(self.retrofitTab, "")
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(ModuleCollection)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ModuleCollection)

    def retranslateUi(self, ModuleCollection):
        ModuleCollection.setWindowTitle(QtWidgets.QApplication.translate("ModuleCollection", "Form", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.collectionTab), QtWidgets.QApplication.translate("ModuleCollection", "All Shipfus", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.retrofitTab), QtWidgets.QApplication.translate("ModuleCollection", "Retrofits", None, -1))

