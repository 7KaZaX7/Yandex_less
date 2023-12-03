import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit
from PyQt5.QtWidgets import QMainWindow


class WordTrick(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 70)
        self.setWindowTitle("Фокус со словами")

        self.trick_button = QPushButton("->", self)
        self.trick_button.resize(100, 50)
        self.trick_button.move(120, 10)

        self.first_value = QLineEdit(self)
        self.first_value.setText("Фокус")
        self.first_value.resize(100, 50)
        self.first_value.move(10, 10)

        self.second_value = QLineEdit(self)
        self.second_value.setText("")
        self.second_value.resize(100, 50)
        self.second_value.move(230, 10)

        self.trick_button.clicked.connect(self.open_second_form)

    def open_second_form(self):
        if self.trick_button.text() == "->":
            self.trick_button.setText("<-")
            self.second_value.setText("Фокус")
            self.first_value.clear()

        else:
            self.trick_button.setText("->")
            self.second_value.clear()
            self.first_value.setText("Фокус")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = WordTrick()
    ex.show()
    sys.exit(app.exec())
