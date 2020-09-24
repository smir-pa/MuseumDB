
# Библиотеки
import sys
import psycopg2
import hashlib
# Модули
from start import *
from security import *
from auction import *
from add_av import *
from fund import *
from add_financing import *
from add_sale import *
from add_shop import *
from add_exhibit_purchase import *
from add_exhibit import *
from delete import *
from senior import *
from add_exhibit_location import *
from add_event import *
from add_excursion import *
from add_master_class import *
from add_employee_workplace import *
from add_employee import *
from add_research_activity import *

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QAction
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QRegExpValidator

# Главное окно


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        slov_logpass = QtCore.QRegExp("[0-9a-zA-Z]{20}")
        validator_logpass = QtGui.QRegExpValidator(slov_logpass)
        self.ui.lineEdit.setValidator(validator_logpass)
        self.ui.lineEdit_2.setValidator(validator_logpass)
        self.ui.label.setVisible(True)
        self.ui.label_2.setVisible(True)
        self.ui.pushButton.clicked.connect(self.login_enter)
        self.ui.pushButton_2.clicked.connect(self.sign_up)
        self.connect_bd()

    # Вход

    def login_enter(self):
        usname = self.ui.lineEdit.text()
        pas = self.ui.lineEdit_2.text()
        pas += usname
        h = hashlib.md5(pas.encode())
        pas = h.hexdigest() + "museum"
        h = hashlib.md5(pas.encode())
        pas = "md5" + h.hexdigest()
        try:
            con = self.connect_bd()
            cur_pass = con.cursor()
            cur_pass.execute("select passwd from pg_shadow WHERE usename = %s", (usname,))
            passw = cur_pass.fetchone()[0]
            if passw == pas:
                cur_role = con.cursor()
                cur_role.execute(
                    "select * from information_schema.applicable_roles WHERE grantee = %s", (usname,))
                role = cur_role.fetchone()[1]
                if role == "security_worker":
                    self.window_security()
                    self.close()
                if role == "auction_participant":
                    self.window_auction()
                    self.close()
                if role == "fund_worker":
                    self.window_fund()
                    self.close()
                if role == "senior_employee":
                    self.window_senior()
                    self.close()
            return con
        except psycopg2.DatabaseError:
            self.ui.label_3.setText("Ошибка авторизации")
            print("Ошибка авторизации")

    # Регистрация

    def sign_up(self):
        usname = self.ui.lineEdit.text()
        pas = self.ui.lineEdit_2.text()
        pas += usname
        h = hashlib.md5(pas.encode())
        pas = h.hexdigest() + "museum"
        h = hashlib.md5(pas.encode())
        pas = "md5" + h.hexdigest()
        try:
            con = self.connect_bd()
            cur = con.cursor()
        #    cur.execute("CREATE USER %s WITH PASSWORD %s", (usname, pas))
            cur.execute("CREATE USER " + usname + " WITH PASSWORD " + "'" + pas + "'")
            con.commit()
        #    cur.execute("GRANT auction_participant TO %s", (usname,))
            cur.execute("GRANT auction_participant TO " + usname)
            con.commit()
            con.close()
            self.ui.label_3.setText("Регистрация прошла успешно")
        except psycopg2.DatabaseError:
            self.ui.label_3.setText("Ошибка регистрации")
            print("Ошибка регистрации")

    # Пользовательские окна

    def window_security(self):
        self.w = Window_security()
        self.w.show()

    def window_auction(self):
        self.w = Window_auction()
        self.w.show()

    def window_fund(self):
        self.w = Window_fund()
        self.w.show()

    def window_senior(self):
        self.w = Window_senior()
        self.w.show()

    # Подключение к бд

    def connect_bd(self):
        try:
            con = psycopg2.connect(
                database="Museum",
                user="postgres",
                password="1",
                host="127.0.0.1",
                port="5432"
            )
            print("Коннект")
            return con
        except psycopg2.DatabaseError:
            print("Не коннект")

# Классы пользовательских форм


class Window_security(QMainWindow):
    def __init__(self):
        super(Window_security, self).__init__()
        self.ui = Ui_Security()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.search_fn)
        self.ui.pushButton_2.clicked.connect(self.search_tn)
        self.ui.pushButton_3.clicked.connect(self.back)
        con = Window().connect_bd()
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM visitor")
            result = cur.fetchall()
            self.ui.tableWidget.setRowCount(0)
            self.ui.tableWidget.setColumnCount(4)
            self.ui.tableWidget.setHorizontalHeaderLabels(["id", "ФИО", "Код экскурсии", "Номер билета"])
            self.ui.tableWidget.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
            self.ui.tableWidget.sizeHintForColumn(4)
            for row_number, row_data in enumerate(result):
                self.ui.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                self.ui.tableWidget.setColumnCount(column_number + 1)
            con.commit()
            con.close()
            self.ui.tableWidget.resizeColumnsToContents()
            print("Выполнено!")
        except psycopg2.DatabaseError:
            print("Ошибка!")
        finally:
            if con:
                con.close()

    def search_fn(self):
        full_name = "%" + self.ui.lineEdit.text() + "%"
        con = Window().connect_bd()
        cur = con.cursor()
        try:
            cur.execute("select * from visitor where full_name like %s order by full_name", (full_name,))
            result = cur.fetchall()
            self.ui.tableWidget.setRowCount(0)
            self.ui.tableWidget.setColumnCount(4)
            self.ui.tableWidget.setHorizontalHeaderLabels(["id", "ФИО", "Код экскурсии", "Номер билета"])
            self.ui.tableWidget.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
            self.ui.tableWidget.sizeHintForColumn(4)
            for row_number, row_data in enumerate(result):
                self.ui.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                self.ui.tableWidget.setColumnCount(column_number + 1)
            con.commit()
            con.close()
            self.ui.tableWidget.resizeColumnsToContents()
            print("Выполнено!")
        except psycopg2.DatabaseError:
            print("Ошибка!")

        finally:
            if con:
                con.close()

    def search_tn(self):
        ticket_number = self.ui.lineEdit.text()
        con = Window().connect_bd()
        cur = con.cursor()
        try:
            cur.execute("select * from visitor where ticket_number = %s", (ticket_number,))
            result = cur.fetchall()
            self.ui.tableWidget.setRowCount(0)
            self.ui.tableWidget.setColumnCount(4)
            self.ui.tableWidget.setHorizontalHeaderLabels(["id", "ФИО", "Код экскурсии", "Номер билета"])
            self.ui.tableWidget.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
            self.ui.tableWidget.sizeHintForColumn(4)
            for row_number, row_data in enumerate(result):
                self.ui.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                self.ui.tableWidget.setColumnCount(column_number + 1)
            con.commit()
            con.close()
            self.ui.tableWidget.resizeColumnsToContents()
            print("Выполнено!")
        except psycopg2.DatabaseError:
            print("Ошибка!")
        finally:
            if con:
                con.close()

    def back(self):
        self.w = Window()
        self.w.show()
        self.close()


