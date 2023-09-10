from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6 import uic
import sys

# QLabel
label = QLabel('Hi 1', self)
# label.setText('Hi')
# label.setNum(15)
# label.move(100, 100)
label.setStyleSheet('color:blue')
# label.clear()

pixmap = QPixmap('py.png')
label.setPixmap(pixmap)

# QLineEdit 
line = QLineEdit(self)  # self or Window
line.setText('Hi 2')
line.setPlaceholderText("Hi")
line.setEnabled(True)
line.setEchoMode(QLineEdit.EchoMode.Password)



