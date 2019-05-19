# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'borrow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Borrow(object):
    def setupUi(self, Borrow):
        Borrow.setObjectName("Borrow")
        Borrow.resize(522, 405)
        self.user_id = QtWidgets.QLineEdit(Borrow)
        self.user_id.setGeometry(QtCore.QRect(200, 210, 211, 21))
        self.user_id.setObjectName("user_id")
        self.book_id = QtWidgets.QLineEdit(Borrow)
        self.book_id.setGeometry(QtCore.QRect(200, 270, 211, 21))
        self.book_id.setObjectName("book_id")
        self.borrow_btn = QtWidgets.QPushButton(Borrow)
        self.borrow_btn.setGeometry(QtCore.QRect(110, 330, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        self.borrow_btn.setFont(font)
        self.borrow_btn.setObjectName("borrow_btn")
        self.label = QtWidgets.QLabel(Borrow)
        self.label.setGeometry(QtCore.QRect(110, 210, 72, 15))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Borrow)
        self.label_2.setGeometry(QtCore.QRect(110, 270, 72, 15))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.MessageBox = QtWidgets.QPlainTextEdit(Borrow)
        self.MessageBox.setEnabled(False)
        self.MessageBox.setGeometry(QtCore.QRect(40, 40, 441, 141))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        self.MessageBox.setFont(font)
        self.MessageBox.setObjectName("MessageBox")
        self.renew_btn = QtWidgets.QPushButton(Borrow)
        self.renew_btn.setGeometry(QtCore.QRect(280, 330, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        self.renew_btn.setFont(font)
        self.renew_btn.setObjectName("renew_btn")

        self.retranslateUi(Borrow)
        self.borrow_btn.clicked.connect(Borrow.borrow)
        self.renew_btn.clicked.connect(Borrow.renew)
        QtCore.QMetaObject.connectSlotsByName(Borrow)

    def retranslateUi(self, Borrow):
        _translate = QtCore.QCoreApplication.translate
        Borrow.setWindowTitle(_translate("Borrow", "Form"))
        self.borrow_btn.setText(_translate("Borrow", "Borrow"))
        self.label.setText(_translate("Borrow", "User ID:"))
        self.label_2.setText(_translate("Borrow", "Book ID:"))
        self.MessageBox.setPlainText(_translate("Borrow", "                               input user id and book id:"))
        self.renew_btn.setText(_translate("Borrow", "Renew"))

