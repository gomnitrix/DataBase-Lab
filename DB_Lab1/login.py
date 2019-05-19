# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QLineEdit

class Ui_Login(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.ID = QtWidgets.QLineEdit(Form)
        self.ID.setGeometry(QtCore.QRect(160, 60, 191, 31))
        self.ID.setObjectName("ID")
        self.passwd = QtWidgets.QLineEdit(Form)
        self.passwd.setGeometry(QtCore.QRect(160, 110, 191, 31))
        self.passwd.setObjectName("passwd")
        self.passwd.setEchoMode(QLineEdit.Password)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 60, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btn_login = QtWidgets.QPushButton(Form)
        self.btn_login.setGeometry(QtCore.QRect(120, 210, 151, 28))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        self.btn_login.setFont(font)
        self.btn_login.setObjectName("btn_login")
        self.prompt = QtWidgets.QLineEdit(Form)
        self.prompt.setEnabled(False)
        self.prompt.setGeometry(QtCore.QRect(50, 170, 301, 21))
        self.prompt.setObjectName("prompt")

        self.retranslateUi(Form)
        self.btn_login.clicked.connect(Form.login)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "ID:"))
        self.label_2.setText(_translate("Form", "Pass Word:"))
        self.btn_login.setText(_translate("Form", "Log In"))

