from PySide2 import QtCore
from PySide2.QtCore import Qt

from user_data import UserData


class RetrofitShipfuTableModel(QtCore.QAbstractTableModel):
    def __init__(self, shipfus, user_shipfus_data):
        super().__init__()
        if shipfus:
            self.shipfus = shipfus
        else:
            self.shipfus = list()
        self.user_shipfus_data = user_shipfus_data
        self.headers = ["Id", "Image", "Name", "Rarity", "Type", "Nation",
                        "Owned"]

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
                shipfu_user_data = UserData.initShipfuData()
                self.user_shipfus_data[shipfu_id] = shipfu_user_data

            values = (self.shipfus[row].Shipfu.shipfu_id,
                      self.shipfus[row].Shipfu.image,
                      self.shipfus[row].Shipfu.name,
                      self.shipfus[row].Rarity.name,
                      self.shipfus[row].ShipType.name,
                      self.shipfus[row].Nation.name,
                      shipfu_user_data["owned"])

            return values[column]

    def setData(self, index, value, role=Qt.DisplayRole):
        if index.column() == len(self.headers) - 1:
            shipfu_id = str(self.shipfus[index.row()].Shipfu.shipfu_id)
            self.user_shipfus_data[shipfu_id]["owned"] = value
            return value
        return value

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.headers[section]

    def flags(self, index):
        default_flags = Qt.ItemIsEnabled | Qt.ItemIsSelectable

        if not index.isValid():
            return None
        if index.column() == len(self.headers) - 1:
            return default_flags | Qt.ItemIsEditable
        return default_flags
