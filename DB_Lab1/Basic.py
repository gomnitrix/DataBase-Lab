class Book:
    def __init__(self, title, author, publisher, bk_type=None, edition=1, price=25.0, amount=1):
        self.title = title
        self.author = author
        self.bk_type = bk_type
        self.edition = edition
        self.price = price
        self.publisher = publisher
        self.amount = amount


class Reader:
    def __init__(self, name, sex, rd_type, phone):
        self.name = name
        self.sex = sex
        self.type = rd_type
        self.phone = phone


class DbException(Exception):
    pass

