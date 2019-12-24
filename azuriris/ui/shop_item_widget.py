from PySide2.QtWidgets import QFrame, QLabel
from PySide2.QtGui import QPixmap, QImage, QFont

from .ui.shop_item_widget import Ui_ShopItemWidget


class ShopItemWidget(QFrame, Ui_ShopItemWidget):
    def __init__(self, shopItem, shopEventItemUserData):
        super().__init__()
        self.shopItem = shopItem
        self.shopEventItemUserData = shopEventItemUserData
        self.total = 0
        self.setupUi()

    def setupUi(self):
        super().setupUi(self)
        qimg = QImage.fromData(self.shopItem.image)
        self.itemIconLabel.setPixmap(QPixmap.fromImage(qimg))
        self.itemNameLabel.setText(self.shopItem.name)

        self.priceUnitLabel.setText(str(self.shopItem.price_per_unit))
        self.quantitySpinBox.setValue(self.shopEventItemUserData["quantity"])
        self.quantitySpinBox.valueChanged.connect(self.onQuantityChanged)
        self.setTotalPrice()

        if self.shopItem.usual_max_per_event:
            self.usualMaxLabel.setText(str(self.shopItem.usual_max_per_event))
        else:
            self.usualMaxLabel.setText("Unknown")

    def setTotalPrice(self):
        self.total = (self.shopItem.price_per_unit *
                      self.quantitySpinBox.value())
        self.totalLabel.setText(str(self.total))

    def onQuantityChanged(self):
        self.shopEventItemUserData["quantity"] = self.quantitySpinBox.value()
        self.setTotalPrice()
