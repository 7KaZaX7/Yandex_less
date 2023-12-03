import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget


class Suffle(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("Form")
        self.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.button = QtWidgets.QPushButton(self)
        self.button.setObjectName("button")
        self.verticalLayout.addWidget(self.button)
        self.text_field = QtWidgets.QTextBrowser(self)
        self.text_field.setObjectName("text_field")
        self.verticalLayout.addWidget(self.text_field)

        self.retranslateUi()

        self.button.clicked.connect(self.get_text)

    def get_text(self):
        data = []
        with open('lines.txt') as file:
            for i in file.readlines():
                data.append(i.strip())
        for i in data:
            if data.index(i) % 2 != 0:
                self.text_field.append(i)
        for i in data:
            if data.index(i) % 2 == 0:
                self.text_field.append(i)


    def retranslateUi(self):
        self.setWindowTitle("Перемешивание")
        self.button.setText("Загрузить строки")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Suffle()
    ex.show()
    sys.exit(app.exec())
