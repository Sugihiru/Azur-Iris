# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'module_comparison.ui',
# licensing of 'module_comparison.ui' applies.
#
# Created: Tue Dec  3 15:34:41 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ModuleComparison(object):
    def setupUi(self, ModuleComparison):
        ModuleComparison.setObjectName("ModuleComparison")
        ModuleComparison.resize(400, 300)
        self.comparisonGridLayout = QtWidgets.QGridLayout(ModuleComparison)
        self.comparisonGridLayout.setObjectName("comparisonGridLayout")
        self.shipTableView = QtWidgets.QTableView(ModuleComparison)
        self.shipTableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.shipTableView.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.shipTableView.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.shipTableView.setObjectName("shipTableView")
        self.comparisonGridLayout.addWidget(self.shipTableView, 1, 0, 1, 1)
        self.widget = QtWidgets.QWidget(ModuleComparison)
        self.widget.setObjectName("widget")
        self.comparisonGridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(ModuleComparison)
        QtCore.QMetaObject.connectSlotsByName(ModuleComparison)

    def retranslateUi(self, ModuleComparison):
        ModuleComparison.setWindowTitle(QtWidgets.QApplication.translate("ModuleComparison", "Form", None, -1))

