# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tool_leveling.ui',
# licensing of 'tool_leveling.ui' applies.
#
# Created: Wed Jan 15 16:23:31 2020
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ToolLeveling(object):
    def setupUi(self, ToolLeveling):
        ToolLeveling.setObjectName("ToolLeveling")
        ToolLeveling.resize(709, 526)
        self.gridLayout = QtWidgets.QGridLayout(ToolLeveling)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(ToolLeveling)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(617, 55))
        self.tableWidget.setMaximumSize(QtCore.QSize(617, 55))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
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
        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 3, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.currentLevelTitleLabel = QtWidgets.QLabel(ToolLeveling)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentLevelTitleLabel.sizePolicy().hasHeightForWidth())
        self.currentLevelTitleLabel.setSizePolicy(sizePolicy)
        self.currentLevelTitleLabel.setObjectName("currentLevelTitleLabel")
        self.gridLayout_2.addWidget(self.currentLevelTitleLabel, 0, 0, 1, 1)
        self.currentLevelSpinBox = QtWidgets.QSpinBox(ToolLeveling)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentLevelSpinBox.sizePolicy().hasHeightForWidth())
        self.currentLevelSpinBox.setSizePolicy(sizePolicy)
        self.currentLevelSpinBox.setMinimum(1)
        self.currentLevelSpinBox.setMaximum(120)
        self.currentLevelSpinBox.setObjectName("currentLevelSpinBox")
        self.gridLayout_2.addWidget(self.currentLevelSpinBox, 0, 1, 1, 1)
        self.currentExpTitleLabel = QtWidgets.QLabel(ToolLeveling)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentExpTitleLabel.sizePolicy().hasHeightForWidth())
        self.currentExpTitleLabel.setSizePolicy(sizePolicy)
        self.currentExpTitleLabel.setObjectName("currentExpTitleLabel")
        self.gridLayout_2.addWidget(self.currentExpTitleLabel, 1, 0, 1, 1)
        self.currentExpSpinBox = QtWidgets.QSpinBox(ToolLeveling)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentExpSpinBox.sizePolicy().hasHeightForWidth())
        self.currentExpSpinBox.setSizePolicy(sizePolicy)
        self.currentExpSpinBox.setMaximum(9999999)
        self.currentExpSpinBox.setObjectName("currentExpSpinBox")
        self.gridLayout_2.addWidget(self.currentExpSpinBox, 1, 1, 1, 1)
        self.realLevelTitleLabel = QtWidgets.QLabel(ToolLeveling)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.realLevelTitleLabel.sizePolicy().hasHeightForWidth())
        self.realLevelTitleLabel.setSizePolicy(sizePolicy)
        self.realLevelTitleLabel.setObjectName("realLevelTitleLabel")
        self.gridLayout_2.addWidget(self.realLevelTitleLabel, 2, 0, 1, 1)
        self.realLevelLabel = QtWidgets.QLabel(ToolLeveling)
        self.realLevelLabel.setObjectName("realLevelLabel")
        self.gridLayout_2.addWidget(self.realLevelLabel, 2, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.retranslateUi(ToolLeveling)
        QtCore.QMetaObject.connectSlotsByName(ToolLeveling)
        ToolLeveling.setTabOrder(self.currentLevelSpinBox, self.currentExpSpinBox)
        ToolLeveling.setTabOrder(self.currentExpSpinBox, self.tableWidget)

    def retranslateUi(self, ToolLeveling):
        ToolLeveling.setWindowTitle(QtWidgets.QApplication.translate("ToolLeveling", "Form", None, -1))
        self.tableWidget.verticalHeaderItem(0).setText(QtWidgets.QApplication.translate("ToolLeveling", "Experience needed", None, -1))
        self.tableWidget.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("ToolLeveling", "100", None, -1))
        self.tableWidget.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("ToolLeveling", "105", None, -1))
        self.tableWidget.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("ToolLeveling", "110", None, -1))
        self.tableWidget.horizontalHeaderItem(3).setText(QtWidgets.QApplication.translate("ToolLeveling", "115", None, -1))
        self.tableWidget.horizontalHeaderItem(4).setText(QtWidgets.QApplication.translate("ToolLeveling", "120", None, -1))
        self.currentLevelTitleLabel.setText(QtWidgets.QApplication.translate("ToolLeveling", "Current level:", None, -1))
        self.currentExpTitleLabel.setText(QtWidgets.QApplication.translate("ToolLeveling", "Current exp:", None, -1))
        self.realLevelTitleLabel.setText(QtWidgets.QApplication.translate("ToolLeveling", "Real level:", None, -1))
        self.realLevelLabel.setText(QtWidgets.QApplication.translate("ToolLeveling", "1", None, -1))

