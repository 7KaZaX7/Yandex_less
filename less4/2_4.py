import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QCheckBox, QPlainTextEdit
from PyQt5.QtWidgets import QMainWindow


class MacOrder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 270, 560)
        self.setWindowTitle("Заказ в Макдональдсе")

        self.one = QCheckBox("Чизбургер", self)
        self.two = QCheckBox("Гамбургер", self)
        self.three = QCheckBox("Кока-кола", self)
        self.four = QCheckBox("Нагетсы", self)

        self.one.move(10, 10)
        self.one.resize(self.one.sizeHint())
        self.two.move(10, 60)
        self.two.resize(self.two.sizeHint())
        self.three.move(10, 110)
        self.three.resize(self.three.sizeHint())
        self.four.move(10, 160)
        self.four.resize(self.four.sizeHint())

        self.order_btn = QPushButton("Заказать", self)
        self.order_btn.resize(self.order_btn.sizeHint())
        self.order_btn.move(10, 200)

        self.result = QPlainTextEdit(self)
        self.result.resize(250, 250)
        self.result.move(10, 280)

        self.menu_checkboxes = [self.one, self.two, self.three, self.four]

        self.order_btn.clicked.connect(self.order)

    def order(self):
        self.result.clear()
        self.result.insertPlainText("Ваш заказ:\n\n")
        if self.one.checkState():
            self.result.insertPlainText("Чизбургер\n")
        if self.two.checkState():
            self.result.insertPlainText("Гамбургер\n")
        if self.three.checkState():
            self.result.insertPlainText("Кока-кола\n")
        if self.four.checkState():
            self.result.insertPlainText("Нагетсы\n")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MacOrder()
    ex.show()
    sys.exit(app.exec())