class Window_auction(QMainWindow):
    def __init__(self):
        super(Window_auction, self).__init__()
        self.ui = Ui_Auction()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.add_info)
        self.ui.pushButton_2.clicked.connect(self.back)
        self.ui.comboBox.currentIndexChanged.connect(self.change)
        con = Window().connect_bd()
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM auction_visitor")
            result = cur.fetchall()
            self.ui.tableWidget.setRowCount(0)
            self.ui.tableWidget.setColumnCount(5)
            self.ui.tableWidget.setHorizontalHeaderLabels(["id", "ФИО", "Дата рождения", "Номер телефона", "Email"])
            self.ui.tableWidget.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
            self.ui.tableWidget.sizeHintForColumn(5)
            for row_number, row_data in enumerate(result):
                self.ui.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                self.ui.tableWidget.setColumnCount(column_number + 1)
            con.commit()
            con.close()
            self.ui.tableWidget.resizeColumnsToContents()
            self.ui.pushButton.setVisible(True)
            print("Выполнено!")
        except psycopg2.DatabaseError:
            print("Ошибка!")
        finally:
            if con:
                con.close()

    def change(self):
        con = Window().connect_bd()
        cur = con.cursor()
        if self.ui.comboBox.currentIndex() == 0:
            try:
                cur.execute("SELECT * FROM auction_visitor")
                result = cur.fetchall()
                self.ui.tableWidget.setRowCount(0)
                self.ui.tableWidget.setColumnCount(5)
                self.ui.tableWidget.setHorizontalHeaderLabels(["id", "ФИО", "Дата рождения", "Номер телефона", "Email"])
                self.ui.tableWidget.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
                self.ui.tableWidget.sizeHintForColumn(5)
                for row_number, row_data in enumerate(result):
                    self.ui.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.ui.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                    self.ui.tableWidget.setColumnCount(column_number + 1)
                con.commit()
                con.close()
                self.ui.tableWidget.resizeColumnsToContents()
                self.ui.pushButton.setVisible(True)
                print("Выполнено!")
            except psycopg2.DatabaseError:
                print("Ошибка!")
            finally:
                if con:
                    con.close()
        elif self.ui.comboBox.currentIndex() == 1:
            try:
                cur.execute("SELECT * FROM show_auction()")
                result = cur.fetchall()
                self.ui.tableWidget.setRowCount(0)
                self.ui.tableWidget.setColumnCount(6)
                self.ui.tableWidget.setHorizontalHeaderLabels(["id", "id экспоната", "Продавец", "Покупатель", "Цена", "Дата"])
                self.ui.tableWidget.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
                self.ui.tableWidget.sizeHintForColumn(6)
                for row_number, row_data in enumerate(result):
                    self.ui.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.ui.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                    self.ui.tableWidget.setColumnCount(column_number + 1)
                con.commit()
                con.close()
                self.ui.tableWidget.resizeColumnsToContents()
                self.ui.pushButton.setVisible(False)
                print("Выполнено!")
            except psycopg2.DatabaseError:
                print("Ошибка!")
            finally:
                if con:
                    con.close()
        elif self.ui.comboBox.currentIndex() == 2:
            try:
                cur.execute("SELECT * FROM exhibit")
                result = cur.fetchall()
                self.ui.tableWidget.setRowCount(0)
                self.ui.tableWidget.setColumnCount(6)
                self.ui.tableWidget.setHorizontalHeaderLabels(["id", "Название", "Автор", "Картинка", "Дата создания", "Тип"])
                self.ui.tableWidget.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
                self.ui.tableWidget.sizeHintForColumn(6)
                for row_number, row_data in enumerate(result):
                    self.ui.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.ui.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                    self.ui.tableWidget.setColumnCount(column_number + 1)
                con.commit()
                con.close()
                self.ui.tableWidget.resizeColumnsToContents()
                self.ui.pushButton.setVisible(False)
                print("Выполнено!")
            except psycopg2.DatabaseError:
                print("Ошибка!")
            finally:
                if con:
                    con.close()

    def add_info(self):
        self.w = Window_add_av()
        self.w.show()

    def back(self):
        self.w = Window()
        self.w.show()
        self.close()


