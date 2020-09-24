# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Павел/PycharmProjects/Museum/add_master_class.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Add_master_class(object):
    def setupUi(self, Add_master_class):
        Add_master_class.setObjectName("MainWindow")
        Add_master_class.resize(438, 258)
        Add_master_class.setMinimumSize(QtCore.QSize(438, 258))
        Add_master_class.setMaximumSize(QtCore.QSize(438, 258))
        self.centralwidget = QtWidgets.QWidget(Add_master_class)
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
        Add_master_class.setCentralWidget(self.centralwidget)

        self.retranslateUi(Add_master_class)
        QtCore.QMetaObject.connectSlotsByName(Add_master_class)

    def retranslateUi(self, Add_master_class):
        _translate = QtCore.QCoreApplication.translate
        Add_master_class.setWindowTitle(_translate("Add_master_class", "Add info"))
        self.label.setText(_translate("Add_master_class", "Название"))
        self.label_2.setText(_translate("Add_master_class", "Результат работы"))
        self.label_3.setText(_translate("Add_master_class", "Краткое описание"))
        self.label_4.setText(_translate("Add_master_class", "Номер уголка творчества"))
        self.pushButton.setText(_translate("Add_master_class", "Добавить"))
