# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'book_insert.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Insert(object):
    def setupUi(self, Insert):
        Insert.setObjectName("Insert")
        Insert.resize(886, 312)
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        Insert.setFont(font)
        self.title_line = QtWidgets.QLineEdit(Insert)
        self.title_line.setGeometry(QtCore.QRect(100, 60, 241, 21))
        self.title_line.setObjectName("title_line")
        self.publisher_line = QtWidgets.QLineEdit(Insert)
        self.publisher_line.setGeometry(QtCore.QRect(100, 110, 241, 21))
        self.publisher_line.setObjectName("publisher_line")
        self.author_line = QtWidgets.QLineEdit(Insert)
        self.author_line.setGeometry(QtCore.QRect(450, 60, 241, 21))
        self.author_line.setObjectName("author_line")
        self.edition_line = QtWidgets.QLineEdit(Insert)
        self.edition_line.setGeometry(QtCore.QRect(100, 160, 121, 21))
        self.edition_line.setObjectName("edition_line")
        self.amount_line = QtWidgets.QLineEdit(Insert)
        self.amount_line.setGeometry(QtCore.QRect(570, 160, 121, 21))
        self.amount_line.setObjectName("amount_line")
        self.type_line = QtWidgets.QLineEdit(Insert)
        self.type_line.setGeometry(QtCore.QRect(450, 110, 241, 21))
        self.type_line.setObjectName("type_line")
        self.price_line = QtWidgets.QLineEdit(Insert)
        self.price_line.setGeometry(QtCore.QRect(320, 160, 131, 21))
        self.price_line.setObjectName("price_line")
        self.label = QtWidgets.QLabel(Insert)
        self.label.setGeometry(QtCore.QRect(20, 60, 72, 15))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Insert)
        self.label_2.setGeometry(QtCore.QRect(370, 60, 72, 15))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Insert)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 72, 15))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Insert)
        self.label_4.setGeometry(QtCore.QRect(370, 110, 72, 15))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Insert)
        self.label_5.setGeometry(QtCore.QRect(20, 160, 72, 15))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Insert)
        self.label_6.setGeometry(QtCore.QRect(260, 160, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Insert)
        self.label_7.setGeometry(QtCore.QRect(490, 160, 72, 15))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.insert_btn = QtWidgets.QPushButton(Insert)
        self.insert_btn.setGeometry(QtCore.QRect(720, 60, 131, 121))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        self.insert_btn.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/insert.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.insert_btn.setIcon(icon)
        self.insert_btn.setIconSize(QtCore.QSize(32, 32))
        self.insert_btn.setObjectName("insert_btn")
        self.message_box = QtWidgets.QPlainTextEdit(Insert)
        self.message_box.setEnabled(False)
        self.message_box.setGeometry(QtCore.QRect(20, 210, 831, 87))
        self.message_box.setObjectName("message_box")

        self.retranslateUi(Insert)
        self.insert_btn.clicked.connect(Insert.book_insert)
        QtCore.QMetaObject.connectSlotsByName(Insert)

    def retranslateUi(self, Insert):
        _translate = QtCore.QCoreApplication.translate
        Insert.setWindowTitle(_translate("Insert", "Form"))
        self.label.setText(_translate("Insert", "Title:"))
        self.label_2.setText(_translate("Insert", "Author:"))
        self.label_3.setText(_translate("Insert", "Publisher:"))
        self.label_4.setText(_translate("Insert", "Type:"))
        self.label_5.setText(_translate("Insert", "Edition:"))
        self.label_6.setText(_translate("Insert", "Price:"))
        self.label_7.setText(_translate("Insert", "Amount:"))
        self.insert_btn.setText(_translate("Insert", "insert:"))

