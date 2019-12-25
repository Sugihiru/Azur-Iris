from PySide2.QtWidgets import QMainWindow

from .module_collection import ModuleCollection
from .module_comparison import ModuleComparison
from .module_retrofit import ModuleRetrofit
from .module_research import ModuleResearch
from .module_shopevent import ModuleShopEvent
from .module_tools import ModuleTools
from user_data import UserData

from .ui.mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.user_data = UserData()
        self.setupUi()

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
