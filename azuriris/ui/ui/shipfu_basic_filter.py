# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shipfu_basic_filter.ui',
# licensing of 'shipfu_basic_filter.ui' applies.
#
# Created: Tue Dec  3 15:34:42 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ShipfuBasicFilter(object):
    def setupUi(self, ShipfuBasicFilter):
        ShipfuBasicFilter.setObjectName("ShipfuBasicFilter")
        ShipfuBasicFilter.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(ShipfuBasicFilter)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.nameLabel = QtWidgets.QLabel(ShipfuBasicFilter)
        self.nameLabel.setObjectName("nameLabel")
        self.horizontalLayout.addWidget(self.nameLabel)
        self.nameLineEdit = QtWidgets.QLineEdit(ShipfuBasicFilter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameLineEdit.sizePolicy().hasHeightForWidth())
        self.nameLineEdit.setSizePolicy(sizePolicy)
        self.nameLineEdit.setMinimumSize(QtCore.QSize(128, 0))
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.horizontalLayout.addWidget(self.nameLineEdit)
        self.rarityLabel = QtWidgets.QLabel(ShipfuBasicFilter)
        self.rarityLabel.setObjectName("rarityLabel")
        self.horizontalLayout.addWidget(self.rarityLabel)
        self.rarityComboBox = QtWidgets.QComboBox(ShipfuBasicFilter)
        self.rarityComboBox.setCurrentText("")
        self.rarityComboBox.setObjectName("rarityComboBox")
        self.horizontalLayout.addWidget(self.rarityComboBox)
        self.nationLabel = QtWidgets.QLabel(ShipfuBasicFilter)
        self.nationLabel.setObjectName("nationLabel")
        self.horizontalLayout.addWidget(self.nationLabel)
        self.nationComboBox = QtWidgets.QComboBox(ShipfuBasicFilter)
        self.nationComboBox.setObjectName("nationComboBox")
        self.horizontalLayout.addWidget(self.nationComboBox)
        self.shipTypeLabel = QtWidgets.QLabel(ShipfuBasicFilter)
        self.shipTypeLabel.setObjectName("shipTypeLabel")
        self.horizontalLayout.addWidget(self.shipTypeLabel)
        self.shipTypeComboBox = QtWidgets.QComboBox(ShipfuBasicFilter)
        self.shipTypeComboBox.setObjectName("shipTypeComboBox")
        self.horizontalLayout.addWidget(self.shipTypeComboBox)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.filterTitle1Label = QtWidgets.QLabel(ShipfuBasicFilter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filterTitle1Label.sizePolicy().hasHeightForWidth())
        self.filterTitle1Label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.filterTitle1Label.setFont(font)
        self.filterTitle1Label.setObjectName("filterTitle1Label")
        self.gridLayout.addWidget(self.filterTitle1Label, 0, 0, 1, 1)

        self.retranslateUi(ShipfuBasicFilter)
        QtCore.QMetaObject.connectSlotsByName(ShipfuBasicFilter)

    def retranslateUi(self, ShipfuBasicFilter):
        ShipfuBasicFilter.setWindowTitle(QtWidgets.QApplication.translate("ShipfuBasicFilter", "Form", None, -1))
        self.nameLabel.setText(QtWidgets.QApplication.translate("ShipfuBasicFilter", "Name", None, -1))
        self.nameLineEdit.setPlaceholderText(QtWidgets.QApplication.translate("ShipfuBasicFilter", "Ship name", None, -1))
        self.rarityLabel.setText(QtWidgets.QApplication.translate("ShipfuBasicFilter", "Rarity", None, -1))
        self.nationLabel.setText(QtWidgets.QApplication.translate("ShipfuBasicFilter", "Nation", None, -1))
        self.shipTypeLabel.setText(QtWidgets.QApplication.translate("ShipfuBasicFilter", "Ship type", None, -1))
        self.filterTitle1Label.setText(QtWidgets.QApplication.translate("ShipfuBasicFilter", "Basic filters", None, -1))

