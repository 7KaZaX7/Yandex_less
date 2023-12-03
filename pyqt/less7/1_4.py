import sys
import random

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget


class RandomString(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("Случайная строка")
        self.resize(612, 88)
        self.button = QtWidgets.QPushButton(self)
        self.button.setGeometry(QtCore.QRect(9, 31, 80, 25))
        self.button.setObjectName("button")
        self.text_field = QtWidgets.QTextEdit(self)
        self.text_field.setGeometry(QtCore.QRect(95, 9, 508, 70))
        self.text_field.setObjectName("text_field")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.button.clicked.connect(self.get_string)

    def get_string(self):
        with open("*.txt") as file:
            lines = file.readlines()
        if not lines:
            self.text_field.setText('')
        else:
            self.text_field.setText(random.choice(lines).strip())


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle("Form")
        self.button.setText("Получить")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = RandomString()
    ex.show()
    sys.exit(app.exec())
