# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shipfu_filter.ui',
# licensing of 'shipfu_filter.ui' applies.
#
# Created: Fri Nov  1 12:35:45 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ShipfuFilter(object):
    def setupUi(self, ShipfuFilter):
        ShipfuFilter.setObjectName("ShipfuFilter")
        ShipfuFilter.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(ShipfuFilter)
        self.gridLayout.setObjectName("gridLayout")
        self.nationLabel = QtWidgets.QLabel(ShipfuFilter)
        self.nationLabel.setObjectName("nationLabel")
        self.gridLayout.addWidget(self.nationLabel, 1, 0, 1, 1)
        self.rarityLabel = QtWidgets.QLabel(ShipfuFilter)
        self.rarityLabel.setObjectName("rarityLabel")
        self.gridLayout.addWidget(self.rarityLabel, 0, 0, 1, 1)
        self.nationComboBox = QtWidgets.QComboBox(ShipfuFilter)
        self.nationComboBox.setObjectName("nationComboBox")
        self.gridLayout.addWidget(self.nationComboBox, 1, 1, 1, 1)
        self.rarityComboBox = QtWidgets.QComboBox(ShipfuFilter)
        self.rarityComboBox.setCurrentText("")
        self.rarityComboBox.setObjectName("rarityComboBox")
        self.gridLayout.addWidget(self.rarityComboBox, 0, 1, 1, 1)
        self.shipTypeLabel = QtWidgets.QLabel(ShipfuFilter)
        self.shipTypeLabel.setObjectName("shipTypeLabel")
        self.gridLayout.addWidget(self.shipTypeLabel, 2, 0, 1, 1)
        self.shipTypeComboBox = QtWidgets.QComboBox(ShipfuFilter)
        self.shipTypeComboBox.setObjectName("shipTypeComboBox")
        self.gridLayout.addWidget(self.shipTypeComboBox, 2, 1, 1, 1)

        self.retranslateUi(ShipfuFilter)
        QtCore.QMetaObject.connectSlotsByName(ShipfuFilter)

    def retranslateUi(self, ShipfuFilter):
        ShipfuFilter.setWindowTitle(QtWidgets.QApplication.translate("ShipfuFilter", "Form", None, -1))
        self.nationLabel.setText(QtWidgets.QApplication.translate("ShipfuFilter", "Nation", None, -1))
        self.rarityLabel.setText(QtWidgets.QApplication.translate("ShipfuFilter", "Rarity", None, -1))
        self.shipTypeLabel.setText(QtWidgets.QApplication.translate("ShipfuFilter", "Ship type", None, -1))

