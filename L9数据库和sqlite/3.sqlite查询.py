#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sqlite3
connect=sqlite3.connect('./testsqlite.db')
cursor = connect.cursor()

# cursor.execute("""update student set name ='小红' WHERE id='2'""")
# connect.commit()
cursor.execute("""select * from student;""")
res1 =cursor.fetchall()
print(res1)

#[(1, '小明'), (2, '小明'), (3, '小明'), (4, ' 小白')]  列表当中的每一项表示一行.每一项是元祖 元组的每一样是字段.默认返回这种结构,不用字典原因节省传输带宽
# res2 = cursor.fetchone()  #(1,'小明')结果集 中取一行,结果result collections执行sql完得到所有结果
# print(res2)

#fetch是去结果集,结果集可能很大,所以不会缓存到某个变量中,同一个cursor第二次fetch结果为空
#

