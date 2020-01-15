# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tool_mission_cost.ui',
# licensing of 'tool_mission_cost.ui' applies.
#
# Created: Wed Jan 15 16:23:31 2020
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ToolMissionCost(object):
    def setupUi(self, ToolMissionCost):
        ToolMissionCost.setObjectName("ToolMissionCost")
        ToolMissionCost.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(ToolMissionCost)
        self.gridLayout.setObjectName("gridLayout")
        self.nbFleetBeforeBossLabel = QtWidgets.QLabel(ToolMissionCost)
        self.nbFleetBeforeBossLabel.setObjectName("nbFleetBeforeBossLabel")
        self.gridLayout.addWidget(self.nbFleetBeforeBossLabel, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 6, 1)
        self.clearFleetCostLabel = QtWidgets.QLabel(ToolMissionCost)
        self.clearFleetCostLabel.setObjectName("clearFleetCostLabel")
        self.gridLayout.addWidget(self.clearFleetCostLabel, 1, 0, 1, 1)
        self.totalCostLabel = QtWidgets.QLabel(ToolMissionCost)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.totalCostLabel.setFont(font)
        self.totalCostLabel.setObjectName("totalCostLabel")
        self.gridLayout.addWidget(self.totalCostLabel, 4, 1, 1, 1)
        self.bossFleetCostSpinBox = QtWidgets.QSpinBox(ToolMissionCost)
        self.bossFleetCostSpinBox.setMaximum(999)
        self.bossFleetCostSpinBox.setObjectName("bossFleetCostSpinBox")
        self.gridLayout.addWidget(self.bossFleetCostSpinBox, 2, 1, 1, 1)
        self.bossFleetCostLabel = QtWidgets.QLabel(ToolMissionCost)
        self.bossFleetCostLabel.setObjectName("bossFleetCostLabel")
        self.gridLayout.addWidget(self.bossFleetCostLabel, 2, 0, 1, 1)
        self.nbFleetBeforeBossSpinBox = QtWidgets.QSpinBox(ToolMissionCost)
        self.nbFleetBeforeBossSpinBox.setObjectName("nbFleetBeforeBossSpinBox")
        self.gridLayout.addWidget(self.nbFleetBeforeBossSpinBox, 0, 1, 1, 1)
        self.totalCostTitleLabel = QtWidgets.QLabel(ToolMissionCost)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.totalCostTitleLabel.setFont(font)
        self.totalCostTitleLabel.setObjectName("totalCostTitleLabel")
        self.gridLayout.addWidget(self.totalCostTitleLabel, 4, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 5, 0, 1, 2)
        self.clearFleetCostSpinBox = QtWidgets.QSpinBox(ToolMissionCost)
        self.clearFleetCostSpinBox.setMaximum(999)
        self.clearFleetCostSpinBox.setObjectName("clearFleetCostSpinBox")
        self.gridLayout.addWidget(self.clearFleetCostSpinBox, 1, 1, 1, 1)
        self.line = QtWidgets.QFrame(ToolMissionCost)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 3, 0, 1, 2)

        self.retranslateUi(ToolMissionCost)
        QtCore.QMetaObject.connectSlotsByName(ToolMissionCost)
        ToolMissionCost.setTabOrder(self.nbFleetBeforeBossSpinBox, self.clearFleetCostSpinBox)
        ToolMissionCost.setTabOrder(self.clearFleetCostSpinBox, self.bossFleetCostSpinBox)

    def retranslateUi(self, ToolMissionCost):
        ToolMissionCost.setWindowTitle(QtWidgets.QApplication.translate("ToolMissionCost", "Form", None, -1))
        self.nbFleetBeforeBossLabel.setText(QtWidgets.QApplication.translate("ToolMissionCost", "Nb fleets before boss:", None, -1))
        self.clearFleetCostLabel.setText(QtWidgets.QApplication.translate("ToolMissionCost", "Clear fleet cost:", None, -1))
        self.totalCostLabel.setText(QtWidgets.QApplication.translate("ToolMissionCost", "0", None, -1))
        self.bossFleetCostLabel.setText(QtWidgets.QApplication.translate("ToolMissionCost", "Boss fleet cost:", None, -1))
        self.totalCostTitleLabel.setText(QtWidgets.QApplication.translate("ToolMissionCost", "Total cost per run:", None, -1))

