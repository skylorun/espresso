import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect("coffee.sqlite")
        self.pushButton.clicked.connect(self.filter)
        self.pushButton_2.clicked.connect(self.up)

    def filter(self):
        cur = self.con.cursor()
        result = cur.execute(f"""
                        SELECT * FROM coffee
                        """).fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.tableWidget.setHorizontalHeaderLabels(['id', 'name_sort', 'degree', 'mol_zer',
                                                    'taste', 'price', 'valuum'])

    def up(self):
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.pushButton.clicked.connect(self.a)

    def a(self):
        cur = self.con.cursor()
        result = cur.execute(f"{self.textEdit.toPlainText()}").fetchall()
        self.con.commit()
        result = cur.execute(f"""
                                SELECT * FROM coffee
                                """).fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))


def main():
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
