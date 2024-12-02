import sqlite3
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QTableWidgetItem, QMainWindow


class CoffeeApp(QMainWindow):
    def __init__(self):
        super(CoffeeApp, self).__init__()
        uic.loadUi('main.ui', self)  # Загрузка интерфейса из файла
        conn = sqlite3.connect('coffee.sqlite')
        cursor = conn.cursor()
        coffee_data = cursor.execute("SELECT * FROM info").fetchall()
        self.tableWidget.setRowCount(len(coffee_data))
        self.tableWidget.setColumnCount(len(coffee_data[0]))
        self.tableWidget.setHorizontalHeaderLabels(
            ['ID', 'Название сорта', 'Степень обжарки', 'Молотый/в зернах(1/0)',
             'Описание вкуса', 'Цена', 'Объем упаковки'])
        for i, k in enumerate(coffee_data):
            for j, v in enumerate(k):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(v)))


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = CoffeeApp()
    window.show()
    app.exec()
