# csv
# csv 一种简单格式的纯文本文件，结构类似python中的列表，类似excel。场景：excel的替代格式，数据库导出文件

import csv

# 读数据
# file_path = 'D:\\PycharmProjects\\tutorial_shanxi\\L11常用包\\5test.csv'
# file_path = '5test.csv'
file_path = r'D:\PycharmProjects\tutorial_shanxi\L11常用包\5test.csv'

with open(file_path, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    print(reader)
    result = list(reader)
    print(result)
    print(result[1][1])

# 写数据
datas = [
    ['编号', '姓名', '年龄'],
    ['1', '小明', '13'],
    ['2', '小红', '10'],
    ['3', '小青', '15'],
]
with open('5write.csv', mode='w', encoding='utf-8', newline='') as file2:   # newline写完数据后是否换行。
    writer = csv.writer(file2)
    for row in datas:
        writer.writerow(row)    # 一次写一行
    print('写完成')
