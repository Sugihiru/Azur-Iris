# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'module_comparison.ui',
# licensing of 'module_comparison.ui' applies.
#
# Created: Tue Dec  3 16:11:53 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ModuleComparison(object):
    def setupUi(self, ModuleComparison):
        ModuleComparison.setObjectName("ModuleComparison")
        ModuleComparison.resize(400, 300)
        self.generalGridLayout = QtWidgets.QGridLayout(ModuleComparison)
        self.generalGridLayout.setObjectName("generalGridLayout")
        self.tabWidget = QtWidgets.QTabWidget(ModuleComparison)
        self.tabWidget.setObjectName("tabWidget")
        self.shipDisplayTab = QtWidgets.QWidget()
        self.shipDisplayTab.setObjectName("shipDisplayTab")
        self.comparisonGridLayout = QtWidgets.QGridLayout(self.shipDisplayTab)
        self.comparisonGridLayout.setObjectName("comparisonGridLayout")
        self.shipTableView = QtWidgets.QTableView(self.shipDisplayTab)
        self.shipTableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.shipTableView.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.shipTableView.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.shipTableView.setSortingEnabled(True)
        self.shipTableView.setObjectName("shipTableView")
        self.comparisonGridLayout.addWidget(self.shipTableView, 2, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.shipDisplayTab)
        self.widget.setObjectName("widget")
        self.comparisonGridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.shipDisplayTab)
        self.widget_2.setObjectName("widget_2")
        self.comparisonGridLayout.addWidget(self.widget_2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.shipDisplayTab, "")
        self.generalGridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(ModuleComparison)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ModuleComparison)

    def retranslateUi(self, ModuleComparison):
        ModuleComparison.setWindowTitle(QtWidgets.QApplication.translate("ModuleComparison", "Form", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.shipDisplayTab), QtWidgets.QApplication.translate("ModuleComparison", "All Shipfus", None, -1))

