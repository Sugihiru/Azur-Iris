import math

from PySide2.QtWidgets import QWidget

from .ui.tool_stage_exp import Ui_ToolStageExp


class ToolStageExp(QWidget, Ui_ToolStageExp):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.baseExpSpinBox.valueChanged.connect(
            self.displayGainedExp)
        self.moraleComboBox.currentIndexChanged.connect(
            self.displayGainedExp)
        self.rankComboBox.currentIndexChanged.connect(
            self.displayGainedExp)
        self.bonusExpSpinBox.valueChanged.connect(
            self.displayGainedExp)
        self.displayGainedExp()

    @staticmethod
    def computeGainedExp(baseExp, sRank=True, moraleMult=1, bonusExp=1,
                         mvp=False, flagship=False):
        return int(math.floor(baseExp *
                              (1.2 if sRank else 1) *
                              moraleMult *
                              bonusExp *
                              (2 if mvp else 1) *
                              (1.5 if flagship else 1)))

    def getMoraleMult(self):
        index = self.moraleComboBox.currentIndex()
        if index == 0:  # Very Happy
            return 1.2
        elif index == 1:  # Happy/Neutral
            return 1
        return 0.5  # Sad

    def displayGainedExp(self):
        baseExp = self.baseExpSpinBox.value()
        sRank = (self.rankComboBox.currentIndex() == 0)
        moraleMult = self.getMoraleMult()
        bonusExp = self.bonusExpSpinBox.value() / 100 + 1

        gainedExp = self.computeGainedExp(
            baseExp, sRank=sRank, moraleMult=moraleMult, bonusExp=bonusExp)
        self.expLabel.setText(str(gainedExp))

        gainedExpMvp = self.computeGainedExp(
            baseExp, sRank=sRank, moraleMult=moraleMult, bonusExp=bonusExp,
            mvp=True)
        self.expMvpLabel.setText(str(gainedExpMvp))

        gainedExpFlagship = self.computeGainedExp(
            baseExp, sRank=sRank, moraleMult=moraleMult, bonusExp=bonusExp,
            flagship=True)
        self.expFlagshipLabel.setText(str(gainedExpFlagship))

        gainedExpMvpFlagship = self.computeGainedExp(
            baseExp, sRank=sRank, moraleMult=moraleMult, bonusExp=bonusExp,
            mvp=True, flagship=True)
        self.expMvpFlagshipLabel.setText(str(gainedExpMvpFlagship))
