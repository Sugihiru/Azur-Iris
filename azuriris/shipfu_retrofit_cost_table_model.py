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


class ProxyShipfuRetrofitCostTableModel(QtCore.QSortFilterProxyModel):
    def lessThan(self, source_left, source_right):
        if source_left.column() in (4, 5, 6):  # Blueprints
            if isinstance(source_left.data(), int):
                left_val = source_left.data()
            else:
                left_val = int(source_left.data().split()[0])
            if isinstance(source_right.data(), int):
                right_val = source_right.data()
            else:
                right_val = int(source_right.data().split()[0])
            return left_val < right_val
        return super().lessThan(source_left, source_right)
