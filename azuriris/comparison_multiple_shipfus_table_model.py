from PySide2 import QtCore

from PySide2.QtCore import Qt


class ComparisonMultipleShipfusTableModel(QtCore.QAbstractTableModel):
    def __init__(self, shipfus, shipfuStats):
        super().__init__()
        if shipfus:
            self.shipfus = shipfus
            self.shipfuStats = shipfuStats
        else:
            self.shipfus = list()
            self.shipfuStats = list()
        self.level_index = 0
        self.headers = ["Id", "Name", "Rarity", "Type", "Nation", "Armor Type",
                        "Health", "Firepower", "Torpedo", "Evasion",
                        "Reload", "Anti-air", "Aviation", "Luck", "Speed",
                        "Accuracy", "Anti-sub", "Cost", "Oxygen", "Ammunition"]

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
            shipfu = self.shipfus[row]
            stats = self.shipfuStats[shipfu][self.level_index]
            values = (shipfu.Shipfu.shipfu_id,
                      shipfu.Shipfu.name,
                      shipfu.Rarity.name,
                      shipfu.ShipType.name,
                      shipfu.Nation.name,
                      "N/A" if not stats else stats.armor_type.name,
                      "N/A" if not stats else stats.health,
                      "N/A" if not stats else stats.firepower,
                      "N/A" if not stats else stats.torpedo,
                      "N/A" if not stats else stats.evasion,
                      "N/A" if not stats else stats.reload,
                      "N/A" if not stats else stats.antiair,
                      "N/A" if not stats else stats.aviation,
                      "N/A" if not stats else stats.luck,
                      "N/A" if not stats else stats.speed,
                      "N/A" if not stats else stats.accuracy,
                      "N/A" if not stats else stats.antisub,
                      "N/A" if not stats else stats.cost,
                      "N/A" if (not stats or not stats.oxygen)
                      else stats.oxygen,
                      "N/A" if (not stats or not stats.ammunition)
                      else stats.ammunition)

            return values[column]

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.headers[section]

    def flags(self, index):
        default_flags = QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

        if not index.isValid():
            return None
        return default_flags

    def setLevelIndex(self, index):
        self.level_index = index


class ProxyComparisonMultipleShipfusTableModel(QtCore.QSortFilterProxyModel):
    def __init__(self, rarities):
        super().__init__()
        # Rarity is already ordered
        self.rarity_order = [rarity.name for rarity in rarities]
        self.armor_type_order = ["N/A", "Light", "Medium", "Heavy"]

    def lessThan(self, source_left, source_right):
        if source_left.column() == 2:  # Sort by rarity
            left_rarity_index = self.rarity_order.index(source_left.data())
            right_rarity_index = self.rarity_order.index(source_right.data())
            return left_rarity_index < right_rarity_index
        if source_left.column() == 5:  # Sort by armor type
            left_armor_type_index = self.armor_type_order.index(
                source_left.data())
            right_armor_type_index = self.armor_type_order.index(
                source_right.data())
            return left_armor_type_index < right_armor_type_index
        return super().lessThan(source_left, source_right)
