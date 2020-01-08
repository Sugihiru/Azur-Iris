import webbrowser

from PySide2.QtWidgets import QDialog

from .ui.update_dialog import Ui_UpdateDialog


class UpdateDialog(QDialog, Ui_UpdateDialog):
    def __init__(self, url):
        super().__init__()
        self.url = url
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.openUpdateUrl)

    def openUpdateUrl(self):
        webbrowser.open(self.url)
