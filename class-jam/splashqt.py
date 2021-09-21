#!/usr/bin/python3
from PyQt5.QtWidgets import QApplication,QSplashScreen
from PyQt5 import QtGui
from PyQt5.QtCore import QSize,Qt

app = QApplication([])
pixmap = QtGui.QPixmap("/usr/share/class-jam/splash.png")
splash = QSplashScreen(pixmap)
splash.setWindowFlags(Qt.WindowStaysOnTopHint)
splash.setWindowFlags(Qt.FramelessWindowHint)
splash.setWindowFlags(Qt.X11BypassWindowManagerHint)
splash.setAttribute(Qt.WA_TranslucentBackground)
splash.setStyleSheet('background:transparent')
splash.show()
app.exec_()
