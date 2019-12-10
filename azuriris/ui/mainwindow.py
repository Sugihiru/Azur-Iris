from PySide2.QtWidgets import QMainWindow

from .module_collection import ModuleCollection
from .module_comparison import ModuleComparison
from .module_retrofit import ModuleRetrofit
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

        self.ui.tabWidget.currentChanged.connect(self.onTabChange)

    def onTabChange(self, index):
        if index == 2:
            self.retrofitTab.setTotalRetrofitCostPerType()
