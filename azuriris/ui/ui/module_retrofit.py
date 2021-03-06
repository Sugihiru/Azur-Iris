# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\module_retrofit.ui',
# licensing of '.\module_retrofit.ui' applies.
#
# Created: Thu Feb 13 12:18:44 2020
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ModuleRetrofit(object):
    def setupUi(self, ModuleRetrofit):
        ModuleRetrofit.setObjectName("ModuleRetrofit")
        ModuleRetrofit.resize(697, 672)
        self.gridLayout = QtWidgets.QGridLayout(ModuleRetrofit)
        self.gridLayout.setObjectName("gridLayout")
        self.resourcesPerShipLabel = QtWidgets.QLabel(ModuleRetrofit)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.resourcesPerShipLabel.setFont(font)
        self.resourcesPerShipLabel.setObjectName("resourcesPerShipLabel")
        self.gridLayout.addWidget(self.resourcesPerShipLabel, 22, 0, 1, 12)
        self.platesGridLayout = QtWidgets.QGridLayout()
        self.platesGridLayout.setObjectName("platesGridLayout")
        self.auxPlatesNbLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.auxPlatesNbLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.auxPlatesNbLabel.setObjectName("auxPlatesNbLabel")
        self.platesGridLayout.addWidget(self.auxPlatesNbLabel, 1, 3, 1, 1)
        self.gunPlatesNbLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.gunPlatesNbLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.gunPlatesNbLabel.setObjectName("gunPlatesNbLabel")
        self.platesGridLayout.addWidget(self.gunPlatesNbLabel, 0, 0, 1, 1)
        self.antiairPlatesIconLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.antiairPlatesIconLabel.setObjectName("antiairPlatesIconLabel")
        self.platesGridLayout.addWidget(self.antiairPlatesIconLabel, 1, 1, 1, 1)
        self.line_5 = QtWidgets.QFrame(ModuleRetrofit)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.platesGridLayout.addWidget(self.line_5, 0, 5, 1, 1)
        self.torpedoPlatesNbLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.torpedoPlatesNbLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.torpedoPlatesNbLabel.setObjectName("torpedoPlatesNbLabel")
        self.platesGridLayout.addWidget(self.torpedoPlatesNbLabel, 0, 3, 1, 1)
        self.aircraftPlatesIconLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.aircraftPlatesIconLabel.setObjectName("aircraftPlatesIconLabel")
        self.platesGridLayout.addWidget(self.aircraftPlatesIconLabel, 0, 7, 1, 1)
        self.antiairPlatesNbLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.antiairPlatesNbLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.antiairPlatesNbLabel.setObjectName("antiairPlatesNbLabel")
        self.platesGridLayout.addWidget(self.antiairPlatesNbLabel, 1, 0, 1, 1)
        self.gunPlatesIconLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.gunPlatesIconLabel.setObjectName("gunPlatesIconLabel")
        self.platesGridLayout.addWidget(self.gunPlatesIconLabel, 0, 1, 1, 1)
        self.line_4 = QtWidgets.QFrame(ModuleRetrofit)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.platesGridLayout.addWidget(self.line_4, 0, 2, 2, 1)
        self.aircraftPlatesNbLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.aircraftPlatesNbLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.aircraftPlatesNbLabel.setObjectName("aircraftPlatesNbLabel")
        self.platesGridLayout.addWidget(self.aircraftPlatesNbLabel, 0, 6, 1, 1)
        self.auxPlatesIconLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.auxPlatesIconLabel.setObjectName("auxPlatesIconLabel")
        self.platesGridLayout.addWidget(self.auxPlatesIconLabel, 1, 4, 1, 1)
        self.torpedoPlatesIconLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.torpedoPlatesIconLabel.setObjectName("torpedoPlatesIconLabel")
        self.platesGridLayout.addWidget(self.torpedoPlatesIconLabel, 0, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.platesGridLayout.addItem(spacerItem, 0, 8, 2, 1)
        self.gridLayout.addLayout(self.platesGridLayout, 21, 0, 1, 12)
        self.titleGlobalNeededLabel = QtWidgets.QLabel(ModuleRetrofit)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.titleGlobalNeededLabel.setFont(font)
        self.titleGlobalNeededLabel.setObjectName("titleGlobalNeededLabel")
        self.gridLayout.addWidget(self.titleGlobalNeededLabel, 15, 0, 1, 12)
        self.resourcesPerShipTableView = QtWidgets.QTableView(ModuleRetrofit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resourcesPerShipTableView.sizePolicy().hasHeightForWidth())
        self.resourcesPerShipTableView.setSizePolicy(sizePolicy)
        self.resourcesPerShipTableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.resourcesPerShipTableView.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.resourcesPerShipTableView.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.resourcesPerShipTableView.setSortingEnabled(True)
        self.resourcesPerShipTableView.setWordWrap(True)
        self.resourcesPerShipTableView.setObjectName("resourcesPerShipTableView")
        self.resourcesPerShipTableView.horizontalHeader().setMinimumSectionSize(50)
        self.resourcesPerShipTableView.verticalHeader().setDefaultSectionSize(50)
        self.resourcesPerShipTableView.verticalHeader().setMinimumSectionSize(50)
        self.gridLayout.addWidget(self.resourcesPerShipTableView, 23, 0, 1, 12)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.destroyersT1NbLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.destroyersT1NbLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.destroyersT1NbLabel.setObjectName("destroyersT1NbLabel")
        self.gridLayout_2.addWidget(self.destroyersT1NbLabel, 2, 0, 1, 1)
        self.cruisersGoldNbLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.cruisersGoldNbLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.cruisersGoldNbLabel.setObjectName("cruisersGoldNbLabel")
        self.gridLayout_2.addWidget(self.cruisersGoldNbLabel, 5, 3, 1, 1)
        self.carriersT1NbLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.carriersT1NbLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.carriersT1NbLabel.setObjectName("carriersT1NbLabel")
        self.gridLayout_2.addWidget(self.carriersT1NbLabel, 2, 9, 1, 1)
        self.carriersGoldNbLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.carriersGoldNbLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.carriersGoldNbLabel.setObjectName("carriersGoldNbLabel")
        self.gridLayout_2.addWidget(self.carriersGoldNbLabel, 5, 9, 1, 1)
        self.destroyersT2IconLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.destroyersT2IconLabel.setObjectName("destroyersT2IconLabel")
        self.gridLayout_2.addWidget(self.destroyersT2IconLabel, 3, 1, 1, 1)
        self.carriersT2NbLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.carriersT2NbLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.carriersT2NbLabel.setObjectName("carriersT2NbLabel")
        self.gridLayout_2.addWidget(self.carriersT2NbLabel, 3, 9, 1, 1)
        self.battleshipsLabel = QtWidgets.QLabel(ModuleRetrofit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.battleshipsLabel.sizePolicy().hasHeightForWidth())
        self.battleshipsLabel.setSizePolicy(sizePolicy)
        self.battleshipsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.battleshipsLabel.setObjectName("battleshipsLabel")
        self.gridLayout_2.addWidget(self.battleshipsLabel, 0, 6, 1, 2)
        self.destroyersT3IconLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.destroyersT3IconLabel.setObjectName("destroyersT3IconLabel")
        self.gridLayout_2.addWidget(self.destroyersT3IconLabel, 4, 1, 1, 1)
        self.battleshipsGoldIconLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.battleshipsGoldIconLabel.setObjectName("battleshipsGoldIconLabel")
        self.gridLayout_2.addWidget(self.battleshipsGoldIconLabel, 5, 7, 1, 1)
        self.cruisersT1NbLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.cruisersT1NbLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.cruisersT1NbLabel.setObjectName("cruisersT1NbLabel")
        self.gridLayout_2.addWidget(self.cruisersT1NbLabel, 2, 3, 1, 1)
        self.line_10 = QtWidgets.QFrame(ModuleRetrofit)
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.gridLayout_2.addWidget(self.line_10, 0, 8, 1, 1)
        self.line_6 = QtWidgets.QFrame(ModuleRetrofit)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout_2.addWidget(self.line_6, 6, 0, 1, 11)
        self.cruisersT2IconLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.cruisersT2IconLabel.setObjectName("cruisersT2IconLabel")
        self.gridLayout_2.addWidget(self.cruisersT2IconLabel, 3, 4, 1, 1)
        self.carriersT2IconLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.carriersT2IconLabel.setObjectName("carriersT2IconLabel")
        self.gridLayout_2.addWidget(self.carriersT2IconLabel, 3, 10, 1, 1)
        self.cruisersT2NbLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.cruisersT2NbLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.cruisersT2NbLabel.setObjectName("cruisersT2NbLabel")
        self.gridLayout_2.addWidget(self.cruisersT2NbLabel, 3, 3, 1, 1)
        self.destroyersGoldIconLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.destroyersGoldIconLabel.setObjectName("destroyersGoldIconLabel")
        self.gridLayout_2.addWidget(self.destroyersGoldIconLabel, 5, 1, 1, 1)
        self.line_7 = QtWidgets.QFrame(ModuleRetrofit)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout_2.addWidget(self.line_7, 1, 0, 1, 11)
        self.battleshipsT2NbLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.battleshipsT2NbLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.battleshipsT2NbLabel.setObjectName("battleshipsT2NbLabel")
        self.gridLayout_2.addWidget(self.battleshipsT2NbLabel, 3, 6, 1, 1)
        self.line_3 = QtWidgets.QFrame(ModuleRetrofit)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_2.addWidget(self.line_3, 2, 8, 4, 1)
        self.battleshipsT1NbLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.battleshipsT1NbLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.battleshipsT1NbLabel.setObjectName("battleshipsT1NbLabel")
        self.gridLayout_2.addWidget(self.battleshipsT1NbLabel, 2, 6, 1, 1)
        self.cruisersT3NbLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.cruisersT3NbLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.cruisersT3NbLabel.setObjectName("cruisersT3NbLabel")
        self.gridLayout_2.addWidget(self.cruisersT3NbLabel, 4, 3, 1, 1)
        self.carriersT3IconLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.carriersT3IconLabel.setObjectName("carriersT3IconLabel")
        self.gridLayout_2.addWidget(self.carriersT3IconLabel, 4, 10, 1, 1)
        self.cruisersGoldIconLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.cruisersGoldIconLabel.setObjectName("cruisersGoldIconLabel")
        self.gridLayout_2.addWidget(self.cruisersGoldIconLabel, 5, 4, 1, 1)
        self.destroyersGoldNbLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.destroyersGoldNbLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.destroyersGoldNbLabel.setObjectName("destroyersGoldNbLabel")
        self.gridLayout_2.addWidget(self.destroyersGoldNbLabel, 5, 0, 1, 1)
        self.line = QtWidgets.QFrame(ModuleRetrofit)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 2, 2, 4, 1)
        self.cruisersT3IconLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.cruisersT3IconLabel.setObjectName("cruisersT3IconLabel")
        self.gridLayout_2.addWidget(self.cruisersT3IconLabel, 4, 4, 1, 1)
        self.cruisersT1IconLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.cruisersT1IconLabel.setObjectName("cruisersT1IconLabel")
        self.gridLayout_2.addWidget(self.cruisersT1IconLabel, 2, 4, 1, 1)
        self.carriersT3NbLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.carriersT3NbLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.carriersT3NbLabel.setObjectName("carriersT3NbLabel")
        self.gridLayout_2.addWidget(self.carriersT3NbLabel, 4, 9, 1, 1)
        self.carriersGoldIconLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.carriersGoldIconLabel.setObjectName("carriersGoldIconLabel")
        self.gridLayout_2.addWidget(self.carriersGoldIconLabel, 5, 10, 1, 1)
        self.battleshipsT3NbLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.battleshipsT3NbLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.battleshipsT3NbLabel.setObjectName("battleshipsT3NbLabel")
        self.gridLayout_2.addWidget(self.battleshipsT3NbLabel, 4, 6, 1, 1)
        self.destroyersLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.destroyersLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.destroyersLabel.setObjectName("destroyersLabel")
        self.gridLayout_2.addWidget(self.destroyersLabel, 0, 0, 1, 2)
        self.battleshipsT1IconLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.battleshipsT1IconLabel.setObjectName("battleshipsT1IconLabel")
        self.gridLayout_2.addWidget(self.battleshipsT1IconLabel, 2, 7, 1, 1)
        self.destroyersT3NbLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.destroyersT3NbLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.destroyersT3NbLabel.setObjectName("destroyersT3NbLabel")
        self.gridLayout_2.addWidget(self.destroyersT3NbLabel, 4, 0, 1, 1)
        self.line_8 = QtWidgets.QFrame(ModuleRetrofit)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout_2.addWidget(self.line_8, 0, 2, 1, 1)
        self.battleshipsT3IconLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.battleshipsT3IconLabel.setObjectName("battleshipsT3IconLabel")
        self.gridLayout_2.addWidget(self.battleshipsT3IconLabel, 4, 7, 1, 1)
        self.line_2 = QtWidgets.QFrame(ModuleRetrofit)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 2, 5, 4, 1)
        self.cruisersLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.cruisersLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.cruisersLabel.setObjectName("cruisersLabel")
        self.gridLayout_2.addWidget(self.cruisersLabel, 0, 3, 1, 2)
        self.battleshipsGoldNbLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.battleshipsGoldNbLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.battleshipsGoldNbLabel.setObjectName("battleshipsGoldNbLabel")
        self.gridLayout_2.addWidget(self.battleshipsGoldNbLabel, 5, 6, 1, 1)
        self.battleshipsT2IconLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.battleshipsT2IconLabel.setObjectName("battleshipsT2IconLabel")
        self.gridLayout_2.addWidget(self.battleshipsT2IconLabel, 3, 7, 1, 1)
        self.line_9 = QtWidgets.QFrame(ModuleRetrofit)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.gridLayout_2.addWidget(self.line_9, 0, 5, 1, 1)
        self.destroyersT1IconLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.destroyersT1IconLabel.setTextFormat(QtCore.Qt.RichText)
        self.destroyersT1IconLabel.setObjectName("destroyersT1IconLabel")
        self.gridLayout_2.addWidget(self.destroyersT1IconLabel, 2, 1, 1, 1)
        self.carriersT1IconLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.carriersT1IconLabel.setObjectName("carriersT1IconLabel")
        self.gridLayout_2.addWidget(self.carriersT1IconLabel, 2, 10, 1, 1)
        self.carriersLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.carriersLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.carriersLabel.setObjectName("carriersLabel")
        self.gridLayout_2.addWidget(self.carriersLabel, 0, 9, 1, 2)
        self.destroyersT2NbLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.destroyersT2NbLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.destroyersT2NbLabel.setObjectName("destroyersT2NbLabel")
        self.gridLayout_2.addWidget(self.destroyersT2NbLabel, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 11, 7, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 5, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.totalGoldNbLabel = QtWidgets.QLabel(ModuleRetrofit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.totalGoldNbLabel.sizePolicy().hasHeightForWidth())
        self.totalGoldNbLabel.setSizePolicy(sizePolicy)
        self.totalGoldNbLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.totalGoldNbLabel.setObjectName("totalGoldNbLabel")
        self.horizontalLayout.addWidget(self.totalGoldNbLabel)
        self.totalGoldIconLabel = QtWidgets.QLabel(ModuleRetrofit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.totalGoldIconLabel.sizePolicy().hasHeightForWidth())
        self.totalGoldIconLabel.setSizePolicy(sizePolicy)
        self.totalGoldIconLabel.setObjectName("totalGoldIconLabel")
        self.horizontalLayout.addWidget(self.totalGoldIconLabel)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout, 17, 0, 2, 1)
        self.infoLabel = QtWidgets.QLabel(ModuleRetrofit)
        self.infoLabel.setObjectName("infoLabel")
        self.gridLayout.addWidget(self.infoLabel, 2, 0, 1, 1)
        self.titlePerShipTypeLabel = QtWidgets.QLabel(ModuleRetrofit)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.titlePerShipTypeLabel.setFont(font)
        self.titlePerShipTypeLabel.setObjectName("titlePerShipTypeLabel")
        self.gridLayout.addWidget(self.titlePerShipTypeLabel, 3, 0, 1, 1)

        self.retranslateUi(ModuleRetrofit)
        QtCore.QMetaObject.connectSlotsByName(ModuleRetrofit)

    def retranslateUi(self, ModuleRetrofit):
        ModuleRetrofit.setWindowTitle(QtWidgets.QApplication.translate("ModuleRetrofit", "Form", None, -1))
        self.resourcesPerShipLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "Resources needed per ship", None, -1))
        self.auxPlatesNbLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "{nb} T3 auxiliary plates", None, -1))
        self.gunPlatesNbLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "{nb} T3 gun plates", None, -1))
        self.antiairPlatesIconLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "AntiairPlatesIcon", None, -1))
        self.torpedoPlatesNbLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "{nb} T3 torpedo plates", None, -1))
        self.aircraftPlatesIconLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "AircraftPlatesIcon", None, -1))
        self.antiairPlatesNbLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "{nb} T3 anti-air plates", None, -1))
        self.gunPlatesIconLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "GunPlatesIcon", None, -1))
        self.aircraftPlatesNbLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "{nb} T3 aircraft plates", None, -1))
        self.auxPlatesIconLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "AuxPlatesIcon", None, -1))
        self.torpedoPlatesIconLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "TorpedoPlatesIcon", None, -1))
        self.titleGlobalNeededLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "Global resources needed", None, -1))
        self.destroyersT1NbLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "T1Nb", None, -1))
        self.cruisersGoldNbLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "GoldNb", None, -1))
        self.carriersT1NbLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "T1Nb", None, -1))
        self.carriersGoldNbLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "GoldNb", None, -1))
        self.destroyersT2IconLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "DDT2Icon", None, -1))
        self.carriersT2NbLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "T2Nb", None, -1))
        self.battleshipsLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "Battleships", None, -1))
        self.destroyersT3IconLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "DDT3Icon", None, -1))
        self.battleshipsGoldIconLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "GoldIcon", None, -1))
        self.cruisersT1NbLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "T1Nb", None, -1))
        self.cruisersT2IconLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "CLT2Icon", None, -1))
        self.carriersT2IconLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "CVT2Icon", None, -1))
        self.cruisersT2NbLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "T2Nb", None, -1))
        self.destroyersGoldIconLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "GoldIcon", None, -1))
        self.battleshipsT2NbLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "T2Nb", None, -1))
        self.battleshipsT1NbLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "T1Nb", None, -1))
        self.cruisersT3NbLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "T3Nb", None, -1))
        self.carriersT3IconLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "CVT3Icon", None, -1))
        self.cruisersGoldIconLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "GoldIcon", None, -1))
        self.destroyersGoldNbLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "GoldNb", None, -1))
        self.cruisersT3IconLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "CLT3Icon", None, -1))
        self.cruisersT1IconLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "CLT1Icon", None, -1))
        self.carriersT3NbLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "T3Nb", None, -1))
        self.carriersGoldIconLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "GoldIcon", None, -1))
        self.battleshipsT3NbLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "T3Nb", None, -1))
        self.destroyersLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "Destroyers", None, -1))
        self.battleshipsT1IconLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "BBT1Icon", None, -1))
        self.destroyersT3NbLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "T3Nb", None, -1))
        self.battleshipsT3IconLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "BBT3Icon", None, -1))
        self.cruisersLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "Cruisers", None, -1))
        self.battleshipsGoldNbLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "GoldNb", None, -1))
        self.battleshipsT2IconLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "BBT2Icon", None, -1))
        self.destroyersT1IconLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "DDT1Icon", None, -1))
        self.carriersT1IconLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "CVT1Icon", None, -1))
        self.carriersLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "Carriers", None, -1))
        self.destroyersT2NbLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "T2Nb", None, -1))
        self.totalGoldNbLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "TotalGoldNb", None, -1))
        self.totalGoldIconLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "GoldIcon", None, -1))
        self.infoLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "<html><head/><body><p>Please register the retrofits that you\'ve already done <a href=\"retrofit_tab\"><span style=\" text-decoration: underline; color:#007af4;\">here</span></a> before using this tool.</p></body></html>", None, -1))
        self.titlePerShipTypeLabel.setText(QtWidgets.QApplication.translate("ModuleRetrofit", "Resources needed per ship type", None, -1))

