from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QVBoxLayout, \
    QLineEdit, QPushButton, QMainWindow, QTableWidget, QTableWidgetItem, QDialog, QComboBox, QToolBar, \
    QStatusBar, QMessageBox
from PyQt6.QtGui import QAction, QIcon
import sys
import sqlite3


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Managment System")
        self.setMinimumSize(800, 600)

        # Nav
        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")
        edit_menu_item = self.menuBar().addMenu("&Search")

        add_student_action = QAction(
            QIcon("icons/add.png"), "Add Student", self)
        add_student_action.triggered.connect(self.insert)
        file_menu_item.addAction(add_student_action)

        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)
        about_action.triggered.connect(self.about_msg)

        search_action = QAction(QIcon("icons/search.png"), "Search", self)
        edit_menu_item.addAction(search_action)
        search_action.triggered.connect(self.search)

        # main table
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(
            ("ID", "NAME", "COURSE", "MOBILE"))
        # hide vertical column labels as we import them from the db
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

        # toolbar
        toolbar = QToolBar()
        toolbar.setMovable(True)
        self.addToolBar(toolbar)
        toolbar.addAction(add_student_action)
        toolbar.addAction(search_action)

        # statusbar and elements
        self.sbar = QStatusBar()
        self.setStatusBar(self.sbar)
        # capture a cell that was clikced in the table
        self.table.cellClicked.connect(self.cell_clicked)
        
    def about_msg(self):
        dialog = AboutDialog()
        dialog.exec()
        

    def cell_clicked(self):
        edit_btn = QPushButton("Edit Record")
        edit_btn.clicked.connect(self.edit)
        del_btn = QPushButton("Delete Record")
        del_btn.clicked.connect(self.delete)

        children = self.findChildren(QPushButton)
        if children:
            for child in children:
                self.sbar.removeWidget(child)

        self.sbar.addWidget(edit_btn)
        self.sbar.addWidget(del_btn)

    def edit(self):
        dialog = EditDialog()
        dialog.exec()

    def delete(self):
        dialog = DeleteDialog()
        dialog.exec()

    def load_data(self):
        con = DBConnebtion().connect()
        result = con.execute("SELECT * FROM students")
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number,
                                   QTableWidgetItem(str(data)))
        con.close()

    def insert(self):
        dialog = InsertDialog()
        dialog.exec()

    def search(self):
        dialog = SearchDialog()
        dialog.exec()


class EditDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Edit")
        self.setFixedSize(300, 300)

        layout = QVBoxLayout()

        index = sma.table.currentRow()
        self.student_id = sma.table.item(index, 0).text()
        student_name = sma.table.item(index, 1).text()
        student_course = sma.table.item(index, 2).text()
        student_mobile = sma.table.item(index, 3).text()

        self.student_name = QLineEdit(student_name)
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        self.course_name = QComboBox()
        courses = ["Biology", "Math", "Astronomy", "Physics"]
        self.course_name.addItems(courses)
        self.course_name.setCurrentText(student_course)
        layout.addWidget(self.course_name)

        self.mobile = QLineEdit(student_mobile)
        self.mobile.setPlaceholderText("Mobile")
        layout.addWidget(self.mobile)

        button = QPushButton("Update")
        button.clicked.connect(self.update_student)
        layout.addWidget(button)

        self.setLayout(layout)

    def update_student(self):
        con = DBConnebtion().connect()
        cursor = con.cursor()
        cursor.execute("UPDATE students SET name = ?, course = ?, mobile = ? WHERE id = ?",
                       (self.student_name.text(),
                        self.course_name.itemText(
                            self.course_name.currentIndex()),
                        self.mobile.text(),
                        self.student_id))
        con.commit()
        cursor.close()
        con.close()
        sma.load_data()


class DeleteDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Delete")

        layout = QGridLayout()

        # confirmation message
        confirmation = QLabel("Are you sure you want to delete?")
        yes = QPushButton("Yes")
        no = QPushButton("No")
        layout.addWidget(confirmation, 0, 0, 1, 2)
        layout.addWidget(yes, 1, 0)
        layout.addWidget(no, 1, 1)
        self.setLayout(layout)

        yes.clicked.connect(self.delete_record)
        no.clicked.connect(self.close_me)
        
    def close_me(self):
        self.close()

    def delete_record(self):
        index = sma.table.currentRow()
        student_id = sma.table.item(index, 0).text()
        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        con.commit()
        cursor.close()
        con.close()
        sma.load_data()
        
        self.close()
        confirmation_message = QMessageBox()
        confirmation_message.setWindowTitle("Success")
        confirmation_message.setText("Record was deleted!")
        confirmation_message.exec()


class SearchDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search for a student")
        self.setFixedSize(300, 300)

        layout = QVBoxLayout()

        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        button = QPushButton("Search")
        button.clicked.connect(self.search_for_student)
        layout.addWidget(button)

        self.setLayout(layout)

    def search_for_student(self):
        name = self.student_name.text()
        con = DBConnebtion().connect()
        cursor = con.cursor()
        result = cursor.execute("SELECT * FROM students WHERE name = ?",
                                (name,))
        rows = list(result)
        items = sma.table.findItems(name, Qt.MatchFlag.MatchFixedString)
        for item in items:
            sma.table.item(item.row(), 1).setSelected(True)
        cursor.close()
        con.close()


class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insert new student")
        self.setFixedSize(300, 300)

        layout = QVBoxLayout()

        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        self.course_name = QComboBox()
        courses = ["Biology", "Math", "Astronomy", "Physics"]
        self.course_name.addItems(courses)
        layout.addWidget(self.course_name)

        self.mobile = QLineEdit()
        self.mobile.setPlaceholderText("Mobile")
        layout.addWidget(self.mobile)

        button = QPushButton("Register")
        button.clicked.connect(self.add_student)
        layout.addWidget(button)

        self.setLayout(layout)

    def add_student(self):
        name = self.student_name.text()
        course = self.course_name.itemText(self.course_name.currentIndex())
        mobile = self.mobile.text()
        con = DBConnebtion().connect()
        cursor = con.cursor()
        cursor.execute("Insert INTO students (name, course, mobile) VALUES (?, ?, ?)",
                       (name, course, mobile))
        con.commit()
        cursor.close()
        con.close()
        sma.load_data()

class AboutDialog(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About")
        content = """
        Created by Nati Roth
        Feel free to modify and reuse this app
        """
        self.setText(content)
        
        
class DBConnebtion():
    def __init__(self, db_file = "database.db"):
        self.db_file = db_file
        
    def connect(self):
        con = sqlite3.connect(self.db_file)
        return con
        
    
         
app = QApplication(sys.argv)
sma = MainWindow()
sma.show()
sma.load_data()
sys.exit(app.exec())
