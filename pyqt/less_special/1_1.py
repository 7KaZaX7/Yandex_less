import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton
import pyqtgraph as pg
import numpy
from math import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Function")
        self.setGeometry(200, 200, 800, 600)

        self.widget = QWidget(self)
        self.setCentralWidget(self.widget)

        self.layout = QVBoxLayout(self.widget)

        self.label = QLabel("Enter function: ", self)
        self.layout.addWidget(self.label)
        self.function = QLineEdit(self)
        self.layout.addWidget(self.function)

        self.range_label = QLabel("Enter range: ", self)
        self.layout.addWidget(self.range_label)
        self.range_edit_min = QLineEdit(self)
        self.layout.addWidget(self.range_edit_min)
        self.range_edit_max = QLineEdit(self)
        self.layout.addWidget(self.range_edit_max)

        self.plot_button = QPushButton("Plot", self)
        self.plot_button.clicked.connect(self.plot_function)
        self.layout.addWidget(self.plot_button)

        self.plot_widget = pg.PlotWidget(self)
        self.layout.addWidget(self.plot_widget)

        self.show()

    def plot_function(self):
        equation = str(self.function.text())
        x_min = float(eval(self.range_edit_min.text()))
        x_max = float(eval(self.range_edit_max.text()))

        x = numpy.linspace(x_min, x_max, 100)
        y = eval(equation)
        self.plot_widget.clear()
        self.plot_widget.plot(x, y, pen=pg.mkPen('g'))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
