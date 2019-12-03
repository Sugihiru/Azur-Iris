from PySide2.QtWidgets import QWidget
from PySide2 import QtWidgets, QtGui

from .ui.module_collection import Ui_ModuleCollection
from .shipfu_filter import ShipfuFilter
from .shipfu_basic_filter import ShipfuBasicFilter
from .checkbox_delegate import CheckBoxDelegate
from shipfu_table_model import ShipfuTableModel, ProxyShipfuTableModel
from retrofit_shipfu_table_model import (RetrofitShipfuTableModel,
                                         ProxyRetrofitShipfuTableModel)


class ModuleCollection(QWidget, Ui_ModuleCollection):
    def __init__(self, data, user_shipfus_data):
        super().__init__()
        self.setupUi(self)
        self.model = ShipfuTableModel(data.non_retrofit_shipfus,
                                      user_shipfus_data)
        self.proxyModel = ProxyShipfuTableModel(data.rarities)
        self.proxyModel.setSourceModel(self.model)
        self.shipTableView.setModel(self.proxyModel)

        self.retrofitModel = RetrofitShipfuTableModel(
            data.retrofit_shipfus, user_shipfus_data)
        self.proxyRetrofitModel = ProxyRetrofitShipfuTableModel(data.rarities)
        self.proxyRetrofitModel.setSourceModel(self.retrofitModel)
        self.retrofitTableView.setModel(self.proxyRetrofitModel)

        for col_idx in (6, 7, 8, 9):
            self.shipTableView.setItemDelegateForColumn(
                col_idx, CheckBoxDelegate(self.shipTableView))
        self.shipTableView.setItemDelegateForColumn(
            1, PixmapDelegate(self.shipTableView))

        self.retrofitTableView.setItemDelegateForColumn(
            self.retrofitModel.columnCount() - 1,
            CheckBoxDelegate(self.retrofitTableView))

        self.filters = ShipfuFilter(data)
        for filterComboBox in (self.filters.rarityComboBox,
                               self.filters.nationComboBox,
                               self.filters.shipTypeComboBox):
            filterComboBox.currentIndexChanged.connect(self.onFilterChanged)
        self.filters.nameLineEdit.textChanged.connect(self.onFilterChanged)
        for cb in (self.filters.buildCheckBox,
                   self.filters.dropCheckBox,
                   self.filters.shopCheckBox,
                   self.filters.eventCheckBox,
                   self.filters.researchCheckBox,
                   self.filters.collectionCheckBox,
                   self.filters.loginRewardCheckBox):
            cb.stateChanged.connect(self.onFilterChanged)
        self.collectionGridLayout.addWidget(self.filters, 0, 0)

        self.retrofitFilters = ShipfuBasicFilter(data)
        for filterComboBox in (self.retrofitFilters.rarityComboBox,
                               self.retrofitFilters.nationComboBox,
                               self.retrofitFilters.shipTypeComboBox):
            filterComboBox.currentIndexChanged.connect(
                self.onRetrofitFilterChanged)
        self.retrofitFilters.nameLineEdit.textChanged.connect(
            self.onRetrofitFilterChanged)
        self.retrofitGridLayout.addWidget(self.retrofitFilters, 0, 0)

    def onFilterChanged(self, new_index):
        self.proxyModel.rarity_filter = self.filters.rarityComboBox.itemData(
            self.filters.rarityComboBox.currentIndex())
        self.proxyModel.nation_filter = self.filters.nationComboBox.itemData(
            self.filters.nationComboBox.currentIndex())
        self.proxyModel.shiptype_filter = \
            self.filters.shipTypeComboBox.itemData(
                self.filters.shipTypeComboBox.currentIndex())

        self.proxyModel.setFilterRegExp(self.filters.nameLineEdit.text())

        self.proxyModel.build_filter = self.filters.buildCheckBox.isChecked()
        self.proxyModel.drop_filter = self.filters.dropCheckBox.isChecked()
        self.proxyModel.shop_filter = self.filters.shopCheckBox.isChecked()
        self.proxyModel.event_filter = self.filters.eventCheckBox.isChecked()
        self.proxyModel.research_filter = \
            self.filters.researchCheckBox.isChecked()
        self.proxyModel.collection_filter = \
            self.filters.collectionCheckBox.isChecked()
        self.proxyModel.login_reward_filter = \
            self.filters.loginRewardCheckBox.isChecked()

        self.proxyModel.invalidateFilter()

    def onRetrofitFilterChanged(self, nex_index):
        self.proxyRetrofitModel.rarity_filter = \
            self.retrofitFilters.rarityComboBox.itemData(
                self.retrofitFilters.rarityComboBox.currentIndex())
        self.proxyRetrofitModel.nation_filter = \
            self.retrofitFilters.nationComboBox.itemData(
                self.retrofitFilters.nationComboBox.currentIndex())
        self.proxyRetrofitModel.shiptype_filter = \
            self.retrofitFilters.shipTypeComboBox.itemData(
                self.retrofitFilters.shipTypeComboBox.currentIndex())

        self.proxyRetrofitModel.setFilterRegExp(
            self.retrofitFilters.nameLineEdit.text())

        self.proxyRetrofitModel.invalidateFilter()


class PixmapDelegate(QtWidgets.QItemDelegate):
    def __init__(self, parent):
        QtWidgets.QItemDelegate.__init__(self, parent)

    def paint(self, painter, option, index):
        """
        Paint a checkbox without the label.
        """
        img = QtGui.QImage.fromData(index.data())
        pixmap = QtGui.QPixmap.fromImage(img)
        self.drawDecoration(painter, option, option.rect, pixmap)
