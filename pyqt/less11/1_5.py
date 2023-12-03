import sys
import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QApplication, QWidget


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setObjectName("Form")
        self.resize(457, 221)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.parameterSelection = QtWidgets.QComboBox(self)
        self.parameterSelection.setObjectName("parameterSelection")
        self.parameterSelection.addItem("")
        self.parameterSelection.addItem("")
        self.parameterSelection.addItem("")
        self.horizontalLayout.addWidget(self.parameterSelection)
        self.queryLine = QtWidgets.QLineEdit(self)
        self.queryLine.setObjectName("queryLine")
        self.horizontalLayout.addWidget(self.queryLine)
        self.queryButton = QtWidgets.QPushButton(self)
        self.queryButton.setObjectName("queryButton")
        self.horizontalLayout.addWidget(self.queryButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.idEdit = QtWidgets.QLineEdit(self)
        self.idEdit.setObjectName("idEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.idEdit)
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.titleEdit = QtWidgets.QLineEdit(self)
        self.titleEdit.setObjectName("titleEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.titleEdit)
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.yearEdit = QtWidgets.QLineEdit(self)
        self.yearEdit.setObjectName("yearEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.yearEdit)
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.genreEdit = QtWidgets.QLineEdit(self)
        self.genreEdit.setObjectName("genreEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.genreEdit)
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.durationEdit = QtWidgets.QLineEdit(self)
        self.durationEdit.setObjectName("durationEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.durationEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.errorLabel = QtWidgets.QLabel(self)
        self.errorLabel.setText("")
        self.errorLabel.setObjectName("errorLabel")
        self.verticalLayout.addWidget(self.errorLabel)

        self.retranslateUi()
        self.queryButton.clicked.connect(self.film_stat)
        
    def film_stat(self):
        option = ''
        if self.parameterSelection.currentText() == "Год выпуска":
            option = 'year'
        elif self.parameterSelection.currentText() == "Название":
            option = 'title'
        else:
            option = 'duration'
        name = str(self.queryLine.text())
        if name == '':
            self.errorLabel.setText('Неправильный запрос')
            self.idEdit.clear()
            self.titleEdit.clear()
            self.yearEdit.clear()
            self.genreEdit.clear()
            self.durationEdit.clear()
            return
        name_db = 'films_db.sqlite'
        con = sqlite3.connect(name_db)
        cur = con.cursor()
        result = cur.execute("SELECT * FROM films WHERE {opt} = '{key}'".format(key=name, opt=option)).fetchall()
        try:
            self.idEdit.setText(str(result[0][0]))
            self.titleEdit.setText(str(result[0][1]))
            self.yearEdit.setText(str(result[0][2]))
            self.genreEdit.setText(str(result[0][3]))
            self.durationEdit.setText(str(result[0][4]))
            self.errorLabel.clear()
        except Exception:
            self.errorLabel.setText('Ничего не найдено')
        con.close()

    def retranslateUi(self):
        self.setWindowTitle("Form")
        self.parameterSelection.setItemText(0, "Год выпуска")
        self.parameterSelection.setItemText(1, "Название")
        self.parameterSelection.setItemText(2, "Продолжительность")
        self.queryButton.setText("Поиск")
        self.label.setText("ID:")
        self.label_2.setText("Name:")
        self.label_4.setText("Year:")
        self.label_3.setText("Genre:")
        self.label_5.setText("Duration:")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())