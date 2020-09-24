# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Павел/PycharmProjects/Museum/add_research_activity.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Add_research_activity(object):
    def setupUi(self, Add_research_activity):
        Add_research_activity.setObjectName("MainWindow")
        Add_research_activity.resize(378, 206)
        Add_research_activity.setMinimumSize(QtCore.QSize(378, 206))
        Add_research_activity.setMaximumSize(QtCore.QSize(378, 206))
        self.centralwidget = QtWidgets.QWidget(Add_research_activity)
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
        Add_research_activity.setCentralWidget(self.centralwidget)

        self.retranslateUi(Add_research_activity)
        QtCore.QMetaObject.connectSlotsByName(Add_research_activity)

    def retranslateUi(self, Add_research_activity):
        _translate = QtCore.QCoreApplication.translate
        Add_research_activity.setWindowTitle(_translate("Add_research_activity", "Add info"))
        self.label.setText(_translate("Add_research_activity", "Название работы"))
        self.label_2.setText(_translate("Add_research_activity", "Дата исследования (ДД.ММ.ГГГГ)"))
        self.label_3.setText(_translate("Add_research_activity", "Автор"))
        self.pushButton.setText(_translate("Add_research_activity", "Добавить"))
