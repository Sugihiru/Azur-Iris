import threading

from PySide2.QtWidgets import QMainWindow
from PySide2 import QtCore

from .module_collection import ModuleCollection
from .module_comparison import ModuleComparison
from .module_retrofit import ModuleRetrofit
from .module_research import ModuleResearch
from .module_shopevent import ModuleShopEvent
from .module_tools import ModuleTools
from .update_dialog import UpdateDialog
from user_data import UserData
import app

from .ui.mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.user_data = UserData()
        self.setupUi()

        self.th = threading.Thread(target=self.checkAppVersion)
        self.th.start()

        self.timer = QtCore.QTimer(self)
        self.connect(self.timer, QtCore.SIGNAL("timeout()"),
                     self.setUpdateInfoMessage)
        self.timer.start(500)

    def setupUi(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.collectionTab = ModuleCollection(self.user_data.data["shipfus"])
        self.ui.tabWidget.addTab(self.collectionTab, "")
        self.ui.tabWidget.setTabText(0, self.tr("Collection"))

        self.comparisonTab = ModuleComparison()
        self.ui.tabWidget.addTab(self.comparisonTab, "")
        self.ui.tabWidget.setTabText(1, self.tr("Comparison"))

        self.retrofitTab = ModuleRetrofit(self.user_data)
        self.ui.tabWidget.addTab(self.retrofitTab, "")
        self.ui.tabWidget.setTabText(2, self.tr("Retrofit"))

        self.researchTab = ModuleResearch(self.user_data.data["pr"])
        self.ui.tabWidget.addTab(self.researchTab, "")
        self.ui.tabWidget.setTabText(3, self.tr("Research"))

        self.shopEventTab = ModuleShopEvent(self.user_data.data["shop_event"])
        self.ui.tabWidget.addTab(self.shopEventTab, "")
        self.ui.tabWidget.setTabText(4, self.tr("Shop Event"))

        self.toolsTab = ModuleTools()
        self.ui.tabWidget.addTab(self.toolsTab, "")
        self.ui.tabWidget.setTabText(5, self.tr("Tools"))

        self.ui.tabWidget.currentChanged.connect(self.onTabChange)

    def onTabChange(self, index):
        if index == 2:
            self.retrofitTab.setTotalRetrofitCostInfos()

    def checkAppVersion(self):
        self.appVersionInfo = app.check_app_version()

    def setUpdateInfoMessage(self):
        self.ui.statusbar.showMessage("Checking current version...", 500)
        if not self.th.isAlive():
            infoMessage = None
            if self.appVersionInfo["error"]:
                infoMessage = "Error while checking version."
            else:
                if self.appVersionInfo["up_to_date"]:
                    infoMessage = "Azur Iris is up-to-date."
                else:
                    updateDialog = UpdateDialog(
                        self.appVersionInfo["update_url"])
                    updateDialog.exec_()

            self.ui.statusbar.showMessage(infoMessage, 2000)
            self.timer.stop()
