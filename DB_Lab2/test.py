import struct

with open("./sorted/small4.bin", "rb+") as file:
    datas = []
    items = file.readlines()
    temp = None
    k = 0
    for item in items:
        if temp:
            item = temp + item
            temp = None
        if len(item) < 16:
            temp = item
            continue
        item = item.strip()
        key = struct.unpack('L', item[:4])[0]
        if key < k:
            print(key)
            break
        else:
            print(key)
            k = key
# with open("./sorted/small4.bin", "rb+") as file:
#     datas = []
#     items = file.readlines()
#     temp = None
#     k = 0
#     for item in items:
#         if temp:
#             item = temp + item
#             temp = None
#         if len(item) < 16:
#             temp = item
#             continue
#         item = item.strip()
#         key = struct.unpack('L', item[:4])[0]
#         value = item[4:].decode()
#         datas.append((key, value))
# from processce import indexing
#
# kvs = indexing(datas, True)
# k = 0
# for kv in kvs:
#     key = struct.pack('L', kv.key)
#     if key < k:
#         print(key)
#         break
#     else:
#         k = key