class Window_fund(QMainWindow):

    ind_combo = 0

    def __init__(self):
        global ind_combo, table
        super(Window_fund, self).__init__()
        self.ui = Ui_Fund()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.tselect)
        self.ui.pushButton_2.clicked.connect(self.tinsert)
        self.ui.pushButton_3.clicked.connect(self.tdelete)
        self.ui.pushButton_5.clicked.connect(self.back)
        self.ui.comboBox.currentIndexChanged.connect(self.change)
        con = Window().connect_bd()
        cur = con.cursor()
        try:
            ind_combo = 0
            table = "fund"
            cur.execute("SELECT * FROM fund ORDER BY id")
            result = cur.fetchall()
            self.ui.tableWidget.setRowCount(0)
            self.ui.tableWidget.setColumnCount(3)
            self.ui.tableWidget.setHorizontalHeaderLabels(["id", "Название", "Отчет"])
            self.ui.tableWidget.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
            self.ui.tableWidget.sizeHintForColumn(3)
            for row_number, row_data in enumerate(result):
                self.ui.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                self.ui.tableWidget.setColumnCount(column_number + 1)
            con.commit()
            con.close()
            self.ui.tableWidget.resizeColumnsToContents()
            print("Выполнено!")
        except psycopg2.DatabaseError:
            print("Ошибка!")
        finally:
            if con:
                con.close()

    def tselect(self):
        self.ui.label.setText("")
        con = Window().connect_bd()
        if ind_combo == 0:
            cur = con.cursor()
            try:
                cur.execute("SELECT * FROM fund ORDER BY id")
                result = cur.fetchall()
                self.ui.tableWidget.setRowCount(0)
                self.ui.tableWidget.setColumnCount(3)
                self.ui.tableWidget.setHorizontalHeaderLabels(["id", "Название", "Отчет"])
                self.ui.tableWidget.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
                self.ui.tableWidget.sizeHintForColumn(3)
                for row_number, row_data in enumerate(result):
                    self.ui.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.ui.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                    self.ui.tableWidget.setColumnCount(column_number + 1)
                con.commit()
                con.close()
                self.ui.tableWidget.resizeColumnsToContents()
                print("Выполнено!")
            except psycopg2.DatabaseError:
                print("Ошибка!")
            finally:
                if con:
                    con.close()
        elif ind_combo == 1:
            cur = con.cursor()
            try:
                cur.execute("SELECT * FROM show_financing() ORDER BY id")
                result = cur.fetchall()
                self.ui.tableWidget.setRowCount(0)
                self.ui.tableWidget.setColumnCount(7)
                self.ui.tableWidget.setHorizontalHeaderLabels(["id", "Спонсор", "Дата финансирования", "Сумма",
                                                               "Номер телефона", "Фонд", "Email"])
                self.ui.tableWidget.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
                self.ui.tableWidget.sizeHintForColumn(7)
                for row_number, row_data in enumerate(result):
                    self.ui.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.ui.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                    self.ui.tableWidget.setColumnCount(column_number + 1)
                con.commit()
                con.close()
                self.ui.tableWidget.resizeColumnsToContents()
                print("Выполнено!")
            except psycopg2.DatabaseError:
                print("Ошибка!")
            finally:
                if con:
                    con.close()
        elif ind_combo == 2:
            cur = con.cursor()
            try:
                cur.execute("SELECT * FROM show_sale() ORDER BY product_id")
                result = cur.fetchall()
                self.ui.tableWidget.setRowCount(0)
                self.ui.tableWidget.setColumnCount(4)
                self.ui.tableWidget.setHorizontalHeaderLabels(["id", "Количество", "Прибыль", "Фонд"])
                self.ui.tableWidget.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
                self.ui.tableWidget.sizeHintForColumn(4)
                for row_number, row_data in enumerate(result):
                    self.ui.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.ui.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                    self.ui.tableWidget.setColumnCount(column_number + 1)
                con.commit()
                con.close()
                self.ui.tableWidget.resizeColumnsToContents()
                print("Выполнено!")
            except psycopg2.DatabaseError:
                print("Ошибка!")
            finally:
                if con:
                    con.close()
        elif ind_combo == 3:
            cur = con.cursor()
            try:
                cur.execute("SELECT * FROM show_shop() ORDER BY id")
                result = cur.fetchall()
                self.ui.tableWidget.setRowCount(0)
                self.ui.tableWidget.setColumnCount(6)
                self.ui.tableWidget.setHorizontalHeaderLabels(["id", "Название", "Цена", "Производитель", "Картинка",
                                                               "Количество"])
                self.ui.tableWidget.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
                self.ui.tableWidget.sizeHintForColumn(6)
                for row_number, row_data in enumerate(result):
                    self.ui.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.ui.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                    self.ui.tableWidget.setColumnCount(column_number + 1)
                con.commit()
                con.close()
                self.ui.tableWidget.resizeColumnsToContents()
                print("Выполнено!")
            except psycopg2.DatabaseError:
                print("Ошибка!")
            finally:
                if con:
                    con.close()
        elif ind_combo == 4:
            cur = con.cursor()
            try:
                cur.execute("SELECT * FROM show_exhibit_purchase() ORDER BY id")
                result = cur.fetchall()
                self.ui.tableWidget.setRowCount(0)
                self.ui.tableWidget.setColumnCount(5)
                self.ui.tableWidget.setHorizontalHeaderLabels(["id", "id экспоната", "Цена", "Дата покупки", "Фонд"])
                self.ui.tableWidget.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
                self.ui.tableWidget.sizeHintForColumn(5)
                for row_number, row_data in enumerate(result):
                    self.ui.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.ui.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                    self.ui.tableWidget.setColumnCount(column_number + 1)
                con.commit()
                con.close()
                self.ui.tableWidget.resizeColumnsToContents()
                print("Выполнено!")
            except psycopg2.DatabaseError:
                print("Ошибка!")
            finally:
                if con:
                    con.close()
        elif ind_combo == 5:
            cur = con.cursor()
            try:
                cur.execute("SELECT * FROM exhibit ORDER BY id")
                result = cur.fetchall()
                self.ui.tableWidget.setRowCount(0)
                self.ui.tableWidget.setColumnCount(6)
                self.ui.tableWidget.setHorizontalHeaderLabels(
                    ["id", "Название", "Автор", "Картинка", "Дата создания", "Тип"])
                self.ui.tableWidget.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
                self.ui.tableWidget.sizeHintForColumn(6)
                for row_number, row_data in enumerate(result):
                    self.ui.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.ui.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                    self.ui.tableWidget.setColumnCount(column_number + 1)
                con.commit()
                con.close()
                self.ui.tableWidget.resizeColumnsToContents()
                print("Выполнено!")
            except psycopg2.DatabaseError:
                print("Ошибка!")
            finally:
                if con:
                    con.close()

    def tinsert(self):
        self.ui.label.setText("")
        con = Window().connect_bd()
        if ind_combo == 0:
            self.ui.label.setText("Вы не можете вставлять данные в эту таблицу. Обратитесь к системному администратору.")
        elif ind_combo == 1:
            self.w = Window_add_financing()
            self.w.show()
        elif ind_combo == 2:
            self.w = Window_add_sale()
            self.w.show()
        elif ind_combo == 3:
            self.w = Window_add_shop()
            self.w.show()
        elif ind_combo == 4:
            self.w = Window_add_exhibit_purchase()
            self.w.show()
        elif ind_combo == 5:
            self.w = Window_add_exhibit()
            self.w.show()

    def tdelete(self):
        global table
        self.ui.label.setText("")
        con = Window().connect_bd()
        if ind_combo == 0 or ind_combo == 5 or ind_combo == 2:
            self.ui.label.setText("Вы не можете удалять данные из этой таблицы. Обратитесь к системному администратору.")
        elif ind_combo in [1, 3, 4]:
            self.w = Window_delete()
            self.w.show()

    def change(self):
        global ind_combo, table
        self.ui.label.setText("")
        ind_combo = int(self.ui.comboBox.currentIndex())
        self.tselect()
        if ind_combo == 0:
            table = "fund"
        elif ind_combo == 1:
            table = "financing"
        elif ind_combo == 2:
            table = "sale"
        elif ind_combo == 3:
            table = "shop"
        elif ind_combo == 4:
            table = "exhibit_purchase"
        elif ind_combo == 5:
            table = "exhibit"

    def back(self):
        self.w = Window()
        self.w.show()
        self.close()


