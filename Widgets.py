from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6 import uic
import sys


class Window(QWidget):  # QWidget....................
    def __init__(self):
        super().__init__()
        self.setGeometry(220, 220, 700, 400)

        # Working with label
        label = QLabel('Hi 1', self)
        label.setText('Hi')
        label.setNum(15)
        label.move(100, 100)
        label.setStyleSheet('color:blue')
        label.clear()
        pixmap = QPixmap('py.png')
        label.setPixmap(pixmap)
        movie = QMovie('py.gif')
        label.setMovie(movie)
        movie.start()


        # QLineEdit 
        line = QLineEdit(self)  # self or Window
        line.setText('Hi 2')
        line.setPlaceholderText("Hi")
        line.setEnabled(True)
        line.setEchoMode(QLineEdit.EchoMode.Password)

        


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())



