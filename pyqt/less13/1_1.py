import sys

import random

from PyQt5.QtCore import QPointF
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QPolygonF
from PyQt5.QtWidgets import QWidget, QApplication, QLabel


class Suprematism(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(1000, 1000)
        self.setWindowTitle('Координаты')

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)

        shape_type = random.choice(['circle', 'square', 'triangle'])
        size = random.randint(20, 100)
        color = QColor(random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255))

        if shape_type == 'circle':
            painter.setBrush(color)
            painter.drawEllipse(self.cursor().pos(), size, size)

        elif shape_type == 'square':
            painter.setBrush(color)
            painter.drawRect(self.cursor().pos().x() - size / 2,
                             self.cursor().pos().y() - size / 2, size, size)

        elif shape_type == 'triangle':
            painter.setBrush(color)
            center = self.cursor().pos()
            side_length = random.randint(20, 100)
            half_height = side_length * 3**0.5 / 2

            polygon = QPolygonF([
                center + QPointF(0, -half_height),
                center + QPointF(-side_length / 2, half_height),
                center + QPointF(side_length / 2, half_height)
            ])
            painter.drawPolygon(polygon)

    def mousePressEvent(self, event):
        size = random.randint(20, 100)
        color = QColor(random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255))
        if event.button() == Qt.LeftButton:
            self.paintEvent(self)
        elif event.button() == Qt.RightButton:
            self.paintEvent(self)
        elif event.button() == Qt.MiddleButton:
            self.paintEvent(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())
