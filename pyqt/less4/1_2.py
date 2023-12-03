import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit
from PyQt5.QtWidgets import QMainWindow, QLabel


class Evaluator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 450, 100)
        self.setWindowTitle("Фокус со словами")

        self.trick_button = QPushButton("->", self)
        self.trick_button.resize(100, 50)
        self.trick_button.move(170, 50)

        self.first_value = QLineEdit(self)
        self.first_value.setText("")
        self.first_value.resize(150, 50)
        self.first_value.move(10, 50)

        self.second_value = QLineEdit(self)
        self.second_value.setText("")
        self.second_value.resize(150, 50)
        self.second_value.move(280, 50)

        self.one = QLabel(self)
        self.one.setText("Выражение:")
        self.one.resize(self.one.sizeHint())
        self.one.move(10, 10)

        self.two = QLabel(self)
        self.two.setText("Результат:")
        self.two.resize(self.two.sizeHint())
        self.two.move(280, 10)

        self.trick_button.clicked.connect(self.open_second_form)

        self.button = 0

    def open_second_form(self):
        self.second_value.setText(str(eval(self.first_value.text())))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Evaluator()
    ex.show()
    sys.exit(app.exec())
