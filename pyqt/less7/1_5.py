import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class FileStat(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("Файловая статистика")
        self.resize(397, 197)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.filenameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.filenameEdit.setObjectName("filenameEdit")
        self.horizontalLayout.addWidget(self.filenameEdit)
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setObjectName("button")
        self.horizontalLayout.addWidget(self.button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.maxEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.maxEdit.setObjectName("maxEdit")
        self.maxEdit.setText("0")
        self.horizontalLayout_2.addWidget(self.maxEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.minEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.minEdit.setObjectName("minEdit")
        self.minEdit.setText("0")
        self.horizontalLayout_3.addWidget(self.minEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.avgEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.avgEdit.setObjectName("avgEdit")
        self.avgEdit.setText("0,00")
        self.horizontalLayout_4.addWidget(self.avgEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()

        self.button.clicked.connect(self.get_stat)

    def get_stat(self):
        data = []
        try:
            file = open(self.filenameEdit.text())
            if not file.read().split():
                raise AttributeError
            file.close()
            with open(self.filenameEdit.text()) as file:
                for i in file.read().rsplit():
                    data.append(int(i.strip()))
            file.close()
            self.minEdit.setText(str(min(data)))
            self.maxEdit.setText(str(max(data)))
            self.avgEdit.setText(str(round(sum(data) / len(data), 2)))
            file_2 = open("out.txt", "w")
            print(
                self.maxEdit.text() + '\n' +
                self.minEdit.text() + '\n' +
                self.avgEdit.text(),
                file=file_2,
            )
            file_2.close()
        except ValueError:
            self.statusbar.showMessage(
                "В файле'{}' содержатся некорректные данные".format(
                    self.filenameEdit.text()
                )
            )
            self.avgEdit.setText("0,00")
            self.maxEdit.setText("0")
            self.minEdit.setText("0")
            file.close()
        except AttributeError:
            self.statusbar.showMessage("Указанный файл пуст")
            self.avgEdit.setText("0,00")
            self.maxEdit.setText("0")
            self.minEdit.setText("0")
            file.close()
        except FileNotFoundError:
            self.statusbar.showMessage(
                "Файл'{}' не найден".format(self.filenameEdit.text())
            )
            self.avgEdit.setText("0,00")
            self.maxEdit.setText("0")
            self.minEdit.setText("0")

    def retranslateUi(self):
        self.setWindowTitle("Файловая статистика")
        self.label.setText("Имя файла")
        self.button.setText("Рассчитать")
        self.label_2.setText("Максимальное значение:")
        self.label_3.setText("Минимальное значение:")
        self.label_4.setText("Среднее значение:")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = FileStat()
    ex.show()
    sys.exit(app.exec())
