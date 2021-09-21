#!/usr/bin/python3
from PyQt5.QtWidgets import QApplication,QSplashScreen
from PyQt5 import QtGui
from PyQt5.QtCore import QSize,Qt

app = QApplication([])
pixmap = QtGui.QPixmap("class-jam/splash.png")
splash = QSplashScreen(pixmap)
splash.show()
app.exec_()