class Window_senior(QMainWindow):

    ind_combo = 0

    def __init__(self):
        global ind_combo, table
        super(Window_senior, self).__init__()
        self.ui = Ui_Senior()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.tselect)
        self.ui.pushButton_2.clicked.connect(self.tinsert)
        self.ui.pushButton_3.clicked.connect(self.tdelete)
        self.ui.pushButton_4.clicked.connect(self.back)
        self.ui.comboBox.currentIndexChanged.connect(self.change)
        con = Window().connect_bd()
        cur = con.cursor()
        try:
            ind_combo = 0
            table = "exhibit"
            cur.execute("SELECT * FROM exhibit ORDER BY id")
            result = cur.fetchall()
            self.ui.tableWidget.setRowCount(0)
            self.ui.tableWidget.setColumnCount(6)
            self.ui.tableWidget.setHorizontalHeaderLabels(
                ["id", "Название", "Автор", "Картинка", "Дата создания", "Тип"])
            self.ui.tableWidget.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
            self.ui.tableWidget.sizeHintForColumn(6)
            for row_number, row_data in enumerate(result):
                self.ui.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                self.ui.tableWidget.setColumnCount(column_number + 1)
            con.commit()
            con.close()
            self.ui.tableWidget.resizeColumnsToContents()
            print("Выполнено!")
        except psycopg2.DatabaseError:
            print("Ошибка!")
        finally:
            if con:
                con.close()

    def tselect(self):
        self.ui.label.setText("")
        con = Window().connect_bd()
        if ind_combo == 0:
            cur = con.cursor()
            try:
                cur.execute("SELECT * FROM exhibit ORDER BY id")
                result = cur.fetchall()
                self.ui.tableWidget.setRowCount(0)
                self.ui.tableWidget.setColumnCount(6)
                self.ui.tableWidget.setHorizontalHeaderLabels(
                    ["id", "Название", "Автор", "Картинка", "Дата создания", "Тип"])
                self.ui.tableWidget.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
                self.ui.tableWidget.sizeHintForColumn(6)
                for row_number, row_data in enumerate(result):
                    self.ui.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.ui.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                    self.ui.tableWidget.setColumnCount(column_number + 1)
                con.commit()
                con.close()
                self.ui.tableWidget.resizeColumnsToContents()
                print("Выполнено!")
            except psycopg2.DatabaseError:
                print("Ошибка!")
            finally:
                if con:
                    con.close()
        elif ind_combo == 1:
            cur = con.cursor()
            try:
                cur.execute("SELECT * FROM exhibit_location ORDER BY exhibit_id")
                result = cur.fetchall()
                self.ui.tableWidget.setRowCount(0)
                self.ui.tableWidget.setColumnCount(4)
                self.ui.tableWidget.setHorizontalHeaderLabels(["id экспоната", "Тип помещения", "id помещения",
                                                               "Номер ячейки"])
                self.ui.tableWidget.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
                self.ui.tableWidget.sizeHintForColumn(4)
                for row_number, row_data in enumerate(result):
                    self.ui.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.ui.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                    self.ui.tableWidget.setColumnCount(column_number + 1)
                con.commit()
                con.close()
                self.ui.tableWidget.resizeColumnsToContents()
                print("Выполнено!")
            except psycopg2.DatabaseError:
                print("Ошибка!")
            finally:
                if con:
                    con.close()
        elif ind_combo == 2:
            cur = con.cursor()
            try:
                cur.execute("SELECT * FROM event ORDER BY id")
                result = cur.fetchall()
                self.ui.tableWidget.setRowCount(0)
                self.ui.tableWidget.setColumnCount(5)
                self.ui.tableWidget.setHorizontalHeaderLabels(["id", "Название", "Дата проведения", "Номер зала",
                                                               "Время начала"])
                self.ui.tableWidget.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
                self.ui.tableWidget.sizeHintForColumn(5)
                for row_number, row_data in enumerate(result):
                    self.ui.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.ui.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                    self.ui.tableWidget.setColumnCount(column_number + 1)
                con.commit()
                con.close()
                self.ui.tableWidget.resizeColumnsToContents()
                print("Выполнено!")
            except psycopg2.DatabaseError:
                print("Ошибка!")
            finally:
                if con:
                    con.close()
        elif ind_combo == 3:
            cur = con.cursor()
            try:
                cur.execute("SELECT * FROM show_excursion() ORDER BY id")
                result = cur.fetchall()
                self.ui.tableWidget.setRowCount(0)
                self.ui.tableWidget.setColumnCount(9)
                self.ui.tableWidget.setHorizontalHeaderLabels(["id", "Время", "График", "Конец", "Код ответственного",
                                                               "Цена", "Название", "Номер зала", "id мастер-класса"])
                self.ui.tableWidget.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
                self.ui.tableWidget.sizeHintForColumn(9)
                for row_number, row_data in enumerate(result):
                    self.ui.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.ui.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                    self.ui.tableWidget.setColumnCount(column_number + 1)
                con.commit()
                con.close()
                self.ui.tableWidget.resizeColumnsToContents()
                print("Выполнено!")
            except psycopg2.DatabaseError:
                print("Ошибка!")
            finally:
                if con:
                    con.close()
        elif ind_combo == 4:
            cur = con.cursor()
            try:
                cur.execute("SELECT * FROM master_class ORDER BY id")
                result = cur.fetchall()
                self.ui.tableWidget.setRowCount(0)
                self.ui.tableWidget.setColumnCount(5)
                self.ui.tableWidget.setHorizontalHeaderLabels(["id", "Название", "Результат", "Краткое описание",
                                                               "Номер уголка творчества"])
                self.ui.tableWidget.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
                self.ui.tableWidget.sizeHintForColumn(5)
                for row_number, row_data in enumerate(result):
                    self.ui.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.ui.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                    self.ui.tableWidget.setColumnCount(column_number + 1)
                con.commit()
                con.close()
                self.ui.tableWidget.resizeColumnsToContents()
                print("Выполнено!")
            except psycopg2.DatabaseError:
                print("Ошибка!")
            finally:
                if con:
                    con.close()
        elif ind_combo == 5:
            cur = con.cursor()
            try:
                cur.execute("SELECT * FROM employee_workplace ORDER BY id")
                result = cur.fetchall()
                self.ui.tableWidget.setRowCount(0)
                self.ui.tableWidget.setColumnCount(4)
                self.ui.tableWidget.setHorizontalHeaderLabels(
                    ["id", "Тип помещения", "id помещения", "id работника"])
                self.ui.tableWidget.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
                self.ui.tableWidget.sizeHintForColumn(4)
                for row_number, row_data in enumerate(result):
                    self.ui.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.ui.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                    self.ui.tableWidget.setColumnCount(column_number + 1)
                con.commit()
                con.close()
                self.ui.tableWidget.resizeColumnsToContents()
                print("Выполнено!")
            except psycopg2.DatabaseError:
                print("Ошибка!")
            finally:
                if con:
                    con.close()
        elif ind_combo == 6:
            cur = con.cursor()
            try:
                cur.execute("SELECT * FROM show_employee() ORDER BY id")
                result = cur.fetchall()
                self.ui.tableWidget.setRowCount(0)
                self.ui.tableWidget.setColumnCount(5)
                self.ui.tableWidget.setHorizontalHeaderLabels(
                    ["id", "ФИО", "Дата рождения", "Должность", "Зарплата"])
                self.ui.tableWidget.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
                self.ui.tableWidget.sizeHintForColumn(5)
                for row_number, row_data in enumerate(result):
                    self.ui.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.ui.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                    self.ui.tableWidget.setColumnCount(column_number + 1)
                con.commit()
                con.close()
                self.ui.tableWidget.resizeColumnsToContents()
                print("Выполнено!")
            except psycopg2.DatabaseError:
                print("Ошибка!")
            finally:
                if con:
                    con.close()
        elif ind_combo == 7:
            cur = con.cursor()
            try:
                cur.execute("SELECT * FROM research_activity ORDER BY id")
                result = cur.fetchall()
                self.ui.tableWidget.setRowCount(0)
                self.ui.tableWidget.setColumnCount(4)
                self.ui.tableWidget.setHorizontalHeaderLabels(
                    ["id", "Название", "Дата исследования", "id автора"])
                self.ui.tableWidget.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
                self.ui.tableWidget.sizeHintForColumn(4)
                for row_number, row_data in enumerate(result):
                    self.ui.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.ui.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                    self.ui.tableWidget.setColumnCount(column_number + 1)
                con.commit()
                con.close()
                self.ui.tableWidget.resizeColumnsToContents()
                print("Выполнено!")
            except psycopg2.DatabaseError:
                print("Ошибка!")
            finally:
                if con:
                    con.close()

    def tinsert(self):
        self.ui.label.setText("")
        con = Window().connect_bd()
        if ind_combo == 0:
            self.w = Window_add_exhibit()
            self.w.show()
        elif ind_combo == 1:
            self.w = Window_add_exhibit_location()
            self.w.show()
        elif ind_combo == 2:
            self.w = Window_add_event()
            self.w.show()
        elif ind_combo == 3:
            self.w = Window_add_excursion()
            self.w.show()
        elif ind_combo == 4:
            self.w = Window_add_master_class()
            self.w.show()
        elif ind_combo == 5:
            self.w = Window_add_employee_workplace()
            self.w.show()
        elif ind_combo == 6:
            self.w = Window_add_employee()
            self.w.show()
        elif ind_combo == 7:
            self.w = Window_add_research_activity()
            self.w.show()

    def tdelete(self):
        global table
        self.ui.label.setText("")
        con = Window().connect_bd()
        if ind_combo == 1:
            self.ui.label.setText("Вы не можете удалять данные из этой таблицы. Обратитесь к системному администратору.")
        else:
            self.w = Window_delete()
            self.w.show()

    def change(self):
        global ind_combo, table
        self.ui.label.setText("")
        ind_combo = int(self.ui.comboBox.currentIndex())
        self.tselect()
        if ind_combo == 0:
            table = "exhibit"
        elif ind_combo == 1:
            table = "exhibit_location"
        elif ind_combo == 2:
            table = "event"
        elif ind_combo == 3:
            table = "excursion"
        elif ind_combo == 4:
            table = "master_class"
        elif ind_combo == 5:
            table = "employee_workplace"
        elif ind_combo == 6:
            table = "employee"
        elif ind_combo == 7:
            table = "research_activity"

    def back(self):
        self.w = Window()
        self.w.show()
        self.close()

