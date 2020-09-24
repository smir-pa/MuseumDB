# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Павел/PycharmProjects/Museum/add_sale.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Add_sale(object):
    def setupUi(self, Add_sale):
        Add_sale.setObjectName("MainWindow")
        Add_sale.resize(250, 206)
        Add_sale.setMinimumSize(QtCore.QSize(250, 206))
        Add_sale.setMaximumSize(QtCore.QSize(250, 206))
        self.centralwidget = QtWidgets.QWidget(Add_sale)
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
        Add_sale.setCentralWidget(self.centralwidget)

        self.retranslateUi(Add_sale)
        QtCore.QMetaObject.connectSlotsByName(Add_sale)

    def retranslateUi(self, Add_sale):
        _translate = QtCore.QCoreApplication.translate
        Add_sale.setWindowTitle(_translate("Add_sale", "Add info"))
        self.label.setText(_translate("Add_sale", "id товара"))
        self.label_2.setText(_translate("Add_sale", "Количество"))
        self.label_3.setText(_translate("Add_sale", "Фонд (id)"))
        self.pushButton.setText(_translate("Add_sale", "Добавить"))
