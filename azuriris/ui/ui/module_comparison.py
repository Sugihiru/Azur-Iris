# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\module_comparison.ui',
# licensing of '.\module_comparison.ui' applies.
#
# Created: Thu Feb 13 12:15:10 2020
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
        self.shipTableView.verticalHeader().setDefaultSectionSize(50)
        self.shipTableView.verticalHeader().setMinimumSectionSize(50)
        self.comparisonGridLayout.addWidget(self.shipTableView, 8, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.selectedTitleLabel = QtWidgets.QLabel(self.shipDisplayTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectedTitleLabel.sizePolicy().hasHeightForWidth())
        self.selectedTitleLabel.setSizePolicy(sizePolicy)
        self.selectedTitleLabel.setObjectName("selectedTitleLabel")
        self.horizontalLayout.addWidget(self.selectedTitleLabel)
        self.selectedLabel = QtWidgets.QLabel(self.shipDisplayTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectedLabel.sizePolicy().hasHeightForWidth())
        self.selectedLabel.setSizePolicy(sizePolicy)
        self.selectedLabel.setObjectName("selectedLabel")
        self.horizontalLayout.addWidget(self.selectedLabel)
        self.comparisonGridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 2)
        self.widget = QtWidgets.QWidget(self.shipDisplayTab)
        self.widget.setObjectName("widget")
        self.comparisonGridLayout.addWidget(self.widget, 0, 0, 1, 2)
        self.resetSelectedShipsPushButton = QtWidgets.QPushButton(self.shipDisplayTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resetSelectedShipsPushButton.sizePolicy().hasHeightForWidth())
        self.resetSelectedShipsPushButton.setSizePolicy(sizePolicy)
        self.resetSelectedShipsPushButton.setObjectName("resetSelectedShipsPushButton")
        self.comparisonGridLayout.addWidget(self.resetSelectedShipsPushButton, 5, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.shipDisplayTab)
        self.widget_2.setObjectName("widget_2")
        self.comparisonGridLayout.addWidget(self.widget_2, 6, 0, 1, 1)
        self.tabWidget.addTab(self.shipDisplayTab, "")
        self.generalGridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(ModuleComparison)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ModuleComparison)

    def retranslateUi(self, ModuleComparison):
        ModuleComparison.setWindowTitle(QtWidgets.QApplication.translate("ModuleComparison", "Form", None, -1))
        self.selectedTitleLabel.setText(QtWidgets.QApplication.translate("ModuleComparison", "Selected:", None, -1))
        self.selectedLabel.setText(QtWidgets.QApplication.translate("ModuleComparison", "None", None, -1))
        self.resetSelectedShipsPushButton.setText(QtWidgets.QApplication.translate("ModuleComparison", "Reset selected ships", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.shipDisplayTab), QtWidgets.QApplication.translate("ModuleComparison", "All Shipfus", None, -1))

