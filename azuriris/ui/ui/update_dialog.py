# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\update_dialog.ui',
# licensing of '.\update_dialog.ui' applies.
#
# Created: Wed Jan  8 17:47:15 2020
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_UpdateDialog(object):
    def setupUi(self, UpdateDialog):
        UpdateDialog.setObjectName("UpdateDialog")
        UpdateDialog.resize(232, 112)
        font = QtGui.QFont()
        UpdateDialog.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(UpdateDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(UpdateDialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.buttonBox = QtWidgets.QDialogButtonBox(UpdateDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(UpdateDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), UpdateDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), UpdateDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(UpdateDialog)

    def retranslateUi(self, UpdateDialog):
        UpdateDialog.setWindowTitle(QtWidgets.QApplication.translate("UpdateDialog", "Update available", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("UpdateDialog", "A new update is available. Would you like to be redirected to the download page ?", None, -1))

