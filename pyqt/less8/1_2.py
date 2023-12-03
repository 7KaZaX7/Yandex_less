from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QButtonGroup, QFileDialog
from PyQt5.QtGui import QImage, QPixmap
import sys
from PIL import Image

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(502, 442)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.alpha = QtWidgets.QSlider(self.centralwidget)
        self.alpha.setGeometry(QtCore.QRect(0, 0, 71, 381))
        self.alpha.setOrientation(QtCore.Qt.Vertical)
        self.alpha.setObjectName("alpha")
        self.alpha.maximum = 255
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 50, 300, 300))
        self.label.setText("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 502, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))



class AlphaManagement(QMainWindow, Ui_MainWindow):
    curr_image = QImage()
    def init(self):
        super().init()
        self.setupUi(self)
        channelButtons = QButtonGroup()
        

        self.fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        self.curr_image.load(self.fname)
        self.pixmap = QPixmap.fromImage(self.curr_image)
        Image.open(self.fname).convert('RGB').save("orig.jpg")
        self.label.setPixmap(self.pixmap)
        self.alpha.valueChanged.connect(self.change_alpha)


    def change_alpha(self):
        tmp = Image.open("orig.jpg").convert('RGB')
        tmp.convert('RGBA')
        tmp.putalpha(int(self.alpha.value()*(255/100)))
        tmp.save("new.png")
        
        self.curr_image.load("new.png")
        self.pixmap = QPixmap.fromImage(self.curr_image)
        self.label.setPixmap(self.pixmap)
        # tmp.show()





if __name__ == 'main':
    app = QApplication(sys.argv)
    ex = AlphaManagement()
    ex.show()
    sys.exit(app.exec_())