# Классы форм для добавления данных


class Window_add_av(QMainWindow):
    def __init__(self):
        super(Window_add_av, self).__init__()
        self.ui = Ui_Add_av()
        self.ui.setupUi(self)
        date_logpass = QtCore.QRegExp("[0-9.]{10}")
        validator_logpass = QtGui.QRegExpValidator(date_logpass)
        self.ui.lineEdit_2.setValidator(validator_logpass)
        phone_logpass = QtCore.QRegExp("[+0-9]{12}")
        validator_logpass = QtGui.QRegExpValidator(phone_logpass)
        self.ui.lineEdit_3.setValidator(validator_logpass)
        email_logpass = QtCore.QRegExp("[0-9a-z.@_-]{25}")
        validator_logpass = QtGui.QRegExpValidator(email_logpass)
        self.ui.lineEdit_4.setValidator(validator_logpass)
        self.ui.pushButton.clicked.connect(self.add_record)

    def add_record(self):
        con = Window().connect_bd()
        cur_id = con.cursor()
        cur_id.execute("SELECT id FROM auction_visitor ORDER BY id DESC")
        id = int(cur_id.fetchone()[0]) + 1
        cur = con.cursor()
        cur.execute("INSERT INTO auction_visitor(id, full_name, date_of_birth, phone_number, email) "
                    "VALUES (%s, %s, %s, %s, %s);", (str(id), self.ui.lineEdit.text(), self.ui.lineEdit_2.text(),
                                                     self.ui.lineEdit_3.text(), self.ui.lineEdit_4.text()))
        con.commit()
        con.close()
        self.close()


