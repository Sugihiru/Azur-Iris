import sys

from PySide2 import QtWidgets

import app
from ui.mainwindow import MainWindow


def main():
    try:
        app.check_and_update_data()
    except Exception:
        pass

    qapp = QtWidgets.QApplication(sys.argv)
    mw = MainWindow()

    mw.showMaximized()
    ret = qapp.exec_()
    mw.user_data.save()
    sys.exit(ret)


if __name__ == '__main__':
    main()
