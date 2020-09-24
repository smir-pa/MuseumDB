# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Павел/PycharmProjects/Museum/fund.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Fund(object):
    def setupUi(self, Fund):
        Fund.setObjectName("MainWindow")
        Fund.resize(798, 596)
        Fund.setMaximumSize(QtCore.QSize(798, 596))
        Fund.setMinimumSize(QtCore.QSize(798, 596))
        self.centralwidget = QtWidgets.QWidget(Fund)
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
        self.gridLayout.addWidget(self.comboBox, 3, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 2, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 6, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 7, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 7, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 4, 0, 1, 1)
        Fund.setCentralWidget(self.centralwidget)

        self.retranslateUi(Fund)
        QtCore.QMetaObject.connectSlotsByName(Fund)

    def retranslateUi(self, Fund):
        _translate = QtCore.QCoreApplication.translate
        Fund.setWindowTitle(_translate("Fund", "Fund"))
        self.comboBox.setItemText(0, _translate("Fund", "Фонд"))
        self.comboBox.setItemText(1, _translate("Fund", "Финансирование"))
        self.comboBox.setItemText(2, _translate("Fund", "Продажа"))
        self.comboBox.setItemText(3, _translate("Fund", "Товары"))
        self.comboBox.setItemText(4, _translate("Fund", "Закупка экспонатов"))
        self.comboBox.setItemText(5, _translate("Fund", "Экспонаты"))
        self.pushButton.setText(_translate("Fund", "Вывести"))
        self.pushButton_3.setText(_translate("Fund", "Удалить"))
        self.pushButton_5.setText(_translate("Fund", "Выход к стартовому окну"))
        self.pushButton_2.setText(_translate("Fund", "Добавить"))
