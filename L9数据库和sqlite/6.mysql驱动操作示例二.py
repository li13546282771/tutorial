#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql.cursors
connection=pymysql.connect(host='127.0.0.1',
                port=3306,
                user='root',
                # password='',数据库暂时没有密码
                db= 'job51',  #库  db= 'job51',db必须小写
                charset='utf8mb4',
                cursorclass = pymysql.cursors.DictCursor
                )
try:
    with connection.cursor() as cursor:
        sql = """select * from lianxi;"""
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

        # result2=[]
        # description = cursor.description
        # print(description)#(('id', 3, None, 11, 11, 0, False), ('name', 253, None, 80, 80, 0, True))
        # for index,stu in result:
        #     result2.append(dict(description[index][0]))
        #     print()
except Exception as e:
    print(e)
finally:
    connection.close()


# fetchall()(('大数据研发工程师', '“前程无忧”51job.com（上海）')  优点节省带宽.缺点:字段多的时候不好对应
# 需求({'id':1,'name':'小明'},{'id':2,'name':'小红'})

    # 返回结果集每一行默认元组,能不能改成字典取值方便
    # result2 = []
    # for res in result:
    #     result2.append({
    #         'id': res[0],
    #         'name': res[1]}
    #
    #     )
    # print(result2)


# with   as关键字理解   as很像等号
# flie =open('aaa.txt')
# content = flie.read()
# print(content)
# flie.close()
#
# with open('aaa.txt') as  file:
#     #start 打开资源
#     conetn = file.read()
#     #end   file.close