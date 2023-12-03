import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QLabel

SCREEN_SIZE = [400, 400]


class MyPillow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("Form")
        self.resize(400, 300)
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(10, 40, 82, 120))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.channelButtons = QtWidgets.QButtonGroup(self)
        self.channelButtons.setObjectName("channelButtons")
        self.channelButtons.addButton(self.pushButton)
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.channelButtons.addButton(self.pushButton_2)
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.channelButtons.addButton(self.pushButton_3)
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.channelButtons.addButton(self.pushButton_4)
        self.verticalLayout.addWidget(self.pushButton_4)
        self.widget1 = QtWidgets.QWidget(self)
        self.widget1.setGeometry(QtCore.QRect(20, 220, 339, 27))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_5.setObjectName("pushButton_5")
        self.rotateButtons = QtWidgets.QButtonGroup(self)
        self.rotateButtons.setObjectName("rotateButtons")
        self.rotateButtons.addButton(self.pushButton_5)
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_6.setObjectName("pushButton_6")
        self.rotateButtons.addButton(self.pushButton_6)
        self.horizontalLayout.addWidget(self.pushButton_6)
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите изображение", "", "Изображения (*.png *.jpg *.bmp)")
        self.curr_image = QImage(file_path)
        self.curr_image.


        self.pushButton.clicked.connect(lambda: self.change_channel(0))
        self.pushButton_2.clicked.connect(lambda: self.change_channel(1))
        self.pushButton_3.clicked.connect(lambda: self.change_channel(2))
        self.pushButton_5.clicked.connect(lambda: self.rotate_image(-90))
        self.pushButton_6.clicked.connect(lambda: self.rotate_image(90))
        self.retranslateUi()


    def change_channel(self, id):
        pass

    def rotate_image(self, id):
        pass

    def retranslateUi(self):
        self.setWindowTitle("Form")
        self.pushButton.setText("R")
        self.pushButton_2.setText("G")
        self.pushButton_3.setText("B")
        self.pushButton_4.setText("ALL")
        self.pushButton_5.setText("Против часовой стрелки")
        self.pushButton_6.setText("По часовой стрелки")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyPillow()
    ex.show()
    sys.exit(app.exec())
