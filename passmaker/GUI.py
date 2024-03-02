from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow, QRadioButton, QSlider, QLabel, QButtonGroup
from PyQt6.QtCore import Qt
import sys
from funcs import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #main
        self.setWindowTitle("PassMaker")
        #self.setWindowIcon(QIcon('./assets/KitovLogo.gif'))
        self.setGeometry(25, 50, 300, 400)

        ###Radio buttons
        self.rbtn_group_title = QLabel(self)
        self.rbtn_group_title.resize(200, 20)
        self.rbtn_group_title.move(20, 10)
        self.rbtn_group_title.setText('Password strength and length:')
       
        self.lc_rbtn = QRadioButton('Lower Case', self)
        self.lc_rbtn.setProperty("class", "rbtn")
        self.lc_rbtn.move(20, 30)
        self.lc_rbtn.setChecked(True)

        self.uc_rbtn = QRadioButton('Upper Case', self)
        self.uc_rbtn.setProperty("class", "rbtn")
        self.uc_rbtn.move(20, 50)
     

        self.num_rbtn = QRadioButton('Numbers', self)
        self.num_rbtn.setProperty("class", "rbtn")
        self.num_rbtn.move(20, 70)
 

        self.sym_rbtn = QRadioButton('Symbols', self)
        self.sym_rbtn.setProperty("class", "rbtn")
        self.sym_rbtn.move(20, 90)
  

        ###Radio button groups
        self.btn_group = QButtonGroup(self)
        self.btn_group.setExclusive(False)
        self.btn_group.addButton(self.uc_rbtn)
        self.btn_group.addButton(self.lc_rbtn)
        self.btn_group.addButton(self.num_rbtn)
        self.btn_group.addButton(self.sym_rbtn)

        self.len_slider = QSlider(Qt.Orientation.Horizontal, self)
        self.len_slider.setGeometry(50, 140, 200, 30)
        self.len_slider.setRange(6,20)
        self.len_slider.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.len_slider.setTickInterval(1)
        self.len_slider.valueChanged[int].connect(self.changeValue)

        self.password_label = QLabel(self)
        self.password_label.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)
        self.password_label.move(100, 160)
        self.password_label.setText('Password Length')
        
        self.password_length_label = QLabel(self)
        self.password_length_label.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)
        self.password_length_label.move(100, 180)
        self.password_length_label.setText('6')

        #Create 
        self.update_btn = QPushButton('Create', self)
        self.update_btn.resize(100, 40)
        self.update_btn.move(100, 240)
        self.update_btn.setProperty("class", "btn")
        self.update_btn.clicked.connect(self.click)

        #Output
        self.password_label= QLabel(self)
        self.password_label.resize(280, 50)
        self.password_label.move(10, 310)
        self.password_label.setProperty("class", "label")
        font = self.password_label.font()
        font.setPointSize(18)
        self.password_label.setFont(font)
        self.password_label.setAlignment(
        Qt.AlignmentFlag.AlignHCenter
        | Qt.AlignmentFlag.AlignVCenter
        )
        self.password_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

    def click(self):
        pass_contains = []
       
        if self.lc_rbtn.isChecked():
           pass_contains.append('lc')
        if self.uc_rbtn.isChecked():
           pass_contains.append('uc')
        if self.num_rbtn.isChecked():
           pass_contains.append('num')
        if self.sym_rbtn.isChecked():
           pass_contains.append('sym')
           
        len = self.password_length_label.text()
        pass_contains.append(len)
        pw = create_pw_diff(pass_contains)
        self.password_label.setText(pw)

    def changeValue(self, value):
        self.password_length_label.setText(str(value))

    
    
app = QApplication(sys.argv)
mw = MainWindow()
mw.setProperty("class", "bg")
mw.setStyleSheet("""
    .btn {
        border-radius: 8;
        background-color: #70B746;
        color : white;
        font-size: 20px;
    }
    .btn:hover {
        background-color: #9CC385;
    }
    .bg {
        background-color: whitesmoke;
    } 
    .label {
        border-style: solid;
        border-width: 2;
        border-color: #70B746;
        border-radius: 8;
    }                       
    """)
mw.show()
sys.exit(app.exec())

