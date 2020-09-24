# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Павел/PycharmProjects/Museum/senior.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Senior(object):
    def setupUi(self, Senior):
        Senior.setObjectName("MainWindow")
        Senior.resize(800, 600)
        Senior.setMinimumSize(QtCore.QSize(800, 600))
        Senior.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(Senior)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 3, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 4, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        Senior.setCentralWidget(self.centralwidget)

        self.retranslateUi(Senior)
        QtCore.QMetaObject.connectSlotsByName(Senior)

    def retranslateUi(self, Senior):
        _translate = QtCore.QCoreApplication.translate
        Senior.setWindowTitle(_translate("Senior", "Senior"))
        self.comboBox.setItemText(0, _translate("Senior", "Экспонаты"))
        self.comboBox.setItemText(1, _translate("Senior", "Расположение"))
        self.comboBox.setItemText(2, _translate("Senior", "Мероприятия"))
        self.comboBox.setItemText(3, _translate("Senior", "Экскурсии"))
        self.comboBox.setItemText(4, _translate("Senior", "Мастер-классы"))
        self.comboBox.setItemText(5, _translate("Senior", "Рабочее место"))
        self.comboBox.setItemText(6, _translate("Senior", "Работники"))
        self.comboBox.setItemText(7, _translate("Senior", "Исследовательская деятельность"))
        self.pushButton_2.setText(_translate("Senior", "Добавить"))
        self.pushButton.setText(_translate("Senior", "Вывести"))
        self.pushButton_4.setText(_translate("Senior", "Выход к стартовому окну"))
        self.pushButton_3.setText(_translate("Senior", "Удалить"))
