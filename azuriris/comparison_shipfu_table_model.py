from PySide2 import QtCore
from PySide2.QtCore import Qt

from data import Data

CHECKBOXES_COLUMNS_IDX = (1,)


class ComparisonShipfuTableModel(QtCore.QAbstractTableModel):
    def __init__(self):
        super().__init__()
        self.shipfus = Data.getShipfus()
        self.id_shipfus_to_compare = list()
        self.headers = ["Id", "Compare", "Name", "Rarity", "Type", "Nation"]

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
            shipfu_id = self.shipfus[row].Shipfu.shipfu_id
            values = (shipfu_id,
                      shipfu_id in self.id_shipfus_to_compare,
                      self.shipfus[row].Shipfu.name,
                      self.shipfus[row].Rarity.name,
                      self.shipfus[row].ShipType.name,
                      self.shipfus[row].Nation.name)

            return values[column]

    def setData(self, index, value, role=Qt.DisplayRole):
        if index.column() in CHECKBOXES_COLUMNS_IDX:
            shipfu_id = self.shipfus[index.row()].Shipfu.shipfu_id
            if value:
                self.id_shipfus_to_compare.append(shipfu_id)
            else:
                self.id_shipfus_to_compare.remove(shipfu_id)
            self.dataChanged.emit(QtCore.QModelIndex(), QtCore.QModelIndex())
            return value
        return value

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.headers[section]

    def flags(self, index):
        default_flags = Qt.ItemIsEnabled | Qt.ItemIsSelectable

        if not index.isValid():
            return None
        if index.column() in CHECKBOXES_COLUMNS_IDX:
            return default_flags | Qt.ItemIsEditable
        return default_flags

    def reset(self):
        self.id_shipfus_to_compare = list()

    def getSelectedShipfus(self):
        return [shipfu for shipfu in self.shipfus
                if shipfu.Shipfu.shipfu_id
                in self.id_shipfus_to_compare]
