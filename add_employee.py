# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Павел/PycharmProjects/Museum/add_employee.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Add_employee(object):
    def setupUi(self, Add_employee):
        Add_employee.setObjectName("MainWindow")
        Add_employee.resize(378, 258)
        Add_employee.setMinimumSize(QtCore.QSize(378, 258))
        Add_employee.setMaximumSize(QtCore.QSize(378, 258))
        self.centralwidget = QtWidgets.QWidget(Add_employee)
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
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        Add_employee.setCentralWidget(self.centralwidget)

        self.retranslateUi(Add_employee)
        QtCore.QMetaObject.connectSlotsByName(Add_employee)

    def retranslateUi(self, Add_employee):
        _translate = QtCore.QCoreApplication.translate
        Add_employee.setWindowTitle(_translate("Add_employee", "Add info"))
        self.label.setText(_translate("Add_employee", "ФИО"))
        self.label_2.setText(_translate("Add_employee", "Дата рождения (ДД.ММ.ГГГГ)"))
        self.label_3.setText(_translate("Add_employee", "Должность"))
        self.label_4.setText(_translate("Add_employee", "Зарплата"))
        self.pushButton.setText(_translate("Add_employee", "Добавить"))
