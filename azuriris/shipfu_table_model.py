from PySide2 import QtCore

from PySide2.QtCore import Qt

import user_data
import db_manager


class ShipfuTableModel(QtCore.QAbstractTableModel):
    def __init__(self, shipfus, user_shipfus_data):
        super().__init__()
        if shipfus:
            self.shipfus = shipfus
        else:
            self.shipfus = list()
        self.user_shipfus_data = user_shipfus_data
        self.headers = ["Id", "Image", "Name", "Rarity", "Type", "Nation",
                        "Owned", "MLB", "Level 120", "Max Affection",
                        "How to obtain"]
        self.checkboxes_columns_idx = (6, 7, 8, 9)

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
                      self.shipfus[row].Shipfu.image,
                      self.shipfus[row].Shipfu.name,
                      self.shipfus[row].Rarity.name,
                      self.shipfus[row].ShipType.name,
                      self.shipfus[row].Nation.name,
                      shipfu_user_data["owned"],
                      shipfu_user_data["mlb"],
                      shipfu_user_data["max_level"],
                      shipfu_user_data["max_affection"],
                      db_manager.get_shipfu_obtention_method(
                          self.shipfus[row].Shipfu))

            return values[column]

    def setData(self, index, value, role=QtCore.Qt.DisplayRole):
        if index.column() in self.checkboxes_columns_idx:
            shipfu_id = str(self.shipfus[index.row()].Shipfu.shipfu_id)
            shipfus_data_keys = {
                6: "owned",
                7: "mlb",
                8: "max_level",
                9: "max_affection"
            }
            shipfus_data_key = shipfus_data_keys[index.column()]
            self.user_shipfus_data[shipfu_id][shipfus_data_key] = value
            return value
        return value

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.headers[section]

    def flags(self, index):
        default_flags = QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

        if not index.isValid():
            return None
        if index.column() in self.checkboxes_columns_idx:
            return default_flags | QtCore.Qt.ItemIsEditable
        return default_flags


class ProxyShipfuTableModel(QtCore.QSortFilterProxyModel):
    def __init__(self):
        super().__init__()
        self.rarity_order = (
            "Normal", "Rare", "Elite", "Super Rare", "Ultra Rare",
            "Priority", "Decisive")

    def lessThan(self, source_left, source_right):
        unsortable_columns_idx = (6, 7, 8, 9, 10)
        if source_left.column() in unsortable_columns_idx:
            return False
        if source_left.column() == 3:  # Sort by rarity
            left_rarity_index = self.rarity_order.index(source_left.data())
            right_rarity_index = self.rarity_order.index(source_right.data())
            return left_rarity_index < right_rarity_index
        return super().lessThan(source_left, source_right)
