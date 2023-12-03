import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget


class Pseudonym(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("Form")
        self.resize(512, 364)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.stones = QtWidgets.QSpinBox(self)
        self.stones.setObjectName("stones")
        self.horizontalLayout.addWidget(self.stones)
        self.startButton = QtWidgets.QPushButton(self)
        self.startButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.startButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.remainLcd = QtWidgets.QLCDNumber(self)
        self.remainLcd.setObjectName("remainLcd")
        self.verticalLayout.addWidget(self.remainLcd)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.takeInput = QtWidgets.QLineEdit(self)
        self.takeInput.setObjectName("takeInput")
        self.horizontalLayout_2.addWidget(self.takeInput)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.takeButton = QtWidgets.QPushButton(self)
        self.takeButton.setObjectName("takeButton")
        self.verticalLayout.addWidget(self.takeButton)
        self.listWidget = QtWidgets.QListWidget(self)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.resultLabel = QtWidgets.QLabel(self)
        self.resultLabel.setText("")
        self.resultLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.resultLabel.setObjectName("resultLabel")
        self.verticalLayout.addWidget(self.resultLabel)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.startButton.clicked.connect(self.take)
        self.takeButton.clicked.connect(self.push)

    def take(self):
        self.remainLcd.display(int(self.stones.text()))
        self.listWidget.clear()
        self.resultLabel.clear()

    def push(self):
        num = int(self.takeInput.text())
        self.listWidget.addItem(f"Игрок взял - {num}")
        if self.remainLcd.intValue() - num > 3:
            self.listWidget.addItem(f"Компьютер взял - 1")
            num += 1
        elif 0 < self.remainLcd.intValue() - num <= 3:
            self.listWidget.addItem(f"Компьютер взял - 3")
            self.remainLcd.display(0)
            self.resultLabel.setText(f"<b>Победа компьютера!</b>")
            num = 0
        if num > 0 and self.remainLcd.intValue() - num == 0:
            self.remainLcd.display(0)
            self.resultLabel.setText(f"<b>Победа игрока!</b>")
        else:
            self.remainLcd.display(self.remainLcd.intValue() - num)

    def retranslateUi(self):
        self.setWindowTitle("Псевдоним. Возвращение")
        self.label.setText("Задать количество камней")
        self.startButton.setText("Задать")
        self.label_2.setText("Сколько камней взять?")
        self.takeButton.setText("Взять")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Pseudonym()
    ex.show()
    sys.exit(app.exec())
