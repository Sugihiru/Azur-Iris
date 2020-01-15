from PySide2 import QtCore

from data import Data


class GenericProxyShipfuTableModel(QtCore.QSortFilterProxyModel):
    def __init__(self):
        super().__init__()
        # Rarity is already ordered
        self.rarity_order = [rarity.name for rarity in Data.getRarities()]
        self.rarity_filter = None
        self.nation_filter = None
        self.shiptype_filter = None
        self.position_filter = None

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

        if self.position_filter == 1 and not shipfu.ShipType.isMainFleet():
            return False
        if self.position_filter == 2 and not shipfu.ShipType.isVanguard():
            return False

        pattern = self.filterRegExp().pattern().lower()
        return pattern in shipfu.Shipfu.name.lower()

    def lessThan(self, source_left, source_right):
        if source_left.column() == 3:  # Sort by rarity
            left_rarity_index = self.rarity_order.index(source_left.data())
            right_rarity_index = self.rarity_order.index(source_right.data())
            return left_rarity_index < right_rarity_index
        return super().lessThan(source_left, source_right)
