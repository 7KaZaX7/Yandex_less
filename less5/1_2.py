
import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class FlagMaker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("MainWindow")
        self.setEnabled(True)
        self.setFixedSize(900, 900)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.make_flag = QtWidgets.QPushButton(self.centralwidget)
        self.make_flag.setGeometry(QtCore.QRect(530, 260, 111, 25))
        self.make_flag.setObjectName("make_flag")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(40, 320, 341, 31))
        self.result.setObjectName("result")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 80, 550, 168))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.color_group_1 = QtWidgets.QLabel(self.layoutWidget)
        self.color_group_1.setObjectName("color_group_1")
        self.verticalLayout.addWidget(self.color_group_1)
        self.radioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.buttonGroup = QtWidgets.QButtonGroup(self)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton)
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.buttonGroup.addButton(self.radioButton_2)
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.buttonGroup.addButton(self.radioButton_3)
        self.verticalLayout.addWidget(self.radioButton_3)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        spacerItem = QtWidgets.QSpacerItem(
            88, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.color_group_2 = QtWidgets.QLabel(self.layoutWidget)
        self.color_group_2.setObjectName("color_group_2")
        self.verticalLayout_5.addWidget(self.color_group_2)
        self.verticalLayout_7.addLayout(self.verticalLayout_5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton_4 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_4.setObjectName("radioButton_4")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(self)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButton_4)
        self.verticalLayout_2.addWidget(self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_5.setObjectName("radioButton_5")
        self.buttonGroup_2.addButton(self.radioButton_5)
        self.verticalLayout_2.addWidget(self.radioButton_5)
        self.radioButton_6 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_6.setObjectName("radioButton_6")
        self.buttonGroup_2.addButton(self.radioButton_6)
        self.verticalLayout_2.addWidget(self.radioButton_6)
        self.verticalLayout_7.addLayout(self.verticalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        spacerItem1 = QtWidgets.QSpacerItem(
            88, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.color_group_3 = QtWidgets.QLabel(self.layoutWidget)
        self.color_group_3.setObjectName("color_group_3")
        self.verticalLayout_6.addWidget(self.color_group_3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radioButton_7 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_7.setObjectName("radioButton_7")
        self.buttonGroup_3 = QtWidgets.QButtonGroup(self)
        self.buttonGroup_3.setObjectName("buttonGroup_3")
        self.buttonGroup_3.addButton(self.radioButton_7)
        self.verticalLayout_3.addWidget(self.radioButton_7)
        self.radioButton_8 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_8.setObjectName("radioButton_8")
        self.buttonGroup_3.addButton(self.radioButton_8)
        self.verticalLayout_3.addWidget(self.radioButton_8)
        self.radioButton_9 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_9.setObjectName("radioButton_9")
        self.buttonGroup_3.addButton(self.radioButton_9)
        self.verticalLayout_3.addWidget(self.radioButton_9)
        self.verticalLayout_6.addLayout(self.verticalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.make_flag.clicked.connect(
            lambda: self.answer(
                [self.buttonGroup, self.buttonGroup_2, self.buttonGroup_3]
            )
        )

    def answer(self, group):
        ans = []
        for i in group:
            i = i.buttons()
            for y in i:
                if y.isChecked():
                    ans.append(y.text())
        self.result.setText(f"Цвета: {ans[0]}, {ans[1]} и {ans[2]}")

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle("Текстовый флаг")
        self.make_flag.setText("Сделать флаг")
        self.result.setText("")
        self.color_group_1.setText("<b>Цвет №1</b>")
        self.radioButton.setText("Синий")
        self.radioButton_2.setText("Красный")
        self.radioButton_3.setText("Зелёный")
        self.color_group_2.setText("<b>Цвет №2</b>")
        self.radioButton_4.setText("Синий")
        self.radioButton_5.setText("Красный")
        self.radioButton_6.setText("Зелёный")
        self.color_group_3.setText("<b>Цвет №3</b>")
        self.radioButton_7.setText("Синий")
        self.radioButton_8.setText("Красный")
        self.radioButton_9.setText("Зелёный")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = FlagMaker()
    ex.show()
    sys.exit(app.exec())
