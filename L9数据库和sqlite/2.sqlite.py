#!/usr/bin/env python
# -*- coding:utf-8 -*-
# sqlite  轻量级数据库,场景 手机app 快速验证想法.python内置操作他的驱动.sqlite本质纯文本文件
import sqlite3
#驱动,编程语言和数据库操作接口之间的中介,有配套驱动编程语言才能操作数据库


#连接数据库,参数是数据库路径和名字,不存在会自动创建,得到会话对象
connect = sqlite3.connect('testsqlite.db')
#从会话中得到游标对象,游标,好想操作excel时的鼠标,在数据库中对表进行行操作要先取得游标
cursor=connect.cursor()
#执行sql语句
# sql语句较长且需要空格,使用三引号扩住字符串,某些驱动会把第一行空行解释为语法错误,所以字符串开头不要有空格直接接关键字,驱动会自动转换关键字,所以下面的varchar表示sqlite中的text
#创建成功后注释,否则报表已存在报错,观察.db文件,发现表结构已经存在
# cursor.execute("""CREATE TABLE student(
#  id int PRIMARY KEY,name varchar(10)
# );
# """)

#插入一条数据
#里面的引号可以用转义字符,或跟外层引号错开,小明的引号不能省略,对数据库来讲的字符串
# cursor.execute("""INSERT INTO student (id,name)VALUES (1,'小明');""")

cursor.execute("""SELECT * FROM student;""")
result=cursor.fetchall()
print(result)


#提交.insert和更新操作,必须提交才真正生效,查询不需要提交.否则当未插入,就像关闭文档提示是否保存.未提交的更改档次select可以看到,但是数据库没保存,下次select会看不到,用过id不能再用
cursor.close()#关闭释放游标资源
connect.commit()
connect.close()#关闭会话中断连接数据库  不写驱动会默认帮你关闭,平时应该显式写出


#报错
# 1.主键重复输入