from PySide2.QtWidgets import (QWidget, QLabel, QTableWidget, QSizePolicy,
                               QTableWidgetItem, QAbstractItemView)
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

        if self.hasFateSimulation(self.researchShip):
            self.addFateSimulationTable()
            if self.researchShipUserData["level"] == 30:
                self.fateSimulationPhaseSpinBox.setEnabled(True)
            self.fateSimulationPhaseSpinBox.setValue(
                self.researchShipUserData["fate_simul_phase"])
            self.fateSimulationPhaseSpinBox.valueChanged.connect(
                self.onFieldChanged)

        self.researchLevelSpinBox.setValue(self.researchShipUserData["level"])
        self.researchLevelSpinBox.valueChanged.connect(self.onFieldChanged)
        self.currentBpSpinBox.setValue(self.researchShipUserData["bp"])
        self.currentBpSpinBox.valueChanged.connect(self.onFieldChanged)

    @staticmethod
    def hasFateSimulation(shipfu):
        return shipfu.ResearchShip.season <= MAX_FATE_SIMUL_SEASON

    def addFateSimulationTable(self):
        """Add the Fate Simulation table widget to the widget's layout"""
        boldFont = QFont()
        boldFont.setBold(True)

        self.fateSimulationTitleLabel = QLabel(
            "Blueprints needed per Fate Simulation level")
        self.fateSimulationTitleLabel.setFont(boldFont)
        self.gridLayout.addWidget(self.fateSimulationTitleLabel, 7, 0, 1, 6)

        # Setup table widget
        self.fateSimulationTableWidget = QTableWidget(self)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.fateSimulationTableWidget.setSizePolicy(sizePolicy)
        self.fateSimulationTableWidget.setMinimumSize(QSize(620, 55))
        self.fateSimulationTableWidget.setRowCount(1)
        self.fateSimulationTableWidget.setColumnCount(5)

        self.fateSimulationTableWidget.setEditTriggers(
            QAbstractItemView.NoEditTriggers)

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

        self.gridLayout.addWidget(self.fateSimulationTableWidget, 8, 0, 1, 6)

    def setRequiredBlueprints(self):
        """Compute and display required blueprints"""
        for i, target_level in enumerate((5, 10, 15, 20, 25, 30)):
            req_bp = self.computeRequiredBlueprintsForStrengthenLevel(
                target_level,
                self.researchShipUserData["level"],
                self.researchShipUserData["bp"],
                self.isDecisiveShip(self.researchShip.Shipfu))

            item = QTableWidgetItem(str(req_bp))
            item.setTextAlignment(Qt.AlignCenter)
            self.strengthenLevelTableWidget.setItem(0, i, item)

        if self.hasFateSimulation(self.researchShip):
            req_bp_to_level_30 = \
                self.computeRequiredBlueprintsForStrengthenLevel(
                    30,
                    self.researchShipUserData["level"],
                    self.researchShipUserData["bp"],
                    self.isDecisiveShip(self.researchShip.Shipfu))
            for target_phase in range(1, 6):
                req_bp = self.computeRequiredBlueprintsForFateSimulation(
                    target_phase,
                    self.researchShipUserData["fate_simul_phase"],
                    self.researchShipUserData["bp"])
                req_bp += req_bp_to_level_30

                item = QTableWidgetItem(str(req_bp))
                item.setTextAlignment(Qt.AlignCenter)
                self.fateSimulationTableWidget.setItem(0, target_phase - 1,
                                                       item)

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
        res = (req_bps_per_cap[target_level_idx] -
               sum(req_bps_per_level[:current_level]) -
               current_bp)
        if res < 0:
            res = 0
        return res

    @staticmethod
    def computeRequiredBlueprintsForFateSimulation(target_phase,
                                                   current_phase,
                                                   current_bp):
        if current_phase >= 5 or target_phase <= current_phase:
            return 0

        req_bps = (10, 20, 30, 40, 65)

        res = (sum(req_bps[:target_phase]) -
               sum(req_bps[:current_phase]) -
               current_bp)
        if res < 0:
            res = 0
        return res

    @staticmethod
    def isDecisiveShip(shipfu):
        return shipfu.rarity_id == 7

    def onFieldChanged(self):
        """Save user data and update required blueprints"""
        self.researchShipUserData["level"] = \
            self.researchLevelSpinBox.value() or 0
        self.researchShipUserData["bp"] = self.currentBpSpinBox.value() or 0
        self.researchShipUserData["fate_simul_phase"] = \
            self.fateSimulationPhaseSpinBox.value() or 0
        if self.researchShipUserData["level"] == 30:
            self.fateSimulationPhaseSpinBox.setEnabled(True)
        else:
            self.fateSimulationPhaseSpinBox.setEnabled(False)
        self.setRequiredBlueprints()
