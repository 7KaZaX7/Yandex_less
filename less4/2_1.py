import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QLabel
from PyQt5.QtWidgets import QMainWindow


class Arifmometr(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 1000, 1000)
        self.setWindowTitle("Арифмометр")

        self.f = QLabel(self)
        self.f.move(300, 10)
        self.f.setText("=")

        self.first_value = QLineEdit('0', self)
        self.first_value.move(10, 10)

        self.second_value = QLineEdit('0', self)
        self.second_value.move(200, 10)

        self.result = QLineEdit('0', self)
        self.result.setEnabled(False)
        self.result.move(310, 10)

        self.add_button, self.substract_button, self.multiply_button = (
            QPushButton(self),
            QPushButton(self),
            QPushButton(self),
        )
        self.add_button.resize(30, 30)
        self.add_button.move(110, 10)
        self.add_button.setText("+")
        self.substract_button.resize(30, 30)
        self.substract_button.move(140, 10)
        self.substract_button.setText("-")
        self.multiply_button.resize(30, 30)
        self.multiply_button.move(170, 10)
        self.multiply_button.setText("*")

        self.add_button.clicked.connect(self.add)
        self.substract_button.clicked.connect(self.sub)
        self.multiply_button.clicked.connect(self.mul)

    def add(self):
        self.result.setText(
            str(eval(f"{self.first_value.text()} + {self.second_value.text()}"))
        )

    def sub(self):
        self.result.setText(
            str(eval(f"{self.first_value.text()} - {self.second_value.text()}"))
        )

    def mul(self):
        self.result.setText(
            str(eval(f"{self.first_value.text()} * {self.second_value.text()}"))
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Arifmometr()
    ex.show()
    sys.exit(app.exec())
