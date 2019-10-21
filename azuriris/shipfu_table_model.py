from PySide2 import QtCore

from PySide2.QtCore import Qt

import user_data


class ShipfuTableModel(QtCore.QAbstractTableModel):
    def __init__(self, shipfus, user_shipfus_data):
        super().__init__()
        if shipfus:
            self.shipfus = shipfus
        else:
            self.shipfus = list()
        self.user_shipfus_data = user_shipfus_data
        self.headers = ["Image", "Name", "Rarity", "Type", "Nation", "Owned",
                        "MLB", "Level 120", "Max Affection"]
        self.checkboxes_columns_idx = (5, 6, 7, 8)

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

            values = (self.shipfus[row].Shipfu.image,
                      self.shipfus[row].Shipfu.name,
                      self.shipfus[row].Rarity.name,
                      self.shipfus[row].ShipType.name,
                      self.shipfus[row].Nation.name,
                      shipfu_user_data["owned"],
                      shipfu_user_data["mlb"],
                      shipfu_user_data["max_level"],
                      shipfu_user_data["max_affection"])

            return values[column]

    def setData(self, index, value, role=QtCore.Qt.DisplayRole):
        if index.column() in self.checkboxes_columns_idx:
            shipfu_id = str(self.shipfus[index.row()].Shipfu.shipfu_id)
            shipfus_data_keys = {
                5: "owned",
                6: "mlb",
                7: "max_level",
                8: "max_affection"
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
