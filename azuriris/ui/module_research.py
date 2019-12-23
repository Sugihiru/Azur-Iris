from PySide2.QtWidgets import QWidget

from data import Data
from user_data import UserData
from .research_widget import ResearchWidget

from .ui.module_research import Ui_ModuleResearch


class ModuleResearch(QWidget, Ui_ModuleResearch):
    def __init__(self, researchUserData):
        super().__init__()
        self.setupUi(self)
        self.researchUserData = researchUserData

        researchShips = Data.getResearchShips()
        for researchShip in researchShips:
            shipfu_id = researchShip.Shipfu.shipfu_id
            try:
                researchShipUserData = self.researchUserData[shipfu_id]
            except KeyError:
                researchShipUserData = UserData.initResearchData()
                self.researchUserData[shipfu_id] = researchShipUserData

            self.gridLayout.addWidget(ResearchWidget(researchShip,
                                                     researchShipUserData))
