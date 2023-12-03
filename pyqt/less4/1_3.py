import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QLCDNumber
from PyQt5.QtWidgets import QMainWindow, QLabel


class MiniCalcularor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 1000, 1000)
        self.setWindowTitle("Миникалькулятор")

        self.calculate_button = QPushButton("->", self)
        self.calculate_button.resize(100, 50)
        self.calculate_button.move(200, 60)

        self.number_1 = QLineEdit(self)
        self.number_1.setText("")
        self.number_1.resize(150, 50)
        self.number_1.move(10, 60)

        self.number_2 = QLineEdit(self)
        self.number_2.setText("")
        self.number_2.resize(150, 50)
        self.number_2.move(10, 170)

        self.one = QLabel(self)
        self.one.setText("Первое число(целое):")
        self.one.resize(self.one.sizeHint())
        self.one.move(10, 10)

        self.two = QLabel(self)
        self.two.setText("Второе число(целое):")
        self.two.resize(self.two.sizeHint())
        self.two.move(10, 120)

        self.sum = QLabel(self)
        self.sum.setText("Сумма:")
        self.sum.resize(self.two.sizeHint())
        self.sum.move(350, 50)

        self.sub = QLabel(self)
        self.sub.setText("Разность:")
        self.sub.resize(self.two.sizeHint())
        self.sub.move(350, 100)

        self.mul = QLabel(self)
        self.mul.setText("Произведение:")
        self.mul.resize(self.two.sizeHint())
        self.mul.move(350, 150)

        self.div = QLabel(self)
        self.div.setText("Частное:")
        self.div.resize(self.two.sizeHint())
        self.div.move(350, 200)

        self.result_sum = QLCDNumber(self)
        self.result_sum.move(580, 50)

        self.result_sub = QLCDNumber(self)
        self.result_sub.move(580, 100)

        self.result_mul = QLCDNumber(self)
        self.result_mul.move(580, 150)

        self.result_div = QLCDNumber(self)
        self.result_div.move(580, 200)

        self.calculate_button.clicked.connect(self.open_second_form)

    def open_second_form(self):
        self.result_sum.display(
            eval(f"{self.number_1.text()} + {self.number_2.text()}")
        )
        self.result_sub.display(
            eval(f"{self.number_1.text()} - {self.number_2.text()}")
        )
        self.result_mul.display(
            eval(f"{self.number_1.text()} * {self.number_2.text()}")
        )
        try:
            num = "%.3f" % float(eval(f"{self.number_1.text()} / {self.number_2.text()}"))
            self.result_div.display(
                num
            )
        except ZeroDivisionError:
            self.result_div.display("Error")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MiniCalcularor()
    ex.show()
    sys.exit(app.exec())