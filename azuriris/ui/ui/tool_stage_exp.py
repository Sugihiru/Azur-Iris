# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\tool_stage_exp.ui',
# licensing of '.\tool_stage_exp.ui' applies.
#
# Created: Fri Dec 27 14:43:27 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ToolStageExp(object):
    def setupUi(self, ToolStageExp):
        ToolStageExp.setObjectName("ToolStageExp")
        ToolStageExp.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(ToolStageExp)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 6, 1)
        self.rankComboBox = QtWidgets.QComboBox(ToolStageExp)
        self.rankComboBox.setObjectName("rankComboBox")
        self.rankComboBox.addItem("")
        self.rankComboBox.addItem("")
        self.gridLayout.addWidget(self.rankComboBox, 1, 1, 1, 1)
        self.baseExpSpinBox = QtWidgets.QSpinBox(ToolStageExp)
        self.baseExpSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.baseExpSpinBox.setMaximum(9999)
        self.baseExpSpinBox.setObjectName("baseExpSpinBox")
        self.gridLayout.addWidget(self.baseExpSpinBox, 0, 1, 1, 1)
        self.expMvpFlagshipTitleLabel = QtWidgets.QLabel(ToolStageExp)
        self.expMvpFlagshipTitleLabel.setObjectName("expMvpFlagshipTitleLabel")
        self.gridLayout.addWidget(self.expMvpFlagshipTitleLabel, 8, 0, 1, 1)
        self.expMvpLabel = QtWidgets.QLabel(ToolStageExp)
        self.expMvpLabel.setObjectName("expMvpLabel")
        self.gridLayout.addWidget(self.expMvpLabel, 6, 1, 1, 1)
        self.bonusExpSpinBox = QtWidgets.QSpinBox(ToolStageExp)
        self.bonusExpSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.bonusExpSpinBox.setMaximum(100)
        self.bonusExpSpinBox.setObjectName("bonusExpSpinBox")
        self.gridLayout.addWidget(self.bonusExpSpinBox, 3, 1, 1, 1)
        self.expFlagshipLabel = QtWidgets.QLabel(ToolStageExp)
        self.expFlagshipLabel.setObjectName("expFlagshipLabel")
        self.gridLayout.addWidget(self.expFlagshipLabel, 7, 1, 1, 1)
        self.expLabel = QtWidgets.QLabel(ToolStageExp)
        self.expLabel.setObjectName("expLabel")
        self.gridLayout.addWidget(self.expLabel, 5, 1, 1, 1)
        self.expMvpTitleLabel = QtWidgets.QLabel(ToolStageExp)
        self.expMvpTitleLabel.setObjectName("expMvpTitleLabel")
        self.gridLayout.addWidget(self.expMvpTitleLabel, 6, 0, 1, 1)
        self.baseExpTitleLabel = QtWidgets.QLabel(ToolStageExp)
        self.baseExpTitleLabel.setObjectName("baseExpTitleLabel")
        self.gridLayout.addWidget(self.baseExpTitleLabel, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 9, 0, 1, 3)
        self.expTitleLabel = QtWidgets.QLabel(ToolStageExp)
        self.expTitleLabel.setObjectName("expTitleLabel")
        self.gridLayout.addWidget(self.expTitleLabel, 5, 0, 1, 1)
        self.rankTitleLabel = QtWidgets.QLabel(ToolStageExp)
        self.rankTitleLabel.setObjectName("rankTitleLabel")
        self.gridLayout.addWidget(self.rankTitleLabel, 1, 0, 1, 1)
        self.bonusExpTitleLabel = QtWidgets.QLabel(ToolStageExp)
        self.bonusExpTitleLabel.setObjectName("bonusExpTitleLabel")
        self.gridLayout.addWidget(self.bonusExpTitleLabel, 3, 0, 1, 1)
        self.moraleTitleLabel = QtWidgets.QLabel(ToolStageExp)
        self.moraleTitleLabel.setObjectName("moraleTitleLabel")
        self.gridLayout.addWidget(self.moraleTitleLabel, 2, 0, 1, 1)
        self.expFlagshipTitleLabel = QtWidgets.QLabel(ToolStageExp)
        self.expFlagshipTitleLabel.setObjectName("expFlagshipTitleLabel")
        self.gridLayout.addWidget(self.expFlagshipTitleLabel, 7, 0, 1, 1)
        self.expMvpFlagshipLabel = QtWidgets.QLabel(ToolStageExp)
        self.expMvpFlagshipLabel.setObjectName("expMvpFlagshipLabel")
        self.gridLayout.addWidget(self.expMvpFlagshipLabel, 8, 1, 1, 1)
        self.moraleComboBox = QtWidgets.QComboBox(ToolStageExp)
        self.moraleComboBox.setObjectName("moraleComboBox")
        self.moraleComboBox.addItem("")
        self.moraleComboBox.addItem("")
        self.moraleComboBox.addItem("")
        self.gridLayout.addWidget(self.moraleComboBox, 2, 1, 1, 1)
        self.line = QtWidgets.QFrame(ToolStageExp)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 4, 0, 1, 2)

        self.retranslateUi(ToolStageExp)
        QtCore.QMetaObject.connectSlotsByName(ToolStageExp)

    def retranslateUi(self, ToolStageExp):
        ToolStageExp.setWindowTitle(QtWidgets.QApplication.translate("ToolStageExp", "Form", None, -1))
        self.rankComboBox.setItemText(0, QtWidgets.QApplication.translate("ToolStageExp", "S", None, -1))
        self.rankComboBox.setItemText(1, QtWidgets.QApplication.translate("ToolStageExp", "A or less", None, -1))
        self.expMvpFlagshipTitleLabel.setText(QtWidgets.QApplication.translate("ToolStageExp", "Experience MVP Flagship:", None, -1))
        self.expMvpLabel.setText(QtWidgets.QApplication.translate("ToolStageExp", "{exp_mvp}", None, -1))
        self.expFlagshipLabel.setText(QtWidgets.QApplication.translate("ToolStageExp", "{exp_flag}", None, -1))
        self.expLabel.setText(QtWidgets.QApplication.translate("ToolStageExp", "{exp}", None, -1))
        self.expMvpTitleLabel.setText(QtWidgets.QApplication.translate("ToolStageExp", "Experience MVP:", None, -1))
        self.baseExpTitleLabel.setText(QtWidgets.QApplication.translate("ToolStageExp", "Enemy node base experience:", None, -1))
        self.expTitleLabel.setText(QtWidgets.QApplication.translate("ToolStageExp", "Experience:", None, -1))
        self.rankTitleLabel.setText(QtWidgets.QApplication.translate("ToolStageExp", "Rank:", None, -1))
        self.bonusExpTitleLabel.setText(QtWidgets.QApplication.translate("ToolStageExp", "Bonus experience (%):", None, -1))
        self.moraleTitleLabel.setText(QtWidgets.QApplication.translate("ToolStageExp", "Ships\' Morale:", None, -1))
        self.expFlagshipTitleLabel.setText(QtWidgets.QApplication.translate("ToolStageExp", "Experience Flagship:", None, -1))
        self.expMvpFlagshipLabel.setText(QtWidgets.QApplication.translate("ToolStageExp", "{exp_mvp_flag}", None, -1))
        self.moraleComboBox.setItemText(0, QtWidgets.QApplication.translate("ToolStageExp", "Very Happy (120+)", None, -1))
        self.moraleComboBox.setItemText(1, QtWidgets.QApplication.translate("ToolStageExp", "Happy/Neutral (1-119)", None, -1))
        self.moraleComboBox.setItemText(2, QtWidgets.QApplication.translate("ToolStageExp", "Sad (0)", None, -1))

