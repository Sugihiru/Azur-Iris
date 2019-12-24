from PySide2.QtWidgets import QWidget

from data import Data
from user_data import UserData
from .shop_item_widget import ShopItemWidget

from .ui.module_shopevent import Ui_ModuleShopEvent


NB_GRID_COLUMNS = 3


class ModuleShopEvent(QWidget, Ui_ModuleShopEvent):
    def __init__(self, shopEventUserData):
        super().__init__()
        self.setupUi(self)
        self.shopEventUserData = shopEventUserData
        self.itemWidgets = list()

        shopEventItems = Data.getShopEventItems()
        for i, shopEventItem in enumerate(shopEventItems):
            itemId = str(shopEventItem.event_buyable_id)
            try:
                shopEventItemUserData = self.shopEventUserData[itemId]
            except KeyError:
                shopEventItemUserData = UserData.initShopEventData()
                self.shopEventUserData[itemId] = shopEventItemUserData

            itemWidget = ShopItemWidget(shopEventItem, shopEventItemUserData)
            itemWidget.quantitySpinBox.valueChanged.connect(
                self.displayTotalPrice)
            self.itemWidgets.append(itemWidget)
            self.gridLayout.addWidget(itemWidget,
                                      i // NB_GRID_COLUMNS,
                                      i % NB_GRID_COLUMNS)
        self.displayTotalPrice()

    def displayTotalPrice(self):
        total = sum(x.total for x in self.itemWidgets)
        self.reqTokenLabel.setText(str(total))
