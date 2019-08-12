#!/usr/bin/env python
# -*- coding:utf-8 -*-
# json
# 引提:接口   MongoDB,配置等地方都会用到json
student = [
    {'no': 1, 'name': '小明', 'age': 13},
    {'no': 2, 'name': '小李', 'age': 13},
    {'no': 3, 'name': '小红', 'age': 13},
]

students_json2 = """
[
    {"no": 1, "name": "小明", "age": 13}, 
    {"no": 2, "name": "小红", "age": 13}, 
    {"no": 3, "name": "小李", "age": 13}]
"""

#web开发服务器把学生列表 列表套字典,直接返回前台hyml
# 但是不能这么做.原因  [  { 是python解释器所认为的列表字典概念.特殊语法,内部实现机制,传输时候的编码,其他语言并不认识 不互通 js{}表示对象java{}叫map 内部实现原理不一样

# 所以需要一个大家都认识的中介语言来传输信息,1 字符串 2 同一格式 ，json 各语言都可解析 注意json有自己的语法，虽然长得跟python字典一样，但不是一个东西
# 最佳实践：个编程语言自己的数据结构先转成json字符串，在发送给对方电脑，对方接收后在解析成适合自己编程语言的对象
# json主要用户数据传输和配置文件

# json  示例  大括号，键值对，键值对 双引号
# {
#     "student":[
#         {
#             {"no":1,"name":"小明","age":14},
#             {"no":2,"name":"小明","age":14},
#             {"no":3,"name":"小明","age":14},
#         }
#     ]
# }

import json
print(type(student),student)
# student_json1=json.dump("student.py")
student_json=json.dumps(student)
print(type(student_json),student_json)

# json 转对象
# json.loads("")
student2=json.loads(students_json2)
print(type(student2))
#dumps(变量对象)  dump()读取文件
# loads(变量)   load()读接收文件


#“\u5c0f\” 现在py脚本中编写的中文,在py解析器中本质就是Unicode编码,只是我们看到的是自然地数字,计算机存的是编码后的信息
# \u 表示后面不是普通的字符串,而是二进制,5c表示一个字节 00001011
#pycharm 自带的终端不方便解析,功能有限,另一方面win终端默认gbk编码,强行解析会显示乱码,所以显示中间编码船务unicode编码
print("\u5c0f")
# print()可以看到Unicode编码代表的中文
# 中文 (解释器Unicode)  一 编码utf8一 二进制

#XML
"""
<note>
    <to>George</to>
    <from>John</from>
    <heading>Reminder</heading>
    <body>Don't forget the meeting!</body>
</note>
"""

#可扩展置标语言  非常像HTML,表达键值对 HTML是xml的子集.XML和json一样用于计算机信息交互.几年前非常流行,java的接口数据格式一般为xml,xml有自己的版本原信息,注释和属性实现更复杂的功能.另一方面,结构尖括号写起来不方便,所以渐渐被json取代.但是现在仍有一些项目使用xml类型的数据

# 3.YAML
"""
environments:
    dev:
        url: http://dev.bar.com
        name: Developer Setup
    prod:
        url: http://foo.bar.com
        name: My Cool App
my:
    servers:
        - dev.bar.com
        - foo.bar.com"""
# 依靠缩进表示层级,不能表达数字,所以不适合做网络传输介质
# 擅长表达路径,常做配置文件











