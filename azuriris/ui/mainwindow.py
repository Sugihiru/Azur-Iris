from PySide2.QtWidgets import QMainWindow

from .ui.mainwindow import Ui_MainWindow
from .module_collection import ModuleCollection
from data import Data


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.data = Data()
        self.setupUi()

    def setupUi(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.collectionTab = ModuleCollection(self.data.shipfus)
        self.ui.tabWidget.addTab(self.collectionTab, "")
        self.ui.tabWidget.setTabText(0, self.tr("Collection"))
