#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 随机挑人
# 百度 "excel  文本,构造大列表 ,百度'同时操作多行',术语'行编辑模式',搜pycharm行编辑,搜idea 行编辑,google,官方文档.. 筛选信息,尽量搜索时间近一点的,google,官方文档"
import random

student_list=[
    'sada',
    'dasd',
    'asdd',
    'as阿萨方式dd',
    'asda',
]
print(len(student_list))
stu=random.choice(student_list)
print(stu)
random.shuffle(student_list)
print(student_list)
# 随机是怎么产生的