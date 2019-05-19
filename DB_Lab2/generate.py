import os
import random
import string
import struct
from Config import *


def generate_data():
    items = []
    with open("./data.bin", "wb+") as file:
        for i in range(data_size):
            num = struct.pack('L', random.getrandbits(32))
            ran_str = (''.join(random.sample(string.ascii_letters + string.digits, 12))).encode()
            item = num + ran_str + b'\n'
            items.append(item)
        file.writelines(items)


def check_file(func):
    def safely_read():
        if not os.path.exists("./data.bin"):
            generate_data()
        datas = func()
        return datas

    return safely_read


@check_file
def read_data():
    with open("./data.bin", "rb+") as file:
        datas = []
        items = file.readlines()
        temp = None
        for item in items:
            if temp:
                item = temp + item
                temp = None
            if len(item) < 16:
                temp = item
                continue
            item = item.strip(b'\n')
            key = struct.unpack('L', item[:4])[0]
            value = item[4:].decode()
            datas.append((key, value))
    return datas


if __name__ == '__main__':
    pass
