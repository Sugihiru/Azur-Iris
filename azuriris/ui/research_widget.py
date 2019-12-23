from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QPixmap, QImage

from .ui.research_widget import Ui_ResearchWidget


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
