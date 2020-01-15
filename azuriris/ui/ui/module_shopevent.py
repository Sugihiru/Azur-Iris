# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'module_shopevent.ui',
# licensing of 'module_shopevent.ui' applies.
#
# Created: Wed Jan 15 16:23:29 2020
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ModuleShopEvent(object):
    def setupUi(self, ModuleShopEvent):
        ModuleShopEvent.setObjectName("ModuleShopEvent")
        ModuleShopEvent.resize(400, 300)
        self.gridLayout_2 = QtWidgets.QGridLayout(ModuleShopEvent)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.reqTokenTitleLabel = QtWidgets.QLabel(ModuleShopEvent)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.reqTokenTitleLabel.setFont(font)
        self.reqTokenTitleLabel.setObjectName("reqTokenTitleLabel")
        self.gridLayout_2.addWidget(self.reqTokenTitleLabel, 0, 0, 1, 1)
        self.reqTokenLabel = QtWidgets.QLabel(ModuleShopEvent)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.reqTokenLabel.setFont(font)
        self.reqTokenLabel.setObjectName("reqTokenLabel")
        self.gridLayout_2.addWidget(self.reqTokenLabel, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(ModuleShopEvent)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 380, 254))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout.addWidget(self.widget_2, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 1, 0, 1, 3)

        self.retranslateUi(ModuleShopEvent)
        QtCore.QMetaObject.connectSlotsByName(ModuleShopEvent)

    def retranslateUi(self, ModuleShopEvent):
        ModuleShopEvent.setWindowTitle(QtWidgets.QApplication.translate("ModuleShopEvent", "Form", None, -1))
        self.reqTokenTitleLabel.setText(QtWidgets.QApplication.translate("ModuleShopEvent", "Total required event tokens:", None, -1))
        self.reqTokenLabel.setText(QtWidgets.QApplication.translate("ModuleShopEvent", "{req_tokens}", None, -1))

