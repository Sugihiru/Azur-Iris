import sys

from PySide2 import QtWidgets

from ui.mainwindow import MainWindow


def main():
    app = QtWidgets.QApplication(sys.argv)
    mw = MainWindow()

    mw.showMaximized()
    ret = app.exec_()
    mw.user_data.save()
    sys.exit(ret)


if __name__ == '__main__':
    main()
