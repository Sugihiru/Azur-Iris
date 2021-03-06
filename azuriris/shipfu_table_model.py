from PySide2 import QtCore
from PySide2.QtCore import Qt

from generic_proxy_shipfu_table_model import GenericProxyShipfuTableModel

from user_data import UserData


CHECKBOXES_COLUMNS_IDX = (6, 7, 8, 9)


class ShipfuTableModel(QtCore.QAbstractTableModel):
    def __init__(self, shipfus, user_shipfus_data):
        super().__init__()
        if shipfus:
            self.shipfus = shipfus
        else:
            self.shipfus = list()
        self.user_shipfus_data = user_shipfus_data
        self.headers = ["Id", "Image", "Name", "Rarity", "Type", "Nation",
                        "Owned", "MLB", "Level 120", "Max Affection",
                        "How to obtain"]

    def rowCount(self, parent=None):
        return len(self.shipfus)

    def columnCount(self, parent=None):
        return len(self.headers)

    def data(self, index, role=Qt.DisplayRole):
        row = index.row()
        column = index.column()
        if role == Qt.TextAlignmentRole:
            return Qt.AlignCenter

        if role == Qt.DisplayRole:
            shipfu_id = str(self.shipfus[row].Shipfu.shipfu_id)
            try:
                shipfu_user_data = self.user_shipfus_data[shipfu_id]
            except KeyError:
                shipfu_user_data = UserData.initShipfuData()
                self.user_shipfus_data[shipfu_id] = shipfu_user_data

            values = (self.shipfus[row].Shipfu.shipfu_id,
                      self.shipfus[row].Shipfu.image,
                      self.shipfus[row].Shipfu.name,
                      self.shipfus[row].Rarity.name,
                      self.shipfus[row].ShipType.name,
                      self.shipfus[row].Nation.name,
                      shipfu_user_data["owned"],
                      shipfu_user_data["mlb"],
                      shipfu_user_data["max_level"],
                      shipfu_user_data["max_affection"],
                      self.shipfus[row].Shipfu.obtention_methods)

            return values[column]

    def setData(self, index, value, role=Qt.DisplayRole):
        if index.column() in CHECKBOXES_COLUMNS_IDX:
            shipfu_id = str(self.shipfus[index.row()].Shipfu.shipfu_id)
            shipfus_data_keys = {
                CHECKBOXES_COLUMNS_IDX[0]: "owned",
                CHECKBOXES_COLUMNS_IDX[1]: "mlb",
                CHECKBOXES_COLUMNS_IDX[2]: "max_level",
                CHECKBOXES_COLUMNS_IDX[3]: "max_affection"
            }
            shipfus_data_key = shipfus_data_keys[index.column()]
            self.user_shipfus_data[shipfu_id][shipfus_data_key] = value
            return value
        return value

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.headers[section]

    def flags(self, index):
        default_flags = Qt.ItemIsEnabled | Qt.ItemIsSelectable

        if not index.isValid():
            return None
        if index.column() in CHECKBOXES_COLUMNS_IDX:
            return default_flags | Qt.ItemIsEditable
        return default_flags


class ProxyShipfuTableModel(GenericProxyShipfuTableModel):
    def __init__(self):
        super().__init__()

        self.build_filter = True
        self.drop_filter = True
        self.shop_filter = True
        self.event_filter = True
        self.research_filter = True
        self.collection_filter = True
        self.login_reward_filter = True

    def filterAcceptsRow(self, sourceRow, sourceParent):
        if not super().filterAcceptsRow(sourceRow, sourceParent):
            return False

        shipfu = self.sourceModel().shipfus[sourceRow]
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
        return True

    def lessThan(self, source_left, source_right):
        if source_left.column() == 3:  # Sort by rarity
            left_rarity_index = self.rarity_order.index(source_left.data())
            right_rarity_index = self.rarity_order.index(source_right.data())
            return left_rarity_index < right_rarity_index
        return super().lessThan(source_left, source_right)
