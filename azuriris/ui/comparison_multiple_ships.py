from PySide2.QtWidgets import QWidget

from .ui.comparison_multiple_ships import Ui_ComparisonMultipleShips
from data import Data
from comparison_multiple_shipfus_table_model import (
    ComparisonMultipleShipfusTableModel,
    ProxyComparisonMultipleShipfusTableModel)


class ComparisonMultipleShips(QWidget, Ui_ComparisonMultipleShips):
    def __init__(self, shipfus, rarities):
        super().__init__()
        self.setupUi(self)

        self.shipfuStats = dict()
        for shipfu in shipfus:
            self.shipfuStats[shipfu] = Data.getStatsForShipfu(
                shipfu.Shipfu.shipfu_id)

        nb_levels = len(max(self.shipfuStats.values(), key=lambda x: len(x)))

        # Rearrange the selection of levels accordingly
        if self.levelComboBox.count() == 3 and nb_levels == 2:
            self.levelComboBox.removeItem(0)
        elif nb_levels == 3:
            if self.levelComboBox.count() == 2:
                self.levelComboBox.insert(0, "1")
            for stats in self.shipfuStats.values():
                if len(stats) != 3:
                    stats.insert(0, None)

        self.model = ComparisonMultipleShipfusTableModel(shipfus,
                                                         self.shipfuStats)
        self.proxyModel = ProxyComparisonMultipleShipfusTableModel(rarities)
        self.proxyModel.setSourceModel(self.model)
        self.shipTableView.setModel(self.proxyModel)

        self.levelComboBox.currentIndexChanged.connect(self.setLevelIndex)

    def setLevelIndex(self, idx):
        self.model.setLevelIndex(idx)
        # We have no focus on the table, so we need to manually repaint it
        self.shipTableView.viewport().repaint()
