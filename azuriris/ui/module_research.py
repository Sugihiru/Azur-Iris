from PySide2.QtWidgets import QWidget

from data import Data
from .research_widget import ResearchWidget

from .ui.module_research import Ui_ModuleResearch


class ModuleResearch(QWidget, Ui_ModuleResearch):
    def __init__(self, user_data):
        super().__init__()
        self.setupUi(self)
        self.user_data = user_data

        researchShips = Data.getResearchShips()
        for researchShip in researchShips:
            self.gridLayout.addWidget(ResearchWidget(researchShip))
