# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shipfu_filter.ui',
# licensing of 'shipfu_filter.ui' applies.
#
# Created: Wed Nov 13 11:49:54 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ShipfuFilter(object):
    def setupUi(self, ShipfuFilter):
        ShipfuFilter.setObjectName("ShipfuFilter")
        ShipfuFilter.resize(400, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ShipfuFilter.sizePolicy().hasHeightForWidth())
        ShipfuFilter.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(ShipfuFilter)
        self.gridLayout.setObjectName("gridLayout")
        self.shipTypeLabel = QtWidgets.QLabel(ShipfuFilter)
        self.shipTypeLabel.setObjectName("shipTypeLabel")
        self.gridLayout.addWidget(self.shipTypeLabel, 0, 7, 1, 1)
        self.rarityComboBox = QtWidgets.QComboBox(ShipfuFilter)
        self.rarityComboBox.setCurrentText("")
        self.rarityComboBox.setObjectName("rarityComboBox")
        self.gridLayout.addWidget(self.rarityComboBox, 0, 4, 1, 1)
        self.nationLabel = QtWidgets.QLabel(ShipfuFilter)
        self.nationLabel.setObjectName("nationLabel")
        self.gridLayout.addWidget(self.nationLabel, 0, 5, 1, 1)
        self.shipTypeComboBox = QtWidgets.QComboBox(ShipfuFilter)
        self.shipTypeComboBox.setObjectName("shipTypeComboBox")
        self.gridLayout.addWidget(self.shipTypeComboBox, 0, 8, 1, 1)
        self.nameLabel = QtWidgets.QLabel(ShipfuFilter)
        self.nameLabel.setObjectName("nameLabel")
        self.gridLayout.addWidget(self.nameLabel, 0, 0, 1, 1)
        self.nationComboBox = QtWidgets.QComboBox(ShipfuFilter)
        self.nationComboBox.setObjectName("nationComboBox")
        self.gridLayout.addWidget(self.nationComboBox, 0, 6, 1, 1)
        self.nameLineEdit = QtWidgets.QLineEdit(ShipfuFilter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameLineEdit.sizePolicy().hasHeightForWidth())
        self.nameLineEdit.setSizePolicy(sizePolicy)
        self.nameLineEdit.setMinimumSize(QtCore.QSize(128, 0))
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.gridLayout.addWidget(self.nameLineEdit, 0, 1, 1, 1)
        self.rarityLabel = QtWidgets.QLabel(ShipfuFilter)
        self.rarityLabel.setObjectName("rarityLabel")
        self.gridLayout.addWidget(self.rarityLabel, 0, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 9, 1, 1)

        self.retranslateUi(ShipfuFilter)
        QtCore.QMetaObject.connectSlotsByName(ShipfuFilter)

    def retranslateUi(self, ShipfuFilter):
        ShipfuFilter.setWindowTitle(QtWidgets.QApplication.translate("ShipfuFilter", "Form", None, -1))
        self.shipTypeLabel.setText(QtWidgets.QApplication.translate("ShipfuFilter", "Ship type", None, -1))
        self.nationLabel.setText(QtWidgets.QApplication.translate("ShipfuFilter", "Nation", None, -1))
        self.nameLabel.setText(QtWidgets.QApplication.translate("ShipfuFilter", "Name", None, -1))
        self.nameLineEdit.setPlaceholderText(QtWidgets.QApplication.translate("ShipfuFilter", "Ship name", None, -1))
        self.rarityLabel.setText(QtWidgets.QApplication.translate("ShipfuFilter", "Rarity", None, -1))

