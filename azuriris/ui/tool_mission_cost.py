from PySide2.QtWidgets import QWidget

from .ui.tool_mission_cost import Ui_ToolMissionCost


class ToolMissionCost(QWidget, Ui_ToolMissionCost):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.nbFleetBeforeBossSpinBox.valueChanged.connect(
            self.displayTotalCost)
        self.clearFleetCostSpinBox.valueChanged.connect(
            self.displayTotalCost)
        self.bossFleetCostSpinBox.valueChanged.connect(
            self.displayTotalCost)

    def displayTotalCost(self):
        total_cost = (self.nbFleetBeforeBossSpinBox.value() *
                      self.clearFleetCostSpinBox.value() +
                      self.bossFleetCostSpinBox.value())
        self.totalCostLabel.setText(str(total_cost))
