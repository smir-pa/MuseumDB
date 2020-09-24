# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Павел/PycharmProjects/Museum/add_excursion.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Add_excursion(object):
    def setupUi(self, Add_excursion):
        Add_excursion.setObjectName("MainWindow")
        Add_excursion.resize(420, 466)
        Add_excursion.setMinimumSize(QtCore.QSize(420, 466))
        Add_excursion.setMaximumSize(QtCore.QSize(420, 466))
        self.centralwidget = QtWidgets.QWidget(Add_excursion)
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
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout.addWidget(self.lineEdit_7)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout.addWidget(self.lineEdit_8)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        Add_excursion.setCentralWidget(self.centralwidget)

        self.retranslateUi(Add_excursion)
        QtCore.QMetaObject.connectSlotsByName(Add_excursion)

    def retranslateUi(self, Add_excursion):
        _translate = QtCore.QCoreApplication.translate
        Add_excursion.setWindowTitle(_translate("Add_excursion", "Add info"))
        self.label.setText(_translate("Add_excursion", "Время начала (ЧЧ:ММ)"))
        self.label_2.setText(_translate("Add_excursion", "График"))
        self.label_3.setText(_translate("Add_excursion", "Конец (дата ДД.ММ.ГГГГ)"))
        self.label_4.setText(_translate("Add_excursion", "Код ответственного"))
        self.label_5.setText(_translate("Add_excursion", "Цена"))
        self.label_6.setText(_translate("Add_excursion", "Название"))
        self.label_7.setText(_translate("Add_excursion", "Номер зала"))
        self.label_8.setText(_translate("Add_excursion", "Мастер-класс (id)"))
        self.pushButton.setText(_translate("Add_excursion", "Добавить"))
