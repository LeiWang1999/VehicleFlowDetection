import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from GUI.Ui_Main import UiMain

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = UiMain()
    ui.show()
    sys.exit(app.exec_())
