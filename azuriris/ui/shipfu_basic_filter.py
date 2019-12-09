from PySide2.QtWidgets import QWidget

from .ui.shipfu_basic_filter import Ui_ShipfuBasicFilter


class ShipfuBasicFilter(QWidget, Ui_ShipfuBasicFilter):
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

        self.resetFiltersPushButton.clicked.connect(self.reset)

    def reset(self):
        self.nameLineEdit.setText("")
        for comboBox in (self.rarityComboBox,
                         self.nationComboBox,
                         self.shipTypeComboBox):
            comboBox.setCurrentIndex(0)
