from PySide2.QtWidgets import QWidget

from .tool_mission_cost import ToolMissionCost
from .tool_leveling import ToolLeveling
from .tool_stage_exp import ToolStageExp
from .tool_damage_calc import ToolDamageCalc
from .ui.module_tools import Ui_ModuleTools


class ModuleTools(QWidget, Ui_ModuleTools):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.missionCostTab = ToolMissionCost()
        self.tabWidget.addTab(self.missionCostTab, "")
        self.tabWidget.setTabText(0, self.tr("Mission Cost"))

        self.levelingTab = ToolLeveling()
        self.tabWidget.addTab(self.levelingTab, "")
        self.tabWidget.setTabText(1, self.tr("Leveling"))

        self.stageExpTab = ToolStageExp()
        self.tabWidget.addTab(self.stageExpTab, "")
        self.tabWidget.setTabText(2, self.tr("Stage Experience"))

        self.damageCalcTab = ToolDamageCalc()
        self.tabWidget.addTab(self.damageCalcTab, "")
        self.tabWidget.setTabText(3, self.tr("Damage Calculator"))
