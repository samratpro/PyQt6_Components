"""
QSpinBox (Spin Box):
valueChanged

QDateEdit (Date Edit):
dateChanged

QTimeEdit (Time Edit):
timeChanged

QDateTimeEdit (Date and Time Edit):
dateTimeChanged

QSlider (Slider):
valueChanged

QScrollBar (Scroll Bar):
valueChanged

QFileDialog (File Dialog):
Signals like fileSelected and filesSelected are generated when files are selected in the file dialog.

QColorDialog (Color Dialog):
colorSelected

QFontDialog (Font Dialog):
fontSelected

QInputDialog (Input Dialog):
intValueChanged, doubleValueChanged, intValueSelected, doubleValueSelected

valueChanged: Generated when the value of the dial changes.
QTextEdit (Text Edit):

"""



from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6 import uic
import sys
from PyQt6.QtCore import Qt


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
        self.line.editingFinished.connect(self.on_editing_finished)
      
        # Spin Box and QHBoxLayout
        self.spinbox = QSpinBox(self)
        self.spinbox.valueChanged.connect(self.price_change)  # When User will scroll up price will change for price_change function

    
        # Q Push Button with event                   
        self.btn = QPushButton('My Data', sel
        self.btn.clicked.connect(self.create_message)   

        # Radio Button               
        self.radio_button = QRadioButton('Option 1')
        self.radio_button.toggled.connect(self.on_radio_toggled)


        # *************** QTextEdit ********************
        layout = QVBoxLayout()
        self.text_edit = QTextEdit()
        self.text_edit.textChanged.connect(self.on_text_changed)
        self.text_edit.cursorPositionChanged.connect(self.on_cursor_position_changed)
        self.text_edit.copyAvailable.connect(self.on_copy_available)
        self.text_edit.redoAvailable.connect(self.on_redo_available)
        self.text_edit.undoAvailable.connect(self.on_undo_available)
        layout.addWidget(self.text_edit)
        self.setLayout(layout)


        # ******************** QCheckBox ********************
        layout = QVBoxLayout()
        self.checkbox = QCheckBox('Check me')
        self.checkbox.stateChanged.connect(self.on_checkbox_state_changed)
        layout.addWidget(self.checkbox)
        self.setLayout(layout)

        # *********** Combobox ******************
        layout = QVBoxLayout()
        self.combo_box = QComboBox()
        self.combo_box.addItem('Option 1')
        self.combo_box.addItem('Option 2')
        self.combo_box.activated.connect(self.on_activated)
        self.combo_box.currentIndexChanged.connect(self.on_current_index_changed)
        layout.addWidget(self.combo_box)
        self.setLayout(layout)

        # ***************** Q List *********************
        layout = QVBoxLayout()
        self.list_widget = QListWidget()
        self.list_widget.addItem('Item 1')
        self.list_widget.addItem('Item 2')
        self.list_widget.itemClicked.connect(self.on_item_clicked)
        self.list_widget.itemDoubleClicked.connect(self.on_item_double_clicked)
        self.list_widget.itemSelectionChanged.connect(self.on_item_selection_changed)
        layout.addWidget(self.list_widget)
        self.setLayout(layout)

        # **************** Table ******************
        layout = QVBoxLayout()
        self.table_widget = QTableWidget()
        self.table_widget.setRowCount(1)
        self.table_widget.setColumnCount(1)
        self.table_widget.setItem(0, 0, QTableWidgetItem('Row 1, Col 1'))
        self.table_widget.cellClicked.connect(self.on_cell_clicked)
        self.table_widget.cellDoubleClicked.connect(self.on_cell_double_clicked)
        self.table_widget.itemSelectionChanged.connect(self.on_item_selection_changed)
        layout.addWidget(self.table_widget)
        self.setLayout(layout)

        # ***************** Q Slider or Progress Bar **********************
        layout = QVBoxLayout()
        self.slider = QSlider()
        self.slider.setOrientation(Qt.Orientation.Horizontal)
        self.slider.sliderMoved.connect(self.on_slider_moved)
        self.slider.sliderPressed.connect(self.on_slider_pressed)
        self.slider.sliderReleased.connect(self.on_slider_released)
        layout.addWidget(self.slider)
        self.setLayout(layout)

    
    # *************** QTextEdit ****************
    def on_text_changed(self): 
        print("Text changed:", self.text_edit.toPlainText())
    def on_cursor_position_changed(self):
        cursor_position = self.text_edit.textCursor().position()
        print("Cursor position:", cursor_position)
    def on_copy_available(self, enable):
        if enable:
            print("Text can be copied to clipboard")
        else:
            print("No text available to copy")
    def on_redo_available(self, enable):
        if enable:
            print("Redo actions are available")
        else:
            print("No redo actions available")
    def on_undo_available(self, enable):
        if enable:
            print("Undo actions are available")
        else:
            print("No undo actions available")

    # ******************** QCheckBox ********************
    def on_checkbox_state_changed(self, state):
        if state == 2:  # Checked state
            print("Check box checked")
        else:
            print("Check box unchecked")

    # *********** Combobox ******************
    def on_activated(self, index):
        selected_item = self.combo_box.itemText(index)
        print(f"Activated: {selected_item}")
    def on_current_index_changed(self, index):
        selected_item = self.combo_box.itemText(index)
        print(f"Current Index Changed: {selected_item}") 
        

    # ***************** Q List *********************
    def on_item_clicked(self, item):
        print(f"Item clicked: {item.text()}")
    def on_item_double_clicked(self, item):
        print(f"Item double-clicked: {item.text()}")
    def on_item_selection_changed(self):
        selected_items = [item.text() for item in self.list_widget.selectedItems()]
        print(f"Selection changed: {selected_items}")
       

   # **************** Table ******************
   def on_cell_clicked(self, row, column):
      item_text = self.table_widget.item(row, column).text()
      print(f"Cell clicked: {item_text}")
   def on_cell_double_clicked(self, row, column):
      item_text = self.table_widget.item(row, column).text()
      print(f"Cell double-clicked: {item_text}")
   def on_item_selection_changed(self):
      selected_items = [item.text() for item in self.table_widget.selectedItems()]
      print(f"Selection changed: {selected_items}")

   # ***************** Q Slider or Progress Bar **********************
   def on_slider_moved(self, value):
        print(f"Slider moved to {value}")
   def on_slider_pressed(self):
        print("Slider pressed")
   def on_slider_released(self):
        print("Slider released")

     
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
