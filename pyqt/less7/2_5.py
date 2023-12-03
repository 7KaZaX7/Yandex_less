import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget


class Notebook(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("Form")
        self.resize(400, 300)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.filename_edit = QtWidgets.QLineEdit(self)
        self.filename_edit.setObjectName("filename_edit")
        self.verticalLayout.addWidget(self.filename_edit)
        self.new_button = QtWidgets.QPushButton(self)
        self.new_button.setObjectName("new_button")
        self.verticalLayout.addWidget(self.new_button)
        self.save_button = QtWidgets.QPushButton(self)
        self.save_button.setObjectName("save_button")
        self.verticalLayout.addWidget(self.save_button)
        self.open_button = QtWidgets.QPushButton(self)
        self.open_button.setObjectName("open_button")
        self.verticalLayout.addWidget(self.open_button)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.text_edit = QtWidgets.QPlainTextEdit(self)
        self.text_edit.setObjectName("text_edit")
        self.horizontalLayout.addWidget(self.text_edit)

        self.retranslateUi()
        self.new_button.clicked.connect(self.create_file)
        self.save_button.clicked.connect(self.save_file)
        self.open_button.clicked.connect(self.open_file)

    def create_file(self):
        try:
            name = self.filename_edit.text()
            self.filename_edit.clear()
            self.text_edit.clear()
            file = open(name, "x")
            file.close()
        except FileExistsError:
            pass

    def save_file(self):
        try:
            file = open(self.filename_edit.text(), "w")
            print(self.text_edit.toPlainText().strip(), file=file)
            file.close()
        except FileNotFoundError:
            pass

    def open_file(self):
        try:
            file = open(self.filename_edit.text())
            text = "".join(file)
            self.text_edit.setPlainText(text)
            file.close()
        except FileNotFoundError:
            pass

    def retranslateUi(self):
        self.setWindowTitle("Текстовый редактор")
        self.new_button.setText("Создать новый")
        self.save_button.setText("Сохранить файл")
        self.open_button.setText("Открыть файл")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Notebook()
    ex.show()
    sys.exit(app.exec())
