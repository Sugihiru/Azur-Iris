from PySide2.QtWidgets import (QWidget, QLabel, QTableWidget, QSizePolicy,
                               QTableWidgetItem)
from PySide2.QtGui import QPixmap, QImage, QFont
from PySide2.QtCore import QSize

from .ui.research_widget import Ui_ResearchWidget

# Indicate the maximum Research Season where a Fate Simulation is possible
# Currently, only PR S1 have Fate Simulation
MAX_FATE_SIMUL_SEASON = 1


class ResearchWidget(QWidget, Ui_ResearchWidget):
    def __init__(self, researchShip):
        super().__init__()
        self.researchShip = researchShip
        self.setupUi()

    def setupUi(self):
        super().setupUi(self)
        qimg = QImage.fromData(self.researchShip.Shipfu.image)
        self.shipIconLabel.setPixmap(QPixmap.fromImage(qimg))
        self.shipNameLabel.setText(self.researchShip.Shipfu.name)

        if self.researchShip.ResearchShip.season <= MAX_FATE_SIMUL_SEASON:
            self.addFateSimulationTable()

    def addFateSimulationTable(self):
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
