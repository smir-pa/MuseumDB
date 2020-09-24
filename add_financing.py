# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Павел/PycharmProjects/Museum/add_financing.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Add_financing(object):
    def setupUi(self, Add_financing):
        Add_financing.setObjectName("MainWindow")
        Add_financing.resize(490, 362)
        Add_financing.setMinimumSize(QtCore.QSize(490, 362))
        Add_financing.setMaximumSize(QtCore.QSize(490, 362))
        self.centralwidget = QtWidgets.QWidget(Add_financing)
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
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout.addWidget(self.lineEdit_6)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        Add_financing.setCentralWidget(self.centralwidget)

        self.retranslateUi(Add_financing)
        QtCore.QMetaObject.connectSlotsByName(Add_financing)

    def retranslateUi(self, Add_financing):
        _translate = QtCore.QCoreApplication.translate
        Add_financing.setWindowTitle(_translate("Add_financing", "Add info"))
        self.label.setText(_translate("Add_financing", "Спонсор"))
        self.label_2.setText(_translate("Add_financing", "Дата финансирования (ДД.ММ.ГГГГ)"))
        self.label_3.setText(_translate("Add_financing", "Сумма финансирования"))
        self.label_4.setText(_translate("Add_financing", "Контактный номер телефона (+7ХХХХХХХХХХ)"))
        self.label_5.setText(_translate("Add_financing", "Фонд (id)"))
        self.label_6.setText(_translate("Add_financing", "Email"))
        self.pushButton.setText(_translate("Add_financing", "Добавить"))
