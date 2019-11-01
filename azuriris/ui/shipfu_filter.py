from PySide2.QtWidgets import QWidget

from .ui.shipfu_filter import Ui_ShipfuFilter


class ShipfuFilter(QWidget, Ui_ShipfuFilter):
    def __init__(self, data):
        super().__init__()
        self.rarities = data.rarities
        self.nations = data.nations
        self.ship_types = data.ship_types
        self.setupUi()

    def setupUi(self):
        super().setupUi(self)
        for comboBox, data_set in ((self.rarityComboBox, self.rarities),
                                   (self.nationComboBox, self.nations),
                                   (self.shipTypeComboBox, self.ship_types)):
            comboBox.addItem("All")
            comboBox.setItemData(0, None)
            comboBox.addItems([data.name for data in data_set])
            for i, data in enumerate(data_set):
                comboBox.setItemData(i + 1, data)
