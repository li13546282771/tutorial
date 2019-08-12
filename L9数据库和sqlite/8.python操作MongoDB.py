#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymongo

client = pymongo.MongoClient('127.0.0.1',27017)
#切换到一个库,不存在则自动创建
db = client.test
print(db)
#创建collection集合(存放数据的空间)(层级上类似关系型数据库的表)
print(db.my_collection)
#插入数据    文档(层级上类似关系型数据库的一行数据)
# db.my_collection.insert_one({'x':10})
# db.my_collection.insert_one({'x':11})
# db.my_collection.insert_one({'x':12})
#查找数据
res=db.my_collection.find_one()
print(res)#{'_id': ObjectId('5d22e6568d810cd6d8dd6b7d'), 'x': 10}每行数据自动生成唯一id
#查找所有
res1 = db.my_collection.find()
print(res1)#生成器
for x in res1:
    print(x)




