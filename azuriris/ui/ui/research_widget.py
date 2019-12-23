# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\research_widget.ui',
# licensing of '.\research_widget.ui' applies.
#
# Created: Mon Dec 23 14:55:44 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ResearchWidget(object):
    def setupUi(self, ResearchWidget):
        ResearchWidget.setObjectName("ResearchWidget")
        ResearchWidget.resize(765, 294)
        self.gridLayout = QtWidgets.QGridLayout(ResearchWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.shipNameLabel = QtWidgets.QLabel(ResearchWidget)
        self.shipNameLabel.setObjectName("shipNameLabel")
        self.gridLayout.addWidget(self.shipNameLabel, 0, 1, 2, 1)
        self.currentBpLabel = QtWidgets.QLabel(ResearchWidget)
        self.currentBpLabel.setObjectName("currentBpLabel")
        self.gridLayout.addWidget(self.currentBpLabel, 1, 2, 1, 1)
        self.shipIconLabel = QtWidgets.QLabel(ResearchWidget)
        self.shipIconLabel.setObjectName("shipIconLabel")
        self.gridLayout.addWidget(self.shipIconLabel, 0, 0, 2, 1)
        self.tableWidget = QtWidgets.QTableWidget(ResearchWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(720, 55))
        self.tableWidget.setBaseSize(QtCore.QSize(0, 0))
        self.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 6)
        self.researchLevelLabel = QtWidgets.QLabel(ResearchWidget)
        self.researchLevelLabel.setObjectName("researchLevelLabel")
        self.gridLayout.addWidget(self.researchLevelLabel, 0, 2, 1, 1)
        self.bpNeededPerLevelTitleLabel = QtWidgets.QLabel(ResearchWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.bpNeededPerLevelTitleLabel.setFont(font)
        self.bpNeededPerLevelTitleLabel.setObjectName("bpNeededPerLevelTitleLabel")
        self.gridLayout.addWidget(self.bpNeededPerLevelTitleLabel, 2, 0, 1, 6)
        self.currentBpLineEdit = QtWidgets.QLineEdit(ResearchWidget)
        self.currentBpLineEdit.setObjectName("currentBpLineEdit")
        self.gridLayout.addWidget(self.currentBpLineEdit, 1, 4, 1, 1)
        self.researchLevelSpinBox = QtWidgets.QSpinBox(ResearchWidget)
        self.researchLevelSpinBox.setMinimum(1)
        self.researchLevelSpinBox.setMaximum(30)
        self.researchLevelSpinBox.setObjectName("researchLevelSpinBox")
        self.gridLayout.addWidget(self.researchLevelSpinBox, 0, 4, 1, 1)

        self.retranslateUi(ResearchWidget)
        QtCore.QMetaObject.connectSlotsByName(ResearchWidget)

    def retranslateUi(self, ResearchWidget):
        ResearchWidget.setWindowTitle(QtWidgets.QApplication.translate("ResearchWidget", "Form", None, -1))
        self.shipNameLabel.setText(QtWidgets.QApplication.translate("ResearchWidget", "ShipName", None, -1))
        self.currentBpLabel.setText(QtWidgets.QApplication.translate("ResearchWidget", "Current blueprints owned", None, -1))
        self.shipIconLabel.setText(QtWidgets.QApplication.translate("ResearchWidget", "ShipIcon", None, -1))
        self.tableWidget.verticalHeaderItem(0).setText(QtWidgets.QApplication.translate("ResearchWidget", "Required blueprints", None, -1))
        self.tableWidget.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("ResearchWidget", "Level 5", None, -1))
        self.tableWidget.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("ResearchWidget", "Level 10", None, -1))
        self.tableWidget.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("ResearchWidget", "Level 15", None, -1))
        self.tableWidget.horizontalHeaderItem(3).setText(QtWidgets.QApplication.translate("ResearchWidget", "Level 20", None, -1))
        self.tableWidget.horizontalHeaderItem(4).setText(QtWidgets.QApplication.translate("ResearchWidget", "Level 25", None, -1))
        self.tableWidget.horizontalHeaderItem(5).setText(QtWidgets.QApplication.translate("ResearchWidget", "Level 30", None, -1))
        self.researchLevelLabel.setText(QtWidgets.QApplication.translate("ResearchWidget", "Research level", None, -1))
        self.bpNeededPerLevelTitleLabel.setText(QtWidgets.QApplication.translate("ResearchWidget", "Blueprints needed per Strengthen level", None, -1))
