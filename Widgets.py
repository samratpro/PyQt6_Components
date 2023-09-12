from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6 import uic
import sys


class Window(QWidget):  # QWidget....................
    def __init__(self):
        super().__init__()
        self.setGeometry(220, 220, 700, 400)
        self.setWindowTitle('Hello App')
        self.setWindowIcon(QIcon("py.png"))

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


        # Spin Box
        HBox = QHBoxLayout(self)
        self.label = QLabel('Price : ')
        self.spinbox = QSpinBox(self)
        self.spinbox.valueChanged.connect(self.price_change)  # When User will scroll up price will change
        self.line = QLineEdit(self)
        self.line.setFixedWidth(300)
        HBox.addWidget(self.label)
        HBox.addWidget(self.spinbox)
        HBox.addWidget(self.line)
        self.setLayout(HBox)

    def price_change(self):
        spin_data = self.spinbox.value()
        self.line.setText(str(spin_data * 500))  # Must be pass as string


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())



