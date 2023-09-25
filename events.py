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
        self.label = QLabel()
        self.line = QLineEdit(self)
        self.line.textChanged.connect(self.label.setText)
      
        # Spin Box and QHBoxLayout
        self.spinbox = QSpinBox(self)
        self.spinbox.valueChanged.connect(self.price_change)  # When User will scroll up price will change for price_change function

    
        # Q Push Button with event                   
        self.btn = QPushButton('My Data', sel
        self.btn.clicked.connect(self.create_message)   


        def mouseMoveEvent(self, e):
          if e.button == Qt.MouseButton.RightButton:
            self.label.setText("mouseMoveEvent  ###############")

        def mousePressEvent(self, e):
          if e.button() == Qt.MouseButton.LeftButton:
              self.label.setText("mousePressEvent LEFT ..............")
  
          elif e.button() == Qt.MouseButton.MiddleButton:
              self.label.setText("mousePressEvent MIDDLE .........")
  
          elif e.button() == Qt.MouseButton.RightButton:
              self.label.setText("mousePressEvent RIGHT ...............")
  
  
        def mouseReleaseEvent(self, e):
          if e.button() == Qt.MouseButton.LeftButton:
              self.label.setText("mouseReleaseEvent LEFT>>>>>>>>>>>>>>>>>>>")
  
          elif e.button() == Qt.MouseButton.MiddleButton:
              self.label.setText("mouseReleaseEvent MIDDLE>>>>>>>>>>>>>")
  
          elif e.button() == Qt.MouseButton.RightButton:
              self.label.setText("mouseReleaseEvent RIGHT>>>>>>>>>>>>>>")
  
  
        def mouseDoubleClickEvent(self, e):
            if e.button() == Qt.MouseButton.LeftButton:
                self.label.setText("mouseDoubleClickEvent LEFT<<<<<<<<<<<<<<<<<<<<<<<<")
    
            elif e.button() == Qt.MouseButton.MiddleButton:
                self.label.setText("mouseDoubleClickEvent MIDDLE<<<<<<<<<<<<<<<<<<<<<<")
    
            elif e.button() == Qt.MouseButton.RightButton:
                self.label.setText("mouseDoubleClickEvent RIGHT<<<<<<<<<<<<<<<<<")


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
