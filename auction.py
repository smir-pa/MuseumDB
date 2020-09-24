# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Павел/PycharmProjects/Museum/auction.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Auction(object):
    def setupUi(self, Auction):
        Auction.setObjectName("MainWindow")
        Auction.resize(800, 398)
        Auction.setMinimumSize(QtCore.QSize(800, 398))
        Auction.setMaximumSize(QtCore.QSize(800, 398))
        self.centralwidget = QtWidgets.QWidget(Auction)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 2, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 2, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 4, 2, 1, 1)
        Auction.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Auction)
        self.statusbar.setObjectName("statusbar")
        Auction.setStatusBar(self.statusbar)

        self.retranslateUi(Auction)
        QtCore.QMetaObject.connectSlotsByName(Auction)

    def retranslateUi(self, Auction):
        _translate = QtCore.QCoreApplication.translate
        Auction.setWindowTitle(_translate("Auction", "Auction"))
        self.pushButton.setText(_translate("Auction", "Добавить информацию о себе"))
        self.comboBox.setItemText(0, _translate("Auction", "Посетители"))
        self.comboBox.setItemText(1, _translate("Auction", "Аукцион"))
        self.comboBox.setItemText(2, _translate("Auction", "Экспонаты"))
        self.pushButton_2.setText(_translate("Auction", "Выход к стартовому окну"))
