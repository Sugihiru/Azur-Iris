from PySide2 import QtCore
from PySide2.QtCore import Qt

from data import Data


class ShipfuRetrofitCostTableModel(QtCore.QAbstractTableModel):
    def __init__(self, retrofitCosts):
        super().__init__()
        self.retrofitCosts = list()
        for retrofitCost in retrofitCosts:
            if (self.retrofitCosts and
                    retrofitCost.shipfu_id == self.retrofitCosts[-1][0]):
                if retrofitCost.t1_bp:
                    self.retrofitCosts[-1][4] = "{} + {} {} blueprints".format(
                        self.retrofitCosts[-1][4],
                        retrofitCost.t1_bp,
                        retrofitCost.shipTypeIdToName())
                if retrofitCost.t2_bp:
                    self.retrofitCosts[-1][5] = "{} + {} {} blueprints".format(
                        self.retrofitCosts[-1][5],
                        retrofitCost.t2_bp,
                        retrofitCost.shipTypeIdToName())
                if retrofitCost.t3_bp:
                    self.retrofitCosts[-1][6] = "{} + {} {} blueprints".format(
                        self.retrofitCosts[-1][6],
                        retrofitCost.t3_bp,
                        retrofitCost.shipTypeIdToName())
            else:
                shipfu = Data.getShipfuFromId(retrofitCost.shipfu_id)

                dataElement = [shipfu.Shipfu.shipfu_id,
                               shipfu.Shipfu.image,
                               shipfu.Shipfu.name,
                               retrofitCost.shipTypeIdToName(),
                               retrofitCost.t1_bp,
                               retrofitCost.t2_bp,
                               retrofitCost.t3_bp,
                               retrofitCost.gold]

                if retrofitCost.hasPlatesReq:
                    otherReq = list()
                    if retrofitCost.gun_plates:
                        otherReq.append(
                            f"{retrofitCost.gun_plates} gun plates")
                    if retrofitCost.torpedo_plates:
                        otherReq.append(
                            f"{retrofitCost.torpedo_plates} torpedo plates")
                    if retrofitCost.aircraft_plates:
                        otherReq.append(
                            f"{retrofitCost.aircraft_plates} aircraft plates")
                    if retrofitCost.antiair_plates:
                        otherReq.append(
                            f"{retrofitCost.antiair_plates} anti-air plates")
                    if retrofitCost.aux_plates:
                        otherReq.append(
                            f"{retrofitCost.aux_plates} auxiliary plates")
                    dataElement.append(", ".join(otherReq))
                else:
                    dataElement.append("")
                self.retrofitCosts.append(dataElement)
        # self.retrofitCosts = retrofitCosts
        # self.nbShipfus = len(set(x.shipfu_id for x in self.retrofitCosts))
        self.headers = ["Id", "Image", "Name", "BP Type", "T1Icon", "T2Icon",
                        "T3Icon", "Gold", "Other"]

    def rowCount(self, parent=None):
        return len(self.retrofitCosts)

    def columnCount(self, parent=None):
        return len(self.headers)

    def data(self, index, role=Qt.DisplayRole):
        row = index.row()
        column = index.column()
        if role == Qt.TextAlignmentRole:
            return Qt.AlignCenter

        if role == Qt.DisplayRole:
            return self.retrofitCosts[row][column]

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.headers[section]




class ProxyShipfuTableModel(QtCore.QSortFilterProxyModel):
    def __init__(self):
        super().__init__()
        # Rarity is already ordered
        self.rarity_order = [rarity.name for rarity in Data.getRarities()]
        self.rarity_filter = None
        self.nation_filter = None
        self.shiptype_filter = None

        self.build_filter = True
        self.drop_filter = True
        self.shop_filter = True
        self.event_filter = True
        self.research_filter = True
        self.collection_filter = True
        self.login_reward_filter = True

    def filterAcceptsRow(self, sourceRow, sourceParent):
        if sourceRow >= self.sourceModel().rowCount():
            return False

        shipfu = self.sourceModel().shipfus[sourceRow]
        for (shipfu_value, shipfu_filter) in (
                (shipfu.Rarity, self.rarity_filter),
                (shipfu.Nation, self.nation_filter),
                (shipfu.ShipType, self.shiptype_filter)):
            if shipfu_filter and shipfu_value != shipfu_filter:
                return False

        obtention_filters = (
            (self.build_filter and shipfu.Shipfu.is_buildable()) or
            (self.drop_filter and shipfu.Shipfu.drops) or
            (self.shop_filter and shipfu.Shipfu.is_buyable()) or
            (self.event_filter and shipfu.Shipfu.is_event_ship) or
            (self.research_filter and shipfu.Shipfu.is_pr_ship()) or
            (self.collection_filter and shipfu.Shipfu.is_collection_ship) or
            (self.login_reward_filter and shipfu.Shipfu.is_login_reward_ship)
        )

        if not obtention_filters:
            print(shipfu.Shipfu)
            return False

        pattern = self.filterRegExp().pattern().lower()
        return pattern in shipfu.Shipfu.name.lower()

    def lessThan(self, source_left, source_right):
        if source_left.column() == 3:  # Sort by rarity
            left_rarity_index = self.rarity_order.index(source_left.data())
            right_rarity_index = self.rarity_order.index(source_right.data())
            return left_rarity_index < right_rarity_index
        return super().lessThan(source_left, source_right)
