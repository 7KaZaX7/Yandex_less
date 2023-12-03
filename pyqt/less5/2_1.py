import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication


class MyNotes(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setObjectName("Form")
        self.resize(420, 441)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.contactName = QtWidgets.QLineEdit(self)
        self.contactName.setObjectName("contactName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.contactName)
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.contactNumber = QtWidgets.QLineEdit(self)
        self.contactNumber.setObjectName("contactNumber")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.contactNumber)
        self.horizontalLayout.addLayout(self.formLayout)
        self.addContactBtn = QtWidgets.QPushButton(self)
        self.addContactBtn.setObjectName("addContactBtn")
        self.horizontalLayout.addWidget(self.addContactBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.listWidget = QtWidgets.QListWidget(self)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.addContactBtn.clicked.connect(self.answer)

    def answer(self):
        self.listWidget.addItem(f"{self.contactName.text()} {self.contactNumber.text()}")

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle("Записная книжка")
        self.label.setText("Имя")
        self.label_2.setText("Телефон")
        self.addContactBtn.setText("Добавить")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyNotes()
    ex.show()
    sys.exit(app.exec())
