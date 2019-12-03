from PySide2 import QtCore

from PySide2.QtCore import Qt

import user_data


class RetrofitShipfuTableModel(QtCore.QAbstractTableModel):
    def __init__(self, shipfus, user_shipfus_data):
        super().__init__()
        if shipfus:
            self.shipfus = shipfus
        else:
            self.shipfus = list()
        self.user_shipfus_data = user_shipfus_data
        self.headers = ["Id", "Name", "Rarity", "Type", "Nation", "Owned"]

    def rowCount(self, parent=None):
        return len(self.shipfus)

    def columnCount(self, parent=None):
        return len(self.headers)

    def data(self, index, role=Qt.DisplayRole):
        row = index.row()
        column = index.column()
        if role == Qt.TextAlignmentRole:
            return Qt.AlignCenter

        if role == Qt.DisplayRole:
            shipfu_id = str(self.shipfus[row].Shipfu.shipfu_id)
            try:
                shipfu_user_data = self.user_shipfus_data[shipfu_id]
            except KeyError:
                shipfu_user_data = user_data.init_shipfu_data()
                self.user_shipfus_data[shipfu_id] = shipfu_user_data

            values = (self.shipfus[row].Shipfu.shipfu_id,
                      self.shipfus[row].Shipfu.name,
                      self.shipfus[row].Rarity.name,
                      self.shipfus[row].ShipType.name,
                      self.shipfus[row].Nation.name,
                      shipfu_user_data["owned"])

            return values[column]

    def setData(self, index, value, role=QtCore.Qt.DisplayRole):
        if index.column() == len(self.headers) - 1:
            shipfu_id = str(self.shipfus[index.row()].Shipfu.shipfu_id)
            self.user_shipfus_data[shipfu_id]["owned"] = value
            return value
        return value

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.headers[section]

    def flags(self, index):
        default_flags = QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

        if not index.isValid():
            return None
        if index.column() == len(self.headers) - 1:
            return default_flags | QtCore.Qt.ItemIsEditable
        return default_flags


class ProxyRetrofitShipfuTableModel(QtCore.QSortFilterProxyModel):
    def __init__(self, rarities):
        super().__init__()
        # Rarity is already ordered
        self.rarity_order = [rarity.name for rarity in rarities]
        self.rarity_filter = None
        self.nation_filter = None
        self.shiptype_filter = None

    def filterAcceptsRow(self, sourceRow, sourceParent):
        if sourceRow >= self.sourceModel().rowCount():
            return False

        shipfu = self.sourceModel().shipfus[sourceRow]
        for (shipfu_value, shipfu_filter) in (
                (shipfu.Rarity, self.rarity_filter),
                (shipfu.Nation, self.nation_filter),
                (shipfu.ShipType, self.shiptype_filter)):
            if shipfu_filter and shipfu_value != shipfu_filter:
                return False

        pattern = self.filterRegExp().pattern().lower()
        return pattern in shipfu.Shipfu.name.lower()

    def lessThan(self, source_left, source_right):
        if source_left.column() == 3:  # Sort by rarity
            left_rarity_index = self.rarity_order.index(source_left.data())
            right_rarity_index = self.rarity_order.index(source_right.data())
            return left_rarity_index < right_rarity_index
        return super().lessThan(source_left, source_right)
