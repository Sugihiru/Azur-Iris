from PySide2 import QtCore
from PySide2.QtCore import Qt


class ShipfuTableModel(QtCore.QAbstractTableModel):
    def __init__(self, shipfus=None):
        super().__init__()
        if shipfus:
            self.shipfus = shipfus
        else:
            self.shipfus = list()
        self.headers = ["Image", "Name", "Rarity", "Type", "Nation", "Owned"]

    def rowCount(self, parent=None):
        return len(self.shipfus)

    def columnCount(self, parent=None):
        return len(self.headers)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            row = index.row()
            column = index.column()
            if column == 0:
                value = "None"
            elif column == 1:
                value = self.shipfus[row].name
            elif column == 2:
                value = self.shipfus[row].rarity_id
            elif column == 3:
                value = self.shipfus[row].ship_type_id
            elif column == 4:
                value = self.shipfus[row].nation_id
            elif column == 5:
                value = "nope"
            return value

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.headers[section]
