# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Павел/PycharmProjects/Museum/add_exhibit.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Add_exhibit(object):
    def setupUi(self, Add_exhibit):
        Add_exhibit.setObjectName("MainWindow")
        Add_exhibit.resize(432, 310)
        Add_exhibit.setMinimumSize(QtCore.QSize(432, 310))
        Add_exhibit.setMaximumSize(QtCore.QSize(432, 310))
        self.centralwidget = QtWidgets.QWidget(Add_exhibit)
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
        Add_exhibit.setCentralWidget(self.centralwidget)

        self.retranslateUi(Add_exhibit)
        QtCore.QMetaObject.connectSlotsByName(Add_exhibit)

    def retranslateUi(self, Add_exhibit):
        _translate = QtCore.QCoreApplication.translate
        Add_exhibit.setWindowTitle(_translate("Add_exhibit", "Add info"))
        self.label.setText(_translate("Add_exhibit", "Название"))
        self.label_2.setText(_translate("Add_exhibit", "Автор"))
        self.label_3.setText(_translate("Add_exhibit", "Картинка (путь к файлу, если есть)"))
        self.label_4.setText(_translate("Add_exhibit", "Дата создания (ДД.ММ.ГГГГ)"))
        self.label_5.setText(_translate("Add_exhibit", "Тип (картина/скульптура)"))
        self.pushButton.setText(_translate("Add_exhibit", "Добавить"))
