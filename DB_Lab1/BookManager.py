import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from Basic import *
from DB_Helper import DBHelper
from book_insert import Ui_Insert
from borrow import Ui_Borrow
from login import Ui_Login
from main_window import Ui_MainWindow
from register import Ui_Register
from PyQt5 import QtGui


class LoginWindow(QMainWindow):
    def __init__(self, home, mydb_helper):
        QMainWindow.__init__(self)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.setWindowTitle("LogIn")
        self.home = home
        self.db_helper = mydb_helper

    def manager_init(self, manager_id):
        self.home.main_Ui.bk_info.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        info = self.home.main_Ui.manager_info
        manager = self.db_helper.get_manager_info(manager_id)
        idItem = QTableWidgetItem(str(manager["manager_id"]))
        ageItem = QTableWidgetItem(str(manager["manager_age"]))
        nameItem = QTableWidgetItem(manager["manager_name"])
        phoneItem = QTableWidgetItem(manager["manager_phone"])
        info.setItem(0, 0, idItem)
        info.setItem(1, 0, nameItem)
        info.setItem(2, 0, ageItem)
        info.setItem(3, 0, phoneItem)
        items = [idItem, ageItem, nameItem, phoneItem]
        for item in items:
            item.setTextAlignment(Qt.AlignCenter)

    def login(self):
        manager_id = self.ui.ID.text()
        passwd = self.ui.passwd.text()
        log = self.db_helper.check_login(manager_id, passwd)
        if log:
            self.manager_init(manager_id)
            self.home.show()
            self.close()
        else:
            self.ui.prompt.insert("wrong password!")


class HomePage(QMainWindow):
    def __init__(self, mydb_helper):
        QMainWindow.__init__(self)
        self.main_Ui = Ui_MainWindow()
        self.main_Ui.setupUi(self)
        self.setWindowTitle("BookManager")
        self.mydb_helper = mydb_helper
        self.regi_page = None
        self.insert_page = None
        self.brw_page = None
        self.rt_page = None
        self.search_page = None
        self.main_Ui.new_reg.triggered.connect(self.register)
        self.main_Ui.new_book.triggered.connect(self.insert_book_page_show)
        self.main_Ui.handle_borrow.triggered.connect(self.borrow_page_show)
        self.main_Ui.handle_return.triggered.connect(self.return_page_show)
        self.main_Ui.handle_loss.triggered.connect(self.return_page_show)
        self.main_Ui.item_search.triggered.connect(self.search_page_show)
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("./icons/background.png")))
        self.setPalette(window_pale)
    def get_headers(self):
        bs_items, bk_items = [], []
        bk_bsinfo = self.main_Ui.bk_bsinfo
        bk_info = self.main_Ui.bk_info
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
        for i in range(4):
            bk_items.append(bk_info.horizontalHeaderItem(i).text())
        return bs_items, bk_items

    def bk_search(self):
        bk_title = self.main_Ui.bk_name_line.text()
        bk_author = self.main_Ui.bk_author_line.text()
        bk_publisher = self.main_Ui.publisher_line.text()
        if not (bk_title or bk_author or bk_publisher):
            self.main_Ui.log_area.setPlainText("please input something...")
            return
        book = Book(bk_title, bk_author, bk_publisher)
        base_info, books = self.mydb_helper.search_book(book)
        if not base_info:
            self.main_Ui.log_area.setPlainText("no such book...")
            return
        bs_len = len(base_info)
        bk_len = 0
        for i in range(bs_len):
            bk_len += len(books[i])
        bk_bsinfo, bk_info = self.main_Ui.bk_bsinfo, self.main_Ui.bk_info
        bk_bsinfo.setRowCount(bs_len)
        bk_info.setRowCount(bk_len)
        bk_bsinfo.verticalHeader().setVisible(False)
        bk_info.verticalHeader().setVisible(False)
        bk_index = 0
        bs_items, bk_items = self.get_headers()
        for i in range(bs_len):
            for j in range(9):
                item = bs_items[j]
                bk_bsinfo.setItem(i, j, QTableWidgetItem(str(base_info[i][item])))
            for k in range(len(books[i])):
                for l in range(4):
                    item = bk_items[l]
                    bk_info.setItem(bk_index, l, QTableWidgetItem(str(books[i][k][item])))
                bk_index += 1

    def register(self):
        self.regi_page = None
        self.regi_page = Register(self.mydb_helper)
        self.regi_page.show()

    def insert_book_page_show(self):
        self.insert_page = None
        self.insert_page = Insertor(self.mydb_helper)
        self.insert_page.show()

    def borrow_page_show(self):
        self.brw_page = None
        self.brw_page = Borrow(self.mydb_helper)
        self.brw_page.show()

    def return_page_show(self):
        self.rt_page = None
        self.rt_page = Borrow(self.mydb_helper)
        self.rt_page.setWindowTitle("Return")
        self.rt_page.ui.borrow_btn.setText("Return")
        self.rt_page.ui.borrow_btn.clicked.connect(self.rt_page.bk_return)
        self.rt_page.ui.renew_btn.setText("Loss")
        self.rt_page.ui.renew_btn.clicked.connect(self.rt_page.bk_loss)
        self.rt_page.show()

    def search_page_show(self):
        self.search_page = None
        self.search_page = Search(self.mydb_helper)
        self.search_page.show()


