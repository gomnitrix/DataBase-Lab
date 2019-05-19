# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homework.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(941, 746)
        self.author_line = QtWidgets.QLineEdit(Form)
        self.author_line.setGeometry(QtCore.QRect(210, 60, 241, 21))
        self.author_line.setObjectName("author_line")
        self.title_line = QtWidgets.QLineEdit(Form)
        self.title_line.setGeometry(QtCore.QRect(210, 120, 241, 21))
        self.title_line.setObjectName("title_line")
        self.publisher_line = QtWidgets.QLineEdit(Form)
        self.publisher_line.setGeometry(QtCore.QRect(210, 180, 241, 21))
        self.publisher_line.setObjectName("publisher_line")
        self.type_line = QtWidgets.QLineEdit(Form)
        self.type_line.setGeometry(QtCore.QRect(580, 60, 231, 21))
        self.type_line.setObjectName("type_line")
        self.edition_line = QtWidgets.QLineEdit(Form)
        self.edition_line.setGeometry(QtCore.QRect(580, 120, 231, 21))
        self.edition_line.setObjectName("edition_line")
        self.price_start = QtWidgets.QLineEdit(Form)
        self.price_start.setGeometry(QtCore.QRect(580, 180, 101, 21))
        self.price_start.setObjectName("price_start")
        self.price_end = QtWidgets.QLineEdit(Form)
        self.price_end.setGeometry(QtCore.QRect(710, 180, 101, 21))
        self.price_end.setObjectName("price_end")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 60, 72, 15))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(90, 120, 72, 15))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(90, 180, 72, 15))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(470, 60, 72, 15))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(470, 120, 72, 15))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(470, 180, 72, 15))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(180, 60, 16, 19))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(180, 120, 16, 19))
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(Form)
        self.checkBox_3.setGeometry(QtCore.QRect(180, 180, 16, 19))
        self.checkBox_3.setText("")
        self.checkBox_3.setObjectName("checkBox_3")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(690, 180, 21, 16))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.checkBox_4 = QtWidgets.QCheckBox(Form)
        self.checkBox_4.setGeometry(QtCore.QRect(550, 60, 16, 19))
        self.checkBox_4.setText("")
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(Form)
        self.checkBox_5.setGeometry(QtCore.QRect(550, 120, 16, 19))
        self.checkBox_5.setText("")
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(Form)
        self.checkBox_6.setGeometry(QtCore.QRect(550, 180, 16, 19))
        self.checkBox_6.setText("")
        self.checkBox_6.setObjectName("checkBox_6")
        self.sql_area = QtWidgets.QPlainTextEdit(Form)
        self.sql_area.setEnabled(False)
        self.sql_area.setGeometry(QtCore.QRect(90, 270, 751, 151))
        self.sql_area.setObjectName("sql_area")
        self.bk_bsinfo = QtWidgets.QTableWidget(Form)
        self.bk_bsinfo.setGeometry(QtCore.QRect(90, 430, 751, 301))
        self.bk_bsinfo.setObjectName("bk_bsinfo")
        self.bk_bsinfo.setColumnCount(9)
        self.bk_bsinfo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.bk_bsinfo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.bk_bsinfo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.bk_bsinfo.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.bk_bsinfo.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.bk_bsinfo.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.bk_bsinfo.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.bk_bsinfo.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.bk_bsinfo.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.bk_bsinfo.setHorizontalHeaderItem(8, item)
        self.search = QtWidgets.QPushButton(Form)
        self.search.setGeometry(QtCore.QRect(310, 220, 291, 28))
        self.search.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/chaxun.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search.setIcon(icon)
        self.search.setObjectName("search")

        self.retranslateUi(Form)
        self.checkBox.stateChanged['int'].connect(Form.set_author)
        self.checkBox_2.stateChanged['int'].connect(Form.set_title)
        self.checkBox_3.stateChanged['int'].connect(Form.set_publisher)
        self.checkBox_4.stateChanged['int'].connect(Form.set_type)
        self.checkBox_5.stateChanged['int'].connect(Form.set_edition)
        self.checkBox_6.stateChanged['int'].connect(Form.set_price)
        self.search.clicked.connect(Form.search)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "author:"))
        self.label_2.setText(_translate("Form", "title:"))
        self.label_3.setText(_translate("Form", "publisher:"))
        self.label_4.setText(_translate("Form", "type:"))
        self.label_5.setText(_translate("Form", "edition:"))
        self.label_6.setText(_translate("Form", "price from"))
        self.label_7.setText(_translate("Form", "to"))
        item = self.bk_bsinfo.horizontalHeaderItem(0)
        item.setText(_translate("Form", "BS_ID"))
        item = self.bk_bsinfo.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Title"))
        item = self.bk_bsinfo.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Author"))
        item = self.bk_bsinfo.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Type"))
        item = self.bk_bsinfo.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Edition"))
        item = self.bk_bsinfo.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Publisher"))
        item = self.bk_bsinfo.horizontalHeaderItem(6)
        item.setText(_translate("Form", "C_Num"))
        item = self.bk_bsinfo.horizontalHeaderItem(7)
        item.setText(_translate("Form", "T_Num"))
        item = self.bk_bsinfo.horizontalHeaderItem(8)
        item.setText(_translate("Form", "Price"))