class Window_add_financing(QMainWindow):
    def __init__(self):
        super(Window_add_financing, self).__init__()
        self.ui = Ui_Add_financing()
        self.ui.setupUi(self)
        date_logpass = QtCore.QRegExp("[0-9.]{10}")
        validator_logpass = QtGui.QRegExpValidator(date_logpass)
        self.ui.lineEdit_2.setValidator(validator_logpass)
        phone_logpass = QtCore.QRegExp("[+0-9]{12}")
        validator_logpass = QtGui.QRegExpValidator(phone_logpass)
        self.ui.lineEdit_4.setValidator(validator_logpass)
        email_logpass = QtCore.QRegExp("[0-9a-z.@_-]{25}")
        validator_logpass = QtGui.QRegExpValidator(email_logpass)
        self.ui.lineEdit_6.setValidator(validator_logpass)
        self.ui.pushButton.clicked.connect(self.add_record)

    def add_record(self):
        con = Window().connect_bd()
        cur_id = con.cursor()
        cur_id.execute("SELECT id FROM financing ORDER BY id DESC")
        id = int(cur_id.fetchone()[0]) + 1
        cur = con.cursor()
        cur.execute("INSERT INTO financing(id, sponsor, date_of_financing, amount_of_money, phone_number, fund, email) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s);", (str(id), self.ui.lineEdit.text(), self.ui.lineEdit_2.text(),
                                                             self.ui.lineEdit_3.text(), self.ui.lineEdit_4.text(),
                                                             self.ui.lineEdit_5.text(), self.ui.lineEdit_6.text()))
        con.commit()
        con.close()
        self.close()


class Window_add_sale(QMainWindow):
    def __init__(self):
        super(Window_add_sale, self).__init__()
        self.ui = Ui_Add_sale()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.add_record)

    def add_record(self):
        con = Window().connect_bd()
        cur = con.cursor()
        cur.execute("INSERT INTO sale(product_id, quantity, fund) "
                    "VALUES (%s, %s, %s);", (self.ui.lineEdit.text(), self.ui.lineEdit_2.text(),
                                             self.ui.lineEdit_3.text()))
        con.commit()
        con.close()
        self.close()


