from PySide2.QtWidgets import QWidget, QTableWidgetItem
from PySide2.QtCore import Qt

from .ui.tool_leveling import Ui_ToolLeveling


class ToolLeveling(QWidget, Ui_ToolLeveling):
    # Table from https://azurlane.koumakan.jp/Experience
    expTable = [
        0, 100, 300, 600, 1_000, 1_500, 2_100, 2_800, 3_600, 4_500,
        5_500, 6_600, 7_800, 9_100, 10_500, 12_000, 13_600, 15_300, 17_100, 19_000,  # noqa
        21_000, 23_100, 25_300, 27_600, 30_000, 32_500, 35_100, 37_800, 40_600, 43_500,  # noqa
        46_500, 49_600, 52_800, 56_100, 59_500, 63_000, 66_600, 70_300, 74_100, 78_000,  # noqa
        82_000, 86_200, 90_600, 95_200, 100_000, 105_000, 110_200, 115_600, 121_200, 127_000,  # noqa
        133_000, 139_200, 145_600, 152_200, 159_000, 166_000, 173_200, 180_600, 188_200, 196_000,  # noqa
        204_000, 212_300, 220_900, 229_800, 239_000, 248_500, 258_300, 268_400, 278_800, 289_500,  # noqa
        301_600, 314_140, 327_120, 340_540, 354_400, 368_700, 383_440, 398_620, 414_240, 430_300,  # noqa
        447_550, 465_375, 483_775, 502_750, 522_300, 542_425, 563_125, 584_400, 606_250, 628_675,  # noqa
        652_675, 677_875, 704_275, 733_075, 764_275, 800_275, 842_275, 890_275, 962_275, 1_120_675,  # noqa
        1_190_675, 1_262_675, 1_336_675, 1_412_675, 1_490_675, 1_575_675, 1_672_675, 1_781_675, 1_902_675, 2_035_675,  # noqa
        2_180_675, 2_343_675, 2_524_675, 2_723_675, 2_940_675, 3_175_675, 3_431_675, 3_708_675, 4_006_675, 4_325_675]  # noqa

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.currentLevelSpinBox.valueChanged.connect(
            self.displayNeededExp)
        self.currentExpSpinBox.valueChanged.connect(
            self.displayNeededExp)
        self.displayNeededExp()

    @classmethod
    def computeRealLevel(cls, currentLevel, currentExp):
        # Max level
        if currentLevel == 120:
            return 120

        while (currentLevel < 120 and
               cls.expTable[currentLevel - 1] + currentExp >=
               cls.expTable[currentLevel]):
            currentExp -= (cls.expTable[currentLevel] -
                           cls.expTable[currentLevel - 1])
            currentLevel += 1
        return currentLevel

    @classmethod
    def computeNeededExpForLevel(cls, targetLevel, currentLevel, currentExp):
        if currentLevel >= targetLevel:
            return 0
        currentTotalExp = cls.expTable[currentLevel - 1] + currentExp
        neededExp = cls.expTable[targetLevel - 1] - currentTotalExp
        return neededExp if neededExp > 0 else 0

    def displayNeededExp(self):
        currentLevel = self.currentLevelSpinBox.value()
        currentExp = self.currentExpSpinBox.value()

        realLevel = self.computeRealLevel(currentLevel, currentExp)
        self.realLevelLabel.setText(str(realLevel))

        for i, targetLevel in enumerate((100, 105, 110, 115, 120)):
            neededExp = self.computeNeededExpForLevel(
                targetLevel, currentLevel, currentExp)

            item = QTableWidgetItem(f"{neededExp:,}".replace(',', ' '))
            item.setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(0, i, item)
