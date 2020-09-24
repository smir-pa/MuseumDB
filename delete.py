# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Павел/PycharmProjects/Museum/delete.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Delete(object):
    def setupUi(self, Delete):
        Delete.setObjectName("MainWindow")
        Delete.resize(288, 89)
        Delete.setMinimumSize(QtCore.QSize(288, 89))
        Delete.setMaximumSize(QtCore.QSize(288, 89))
        self.centralwidget = QtWidgets.QWidget(Delete)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        Delete.setCentralWidget(self.centralwidget)

        self.retranslateUi(Delete)
        QtCore.QMetaObject.connectSlotsByName(Delete)

    def retranslateUi(self, Delete):
        _translate = QtCore.QCoreApplication.translate
        Delete.setWindowTitle(_translate("Delete", "Delete"))
        self.label.setText(_translate("Delete", "Удалить по ID. Вы уверены?"))
        self.pushButton.setText(_translate("Delete", "Удалить"))
