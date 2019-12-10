from PySide2.QtWidgets import QWidget

from data import Data
from .ui.comparison_two_ships import Ui_ComparisonTwoShips


class ComparisonTwoShips(QWidget, Ui_ComparisonTwoShips):
    def __init__(self, shipfu1, shipfu2):
        super().__init__()
        self.setupUi(self)
        self.higherStatStyleSheet = "color: green"
        self.lowerStatStyleSheet = "color: red"

        self.shipfuStats1 = Data.getStatsForShipfu(shipfu1.Shipfu.shipfu_id)
        self.shipfuStats2 = Data.getStatsForShipfu(shipfu2.Shipfu.shipfu_id)

        # In case of retrofits, there is no data for level 1
        # so we just cut the data to compare data at levels 100 and 120
        if len(self.shipfuStats1) != len(self.shipfuStats2):
            if len(self.shipfuStats1) > len(self.shipfuStats2):
                self.shipfuStats1 = self.shipfuStats1[1:]
            elif len(self.shipfuStats1) < len(self.shipfuStats2):
                self.shipfuStats2 = self.shipfuStats2[1:]

        # Rearrange the selection of levels accordingly
        if self.levelComboBox.count() == 3 and len(self.shipfuStats1) == 2:
            self.levelComboBox.removeItem(0)
        elif self.levelComboBox.count() == 2 and len(self.shipfuStats1) == 3:
            self.levelComboBox.insert(0, "1")

        self.setStaticLabels(shipfu1, shipfu2)
        self.setLabels()
        self.levelComboBox.currentIndexChanged.connect(self.setLabels)

    def setStaticLabels(self, shipfu1, shipfu2):
        label_infos_corresp = [
            (self.ship1NameLabel, shipfu1.Shipfu.name),
            (self.ship2NameLabel, shipfu2.Shipfu.name),
            (self.ship1TypeLabel, shipfu1.ShipType.name),
            (self.ship2TypeLabel, shipfu2.ShipType.name),
            (self.ship1NationLabel, shipfu1.Nation.name),
            (self.ship2NationLabel, shipfu2.Nation.name),
            (self.ship1RarityLabel, shipfu1.Rarity.name),
            (self.ship2RarityLabel, shipfu2.Rarity.name),
        ]

        for (label, info) in label_infos_corresp:
            label.setText(str(info))

    def setLabels(self, level_idx=0):
        stats = self.shipfuStats1[level_idx]
        stats2 = self.shipfuStats2[level_idx]

        self.ship1ArmorTypeLabel.setText(stats.armor_type.name)
        self.ship2ArmorTypeLabel.setText(stats.armor_type.name)

        label_stats_corresp = [
            (self.ship1HealthLabel, self.ship2HealthLabel,
             stats.health, stats2.health),
            (self.ship1FirepowerLabel, self.ship2FirepowerLabel,
             stats.firepower, stats2.firepower),
            (self.ship1TorpedoLabel, self.ship2TorpedoLabel,
             stats.torpedo, stats2.torpedo),
            (self.ship1EvasionLabel, self.ship2EvasionLabel,
             stats.evasion, stats2.evasion),
            (self.ship1ReloadLabel, self.ship2ReloadLabel,
             stats.reload, stats2.reload),
            (self.ship1AntiairLabel, self.ship2AntiairLabel,
             stats.antiair, stats2.antiair),
            (self.ship1AviationLabel, self.ship2AviationLabel,
             stats.aviation, stats2.aviation),
            (self.ship1LuckLabel, self.ship2LuckLabel,
             stats.luck, stats2.luck),
            (self.ship1SpeedLabel, self.ship2SpeedLabel,
             stats.speed, stats2.speed),
            (self.ship1AccuracyLabel, self.ship2AccuracyLabel,
             stats.accuracy, stats2.accuracy),
            (self.ship1AntisubLabel, self.ship2AntisubLabel,
             stats.antisub, stats2.antisub),
            (self.ship1CostLabel, self.ship2CostLabel,
             stats.cost, stats2.cost),
            (self.ship1OxygenLabel, self.ship2OxygenLabel,
             stats.oxygen, stats2.oxygen),
            (self.ship1AmmunitionLabel, self.ship2AmmunitionLabel,
             stats.ammunition, stats2.ammunition),
        ]

        for (label1, label2, stat1, stat2) in label_stats_corresp:
            if stat1 is not None and stat2 is not None and stat1 != stat2:
                diff = abs(stat1 - stat2)
                if stat1 > stat2:
                    label1.setText(f"{stat1} (+{diff})")
                    label1.setStyleSheet(self.higherStatStyleSheet)
                    label2.setText(f"{stat2} (-{diff})")
                    label2.setStyleSheet(self.lowerStatStyleSheet)
                elif stat1 < stat2:
                    label1.setText(f"{stat1} (-{diff})")
                    label1.setStyleSheet(self.lowerStatStyleSheet)
                    label2.setText(f"{stat2} (+{diff})")
                    label2.setStyleSheet(self.higherStatStyleSheet)
            else:
                label1.setText("N/A" if stat1 is None else str(stat1))
                label1.setStyleSheet("")
                label2.setText("N/A" if stat2 is None else str(stat2))
                label2.setStyleSheet("")

        # Reverse sheets for cost
        tmp_stylesheet = self.ship1CostLabel.styleSheet()
        self.ship1CostLabel.setStyleSheet(self.ship2CostLabel.styleSheet())
        self.ship2CostLabel.setStyleSheet(tmp_stylesheet)
