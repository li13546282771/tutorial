#!/usr/bin/env python
# -*- coding:utf-8 -*-

# (重点)python 通过驱动操作mysql数据库
# 检查mysql 是否启动 (或window服务mysql是否启动),用图形工具
# 开启服务  管理员终端 简写mysqld.exe --console
#
import pymysql
#建立会话
connection=pymysql.connect(host='127.0.0.1',
                port=3306,
                user='root',
                # password='',数据库暂时没有密码
                db= 'job51',  #库  db= 'job51',db必须小写
                charset='utf8mb4',
                # cursorclass =
                )
# print(connection)
cursor = connection.cursor()
cursor.execute(
    """select * from xinxi;"""
)
#取数据 .一般通过循环和下标把每行每列的值取出
result = cursor.fetchall()
# print(result)
for index,xi in enumerate(result):
    print(f'第{index+1}行数据.职位为{xi[0]},公司{xi[1]},薪资{xi[3]}')
# 如果有insert update需要commit
connection.commit()
# 关闭数据库链接.驱动自动帮忙关闭,但建议显式写出
cursor.close()
connection.close()

























