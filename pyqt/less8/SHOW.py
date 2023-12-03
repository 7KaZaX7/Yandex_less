import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QVBoxLayout, QLabel, QGroupBox, QPushButton, QWidget
from PyQt5.QtGui import QImage, QPixmap, QColor, QTransform

class MyPillow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PIL 2.0")

        self.image_label = QLabel()
        self.red_button = QPushButton("R")
        self.green_button = QPushButton("G")
        self.blue_button = QPushButton("B")
        self.defauld = QPushButton("ALL")
        self.left_button = QPushButton("Против часовой стрелки")
        self.right_button = QPushButton("По часовой стрелки")

        self.channelButtons = QGroupBox()
        channelButtons = QVBoxLayout()
        channelButtons.addWidget(self.red_button)
        channelButtons.addWidget(self.green_button)
        channelButtons.addWidget(self.blue_button)
        channelButtons.addWidget(self.defauld)
        self.channelButtons.setLayout(channelButtons)

        self.rotateButtons = QGroupBox()
        rotateButtons = QVBoxLayout()
        rotateButtons.addWidget(self.left_button)
        rotateButtons.addWidget(self.right_button)
        self.rotateButtons.setLayout(rotateButtons)

        widget = QWidget()
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.image_label)

        main_layout.addWidget(self.channelButtons)
        main_layout.addWidget(self.rotateButtons)
        widget.setLayout(main_layout)

        self.setCentralWidget(widget)

        self.open_image()
        self.red_button.clicked.connect(lambda: self.change_channel(0))
        self.green_button.clicked.connect(lambda: self.change_channel(1))
        self.blue_button.clicked.connect(lambda: self.change_channel(2))
        self.defauld.clicked.connect(lambda: self.change_channel(3))
        self.left_button.clicked.connect(lambda: self.rotate_image(-90))
        self.right_button.clicked.connect(lambda: self.rotate_image(90))

        

    def open_image(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Выберите изображение", "", "Изображения (*.png *.jpg *.bmp)")

        if file_path:
            self.curr_image = QImage(file_path)
            self.update_image()
            self.const_image = self.curr_image.copy()

    def change_channel(self, channel):
        self.curr_image = self.const_image
        modified_image = self.curr_image.copy()
        for x in range(modified_image.width()):
            for y in range(modified_image.height()):
                old_color = QColor(modified_image.pixelColor(x, y))
                if channel == 0:
                    modified_color = QColor(old_color.red(), 0, 0)
                    modified_image.setPixelColor(x, y, modified_color)
                elif channel == 1:
                    modified_color = QColor(0, old_color.green(), 0)
                    modified_image.setPixelColor(x, y, modified_color)
                elif channel == 2:
                    modified_color = QColor(0, 0, old_color.blue())
                    modified_image.setPixelColor(x, y, modified_color)
                elif channel == 3:
                    modified_image = self.const_image             
        self.curr_image = modified_image
        self.update_image()

    def rotate_image(self, angle):
        transform = QTransform().rotate(angle)
        modified_image = self.curr_image.transformed(transform)

        self.curr_image = modified_image
        self.update_image()

    def update_image(self):
        pixmap = QPixmap.fromImage(self.curr_image)
        self.image_label.setPixmap(pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    pillow = MyPillow()
    pillow.show()

    sys.exit(app.exec())