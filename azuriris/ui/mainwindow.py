from PySide2.QtWidgets import QMainWindow

from .ui.mainwindow import Ui_MainWindow
from .module_collection import ModuleCollection
from data import Data
from user_data import UserData


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.data = Data()
        self.user_data = UserData()
        self.setupUi()

    def setupUi(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.collectionTab = ModuleCollection(
            self.data.shipfus,
            self.data.retrofit_shipfus,
            self.user_data.data["shipfus"])
        self.ui.tabWidget.addTab(self.collectionTab, "")
        self.ui.tabWidget.setTabText(0, self.tr("Collection"))
