from PySide2.QtWidgets import QWidget

from .ui.module_collection import Ui_ModuleCollection
from shipfu_table_model import ShipfuTableModel


class ModuleCollection(QWidget, Ui_ModuleCollection):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        super().setupUi(self)

        self.model = ShipfuTableModel()
        self.shipTableView.setModel(self.model)
