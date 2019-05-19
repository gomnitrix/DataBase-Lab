# author = liuwei date = 2017-06-02
# 数据库帮助类
import pymysql
from Basic import *

__metaclass__ = type


class DBHelper:
    @staticmethod
    def get_con():
        config = {
            'host': 'localhost',
            'port': 3306,
            'user': '1160300103',
            'password': '19981017',
            'db': 'book_management_system',
            'charset': 'utf8',
            'cursorclass': pymysql.cursors.DictCursor,
        }
        '''获取操作数据库的curcor即游标，首先的建立连接，需要服务器地址，端口号，用户名，密码和数据库名'''
        conn = pymysql.connect(**config)
        return conn

    @staticmethod
    def execute(sql, conn, args=None):
        if not conn:
            raise DbException("connect failed")
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        num = cursor.execute(sql, args)
        return cursor, num

    @staticmethod
    def close(conn=None, cursor=None):
        if conn:
            conn.close()
        if cursor:
            cursor.close()

    def search_book(self, book):
        base_info = self.search_book_bsinfo(book, edition=False)
        if base_info:
            conn, cursor = self.get_con(), None
            books = []
            try:
                for info in base_info:
                    BS_ID = info["BS_ID"]
                    sql = "select * from book_info where BS_ID='{}'".format(BS_ID)
                    cursor, num = self.execute(sql, conn)
                    books.append(cursor.fetchall())
            except DbException:
                raise DbException("search failed")
            finally:
                self.close(conn, cursor)
        else:
            books = None
        return base_info, books

    def search_book_bsinfo(self, book, edition=True, sql=None):
        if not sql:
            sql = "select * from book_management_system.book_bsinfo where "
            pros = []
            if not (book.title or book.author or book.publisher):
                raise DbException("could not search null")
            if book.title:
                pros.append("title = '{}'".format(book.title))
            if book.author:
                pros.append("author = '{}'".format(book.author))
            if book.publisher:
                pros.append("publisher = '{}'".format(book.publisher))
            if edition:
                pros.append("edition = '{}'".format(book.edition))
            pros = " and ".join(pros)
            sql += pros
        cursor, conn = None, DBHelper.get_con()
        try:
            cursor, num = self.execute(sql, conn)
            if not num:
                return None
            res = cursor.fetchall()
            if edition:
                return res[0]
            else:
                return res
        except DbException as e:
            raise DbException("search book_bsinfo failed")
        finally:
            DBHelper.close(conn, cursor)

    def insert_book(self, book):
        '''
            向数据库中book表插入书本信息，book为Book类对象，包含书本基本信息
        '''
        exist = self.search_book_bsinfo(book)
        conn = DBHelper.get_con()
        cursor = None
        try:
            if exist:
                BS_ID = exist['BS_ID']
                sql = "update book_bsinfo set cur_amount = cur_amount + '{}', tol_amount = tol_amount + '{}' where BS_ID = '{}'".format(
                    book.amount,
                    book.amount,
                    BS_ID)
                cursor, num = self.execute(sql, conn=conn)
            else:
                sql = "insert into book_bsinfo (title,author,bk_type,edition,price,publisher,cur_amount,tol_amount) " \
                      "values (%s, %s, %s, %s, %s, %s, %s, %s)"
                cursor, num = self.execute(sql, args=(book.title, book.author,
                                                      book.bk_type, book.edition,
                                                      book.price,
                                                      book.publisher,
                                                      book.amount,
                                                      book.amount), conn=conn)
                BS_ID = cursor.lastrowid
            sql = "insert into book_info (BS_ID) values ('{}')".format(BS_ID)
            for i in range(book.amount):
                self.execute(sql, conn)
            print("insert success!")
        except Exception as e:
            conn.rollback()
            raise DbException("insert failed!")
        finally:
            conn.commit()
            DBHelper.close(conn, cursor)

    def check_login(self, manager_id, manager_pwd):
        conn, cursor, passwd = DBHelper.get_con(), None, None
        sql = "select passwd from manager where manager_id = '{}'".format(manager_id)
        try:
            cursor, num = self.execute(sql, conn)
            item = cursor.fetchone()
            passwd = item["passwd"]
        except pymysql.Error as e:
            pass
        finally:
            self.close(conn, cursor)
        if manager_pwd == passwd:
            return True
        else:
            return False

    def get_manager_info(self, manager_id):
        conn = self.get_con()
        cursor, manager = None, None
        sql = "select * from manager where manager_id='{}'".format(manager_id)
        try:
            cursor, num = self.execute(sql, conn)
            manager = cursor.fetchone()
        except pymysql.Error as e:
            print(e)
        finally:
            self.close(conn, cursor)
        return manager

    def db_register(self, reader):
        conn = self.get_con()
        cursor = None
        sql = "insert into readers (name,phone,sex,type) values ('{}','{}','{}','{}')".format(
            reader.name, reader.phone, reader.sex, reader.type)
        try:
            cursor, num = self.execute(sql, conn)
            if not num:
                raise DbException("register failed")
        except DbException as e:
            conn.rollback()
        finally:
            conn.commit()
            self.close(conn, cursor)

    def borrow(self, user_id, book_id):
        sql_user = "select 可借册数-borrow_num as remain,可借时间 as borrow_time from readers,reader_type where readers.type " \
                   "= reader_type.身份 and userID='{}'".format(user_id)
        sql_book = "select if_rented,BS_ID from book_info where bk_id = '{}'".format(book_id)
        sql_insert = "insert into borrow (bk_id,reader_id,borrow_date,return_date) values " \
                     "(%s,%s,current_date(),date_add(current_date(),INTERVAL %s DAY))"
        conn = self.get_con()
        cursor = None
        try:
            cursor, num = self.execute(sql_user, conn)
            if not num:
                raise DbException("no such user... please check you input")
            item = cursor.fetchone()
            user_remain = int(item['remain'])
            borrow_time = item['borrow_time']
            if user_remain <= 0:
                raise DbException("Your available borrows are insufficient")
            cursor, num = self.execute(sql_book, conn)
            if not num:
                raise DbException("no such book...please check your input")
            book = cursor.fetchone()
            book_state = book['if_rented']
            BS_ID = book['BS_ID']
            if book_state == 'Yes':
                raise DbException("this book is already be borrowed,you could choose another one")
            cursor, num = self.execute(sql_insert, conn, (book_id, user_id, borrow_time))
            sql_user = "update readers set borrow_num = borrow_num + 1 where userID = '{}'".format(user_id)
            sql_book = "update book_info set if_rented = 'Yes' where bk_id = '{}'".format(book_id)
            cursor, num1 = self.execute(sql_user, conn)
            cursor, num2 = self.execute(sql_book, conn)
            sql_book = "update book_bsinfo set cur_amount = cur_amount-1 where BS_ID = '{}'".format(BS_ID)
            cursor, num3 = self.execute(sql_book, conn)
            if not num1 or not num2 or not num3:
                raise DbException("borrow failed...")
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.commit()
            self.close(conn, cursor)

    def renew(self, user_id, book_id):
        sql_user = "select borrow_id,可续借次数-renew_num as renew_times,可借时间 as bw_time " \
                   "from borrow natural join readers natural join reader_type where userID='{}' and bk_id='{}';".format(
            user_id, book_id)
        conn, cursor = self.get_con(), None
        try:
            cursor, num = self.execute(sql_user, conn)
            if not num:
                raise DbException("no such user or borrow record")
            user = cursor.fetchone()
            renew_num = user['renew_times']
            bw_time = user['bw_time']
            borrow_id = user['borrow_id']
            if renew_num <= 0:
                raise DbException("your renewal time is insufficient")
            sql_borrow = "update borrow set renew_num = renew_num+1, " \
                         "return_date = date_add(return_date,INTERVAL %s DAY) where borrow_id = %s"
            cursor, num = self.execute(sql_borrow, conn, (bw_time, borrow_id))
            if not num:
                raise DbException("update failed")
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.commit()
            self.close(conn, cursor)

    def bk_return(self, user_id, book_id):
        sql_check = "select borrow_id,datediff(borrow.return_date,current_date()) as diff from borrow " \
                    "where reader_id='{}' and bk_id = '{}'".format(
            user_id, book_id)
        conn, cursor = self.get_con(), None
        try:
            cursor, num = self.execute(sql_check, conn)
            if not num:
                raise DbException("no such borrow record")
            item = cursor.fetchone()
            if_overdue = item['diff']
            borrow_id = item['borrow_id']
            if if_overdue < 0:
                sql_ticket = "insert into ticket (bk_id,reader_id,amount) values ('{}','{}','{}')".format(book_id,
                                                                                                          user_id, abs(
                        if_overdue))
                cursor, num = self.execute(sql_ticket, conn)
                if not num: raise DbException("make ticket failed...")
            sql_delete = "delete from borrow where borrow_id = '{}'".format(borrow_id)
            cursor, num = self.execute(sql_delete, conn)
            if not num: raise DbException("cancel borrow record failed...")
            sql_return = "insert into bk_return (bk_id,reader_id) values ('{}','{}')".format(book_id, user_id)
            cursor, num = self.execute(sql_return, conn)
            if not num: raise DbException("insert to bk_return failed...")
            sql_user = "update readers set borrow_num = borrow_num - 1 where userID = '{}'".format(user_id)
            sql_book = "update book_bsinfo set cur_amount = cur_amount+1 where BS_ID in " \
                       "(select BS_ID from book_info where bk_id = '{}')".format(
                book_id)
            cursor, num1 = self.execute(sql_user, conn)
            cursor, num2 = self.execute(sql_book, conn)
            sql_book = "update book_info set if_rented = 'No' where bk_id = '{}'".format(book_id)
            cursor, num3 = self.execute(sql_book, conn)
            if not (num1 and num2 and num3): raise DbException("update failed...")
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.commit()
            self.close(conn, cursor)

    def bk_loss(self, user_id, book_id):
        conn, cursor = self.get_con(), None
        try:
            sql_book = "select BS_ID,price from book_bsinfo natural join book_info where book_info.bk_id = '{}'".format(
                book_id)
            cursor, num = self.execute(sql_book, conn)
            if not num: raise Exception("no such book...")
            book = cursor.fetchone()
            price = book['price']
            BS_ID = book['BS_ID']
            sql_ticket = "insert into ticket (bk_id,reader_id,amount) values ('{}','{}','{}')".format(book_id,
                                                                                                      user_id,
                                                                                                      int(price))
            cursor, num = self.execute(sql_ticket, conn)
            if not num: raise DbException("make ticket failed...")
            sql_delete = "delete from borrow where reader_id = '{}' and bk_id = '{}'".format(user_id, book_id)
            cursor, num = self.execute(sql_delete, conn)
            if not num: raise DbException("cancel borrow record failed...")
            sql_user = "update readers set borrow_num = borrow_num - 1 where userID = '{}'".format(user_id)
            sql_book = "update book_bsinfo set tol_amount = tol_amount-1 where BS_ID = '{}'".format(BS_ID)
            cursor, num1 = self.execute(sql_user, conn)
            cursor, num2 = self.execute(sql_book, conn)
            sql_set1 = "set foreign_key_checks = 0"
            sql_book = "delete from book_info where bk_id = '{}'".format(book_id)
            sql_set = "set foreign_key_checks = 1"
            cursor, num5 = self.execute(sql_set1, conn)
            cursor, num3 = self.execute(sql_book, conn)
            cursor, num4 = self.execute(sql_set, conn)
            if not (num1 and num2 and num3): raise DbException("update failed...")
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.commit()
            self.close(conn, cursor)

    def search_record(self, condition, logic="select * from"):
        sql_borrow = logic + " borrow " + condition
        sql_return = logic + " bk_return " + condition
        sql_ticket = logic + " ticket " + condition
        conn, cursor = self.get_con(), None
        try:
            cursor, num = self.execute(sql_borrow, conn)
            borrow_items = cursor.fetchall()
            cursor, num = self.execute(sql_return, conn)
            return_items = cursor.fetchall()
            cursor, num = self.execute(sql_ticket, conn)
            ticket_items = cursor.fetchall()
        except Exception as e:
            raise DbException("search failed")
        finally:
            self.close(conn, cursor)
        return borrow_items, return_items, ticket_items

    def search_items(self, reader_id, book_id):
        pros = []
        if reader_id:
            pros.append("reader_id='{}'".format(reader_id))
        if book_id:
            pros.append("bk_id='{}'".format(book_id))
        conditions = "where " + " and ".join(pros)
        try:
            borrow_items, return_items, ticket_items = self.search_record(conditions)
        except DbException as e:
            raise e
        return borrow_items, return_items, ticket_items

    def group_search(self, conditions):
        try:
            borrow_items, return_items, ticket_items = self.search_record(conditions,
                                                                          logic="select reader_id,count(*) from")
        except Exception as e:
            raise e
        return borrow_items, return_items, ticket_items
