# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Павел/PycharmProjects/Museum/add_employee_workplace.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Add_employee_workplace(object):
    def setupUi(self, Add_employee_workplace):
        Add_employee_workplace.setObjectName("MainWindow")
        Add_employee_workplace.resize(342, 206)
        Add_employee_workplace.setMinimumSize(QtCore.QSize(342, 206))
        Add_employee_workplace.setMaximumSize(QtCore.QSize(342, 206))
        self.centralwidget = QtWidgets.QWidget(Add_employee_workplace)
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
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        Add_employee_workplace.setCentralWidget(self.centralwidget)

        self.retranslateUi(Add_employee_workplace)
        QtCore.QMetaObject.connectSlotsByName(Add_employee_workplace)

    def retranslateUi(self, Add_employee_workplace):
        _translate = QtCore.QCoreApplication.translate
        Add_employee_workplace.setWindowTitle(_translate("Add_employee_workplace", "Add info"))
        self.label.setText(_translate("Add_employee_workplace", "Тип помещения"))
        self.label_2.setText(_translate("Add_employee_workplace", "id помещения"))
        self.label_3.setText(_translate("Add_employee_workplace", "id сотрудника"))
        self.pushButton.setText(_translate("Add_employee_workplace", "Добавить"))