class Window_add_shop(QMainWindow):
    def __init__(self):
        super(Window_add_shop, self).__init__()
        self.ui = Ui_Add_shop()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.add_record)

    def add_record(self):
        con = Window().connect_bd()
        cur_id = con.cursor()
        cur_id.execute("SELECT id FROM shop ORDER BY id DESC")
        id = int(cur_id.fetchone()[0]) + 1
        cur = con.cursor()
        cur.execute("INSERT INTO shop(id, product_name, price, manufacturer, pic, quantity) "
                    "VALUES (%s, %s, %s, %s, %s, %s);", (str(id), self.ui.lineEdit.text(), self.ui.lineEdit_2.text(),
                                                             self.ui.lineEdit_3.text(), self.ui.lineEdit_4.text(),
                                                             self.ui.lineEdit_5.text()))
        con.commit()
        con.close()
        self.close()


class Window_add_exhibit_purchase(QMainWindow):
    def __init__(self):
        super(Window_add_exhibit_purchase, self).__init__()
        self.ui = Ui_Add_exhibit_purchase()
        self.ui.setupUi(self)
        date_logpass = QtCore.QRegExp("[0-9.]{10}")
        validator_logpass = QtGui.QRegExpValidator(date_logpass)
        self.ui.lineEdit_3.setValidator(validator_logpass)
        self.ui.pushButton.clicked.connect(self.add_record)

    def add_record(self):
        con = Window().connect_bd()
        cur_id = con.cursor()
        cur_id.execute("SELECT id FROM exhibit_purchase ORDER BY id DESC")
        id = int(cur_id.fetchone()[0]) + 1
        cur = con.cursor()
        cur.execute("INSERT INTO exhibit_purchase(id, exhibit_id, price, date_of_purchase, fund) "
                    "VALUES (%s, %s, %s, %s, %s);", (str(id), self.ui.lineEdit.text(), self.ui.lineEdit_2.text(),
                                                     self.ui.lineEdit_3.text(), self.ui.lineEdit_4.text()))
        con.commit()
        con.close()
        self.close()


class Window_add_exhibit(QMainWindow):
    def __init__(self):
        super(Window_add_exhibit, self).__init__()
        self.ui = Ui_Add_exhibit()
        self.ui.setupUi(self)
        date_logpass = QtCore.QRegExp("[0-9.]{10}")
        validator_logpass = QtGui.QRegExpValidator(date_logpass)
        self.ui.lineEdit_4.setValidator(validator_logpass)
        self.ui.pushButton.clicked.connect(self.add_record)

    def add_record(self):
        con = Window().connect_bd()
        cur_id = con.cursor()
        cur_id.execute("SELECT id FROM exhibit ORDER BY id DESC")
        id = int(cur_id.fetchone()[0]) + 1
        cur = con.cursor()
        cur.execute("INSERT INTO exhibit(id, name, author, pic, \"date\", \"type\") "
                    "VALUES (%s, %s, %s, %s, %s, %s);", (str(id), self.ui.lineEdit.text(), self.ui.lineEdit_2.text(),
                                                         self.ui.lineEdit_3.text(), self.ui.lineEdit_4.text(),
                                                         self.ui.lineEdit_5.text()))
        con.commit()
        con.close()
        self.close()


class Window_add_exhibit_location(QMainWindow):
    def __init__(self):
        super(Window_add_exhibit_location, self).__init__()
        self.ui = Ui_Add_exhibit_location()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.add_record)

    def add_record(self):
        con = Window().connect_bd()
        cur = con.cursor()
        cur.execute("INSERT INTO exhibit_location(exhibit_id, \"type\", location_id, place_number) "
                    "VALUES (%s, %s, %s, %s);", (self.ui.lineEdit.text(), self.ui.lineEdit_2.text(),
                                                 self.ui.lineEdit_3.text(), self.ui.lineEdit_4.text()))
        con.commit()
        con.close()
        self.close()


class Window_add_event(QMainWindow):
    def __init__(self):
        super(Window_add_event, self).__init__()
        self.ui = Ui_Add_event()
        self.ui.setupUi(self)
        date_logpass = QtCore.QRegExp("[0-9.]{10}")
        validator_logpass = QtGui.QRegExpValidator(date_logpass)
        self.ui.lineEdit_2.setValidator(validator_logpass)
        time_logpass = QtCore.QRegExp("[0-9:]{4}")
        validator_logpass = QtGui.QRegExpValidator(time_logpass)
        self.ui.lineEdit_4.setValidator(validator_logpass)
        self.ui.pushButton.clicked.connect(self.add_record)

    def add_record(self):
        con = Window().connect_bd()
        cur_id = con.cursor()
        cur_id.execute("SELECT id FROM event ORDER BY id DESC")
        id = int(cur_id.fetchone()[0]) + 1
        cur = con.cursor()
        cur.execute("INSERT INTO exhibit(id, name, \"date\", hall, \"time\") "
                    "VALUES (%s, %s, %s, %s, %s);", (str(id), self.ui.lineEdit.text(), self.ui.lineEdit_2.text(),
                                                         self.ui.lineEdit_3.text(), self.ui.lineEdit_4.text()))
        con.commit()
        con.close()
        self.close()


