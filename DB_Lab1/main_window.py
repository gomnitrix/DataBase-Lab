# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1082, 752)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bk_info = QtWidgets.QTableWidget(self.centralwidget)
        self.bk_info.setGeometry(QtCore.QRect(20, 380, 661, 321))
        self.bk_info.setObjectName("bk_info")
        self.bk_info.setColumnCount(4)
        self.bk_info.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.bk_info.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.bk_info.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.bk_info.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.bk_info.setHorizontalHeaderItem(3, item)
        self.bk_info.horizontalHeader().setCascadingSectionResizes(False)
        self.bk_info.horizontalHeader().setSortIndicatorShown(False)
        self.bk_info.horizontalHeader().setStretchLastSection(False)
        self.bk_bsinfo = QtWidgets.QTableWidget(self.centralwidget)
        self.bk_bsinfo.setGeometry(QtCore.QRect(20, 40, 661, 301))
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
        self.bk_name_line = QtWidgets.QLineEdit(self.centralwidget)
        self.bk_name_line.setGeometry(QtCore.QRect(810, 260, 221, 21))
        self.bk_name_line.setObjectName("bk_name_line")
        self.bk_name = QtWidgets.QLabel(self.centralwidget)
        self.bk_name.setGeometry(QtCore.QRect(710, 260, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        self.bk_name.setFont(font)
        self.bk_name.setObjectName("bk_name")
        self.bk_author_line = QtWidgets.QLineEdit(self.centralwidget)
        self.bk_author_line.setGeometry(QtCore.QRect(810, 300, 221, 21))
        self.bk_author_line.setObjectName("bk_author_line")
        self.bk_author = QtWidgets.QLabel(self.centralwidget)
        self.bk_author.setGeometry(QtCore.QRect(710, 300, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        self.bk_author.setFont(font)
        self.bk_author.setObjectName("bk_author")
        self.bk_publisher = QtWidgets.QLabel(self.centralwidget)
        self.bk_publisher.setGeometry(QtCore.QRect(710, 340, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        self.bk_publisher.setFont(font)
        self.bk_publisher.setObjectName("bk_publisher")
        self.publisher_line = QtWidgets.QLineEdit(self.centralwidget)
        self.publisher_line.setGeometry(QtCore.QRect(810, 340, 221, 21))
        self.publisher_line.setObjectName("publisher_line")
        self.manager_info = QtWidgets.QTableWidget(self.centralwidget)
        self.manager_info.setGeometry(QtCore.QRect(710, 520, 361, 151))
        self.manager_info.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.manager_info.setObjectName("manager_info")
        self.manager_info.setColumnCount(1)
        self.manager_info.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.manager_info.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.manager_info.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(230, 230, 230))
        self.manager_info.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.manager_info.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.manager_info.setHorizontalHeaderItem(0, item)
        self.manager_info.horizontalHeader().setVisible(False)
        self.manager_info.horizontalHeader().setStretchLastSection(True)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 161, 16))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 350, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(710, 470, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(810, 380, 221, 28))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/chaxun.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(710, 380, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(710, 440, 361, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.log_area = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.log_area.setEnabled(False)
        self.log_area.setGeometry(QtCore.QRect(710, 40, 361, 191))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        self.log_area.setFont(font)
        self.log_area.setPlaceholderText("")
        self.log_area.setObjectName("log_area")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1082, 26))
        self.menubar.setObjectName("menubar")
        self.menu_home = QtWidgets.QMenu(self.menubar)
        self.menu_home.setTitle("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_home.setIcon(icon1)
        self.menu_home.setObjectName("menu_home")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_search = QtWidgets.QMenu(self.menubar)
        self.menu_search.setObjectName("menu_search")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        self.menu_5 = QtWidgets.QMenu(self.menubar)
        self.menu_5.setObjectName("menu_5")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLog_In = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../.designer/backup/icons/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLog_In.setIcon(icon2)
        self.actionLog_In.setObjectName("actionLog_In")
        self.new_reg = QtWidgets.QAction(MainWindow)
        self.new_reg.setObjectName("new_reg")
        self.new_book = QtWidgets.QAction(MainWindow)
        self.new_book.setObjectName("new_book")
        self.handle_borrow = QtWidgets.QAction(MainWindow)
        self.handle_borrow.setObjectName("handle_borrow")
        self.handle_return = QtWidgets.QAction(MainWindow)
        self.handle_return.setObjectName("handle_return")
        self.handle_loss = QtWidgets.QAction(MainWindow)
        self.handle_loss.setObjectName("handle_loss")
        self.actionrenew = QtWidgets.QAction(MainWindow)
        self.actionrenew.setObjectName("actionrenew")
        self.item_search = QtWidgets.QAction(MainWindow)
        self.item_search.setObjectName("item_search")
        self.menu_home.addAction(self.actionLog_In)
        self.menu.addAction(self.handle_borrow)
        self.menu_2.addAction(self.handle_return)
        self.menu_3.addAction(self.handle_loss)
        self.menu_search.addAction(self.item_search)
        self.menu_4.addAction(self.new_book)
        self.menu_5.addAction(self.new_reg)
        self.menubar.addAction(self.menu_home.menuAction())
        self.menubar.addAction(self.menu_search.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.bk_search)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.bk_info.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "bk_id"))
        item = self.bk_info.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "BS_ID"))
        item = self.bk_info.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "if_rented"))
        item = self.bk_info.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "storage_time"))
        item = self.bk_bsinfo.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "BS_ID"))
        item = self.bk_bsinfo.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Title"))
        item = self.bk_bsinfo.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Author"))
        item = self.bk_bsinfo.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Type"))
        item = self.bk_bsinfo.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Edition"))
        item = self.bk_bsinfo.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Publisher"))
        item = self.bk_bsinfo.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "C_Num"))
        item = self.bk_bsinfo.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "T_Num"))
        item = self.bk_bsinfo.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Price"))
        self.bk_name.setText(_translate("MainWindow", "Title:"))
        self.bk_author.setText(_translate("MainWindow", "Author:"))
        self.bk_publisher.setText(_translate("MainWindow", "publisher:"))
        item = self.manager_info.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.manager_info.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.manager_info.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Age"))
        item = self.manager_info.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Phone"))
        item = self.manager_info.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        self.label.setText(_translate("MainWindow", "Basic Information"))
        self.label_2.setText(_translate("MainWindow", "Book Information"))
        self.label_3.setText(_translate("MainWindow", "Manager Information:"))
        self.label_4.setText(_translate("MainWindow", "Search:"))
        self.log_area.setPlainText(_translate("MainWindow", "                welcome to use book manager!"))
        self.menu.setTitle(_translate("MainWindow", "借阅"))
        self.menu_2.setTitle(_translate("MainWindow", "归还"))
        self.menu_3.setTitle(_translate("MainWindow", "挂失"))
        self.menu_search.setTitle(_translate("MainWindow", "查询"))
        self.menu_4.setTitle(_translate("MainWindow", "上架"))
        self.menu_5.setTitle(_translate("MainWindow", "注册"))
        self.actionLog_In.setText(_translate("MainWindow", "Log In"))
        self.new_reg.setText(_translate("MainWindow", "new user"))
        self.new_book.setText(_translate("MainWindow", "new book"))
        self.handle_borrow.setText(_translate("MainWindow", "new borrow"))
        self.handle_return.setText(_translate("MainWindow", "handle return"))
        self.handle_loss.setText(_translate("MainWindow", "handle loss"))
        self.actionrenew.setText(_translate("MainWindow", "renew"))
        self.item_search.setText(_translate("MainWindow", "search"))

