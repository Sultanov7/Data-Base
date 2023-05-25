import sys
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (
    QTableWidgetItem, 
    QStackedWidget
)

import main_window
import DepositTypeMapping
import DepositTypes
import Deposits
import Investors



class Expample(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        



class Accidents(QtWidgets.QMainWindow,DepositTypeMapping.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Open.clicked.connect(self.test)
        self.Dell.clicked.connect(self.DellAccidents)
        self.Add.clicked.connect(self.AddAccidents)
        self.Change.clicked.connect(self.ChangeAccidents)

    def test(self):

        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\Suhrob\\bakni.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM 'DepositTypeMapping'")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()

    def DellAccidents(self):
           
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\Suhrob\\bakni.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("DELETE FROM DepositTypeMapping WHERE DepositID = ?", (self.DellLine.text(),))
        self.connection.commit()
        self.connection.close()
    
    def AddAccidents(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\Suhrob\\bakni.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO DepositTypeMapping (TypeID) VALUES(?)", (self.AddLine.text(),))
        self.connection.commit()
        self.connection.close()


    def ChangeAccidents(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\Suhrob\\bakni.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"UPDATE DepositTypeMapping SET TypeID='{self.ChangeLine_2.text()}' WHERE DepositID='{self.ChangeLine.text()}'")


        self.connection.commit()
        self.connection.close()

class Drivers(QtWidgets.QMainWindow,DepositTypes.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.Open.clicked.connect(self.test)
        self.Dell.clicked.connect(self.DellDrivers)
        self.Add.clicked.connect(self.AddDrivers)
        self.Change.clicked.connect(self.ChangeDrivers)
        
        
    
    def test(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\Suhrob\\bakni.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM 'DepositTypes'")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()
    
    def DellDrivers(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\Suhrob\\bakni.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("DELETE FROM DepositTypes WHERE ID =?", (self.DellLine.text(),))
        self.connection.commit()
        self.connection.close()

    def AddDrivers(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\Suhrob\\bakni.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO 'DepositTypes' ('Name') VALUES (?)",
                       (self.AddLine.text()))
                           
        self.connection.commit()
        self.connection.close()


    def ChangeDrivers(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\Suhrob\\bakni.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"UPDATE 'DepositTypes' SET Name='{self.ChangeLine_2.text()}' WHERE ID='{self.ChangeLine.text()}'")
        
        self.connection.commit()
        self.connection.close()

class Fuel(QtWidgets.QMainWindow,Deposits.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Open.clicked.connect(self.test)
        self.Dell.clicked.connect(self.DellFuel)
        self.Add.clicked.connect(self.AddFuel)
        self.Change.clicked.connect(self.ChangeFuel)
        

    def test(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\Suhrob\\bakni.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM 'Deposits'")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()

    def DellFuel(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\Suhrob\\bakni.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("DELETE FROM Deposits WHERE ID =?", (self.DellLine.text(),))
        self.connection.commit()
        self.connection.close()

    def AddFuel(self):

        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\Suhrob\\bakni.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO Deposits (InvestorID,Amount,OpeningDate) VALUES(?,?,?)", (self.AddLine.text(), self.AddLine_2.text(),self.AddLine_3.text(),))
        self.connection.commit()
        self.connection.close()


    def ChangeFuel(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\Suhrob\\bakni.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"UPDATE Deposits SET InvestorID='{self.ChangeLine.text()}', Amount='{self.ChangeLine_2.text()}', OpeningDate='{self.ChangeLine_3.text()}' WHERE ID='{self.ChangeLine.text()}'")

        self.connection.commit()
        self.connection.close()


class Inspection(QtWidgets.QMainWindow,Investors.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Open.clicked.connect(self.test1)
        self.Dell.clicked.connect(self.DellInspection)
        self.Add.clicked.connect(self.AddInspection)
        self.Change.clicked.connect(self.ChangeInspection)


    def test1(self):
        
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\Suhrob\\bakni.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM 'Investors'")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()
    
    def DellInspection(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\Suhrob\\bakni.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("DELETE FROM Investors WHERE ID =?", (self.DellLine.text(),))
        self.connection.commit()
        self.connection.close()



    def AddInspection(self):

        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\Suhrob\\bakni.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO Investors (Name,Surname,Phone) VALUES(?,?,?)", (self.AddLine.text(), self.AddLine_2.text(),self.AddLine_3.text(),))
        self.connection.commit()
        self.connection.close()

    def ChangeInspection(self):
        
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\Suhrob\\bakni.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"UPDATE Investors SET Name='{self.ChangeLine_2.text()}', Surname='{self.ChangeLine_3.text()}', Phone='{self.ChangeLine_4.text()}' WHERE ID='{self.ChangeLine.text()}'")

        self.connection.commit()
        self.connection.close()




class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)



        self.example = Expample()
        self.accidents = Accidents()
        self.drivers = Drivers()
        self.fuel = Fuel()
        self.inspection = Inspection()
        

        self.stacked_widget.addWidget(self.example)
        self.stacked_widget.addWidget(self.accidents)
        self.stacked_widget.addWidget(self.drivers)
        self.stacked_widget.addWidget(self.fuel)
        self.stacked_widget.addWidget(self.inspection)
        
    

        self.example.AccidentsBtn.clicked.connect(self.show_accidents)
        self.accidents.Back.clicked.connect(self.show_example)
        self.example.DriversBtn.clicked.connect(self.show_drivers)
        self.drivers.Back.clicked.connect(self.show_example)
        self.example.FuelBtn.clicked.connect(self.show_fuel)
        self.fuel.Back.clicked.connect(self.show_example)
        self.example.InspectionsBtn.clicked.connect(self.show_inspection)
        self.inspection.Back.clicked.connect(self.show_example)
        
        
        

    def show_example(self):
        self.stacked_widget.setCurrentWidget(self.example)

    def show_accidents(self):
        self.stacked_widget.setCurrentWidget(self.accidents)
    
    def show_drivers(self):
        self.stacked_widget.setCurrentWidget(self.drivers)
    
    def show_fuel(self):
        self.stacked_widget.setCurrentWidget(self.fuel)

    def show_inspection(self):
        self.stacked_widget.setCurrentWidget(self.inspection)
    


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
