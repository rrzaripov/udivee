# -*- coding: utf-8 -*-
import sys
from main_window import MainWindow
from PyQt4 import QtGui


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
