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

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.headers[section]
