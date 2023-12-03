import sys

from PyQt5.QtWidgets import QApplication, QLineEdit, QCheckBox
from PyQt5.QtWidgets import QMainWindow


class WidgetsHideNSeek(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 1000, 500)
        self.setWindowTitle("Прятки для виджетов")

        self.edit1, self.edit2, self.edit3, self.edit4 = (
            QLineEdit(self),
            QLineEdit(self),
            QLineEdit(self),
            QLineEdit(self),
        )
        self.checkbox1, self.checkbox2, self.checkbox3, self.checkbox4 = (
            QCheckBox(self),
            QCheckBox(self),
            QCheckBox(self),
            QCheckBox(self),
        )
        self.checkbox1.move(10, 10)
        self.checkbox1.setText("edit1")
        self.checkbox1.toggle()
        self.checkbox2.move(10, 60)
        self.checkbox2.setText("edit2")
        self.checkbox2.toggle()
        self.checkbox3.move(10, 110)
        self.checkbox3.setText("edit3")
        self.checkbox3.toggle()
        self.checkbox4.move(10, 160)
        self.checkbox4.setText("edit4")
        self.checkbox4.toggle()

        self.edit1.move(100, 10)
        self.edit1.resize(self.edit1.sizeHint())
        self.edit1.setText("Поле edit1")

        self.edit2.resize(self.edit1.sizeHint())
        self.edit2.move(100, 60)
        self.edit2.setText("Поле edit2")

        self.edit3.move(100, 110)
        self.edit3.resize(self.edit3.sizeHint())
        self.edit3.setText("Поле edit3")

        self.edit4.move(100, 160)
        self.edit4.resize(self.edit4.sizeHint())
        self.edit4.setText("Поле edit4")

        self.checkbox1.toggled.connect(self.one)
        self.checkbox2.toggled.connect(self.two)
        self.checkbox3.toggled.connect(self.three)
        self.checkbox4.toggled.connect(self.four)

    def one(self):
        if self.checkbox1.isChecked():
            self.edit1.show()
        else:
            self.edit1.hide()

    def two(self):
        if self.checkbox2.isChecked():
            self.edit2.show()
        else:
            self.edit2.hide()

    def three(self):
        if self.checkbox3.isChecked():
            self.edit3.show()
        else:
            self.edit3.hide()

    def four(self):
        if self.checkbox4.isChecked():
            self.edit4.show()
        else:
            self.edit4.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = WidgetsHideNSeek()
    ex.show()
    sys.exit(app.exec())
