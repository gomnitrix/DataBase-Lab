# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'book_return.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Return(object):
    def setupUi(self, Return):
        Return.setObjectName("Return")
        Return.resize(585, 453)
        self.bk_return_btn = QtWidgets.QPushButton(Return)
        self.bk_return_btn.setGeometry(QtCore.QRect(140, 360, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        self.bk_return_btn.setFont(font)
        self.bk_return_btn.setObjectName("bk_return_btn")
        self.user_id = QtWidgets.QLineEdit(Return)
        self.user_id.setGeometry(QtCore.QRect(230, 240, 211, 21))
        self.user_id.setObjectName("user_id")
        self.bk_loss_btn = QtWidgets.QPushButton(Return)
        self.bk_loss_btn.setGeometry(QtCore.QRect(310, 360, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        self.bk_loss_btn.setFont(font)
        self.bk_loss_btn.setObjectName("bk_loss_btn")
        self.book_id = QtWidgets.QLineEdit(Return)
        self.book_id.setGeometry(QtCore.QRect(230, 300, 211, 21))
        self.book_id.setObjectName("book_id")
        self.label_2 = QtWidgets.QLabel(Return)
        self.label_2.setGeometry(QtCore.QRect(140, 300, 72, 15))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.MessageBox = QtWidgets.QPlainTextEdit(Return)
        self.MessageBox.setEnabled(False)
        self.MessageBox.setGeometry(QtCore.QRect(70, 70, 441, 141))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        self.MessageBox.setFont(font)
        self.MessageBox.setObjectName("MessageBox")
        self.label = QtWidgets.QLabel(Return)
        self.label.setGeometry(QtCore.QRect(140, 240, 72, 15))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Return)
        self.bk_return_btn.clicked.connect(Return.bk_return)
        self.bk_loss_btn.clicked.connect(Return.bk_loss)
        QtCore.QMetaObject.connectSlotsByName(Return)

    def retranslateUi(self, Return):
        _translate = QtCore.QCoreApplication.translate
        Return.setWindowTitle(_translate("Return", "Form"))
        self.bk_return_btn.setText(_translate("Return", "Return"))
        self.bk_loss_btn.setText(_translate("Return", "Loss"))
        self.label_2.setText(_translate("Return", "Book ID:"))
        self.MessageBox.setPlainText(_translate("Return", "                               input user id and book id:"))
        self.label.setText(_translate("Return", "User ID:"))

