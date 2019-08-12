#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql

params ={
    'host':'127.0.0.1',
    'port':3306,
    'user':'root',
    'db': 'job51',
    'charset':'utf8mb4'}
connection=pymysql.connect(**params)
cursor = connection.cursor()

# sql = 'insert into job51.lianxi(id,name)VALUES (3,"小白")'

affected_rows =None
try:
    newid = 5
    name = '小w'
    # cursor.execute("insert into job51.lianxi(id,name)VALUES (3,'小白')")
    # cursor.execute(f"insert into job51.lianxi(id,name)VALUES ({newid},'{name}')")
    sql="""insert into lianxi(id,name)VALUES (%s,%s);""".format(newid,name)
    affected_rows=cursor.execute(sql,[newid,name])
    print('受影响的行',affected_rows)
    if affected_rows:
        print(f'插入成功{affected_rows}行')
except Exception as e:
    print(f'受影响行数{affected_rows},插入失败')
    print(e)
finally:
    connection.commit()
    connection.close()





