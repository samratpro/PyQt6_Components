# Qt Designer Path
# env\Lib\site-packages\qt6_applications\Qt\bin


# Functional Way
from PyQt6.QtWidgets import *
import sys

app = QApplication(sys.argv)
window = QMainWindow()
window.statusBar().showMessage("Welcome to here")
window.menuBar().addMenu("Open File")

window.setGeometry(0, 0, 700, 300)
window.show()
sys.exit(app.exec())


# Class Base
from PyQt6.QtWidgets import *
import sys
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 700, 400)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
