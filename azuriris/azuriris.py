import sys

from PySide2 import QtWidgets

from ui.mainwindow import MainWindow


def main():
    app = QtWidgets.QApplication(sys.argv)
    mw = MainWindow()

    mw.showMaximized()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
