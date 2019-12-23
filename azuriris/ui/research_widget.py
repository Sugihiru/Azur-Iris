from PySide2.QtWidgets import (QWidget, QLabel, QTableWidget, QSizePolicy,
                               QTableWidgetItem)
from PySide2.QtGui import QPixmap, QImage, QFont
from PySide2.QtCore import QSize, Qt

from .ui.research_widget import Ui_ResearchWidget

# Indicate the maximum Research Season where a Fate Simulation is possible
# Currently, only PR S1 have Fate Simulation
MAX_FATE_SIMUL_SEASON = 1


class ResearchWidget(QWidget, Ui_ResearchWidget):
    def __init__(self, researchShip, researchShipUserData):
        super().__init__()
        self.researchShip = researchShip
        self.researchShipUserData = researchShipUserData
        self.setupUi()
        self.setRequiredBlueprints()

    def setupUi(self):
        super().setupUi(self)
        qimg = QImage.fromData(self.researchShip.Shipfu.image)
        self.shipIconLabel.setPixmap(QPixmap.fromImage(qimg))
        self.shipNameLabel.setText(self.researchShip.Shipfu.name)

        if self.researchShip.ResearchShip.season <= MAX_FATE_SIMUL_SEASON:
            self.addFateSimulationTable()

        self.researchLevelSpinBox.setValue(self.researchShipUserData["level"])
        self.researchLevelSpinBox.valueChanged.connect(self.onFieldChanged)
        self.currentBpLineEdit.setText(str(self.researchShipUserData["bp"]))
        self.currentBpLineEdit.textChanged.connect(self.onFieldChanged)

    def addFateSimulationTable(self):
        """Add the Fate Simulation table widget to the widget's layout"""
        boldFont = QFont()
        boldFont.setBold(True)

        self.fateSimulationTitleLabel = QLabel(
            "Blueprints needed per Fate Simulation level")
        self.fateSimulationTitleLabel.setFont(boldFont)
        self.gridLayout.addWidget(self.fateSimulationTitleLabel, 4, 0, 1, 6)

        # Setup table widget
        self.fateSimulationTableWidget = QTableWidget(self)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.fateSimulationTableWidget.setSizePolicy(sizePolicy)
        self.fateSimulationTableWidget.setMinimumSize(QSize(620, 55))
        self.fateSimulationTableWidget.setRowCount(1)
        self.fateSimulationTableWidget.setColumnCount(5)

        self.fateSimulationTableWidget.horizontalHeader().setVisible(True)
        self.fateSimulationTableWidget.verticalHeader().setVisible(True)

        item = QTableWidgetItem()
        self.fateSimulationTableWidget.setVerticalHeaderItem(0, item)
        self.fateSimulationTableWidget.verticalHeaderItem(0).setText(
            "Required blueprints")

        for i in range(5):
            item = QTableWidgetItem()
            self.fateSimulationTableWidget.setHorizontalHeaderItem(i, item)
            self.fateSimulationTableWidget.horizontalHeaderItem(i).setText(
                f"Phase {i + 1}")

        self.gridLayout.addWidget(self.fateSimulationTableWidget, 5, 0, 1, 6)

    def setRequiredBlueprints(self):
        """Compute and display required blueprints"""
        for i, level in enumerate((5, 10, 15, 20, 25, 30)):
            if self.researchShipUserData["level"] >= level:
                req_bp = 0
            else:
                req_bp = self.computeRequiredBlueprintsForStrengthenLevel(
                    level,
                    self.researchShipUserData["level"],
                    self.researchShipUserData["bp"],
                    self.isDecisiveShip(self.researchShip.Shipfu))

            item = QTableWidgetItem(str(req_bp))
            item.setTextAlignment(Qt.AlignCenter)
            self.strengthenLevelTableWidget.setItem(0, i, item)

    @staticmethod
    def computeRequiredBlueprintsForStrengthenLevel(target_level,
                                                    current_level,
                                                    current_bp,
                                                    is_decisive_ship):
        if current_level >= 30 or target_level <= current_level:
            return 0

        if not is_decisive_ship:
            req_bps_per_cap = (0, 13, 37, 73, 133, 223, 343)
            # Need to check early levels
            req_bps_per_level = (0, 3, 3, 3, 4,
                                 4, 4, 4, 4, 8,
                                 6, 6, 6, 6, 12,
                                 10, 10, 10, 10, 20,
                                 15, 15, 15, 15, 30,
                                 20, 20, 20, 20, 40)
        else:
            req_bps_per_cap = (0, 20, 56, 110, 200, 333, 513)
            # Need to check everything (but especially early levels)
            req_bps_per_level = (0, 4, 4, 4, 8,
                                 6, 6, 6, 6, 12,
                                 9, 9, 9, 9, 18,
                                 15, 15, 15, 15, 30,
                                 22, 22, 22, 22, 45,
                                 30, 30, 30, 30, 60)

        target_level_idx = target_level // 5
        return (req_bps_per_cap[target_level_idx] -
                sum(req_bps_per_level[:current_level]) -
                current_bp)

    @staticmethod
    def isDecisiveShip(shipfu):
        return shipfu.rarity_id == 7

    def onFieldChanged(self):
        """Save user data and update required blueprints"""
        self.researchShipUserData["level"] = self.researchLevelSpinBox.value()
        self.researchShipUserData["bp"] = int(self.currentBpLineEdit.text())
        self.setRequiredBlueprints()
