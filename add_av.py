# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Павел/PycharmProjects/Museum/add_av.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Add_av(object):
    def setupUi(self, Add_av):
        Add_av.setObjectName("MainWindow")
        Add_av.resize(443, 278)
        Add_av.setMinimumSize(QtCore.QSize(443, 278))
        Add_av.setMaximumSize(QtCore.QSize(443, 278))
        self.centralwidget = QtWidgets.QWidget(Add_av)
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
        self.pushButton.setMaximumSize(QtCore.QSize(421, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.label.raise_()
        self.lineEdit.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_4.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()
        Add_av.setCentralWidget(self.centralwidget)

        self.retranslateUi(Add_av)
        QtCore.QMetaObject.connectSlotsByName(Add_av)

    def retranslateUi(self, Add_av):
        _translate = QtCore.QCoreApplication.translate
        Add_av.setWindowTitle(_translate("Add_av", "Add info"))
        self.label.setText(_translate("Add_av", "Фамилия, имя, отчество"))
        self.label_2.setText(_translate("Add_av", "Дата рождения (ДД.ММ.ГГГГ)"))
        self.label_3.setText(_translate("Add_av", "Номер телефона (+7ХХХХХХХХХХ)"))
        self.label_4.setText(_translate("Add_av", "Email"))
        self.pushButton.setText(_translate("Add_av", "Добавить"))