class Window_add_excursion(QMainWindow):
    def __init__(self):
        super(Window_add_excursion, self).__init__()
        self.ui = Ui_Add_excursion()
        self.ui.setupUi(self)
        date_logpass = QtCore.QRegExp("[0-9.]{10}")
        validator_logpass = QtGui.QRegExpValidator(date_logpass)
        self.ui.lineEdit_3.setValidator(validator_logpass)
        time_logpass = QtCore.QRegExp("[0-9:]{4}")
        validator_logpass = QtGui.QRegExpValidator(time_logpass)
        self.ui.lineEdit.setValidator(validator_logpass)
        self.ui.pushButton.clicked.connect(self.add_record)

    def add_record(self):
        con = Window().connect_bd()
        cur_id = con.cursor()
        cur_id.execute("SELECT id FROM excursion ORDER BY id DESC")
        id = int(cur_id.fetchone()[0]) + 1
        cur = con.cursor()
        cur.execute("INSERT INTO exhibit(id, \"time\", schedule, end, guide, price, name, hall, master_class) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);", (str(id), self.ui.lineEdit.text(), self.ui.lineEdit_2.text(),
                     self.ui.lineEdit_3.text(), self.ui.lineEdit_4.text(), self.ui.lineEdit_5.text(), self.ui.lineEdit_6.text(),
                     self.ui.lineEdit_7.text(), self.ui.lineEdit_8.text()))
        con.commit()
        con.close()
        self.close()


class Window_add_master_class(QMainWindow):
    def __init__(self):
        super(Window_add_master_class, self).__init__()
        self.ui = Ui_Add_master_class()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.add_record)

    def add_record(self):
        con = Window().connect_bd()
        cur_id = con.cursor()
        cur_id.execute("SELECT id FROM master_class ORDER BY id DESC")
        id = int(cur_id.fetchone()[0]) + 1
        cur = con.cursor()
        cur.execute("INSERT INTO exhibit(id, master_class_name, result, short_description, creation_place_id) "
                    "VALUES (%s, %s, %s, %s, %s);", (str(id), self.ui.lineEdit.text(), self.ui.lineEdit_2.text(),
                                                     self.ui.lineEdit_3.text(), self.ui.lineEdit_4.text()))
        con.commit()
        con.close()
        self.close()


class Window_add_employee_workplace(QMainWindow):
    def __init__(self):
        super(Window_add_employee_workplace, self).__init__()
        self.ui = Ui_Add_employee_workplace()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.add_record)

    def add_record(self):
        con = Window().connect_bd()
        cur_id = con.cursor()
        cur_id.execute("SELECT id FROM employee_workplace ORDER BY id DESC")
        id = int(cur_id.fetchone()[0]) + 1
        cur = con.cursor()
        cur.execute("INSERT INTO employee_workplace(id, \"type\", workplace_id, employee_id) "
                    "VALUES (%s, %s, %s, %s);", (str(id), self.ui.lineEdit.text(), self.ui.lineEdit_2.text(),
                                                 self.ui.lineEdit_3.text()))
        con.commit()
        con.close()
        self.close()


class Window_add_employee(QMainWindow):
    def __init__(self):
        super(Window_add_employee, self).__init__()
        self.ui = Ui_Add_employee()
        self.ui.setupUi(self)
        date_logpass = QtCore.QRegExp("[0-9.]{10}")
        validator_logpass = QtGui.QRegExpValidator(date_logpass)
        self.ui.lineEdit_2.setValidator(validator_logpass)
        self.ui.pushButton.clicked.connect(self.add_record)

    def add_record(self):
        con = Window().connect_bd()
        cur_id = con.cursor()
        cur_id.execute("SELECT id FROM employee ORDER BY id DESC")
        id = int(cur_id.fetchone()[0]) + 1
        cur = con.cursor()
        cur.execute("INSERT INTO employee_workplace(id, full_name, date_of_birth, post, salary) "
                    "VALUES (%s, %s, %s, %s, %s);", (str(id), self.ui.lineEdit.text(), self.ui.lineEdit_2.text(),
                                                     self.ui.lineEdit_3.text(), self.ui.lineEdit_4.text()))
        con.commit()
        con.close()
        self.close()


class Window_add_research_activity(QMainWindow):
    def __init__(self):
        super(Window_add_research_activity, self).__init__()
        self.ui = Ui_Add_research_activity()
        self.ui.setupUi(self)
        date_logpass = QtCore.QRegExp("[0-9.]{10}")
        validator_logpass = QtGui.QRegExpValidator(date_logpass)
        self.ui.lineEdit_2.setValidator(validator_logpass)
        self.ui.pushButton.clicked.connect(self.add_record)

    def add_record(self):
        con = Window().connect_bd()
        cur_id = con.cursor()
        cur_id.execute("SELECT id FROM research_activity ORDER BY id DESC")
        id = int(cur_id.fetchone()[0]) + 1
        cur = con.cursor()
        cur.execute("INSERT INTO research_activity(id, name, date_of_research, author) "
                    "VALUES (%s, %s, %s, %s);", (str(id), self.ui.lineEdit.text(), self.ui.lineEdit_2.text(),
                                                 self.ui.lineEdit_3.text()))
        con.commit()
        con.close()
        self.close()

# Класс формы для удаления данных


class Window_delete(QMainWindow):
    def __init__(self):
        super(Window_delete, self).__init__()
        self.ui = Ui_Delete()
        self.ui.setupUi(self)
        id_logpass = QtCore.QRegExp("[0-9]{6}")
        validator_logpass = QtGui.QRegExpValidator(id_logpass)
        self.ui.lineEdit.setValidator(validator_logpass)
        self.ui.pushButton.clicked.connect(self.del_record)

    def del_record(self):
        con = Window().connect_bd()
        id = self.ui.lineEdit.text()
        cur = con.cursor()
        cur.execute("DELETE FROM " + table + " WHERE id = " + id)
        con.commit()
        con.close()
        self.close()


table = ""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = Window()
    myapp.show()
    sys.exit(app.exec_())
