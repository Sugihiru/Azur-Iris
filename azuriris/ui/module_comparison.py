from PySide2.QtWidgets import QWidget, QPushButton, QMessageBox

from .ui.module_comparison import Ui_ModuleComparison
from .comparison_two_ships import ComparisonTwoShips
from .checkbox_delegate import CheckBoxDelegate
from .shipfu_basic_filter import ShipfuBasicFilter
from comparison_shipfu_table_model import (ComparisonShipfuTableModel,
                                           ProxyComparisonShipfuTableModel)


class ModuleComparison(QWidget, Ui_ModuleComparison):
    def __init__(self, data):
        super().__init__()
        self.setupUi(self)

        self.model = ComparisonShipfuTableModel(data.shipfus)
        self.proxyModel = ProxyComparisonShipfuTableModel(data.rarities)
        self.proxyModel.setSourceModel(self.model)
        self.shipTableView.setModel(self.proxyModel)

        self.shipTableView.setItemDelegateForColumn(
            1, CheckBoxDelegate(self.shipTableView))

        self.filters = ShipfuBasicFilter(data)
        for filterComboBox in (self.filters.rarityComboBox,
                               self.filters.nationComboBox,
                               self.filters.shipTypeComboBox):
            filterComboBox.currentIndexChanged.connect(self.onFilterChanged)
        self.filters.nameLineEdit.textChanged.connect(self.onFilterChanged)
        self.comparisonGridLayout.addWidget(self.filters, 0, 0)

        self.compareButton = QPushButton("Compare selected ships")
        self.compareButton.clicked.connect(self.compareShipfus)
        self.comparisonGridLayout.addWidget(self.compareButton, 1, 0)

    def onFilterChanged(self, new_index):
        self.proxyModel.rarity_filter = self.filters.rarityComboBox.itemData(
            self.filters.rarityComboBox.currentIndex())
        self.proxyModel.nation_filter = self.filters.nationComboBox.itemData(
            self.filters.nationComboBox.currentIndex())
        self.proxyModel.shiptype_filter = \
            self.filters.shipTypeComboBox.itemData(
                self.filters.shipTypeComboBox.currentIndex())

        self.proxyModel.setFilterRegExp(self.filters.nameLineEdit.text())
        self.proxyModel.invalidateFilter()

    def reset(self):
        self.filters.reset()
        self.model.reset()

    def compareShipfus(self):
        id_shipfus_to_compare = self.model.id_shipfus_to_compare
        if len(id_shipfus_to_compare) < 2:
            messageBox = QMessageBox()
            messageBox.warning(None, "Error",
                               "Please select at least 2 ships to compare")
            messageBox.setFixedSize(500, 200)
            messageBox.show()
            return

        shipfus_to_compare = [shipfu for shipfu in self.model.shipfus
                              if shipfu.Shipfu.shipfu_id
                              in id_shipfus_to_compare]

        if len(shipfus_to_compare) == 2:
            widget = ComparisonTwoShips(*shipfus_to_compare)
        else:
            widget = ComparisonTwoShips(*shipfus_to_compare[:2])

        prev_widget = self.tabWidget.widget(1)
        if prev_widget:
            del prev_widget
            self.tabWidget.removeTab(1)

        self.reset()

        idx = self.tabWidget.addTab(widget, "Results")
        self.tabWidget.setCurrentIndex(idx)
