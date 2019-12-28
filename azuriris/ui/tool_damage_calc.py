import math

from PySide2.QtWidgets import QWidget, QTableWidgetItem
from PySide2.QtCore import Qt

from .ui.tool_damage_calc import Ui_ToolDamageCalc


class ToolDamageCalc(QWidget, Ui_ToolDamageCalc):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        for spinBox in (self.damageStatSpinBox,
                        self.equipmentDmgSpinBox,
                        self.fireRateDoubleSpinBox,
                        self.shellsPerVolleySpinBox,
                        self.weaponCoeffSpinBox,
                        self.slotEffSpinBox,
                        self.lightArmorMultSpinBox,
                        self.mediumArmorMultSpinBox,
                        self.heavyArmorMultSpinBox):
            spinBox.valueChanged.connect(self.displayDmg)
        self.displayDmg()

    @staticmethod
    def computeDmg(equipmentDmg, weaponCoeff, slotEff, armorMult,
                   dmgStat, levelAdvMult=1):
        """
        Formula is taken from
        https://azurlane.koumakan.jp/Combat#Final_Weapon_Damage
        """
        return int(math.floor(equipmentDmg *
                              weaponCoeff *
                              slotEff *
                              armorMult *
                              levelAdvMult *
                              ((100 + dmgStat) / 100)
                              ))

    def displayDmg(self):
        equipmentDmg = self.equipmentDmgSpinBox.value()
        weaponCoeff = self.weaponCoeffSpinBox.value() / 100
        slotEff = self.slotEffSpinBox.value() / 100
        dmgStat = self.damageStatSpinBox.value()

        dmgsPerShell = list()
        for i, armorMult in enumerate((self.lightArmorMultSpinBox.value(),
                                       self.mediumArmorMultSpinBox.value(),
                                       self.heavyArmorMultSpinBox.value())):
            dmg = self.computeDmg(equipmentDmg, weaponCoeff, slotEff,
                                  armorMult / 100, dmgStat)
            dmgsPerShell.append(dmg)
            item = QTableWidgetItem(str(dmg))
            item.setTextAlignment(Qt.AlignCenter)
            self.damageTableWidget.setItem(0, i, item)

        shellsPerVolley = self.shellsPerVolleySpinBox.value()
        dmgsPerVolley = list()
        for i, dmgPerShell in enumerate(dmgsPerShell):
            dmgPerVolley = dmgPerShell * shellsPerVolley
            dmgsPerVolley.append(dmgPerVolley)
            item = QTableWidgetItem(str(dmgPerVolley))
            item.setTextAlignment(Qt.AlignCenter)
            self.damageTableWidget.setItem(1, i, item)

        fireRate = self.fireRateDoubleSpinBox.value()
        for i, dmgPerVolley in enumerate(dmgsPerVolley):
            dps = int(math.floor(dmgPerVolley / fireRate))
            item = QTableWidgetItem(str(dps))
            item.setTextAlignment(Qt.AlignCenter)
            self.damageTableWidget.setItem(2, i, item)
