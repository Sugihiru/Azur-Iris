from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QPixmap


import data
from .ui.module_retrofit import Ui_ModuleRetrofit

# Qt compiled resource file
from .resources import resources  # noqa


class ModuleRetrofit(QWidget, Ui_ModuleRetrofit):
    def __init__(self, data_obj):
        super().__init__()
        self.retrofitCosts = data.getRetrofitCosts()

        self.DD_TYPE_ID = next(x.ship_type_id for x in data_obj.ship_types
                               if x.abbreviation == "DD")
        self.CRUISER_TYPE_ID = next(x.ship_type_id for x in data_obj.ship_types
                                    if x.abbreviation == "CL")
        self.BATTLESHIP_TYPE_ID = next(
            x.ship_type_id for x in data_obj.ship_types
            if x.abbreviation == "BB")
        self.CARRIER_TYPE_ID = next(x.ship_type_id for x in data_obj.ship_types
                                    if x.abbreviation == "CV")

        self.setupUi()

    def setupUi(self):
        super().setupUi(self)
        for label, imgpath in ((self.destroyersT1IconLabel,
                                ":/blueprints/DestroyerT1BP.png"),
                               (self.destroyersT2IconLabel,
                                ":/blueprints/DestroyerT2BP.png"),
                               (self.destroyersT3IconLabel,
                                ":/blueprints/DestroyerT3BP.png"),
                               (self.cruisersT1IconLabel,
                                ":/blueprints/CruiserT1BP.png"),
                               (self.cruisersT2IconLabel,
                                ":/blueprints/CruiserT2BP.png"),
                               (self.cruisersT3IconLabel,
                                ":/blueprints/CruiserT3BP.png"),
                               (self.battleshipsT1IconLabel,
                                ":/blueprints/BattleshipT1BP.png"),
                               (self.battleshipsT2IconLabel,
                                ":/blueprints/BattleshipT2BP.png"),
                               (self.battleshipsT3IconLabel,
                                ":/blueprints/BattleshipT3BP.png"),
                               (self.carriersT1IconLabel,
                                ":/blueprints/CarrierT1BP.png"),
                               (self.carriersT2IconLabel,
                                ":/blueprints/CarrierT2BP.png"),
                               (self.carriersT3IconLabel,
                                ":/blueprints/CarrierT3BP.png")):
            label.setPixmap(QPixmap(imgpath))
        self.setTotalRetrofitCostPerType()

    def setTotalRetrofitCostPerType(self):
        destroyerRetrofitCosts = [x for x in self.retrofitCosts
                                  if x.bp_type_id == self.DD_TYPE_ID]
        self.destroyersT1NbLabel.setText(str(
            sum(x.t1_bp for x in destroyerRetrofitCosts)))
        self.destroyersT2NbLabel.setText(str(
            sum(x.t2_bp for x in destroyerRetrofitCosts)))
        self.destroyersT3NbLabel.setText(str(
            sum(x.t3_bp for x in destroyerRetrofitCosts)))

        cruiserRetrofitCosts = [x for x in self.retrofitCosts
                                if x.bp_type_id == self.CRUISER_TYPE_ID]
        self.cruisersT1NbLabel.setText(str(
            sum(x.t1_bp for x in cruiserRetrofitCosts)))
        self.cruisersT2NbLabel.setText(str(
            sum(x.t2_bp for x in cruiserRetrofitCosts)))
        self.cruisersT3NbLabel.setText(str(
            sum(x.t3_bp for x in cruiserRetrofitCosts)))

        battleshipRetrofitCosts = [x for x in self.retrofitCosts
                                   if x.bp_type_id == self.BATTLESHIP_TYPE_ID]
        self.battleshipsT1NbLabel.setText(str(
            sum(x.t1_bp for x in battleshipRetrofitCosts)))
        self.battleshipsT2NbLabel.setText(str(
            sum(x.t2_bp for x in battleshipRetrofitCosts)))
        self.battleshipsT3NbLabel.setText(str(
            sum(x.t3_bp for x in battleshipRetrofitCosts)))

        carrierRetrofitCosts = [x for x in self.retrofitCosts
                                if x.bp_type_id == self.CARRIER_TYPE_ID]
        self.carriersT1NbLabel.setText(str(
            sum(x.t1_bp for x in carrierRetrofitCosts)))
        self.carriersT2NbLabel.setText(str(
            sum(x.t2_bp for x in carrierRetrofitCosts)))
        self.carriersT3NbLabel.setText(str(
            sum(x.t3_bp for x in carrierRetrofitCosts)))
