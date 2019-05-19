import json
import ssl
import urllib
import urllib.error
import urllib.request as urllib2

from Basic import *
from DB_Helper import DBHelper


def getInfoFromDouban(isbn):
    try:
        host = 'https://isbn.market.alicloudapi.com'
        path = '/ISBN'
        method = 'GET'
        appcode = '1644c81c6224467f96c626ba3fc79ec5'
        querys = 'is_info=0&isbn=' + isbn
        bodys = {}
        url = host + path + '?' + querys

        result_json = ""

        request = urllib2.Request(url)
        request.add_header('Authorization', 'APPCODE ' + appcode)
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        response = urllib2.urlopen(request, context=ctx)
        content = response.read()
        if (content):
            result_json = json.loads(content)
        else:
            raise urllib.error.HTTPError
    except urllib.error.HTTPError as e:
        raise e
    return result_json


import random


def getBooks():
    data = ""
    db = DBHelper()
    get = lambda x: data['result'][x]
    f = None
    try:
        f = open("test.txt", "r")
        isbns = f.readlines()
    except:
        raise Exception
    for isbn in isbns:
        try:
            data = getInfoFromDouban(isbn)
            f.write(data)
            title = get('title')
            author = get('author')
            publisher = get('publisher')
            price = float(get('price')[:-1])
            bk_type = random.sample(['文学', '小说', '历史', '传记', '科幻', '儿童读物', '杂志'], 1)[0]
            edition = random.choice([1, 2, 3])
            amount = random.randint(1, 20)
            book = Book(title, author, publisher, bk_type, edition, price, amount)
            try:
                db.insert_book(book)
                print('[+] ' + isbn + " insert successfully")
            except:
                print('[-] ' + isbn + " failed")
        except:
            print(data)


if __name__ == '__main__':

    # 导入相应库文件

    import requests

    from lxml import etree

    import csv

    # 创建CSV文件，并写入表头信息

    db = DBHelper()

    # 构造所有的URL链接

    urls = ['https://book.douban.com/top250?start={}'.format(str(i)) for i in range(0, 251, 25)]

    # 添加请求头

    headers = {

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'

    }

    # 循环URL

    for url in urls:
        try:
            html = requests.get(url, headers=headers)

            selector = etree.HTML(html.text)

            # 取大标签，以此循环

            infos = selector.xpath('//tr[@class="item"]')

            for info in infos:
                title = info.xpath('td/div/a/@title')[0]

                url = info.xpath('td/div/a/@href')[0]

                book_infos = info.xpath('td/p/text()')[0]

                author = (book_infos.split('/')[0]).split()[-1]

                publisher = book_infos.split('/')[-3]

                date = book_infos.split('/')[-2]

                price = float((book_infos.split('/')[-1])[:-1])

                rate = info.xpath('td/div/span[2]/text()')[0]

                comments = info.xpath('td/p/span/text()')

                comment = comments[0] if len(comments) != 0 else "空"

                bk_type = random.sample(['文学', '小说', '历史', '传记', '科幻', '儿童读物', '杂志'], 1)[0]
                edition = random.choice([1, 2, 3])
                amount = random.randint(1, 20)
                # 写入数据

                book = Book(title, author, publisher, bk_type, edition, price, amount)
                try:
                    db.insert_book(book)
                    print('[+] ' + title + " insert successfully")
                except:
                    print('[-] ' + title + " insert failed")
        except:
            pass

'''if __name__ == '__main__':
    get = lambda x: input(x)
    db = DBHelper()
    while True:
        title = get('title: ')
        author = get('author: ')
        publisher = get('publisher: ')
        price = float(get('price: '))
        bk_type = random.sample(['文学', '小说', '历史', '传记', '科幻', '儿童读物', '杂志'], 1)[0]
        edition = random.choice([1, 2, 3])
        amount = random.randint(1, 20)
        book = Book(title, author, publisher, bk_type, edition, price, amount)
        try:
            db.insert_book(book)
            print('[+] ' + title + " insert successfully")
        except:
            print('[-] ' + title + " insert failed")'''

