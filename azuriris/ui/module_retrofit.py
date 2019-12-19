from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QPixmap

from data import Data

from .ui.module_retrofit import Ui_ModuleRetrofit
from shipfu_retrofit_cost_table_model import ShipfuRetrofitCostTableModel
# Qt compiled resource file
from .resources import resources  # noqa


class ModuleRetrofit(QWidget, Ui_ModuleRetrofit):
    def __init__(self, user_data):
        super().__init__()
        self.user_data = user_data
        self.retrofitCosts = [x for x in Data.getRetrofitCosts()
                              if not self.user_data.isOwnedShipfu(x.shipfu_id)]

        ship_types = Data.getShipTypes()
        self.DD_TYPE_ID = next(x.ship_type_id for x in ship_types
                               if x.abbreviation == "DD")
        self.CRUISER_TYPE_ID = next(x.ship_type_id for x in ship_types
                                    if x.abbreviation == "CL")
        self.BATTLESHIP_TYPE_ID = next(x.ship_type_id for x in ship_types
                                       if x.abbreviation == "BB")
        self.CARRIER_TYPE_ID = next(x.ship_type_id for x in ship_types
                                    if x.abbreviation == "CV")

        self.setupUi()

        self.model = ShipfuRetrofitCostTableModel(self.retrofitCosts)
        # self.proxyModel = ProxyComparisonMultipleShipfusTableModel(rarities)
        # self.proxyModel.setSourceModel(self.model)
        self.resourcesPerShipTableView.setModel(self.model)

    def setupUi(self):
        super().setupUi(self)
        for label, imgpath in ((self.destroyersT1IconLabel,
                                ":/blueprints/DestroyerT1BP.png"),
                               (self.destroyersT2IconLabel,
                                ":/blueprints/DestroyerT2BP.png"),
                               (self.destroyersT3IconLabel,
                                ":/blueprints/DestroyerT3BP.png"),
                               (self.destroyersGoldIconLabel,
                                ":/general/Coin.png"),
                               (self.cruisersT1IconLabel,
                                ":/blueprints/CruiserT1BP.png"),
                               (self.cruisersT2IconLabel,
                                ":/blueprints/CruiserT2BP.png"),
                               (self.cruisersT3IconLabel,
                                ":/blueprints/CruiserT3BP.png"),
                               (self.cruisersGoldIconLabel,
                                ":/general/Coin.png"),
                               (self.battleshipsT1IconLabel,
                                ":/blueprints/BattleshipT1BP.png"),
                               (self.battleshipsT2IconLabel,
                                ":/blueprints/BattleshipT2BP.png"),
                               (self.battleshipsT3IconLabel,
                                ":/blueprints/BattleshipT3BP.png"),
                               (self.battleshipsGoldIconLabel,
                                ":/general/Coin.png"),
                               (self.carriersT1IconLabel,
                                ":/blueprints/CarrierT1BP.png"),
                               (self.carriersT2IconLabel,
                                ":/blueprints/CarrierT2BP.png"),
                               (self.carriersT3IconLabel,
                                ":/blueprints/CarrierT3BP.png"),
                               (self.carriersGoldIconLabel,
                                ":/general/Coin.png"),
                               (self.totalGoldIconLabel,
                                ":/general/Coin.png"),
                               (self.gunPlatesIconLabel,
                                ":/plates/GunT3Plate.png"),
                               (self.torpedoPlatesIconLabel,
                                ":/plates/TorpT3Plate.png"),
                               (self.aircraftPlatesIconLabel,
                                ":/plates/PlaneT3Plate.png"),
                               (self.antiairPlatesIconLabel,
                                ":/plates/AAT3Plate.png"),
                               (self.auxPlatesIconLabel,
                                ":/plates/AuxT3Plate.png"),):
            label.setPixmap(QPixmap(imgpath))
        self.setTotalRetrofitCostInfos()

    def setTotalRetrofitCostInfos(self):
        self.setTotalRetrofitCostPerType()
        self.setTotalRetrofitCostGlobal()

    def setTotalRetrofitCostPerType(self):
        destroyerRetrofitCosts = [x for x in self.retrofitCosts
                                  if x.bp_type_id == self.DD_TYPE_ID]
        self.destroyersT1NbLabel.setText(str(
            sum(x.t1_bp for x in destroyerRetrofitCosts)))
        self.destroyersT2NbLabel.setText(str(
            sum(x.t2_bp for x in destroyerRetrofitCosts)))
        self.destroyersT3NbLabel.setText(str(
            sum(x.t3_bp for x in destroyerRetrofitCosts)))
        # Use ' ' as a group of 3 separator for numbers (ISO 31-0)
        self.destroyersGoldNbLabel.setText(
            f'{sum(x.gold for x in destroyerRetrofitCosts):,}'
            .replace(',', ' '))

        cruiserRetrofitCosts = [x for x in self.retrofitCosts
                                if x.bp_type_id == self.CRUISER_TYPE_ID]
        self.cruisersT1NbLabel.setText(str(
            sum(x.t1_bp for x in cruiserRetrofitCosts)))
        self.cruisersT2NbLabel.setText(str(
            sum(x.t2_bp for x in cruiserRetrofitCosts)))
        self.cruisersT3NbLabel.setText(str(
            sum(x.t3_bp for x in cruiserRetrofitCosts)))
        self.cruisersGoldNbLabel.setText(
            f'{sum(x.gold for x in cruiserRetrofitCosts):,}'
            .replace(',', ' '))

        battleshipRetrofitCosts = [x for x in self.retrofitCosts
                                   if x.bp_type_id == self.BATTLESHIP_TYPE_ID]
        self.battleshipsT1NbLabel.setText(str(
            sum(x.t1_bp for x in battleshipRetrofitCosts)))
        self.battleshipsT2NbLabel.setText(str(
            sum(x.t2_bp for x in battleshipRetrofitCosts)))
        self.battleshipsT3NbLabel.setText(str(
            sum(x.t3_bp for x in battleshipRetrofitCosts)))
        self.battleshipsGoldNbLabel.setText(
            f'{sum(x.gold for x in battleshipRetrofitCosts):,}'
            .replace(',', ' '))

        carrierRetrofitCosts = [x for x in self.retrofitCosts
                                if x.bp_type_id == self.CARRIER_TYPE_ID]
        self.carriersT1NbLabel.setText(str(
            sum(x.t1_bp for x in carrierRetrofitCosts)))
        self.carriersT2NbLabel.setText(str(
            sum(x.t2_bp for x in carrierRetrofitCosts)))
        self.carriersT3NbLabel.setText(str(
            sum(x.t3_bp for x in carrierRetrofitCosts)))
        self.carriersGoldNbLabel.setText(
            f'{sum(x.gold for x in carrierRetrofitCosts):,}'
            .replace(',', ' '))

    def setTotalRetrofitCostGlobal(self):
        self.totalGoldNbLabel.setText(
            f'{sum(x.gold for x in self.retrofitCosts):,}'
            .replace(',', ' '))

        nb_gun_plates_needed = str(
            sum(x.gun_plates for x in self.retrofitCosts if x.gun_plates))
        nb_torpedo_plates_needed = str(
            sum(x.torpedo_plates for x in self.retrofitCosts
                if x.torpedo_plates))
        nb_aircraft_plates_needed = str(
            sum(x.aircraft_plates for x in self.retrofitCosts
                if x.aircraft_plates))
        nb_antiair_plates_needed = str(
            sum(x.antiair_plates for x in self.retrofitCosts
                if x.antiair_plates))
        nb_aux_plates_needed = str(
            sum(x.aux_plates for x in self.retrofitCosts if x.aux_plates))

        nbs_plates_needed = (nb_gun_plates_needed, nb_torpedo_plates_needed,
                             nb_aircraft_plates_needed,
                             nb_antiair_plates_needed, nb_aux_plates_needed)
        labels = (self.gunPlatesNbLabel, self.torpedoPlatesNbLabel,
                  self.aircraftPlatesNbLabel, self.antiairPlatesNbLabel,
                  self.auxPlatesNbLabel)

        for label, nb_plate in zip(labels, nbs_plates_needed):
            label.setText(label.text().replace("{nb}", nb_plate))
