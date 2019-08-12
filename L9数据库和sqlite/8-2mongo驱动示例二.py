#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pymongo import MongoClient
from pprint import pprint  #格式化输出json到终端中
class Connect(object):
    #静态,"内存"不变的,全局变量(静态变量)或函数一直存在内存中,像什么时候调用就什么时候调用,静态(全局)
    @staticmethod
    def get_connection():
        return MongoClient("127.0.0.1",27017)
client = Connect.get_connection()
db = client.test
#建立集合并插入一行文档
# db.inventory.insert_one({
#     "item":"帆布",
#     "quantity":100,
#     "tags":["棉布"],
#     "size":{
#         "height":20,
#         "width":35.5,
#         "uom":"cm"
#     }
# })
#根据条件查找
# result_set1 =db.inventory.find({})#没有过滤条件
# for item in result_set1:
#     print(item)

#条件查询
from bson.son import SON
# db.inventory.insert_many([
#     {
#         "item":"五金",
#         "quantity":11,
#         "tags":["铁"],
#         "size":{
#             "height":20,
#             "width":35.5,
#             "uom":"cm"
#         }},
# {
#         "item":"螺丝刀",
#         "quantity":11,
#         "tags":["水"],
#         "size":{
#             "height":20,
#             "width":35.5,
#             "uom":"cm"
#         }},{
#         "item":"螺丝",
#         "quantity":11,
#         "tags":["解决"],
#         "size":{
#             "height":20,
#             "width":35.5,
#             "uom":"cm"
#         }},
# ])

result_set2 = db.inventory.find({
    "quantity":200
})
result_set3 = db.inventory.find({"size.height":35.5})
result_set4 = db.inventory.find({"quantity":{"$lt":100}})
result_set5 = db.inventory.find({"quantity":200,"size.height":35.5})

#更新数据
db.inventory.update_one({
    {"item":"螺丝"},  #where item=""
    {'$set':{'quantity':50}}  #update set 字段=值
})

# 删除
db.inventory.delete_one({"item":"旅行"})
# db.inventory.drop()

