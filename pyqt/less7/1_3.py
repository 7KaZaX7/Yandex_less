from PyQt5.QtWidgets import (
    QMainWindow,
    QTableWidget,
    QLineEdit,
    QWidget,
    QVBoxLayout,
    QTableWidgetItem,
    QApplication,
)


class InteractiveReceipt(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Интерактивный чек")

        self.tableWidget = QTableWidget()
        self.total = QLineEdit()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.tableWidget)
        layout.addWidget(self.total)

        headers = ["Товар", "Цена", "Количество"]
        self.tableWidget.setColumnCount(len(headers))
        self.tableWidget.setHorizontalHeaderLabels(headers)

        with open("price.csv", "r") as f:
            data = f.readlines()

        self.tableWidget.setRowCount(len(data))

        for index, line in enumerate(data):
            item_name, item_price = line.strip().split(";")

            name = QTableWidgetItem(item_name)
            price = QTableWidgetItem(item_price)
            tot = QTableWidgetItem("0")

            self.tableWidget.setItem(index, 0, name)
            self.tableWidget.setItem(index, 1, price)
            self.tableWidget.setItem(index, 2, tot)

        self.tableWidget.itemChanged.connect(self.update_total)

        self.total.setReadOnly(True)

    def update_total(self):
        total = 0
        rows = self.tableWidget.rowCount()

        for row in range(rows):
            tot = int(self.tableWidget.item(row, 2).text())
            price = float(self.tableWidget.item(row, 1).text())
            total += tot * price

        self.total.setText(str(total))


if __name__ == "__main__":
    app = QApplication([])
    window = InteractiveReceipt()
    window.show()
    app.exec_()
