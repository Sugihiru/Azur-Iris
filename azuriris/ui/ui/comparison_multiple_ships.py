# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\comparison_multiple_ships.ui',
# licensing of '.\comparison_multiple_ships.ui' applies.
#
# Created: Sun Dec  8 16:36:07 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ComparisonMultipleShips(object):
    def setupUi(self, ComparisonMultipleShips):
        ComparisonMultipleShips.setObjectName("ComparisonMultipleShips")
        ComparisonMultipleShips.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(ComparisonMultipleShips)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.levelLabel = QtWidgets.QLabel(ComparisonMultipleShips)
        self.levelLabel.setObjectName("levelLabel")
        self.horizontalLayout.addWidget(self.levelLabel)
        self.levelComboBox = QtWidgets.QComboBox(ComparisonMultipleShips)
        self.levelComboBox.setObjectName("levelComboBox")
        self.levelComboBox.addItem("")
        self.levelComboBox.addItem("")
        self.levelComboBox.addItem("")
        self.horizontalLayout.addWidget(self.levelComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.shipTableView = QtWidgets.QTableView(ComparisonMultipleShips)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shipTableView.sizePolicy().hasHeightForWidth())
        self.shipTableView.setSizePolicy(sizePolicy)
        self.shipTableView.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.shipTableView.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.shipTableView.setSortingEnabled(True)
        self.shipTableView.setObjectName("shipTableView")
        self.verticalLayout.addWidget(self.shipTableView)

        self.retranslateUi(ComparisonMultipleShips)
        QtCore.QMetaObject.connectSlotsByName(ComparisonMultipleShips)

    def retranslateUi(self, ComparisonMultipleShips):
        ComparisonMultipleShips.setWindowTitle(QtWidgets.QApplication.translate("ComparisonMultipleShips", "Form", None, -1))
        self.levelLabel.setText(QtWidgets.QApplication.translate("ComparisonMultipleShips", "Level:", None, -1))
        self.levelComboBox.setItemText(0, QtWidgets.QApplication.translate("ComparisonMultipleShips", "1", None, -1))
        self.levelComboBox.setItemText(1, QtWidgets.QApplication.translate("ComparisonMultipleShips", "100", None, -1))
        self.levelComboBox.setItemText(2, QtWidgets.QApplication.translate("ComparisonMultipleShips", "120", None, -1))