class Register(QWidget):
    def __init__(self, mydb_helper):
        QWidget.__init__(self)
        self.ui = Ui_Register()
        self.ui.setupUi(self)
        self.setWindowTitle("Register")
        self.mydb_helper = mydb_helper

    def regi_submit(self):
        name = self.ui.name_line.text()
        phone = self.ui.phone_line.text()
        user_type = self.ui.user_type.currentText()
        sex = "M" if self.ui.male.isChecked() else "F" if self.ui.female.isChecked() else None
        if name and phone and user_type and sex:
            reader = Reader(name, sex, user_type, phone)
            self.mydb_helper.db_register(reader)
            self.close()
        else:
            self.ui.message_box.insert("null line exist!")


class Insertor(QWidget):
    def __init__(self, mydb_helper):
        QWidget.__init__(self)
        self.ui = Ui_Insert()
        self.ui.setupUi(self)
        self.setWindowTitle("Insertor")
        self.mydb_helper = mydb_helper

    def book_insert(self):
        title = self.ui.title_line.text()
        author = self.ui.author_line.text()
        publisher = self.ui.publisher_line.text()
        bk_type = self.ui.type_line.text()
        edition = int(self.ui.edition_line.text())
        price = float(self.ui.price_line.text())
        amount = int(self.ui.amount_line.text())
        setText = lambda x: self.ui.message_box.setPlainText(str(x))
        self.ui.message_box.clear()
        if not (title and author and publisher and bk_type):
            setText("title,author,publisher and type must be filled")
        else:
            book = Book(title, author, publisher, bk_type, edition, price, amount)
            try:
                self.mydb_helper.insert_book(book)
                setText("Inserted successfully!")
            except DbException as e:
                setText(e)


class Borrow(QWidget):
    def __init__(self, mydb_helper):
        QWidget.__init__(self)
        self.ui = Ui_Borrow()
        self.ui.setupUi(self)
        self.setWindowTitle("Borrow")
        self.mydb_helper = mydb_helper
        self.setText = lambda x: self.ui.MessageBox.setPlainText(str(x))

    def pre_handle(self, handler):
        setText = self.setText
        user_id = self.ui.user_id.text()
        bk_id = self.ui.book_id.text()
        if user_id and bk_id:
            try:
                handler(user_id, bk_id)
                setText("success!")
            except Exception as e:
                setText(e)
        else:
            setText("user and book could not be blank...")

    def borrow(self):
        self.pre_handle(self.mydb_helper.borrow)

    def renew(self):
        self.pre_handle(self.mydb_helper.renew)

    def bk_return(self):
        self.pre_handle(self.mydb_helper.bk_return)

    def bk_loss(self):
        self.pre_handle(self.mydb_helper.bk_loss)


from search import Ui_Search


class Search(QWidget):
    def __init__(self, mydb_helper):
        QWidget.__init__(self)
        self.ui = Ui_Search()
        self.ui.setupUi(self)
        self.setWindowTitle("Search")
        self.mydb_helper = mydb_helper

    def table_init(self):
        self.ui.borrow_table.verticalHeader().setVisible(False)
        self.ui.return_table.verticalHeader().setVisible(False)
        self.ui.ticket_table.verticalHeader().setVisible(False)

    def set_table_columns(self, bor_list, ret_list, tic_list):
        if bor_list:
            bor_list = list(bor_list[0].keys())
            self.ui.borrow_table.setColumnCount(len(bor_list))
            if len(bor_list) <= 3: self.ui.borrow_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.ui.borrow_table.setHorizontalHeaderLabels(bor_list)
        if ret_list:
            ret_list = list(ret_list[0].keys())
            self.ui.return_table.setColumnCount(len(ret_list))
            if len(ret_list) <= 3: self.ui.return_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.ui.return_table.setHorizontalHeaderLabels(ret_list)
        if tic_list:
            tic_list = list(tic_list[0].keys())
            self.ui.ticket_table.setColumnCount(len(tic_list))
            if len(tic_list) <= 3: self.ui.ticket_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.ui.ticket_table.setHorizontalHeaderLabels(tic_list)

    def set_items(self, table, results):
        if not results:
            table.clear()
        else:
            table.setRowCount(len(results))
            for i in range(len(results)):
                item = list(results[i].values())
                for j in range(len(item)):
                    qitem = QTableWidgetItem(str(item[j]))
                    table.setItem(i, j, qitem)
                    qitem.setTextAlignment(Qt.AlignCenter)

    def prepare(self, borrow_items, return_items, ticket_items):
        self.set_table_columns(borrow_items, return_items, ticket_items)
        self.table_init()
        self.set_items(self.ui.borrow_table, borrow_items)
        self.set_items(self.ui.return_table, return_items)
        self.set_items(self.ui.ticket_table, ticket_items)

    def normal(self):
        reader_id = self.ui.reader_id.text()
        book_id = self.ui.book_id.text()
        if not (reader_id or book_id):
            self.ui.MessageBox.setPlainText("information not be completed...")
        else:
            try:
                borrow_items, return_items, ticket_items = self.mydb_helper.search_items(reader_id, book_id)
                self.prepare(borrow_items, return_items, ticket_items)
            except DbException as e:
                self.ui.MessageBox.setPlainText(str(e))

    def user_group(self):
        try:
            borrow_items, return_items, ticket_items = self.mydb_helper.group_search("group by reader_id")
            self.prepare(borrow_items, return_items, ticket_items)
        except DbException as e:
            self.ui.MessageBox.setPlainText(str(e))

    def book_group(self):
        try:
            borrow_items, return_items, ticket_items = self.mydb_helper.group_search("group by bk_id")
            self.prepare(borrow_items, return_items, ticket_items)
        except DbException as e:
            self.ui.MessageBox.setPlainText(str(e))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    db_helper = DBHelper()
    home_page = HomePage(db_helper)
    login_page = LoginWindow(home_page, db_helper)
    login_page.show()
    sys.exit(app.exec_())
