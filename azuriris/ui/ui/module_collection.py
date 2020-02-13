# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\module_collection.ui',
# licensing of '.\module_collection.ui' applies.
#
# Created: Thu Feb 13 12:01:13 2020
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ModuleCollection(object):
    def setupUi(self, ModuleCollection):
        ModuleCollection.setObjectName("ModuleCollection")
        ModuleCollection.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(ModuleCollection)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(ModuleCollection)
        self.tabWidget.setObjectName("tabWidget")
        self.collectionTab = QtWidgets.QWidget()
        self.collectionTab.setObjectName("collectionTab")
        self.collectionGridLayout = QtWidgets.QGridLayout(self.collectionTab)
        self.collectionGridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.collectionGridLayout.setObjectName("collectionGridLayout")
        self.shipTableView = QtWidgets.QTableView(self.collectionTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shipTableView.sizePolicy().hasHeightForWidth())
        self.shipTableView.setSizePolicy(sizePolicy)
        self.shipTableView.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.shipTableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.shipTableView.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.shipTableView.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.shipTableView.setSortingEnabled(True)
        self.shipTableView.setObjectName("shipTableView")
        self.shipTableView.verticalHeader().setDefaultSectionSize(50)
        self.shipTableView.verticalHeader().setMinimumSectionSize(50)
        self.collectionGridLayout.addWidget(self.shipTableView, 1, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.collectionTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(1, 1))
        self.widget.setObjectName("widget")
        self.collectionGridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.tabWidget.addTab(self.collectionTab, "")
        self.retrofitTab = QtWidgets.QWidget()
        self.retrofitTab.setObjectName("retrofitTab")
        self.retrofitGridLayout = QtWidgets.QGridLayout(self.retrofitTab)
        self.retrofitGridLayout.setObjectName("retrofitGridLayout")
        self.retrofitTableView = QtWidgets.QTableView(self.retrofitTab)
        self.retrofitTableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.retrofitTableView.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.retrofitTableView.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.retrofitTableView.setSortingEnabled(True)
        self.retrofitTableView.setObjectName("retrofitTableView")
        self.retrofitTableView.verticalHeader().setDefaultSectionSize(50)
        self.retrofitTableView.verticalHeader().setMinimumSectionSize(50)
        self.retrofitGridLayout.addWidget(self.retrofitTableView, 1, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.retrofitTab)
        self.widget_2.setObjectName("widget_2")
        self.retrofitGridLayout.addWidget(self.widget_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.retrofitTab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(ModuleCollection)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ModuleCollection)

    def retranslateUi(self, ModuleCollection):
        ModuleCollection.setWindowTitle(QtWidgets.QApplication.translate("ModuleCollection", "Form", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.collectionTab), QtWidgets.QApplication.translate("ModuleCollection", "Non-retrofit Shipfus", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.retrofitTab), QtWidgets.QApplication.translate("ModuleCollection", "Retrofit Shipfus", None, -1))

