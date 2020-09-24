# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Павел/PycharmProjects/Museum/security.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Security(object):
    def setupUi(self, Security):
        Security.setObjectName("MainWindow")
        Security.resize(600, 547)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Security.sizePolicy().hasHeightForWidth())
        Security.setSizePolicy(sizePolicy)
        Security.setMinimumSize(QtCore.QSize(600, 547))
        Security.setMaximumSize(QtCore.QSize(600, 547))
        self.centralwidget = QtWidgets.QWidget(Security)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 2, 2)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 4, 0, 1, 2)
        Security.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Security)
        self.statusbar.setObjectName("statusbar")
        Security.setStatusBar(self.statusbar)

        self.retranslateUi(Security)
        QtCore.QMetaObject.connectSlotsByName(Security)

    def retranslateUi(self, Security):
        _translate = QtCore.QCoreApplication.translate
        Security.setWindowTitle(_translate("Security", "Security"))
        self.pushButton.setText(_translate("Security", "Найти по ФИО"))
        self.pushButton_2.setText(_translate("Security", "Найти по номеру билета"))
        self.pushButton_3.setText(_translate("Security", "Выход к стартовому окну"))
