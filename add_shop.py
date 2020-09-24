# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Павел/PycharmProjects/Museum/add_shop.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Add_shop(object):
    def setupUi(self, Add_shop):
        Add_shop.setObjectName("MainWindow")
        Add_shop.resize(430, 310)
        Add_shop.setMinimumSize(QtCore.QSize(430, 310))
        Add_shop.setMaximumSize(QtCore.QSize(430, 310))
        self.centralwidget = QtWidgets.QWidget(Add_shop)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout.addWidget(self.lineEdit_4)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout.addWidget(self.lineEdit_5)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        Add_shop.setCentralWidget(self.centralwidget)

        self.retranslateUi(Add_shop)
        QtCore.QMetaObject.connectSlotsByName(Add_shop)

    def retranslateUi(self, Add_shop):
        _translate = QtCore.QCoreApplication.translate
        Add_shop.setWindowTitle(_translate("Add_shop", "Add info"))
        self.label.setText(_translate("Add_shop", "Название товара"))
        self.label_2.setText(_translate("Add_shop", "Цена"))
        self.label_3.setText(_translate("Add_shop", "Произодитель"))
        self.label_4.setText(_translate("Add_shop", "Картинка (путь к файлу, если есть)"))
        self.label_5.setText(_translate("Add_shop", "Количество"))
        self.pushButton.setText(_translate("Add_shop", "Добавить"))