from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem
from DB_Helper import DBHelper
from PyQt5.QtCore import Qt
import sys
from Basic import Book


class MyHomeWork(QWidget):
    def __init__(self, mydb_helper):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Searcher")
        self.mydb_helper = mydb_helper
        self.author = None
        self.title = None
        self.publisher = None
        self.type = None
        self.edition = None
        self.price = []

    def set_author(self, state):
        if state == Qt.Checked:
            self.author = self.ui.author_line.text()
        else:
            self.author = ""

    def set_title(self, state):
        if state == Qt.Checked:
            self.title = self.ui.title_line.text()
        else:
            self.title = ""

    def set_publisher(self, state):
        if state == Qt.Checked:
            self.publisher = self.ui.publisher_line.text()
        else:
            self.publisher = ""

    def set_type(self, state):
        if state == Qt.Checked:
            self.type = self.ui.type_line.text()
        else:
            self.type = ""

    def set_edition(self, state):
        if state == Qt.Checked:
            self.edition = self.ui.edition_line.text()
        else:
            self.edition = ""

    def set_price(self, state):
        if state == Qt.Checked:
            self.price.append(float(self.ui.price_start.text()))
            self.price.append(float(self.ui.price_end.text()))
        else:
            self.price = []

    def get_headers(self):
        bs_items = []
        bk_bsinfo = self.ui.bk_bsinfo
        for i in range(9):
            item = bk_bsinfo.horizontalHeaderItem(i).text().lower()
            if item == "type":
                item = "bk_type"
            elif item == "bs_id":
                item = 'BS_ID'
            elif item == "c_num":
                item = "cur_amount"
            elif item == "t_num":
                item = "tol_amount"
            bs_items.append(item)
        return bs_items

    def search(self):
        book = Book(self.title, self.author, self.publisher, self.type, self.edition, self.price)
        sql = "select * from book_management_system.book_bsinfo where "
        pros = []
        if book.title:
            pros.append("title = '{}'".format(book.title))
        if book.author:
            pros.append("author = '{}'".format(book.author))
        if book.publisher:
            pros.append("publisher like '%{}%'".format(book.publisher))
        if self.edition:
            pros.append("edition = '{}'".format(book.edition))
        if self.type:
            pros.append("bk_type = '{}'".format(book.bk_type))
        if self.price:
            pros.append("price between {} and {}".format(*self.price))
        pros = " and ".join(pros)
        sql += pros
        self.ui.sql_area.clear()
        self.ui.sql_area.setPlainText(sql)
        base_info = self.mydb_helper.search_book_bsinfo(book, edition=self.edition, sql=sql)
        if self.edition: base_info = [base_info]
        bs_len = len(base_info)
        bk_bsinfo = self.ui.bk_bsinfo
        bk_bsinfo.setRowCount(bs_len)
        bk_bsinfo.verticalHeader().setVisible(False)
        bs_items = self.get_headers()
        for i in range(bs_len):
            for j in range(9):
                item = bs_items[j]
                bk_bsinfo.setItem(i, j, QTableWidgetItem(str(base_info[i][item])))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_helper = DBHelper()
    home_work = MyHomeWork(my_helper)
    home_work.show()
    sys.exit(app.exec_())
