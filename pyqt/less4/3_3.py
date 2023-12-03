import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("MyWidget")
        self.resize(300, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 190, 280, 300))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setEnabled(False)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(120, 10, 31, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 50, 31, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 90, 31, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 130, 31, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 104, 176))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_4 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout.addWidget(self.checkBox_4)
        self.checkBox_3 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout.addWidget(self.checkBox_3)
        self.checkBox_2 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.orderButton = QtWidgets.QPushButton(self.widget)
        self.orderButton.setObjectName("orderButton")
        self.verticalLayout_2.addWidget(self.orderButton)
        self.setCentralWidget(self.centralwidget)

        self.checkboxs = [
            self.checkBox,
            self.checkBox_2,
            self.checkBox_3,
            self.checkBox_4,
        ]
        self.inputs = [self.lineEdit, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4]

        self.checkboxs[0].toggled.connect(lambda: self.order4())
        self.checkboxs[1].toggled.connect(lambda: self.order3())
        self.checkboxs[2].toggled.connect(lambda: self.order2())
        self.checkboxs[3].toggled.connect(lambda: self.order1())

        self.orderButton.clicked.connect(self.money_order)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle("MainWindow")
        self.checkBox_4.setText("Чизбургер")
        self.checkBox_3.setText("Гамбургер")
        self.checkBox_2.setText("Кока-кола")
        self.checkBox.setText("Нагетсы")
        self.orderButton.setText("PushButton")

    def order1(self):
        if self.checkBox_4.isChecked():
            self.inputs[0].setEnabled(True)
            self.inputs[0].setText("1")
        else:
            self.inputs[0].clear()
            self.inputs[0].setEnabled(False)

    def order2(self):
        if self.checkBox_3.isChecked():
            self.inputs[1].setEnabled(True)
            self.inputs[1].setText("1")
        else:
            self.inputs[1].clear()
            self.inputs[1].setEnabled(False)

    def order3(self):
        if self.checkBox_2.isChecked():
            self.inputs[2].setEnabled(True)
            self.inputs[2].setText("1")
        else:
            self.inputs[2].clear()
            self.inputs[2].setEnabled(False)

    def order4(self):
        if self.checkBox.isChecked():
            self.inputs[3].setEnabled(True)
            self.inputs[3].setText("1")
        else:
            self.inputs[3].clear()
            self.inputs[3].setEnabled(False)

    def money_order(self):
        summa = 0
        self.plainTextEdit.clear()
        self.plainTextEdit.insertPlainText("Ваш заказ:\n\n")
        if self.checkBox_4.checkState():
            self.plainTextEdit.insertPlainText(
                f"Чизбургер{'-' * 5}{self.inputs[0].text()}{'-' * 5}{int(self.lineEdit.text()) * 10}\n"
            )
            summa += int(self.inputs[0].text()) * 10
        if self.checkBox_3.checkState():
            self.plainTextEdit.insertPlainText(
                f"Гамбургер{'-' * 5}{self.inputs[1].text()}{'-' * 5}{int(self.lineEdit_2.text()) * 20}\n"
            )
            summa += int(self.inputs[1].text()) * 20
        
        if self.checkBox_2.checkState():
            self.plainTextEdit.insertPlainText(
                f"Кока-кола{'-' * 5}{self.inputs[2].text()}{'-' * 5}{int(self.lineEdit_3.text()) * 40}\n"
            )
            summa += int(self.inputs[2].text()) * 40
        if self.checkBox.checkState():
            self.plainTextEdit.insertPlainText(
                f"Нагетсы{'-' * 5}{self.inputs[3].text()}{'-' * 5}{int(self.lineEdit_4.text()) * 15}\n"
            )
            summa += int(self.inputs[3].text()) * 15
        self.plainTextEdit.insertPlainText(f"\nИтого: {summa}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
