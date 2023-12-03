import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget


class SimplePlanner(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("Form")
        self.resize(754, 498)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.timeEdit = QtWidgets.QTimeEdit(self)
        self.timeEdit.setObjectName("timeEdit")
        self.verticalLayout.addWidget(self.timeEdit)
        self.calendarWidget = QtWidgets.QCalendarWidget(self)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout.addWidget(self.calendarWidget)
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.addEventBtn = QtWidgets.QPushButton(self)
        self.addEventBtn.setObjectName("addEventBtn")
        self.verticalLayout.addWidget(self.addEventBtn)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.eventList = QtWidgets.QListWidget(self)
        self.eventList.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.eventList)
        self.time_list = []
        self.data_list = {}
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.addEventBtn.clicked.connect(self.answer)

    def answer(self):
        time = self.timeEdit.time().toString("hh:mm:ss")
        date = self.calendarWidget.selectedDate().toString("yyyy-MM-dd")
        self.time_list.append(f"{date} {time}")
        self.time_list = sorted(self.time_list)
        self.data_list[f"{date} {time}"] = f"{self.lineEdit.text()}"
        self.eventList.clear()
        for i in range(len(self.time_list)):
            self.eventList.addItem(f"{self.time_list[i]} - {self.data_list[self.time_list[i]]}")

    def retranslateUi(self):
        self.setWindowTitle("Минипланировщик")
        self.addEventBtn.setText("Добавить событие")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = SimplePlanner()
    ex.show()
    sys.exit(app.exec())
