from PySide2.QtWidgets import QWidget

from .ui.module_comparison import Ui_ModuleComparison
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
            0, CheckBoxDelegate(self.shipTableView))

        self.filters = ShipfuBasicFilter(data)
        for filterComboBox in (self.filters.rarityComboBox,
                               self.filters.nationComboBox,
                               self.filters.shipTypeComboBox):
            filterComboBox.currentIndexChanged.connect(self.onFilterChanged)
        self.filters.nameLineEdit.textChanged.connect(self.onFilterChanged)
        self.comparisonGridLayout.addWidget(self.filters, 0, 0)

        # Add "Compare" button

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
