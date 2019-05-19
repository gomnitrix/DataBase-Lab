import os
import struct

from BplusTree import *
from Config import *
from generate import read_data, check_file


def indexing(items=None, show=False):
    """
    :param items: 要建立索引的数据，默认为空，此时自动读取data中的全部数据
    :param show: 是否显示建立好的B+树，默认不显示
    :return: B+树的全部叶节点的键值对
    """
    items = read_data() if not items else items
    datas = []
    for item in items:
        key = item[0]
        value = item[1]
        datas.append(KeyValue(key, value))
    mybptree = BpTree(10, 10)
    for kv in datas:
        mybptree.insert(kv)
    if show:
        mybptree.show()
    kvs = mybptree.traversal()
    return kvs


def handle_line(item):
    key = struct.unpack('L', item[:4])[0]
    value = item[4:].decode()
    return key, value


def write_small_file(file, kvs, datas):
    with open(file, "wb+") as file:
        for kv in kvs:
            key = struct.pack('L', kv)
            value = datas[kv].encode()
            item = key + value
            file.write(item)


@check_file
def split_file():
    """
    :return:
    """
    with open("./data.bin", "rb+") as file:
        datas = {}
        temp = None
        i = 1
        item = True
        num = (data_size // file_num) + 1
        while True and item:
            item = file.readline()
            if item:
                if temp:
                    item = temp + item
                    temp = None
                if len(item) < 16:
                    temp = item
                    continue
                key, value = handle_line(item)
                datas[key] = value
            if len(datas) == num or not item:
                if not datas:
                    break
                kvs = sorted(datas)
                write_small_file("./sorted/small" + str(i) + ".bin", kvs, datas)
                datas = {}
                i += 1


def read_top(k, file, offset=0):
    results = []
    temp = None
    with open(file, "rb") as f:
        i = 1
        f.seek(offset)
        while i < k:
            item = f.readline()
            if not item:
                break
            if temp:
                item = temp + item
                temp = None
            if len(item) < 16:
                temp = item
                continue
            results.append(item.strip(b'\n'))
            i += 1
    return results


def load(k, file, topmap):
    if not topmap[file][0]:
        topmap[file][0] = read_top(k, file, topmap[file][1] * k * 17)
        topmap[file][1] += 1
        if not topmap[file][0]:
            topmap.pop(file)
            return 10000000000, "None"
    data = topmap[file][0].pop(0)
    return handle_line(data)


def adjust(tree, index):
    win = index
    p = win // 2
    while p > 0:
        if win > 0:
            key = tree[win][0]
        else:
            return
        pkey = tree[tree[p]][0] if tree[p] != -1 else -1
        if key >= pkey:
            tree[p], win = win, tree[p]
        p = p // 2
    tree[0] = win


def init_loser_tree(files, tops):
    length = 2 * file_num
    loser_tree = [-1] * length
    i = file_num
    for file in files:
        key, value = load(queue_size, file, tops)
        loser_tree[i] = (key, value)
        i += 1
    i = file_num
    while i < length:
        adjust(loser_tree, i)
        i += 1
    return loser_tree


def multi_sorted():
    files = os.listdir("./sorted")
    files = ["./sorted/" + x for x in files]
    k = queue_size
    sorted_file = "./sorted/sorted.txt"
    topk_map = {}
    for file in files:
        topk_map[file] = [read_top(k, file, 0), 1]
    tree = init_loser_tree(files, topk_map)
    results = []
    with open(sorted_file, "w+") as f:
        while topk_map:
            winner = tree[0]
            item = tree[winner]
            results.append(str(item[0]) + ' : ' + item[1] + '\n')
            tree[winner] = load(k, files[winner - file_num], topk_map)
            adjust(tree, winner)
            if len(results) == k:
                f.writelines(results)
                results = []
    print("done")


def sort():
    split_file()
    multi_sorted()


if __name__ == '__main__':
    # indexing(show=True)
    sort()
