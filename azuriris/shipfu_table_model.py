from PySide2 import QtCore
from PySide2.QtCore import Qt


class ShipfuTableModel(QtCore.QAbstractTableModel):
    def __init__(self, shipfus=None):
        super().__init__()
        if shipfus:
            self.shipfus = shipfus
        else:
            self.shipfus = list()
        self.headers = ["Image", "Name", "Rarity", "Type", "Nation", "Owned",
                        "MLB", "Level 120", "Max Affection"]

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
                value = self.shipfus[row].Shipfu.name
            elif column == 2:
                value = self.shipfus[row].Rarity.name
            elif column == 3:
                value = self.shipfus[row].ShipType.name
            elif column == 4:
                value = self.shipfus[row].Nation.name
            elif column == 5:
                value = True
            elif column == 6:
                value = False
            elif column == 7:
                value = False
            elif column == 8:
                value = False
            return value

    def setData(self, index, value, role=QtCore.Qt.DisplayRole):
        # Todo: set value for checkboxes
        # if index.column() == 5:
        #     return value
        return value

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.headers[section]

    def flags(self, index):
        default_flags = QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable
        checkboxes_columns_idx = (5, 6, 7, 8)

        if not index.isValid():
            return None
        if index.column() in checkboxes_columns_idx:
            return default_flags | QtCore.Qt.ItemIsEditable
        return default_flags
