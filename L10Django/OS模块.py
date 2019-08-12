#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
# 1.os.path.exists()判断是否存在文件,判断路径是否存在
print(os.path.exists('os模块.py'))#True
print(os.path.exists('1'))#False
# 2.重命名
# os.rename('a','b')
# 3.删除文件
# os.remove('bbb')
# 4.创建文件夹make directory
# os.mkdir('aaa')创建单层路径
# os.makedirs('ddd/dd')创建多层路径
# 5.列出当前文件夹下的文件,相当于cmd中的dir命令
print(os.listdir())
# 6.切换到当前文件夹 change  相当于cmd中的cd命令
# os.chdir('L4js原型')
# 在cmd中尝试dir cd命令
# 7.获取当前工作目录的路径 get work directory
print(os.getcwd())
# 8.判断是文件还是文件夹
os.path.isfile('aaa')
os.path.isfile('一百安徽大')
# >8  （常用）拼接路径,获取脚本的绝对路径
print(os.path.join(os.path.dirname(__file__), 'time包练习.py'))
# >9  返绝对路径  absolute
print(os.path.abspath('./1包引用.py'))
os.path.abspath(os.path.join(os.getcwd(), '3os.py'))
# >10 判断是否路径。
print(os.path.isdir('aaa'))