#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 驱动:数据库有自己的操作接口,每一个编程语言连接到每一种驱动都不一样
# 常见驱动:mysqlDB  pymysql
#  mysqldb驱动为了效率和方便调用 c语言写的并由python直接调用每个操作系统平台识别的二进制不一样,c源码需要通过VC编译器编译后才能运行,情况太多所以pypi平台上没有这个包.
# 方法一  :到官网下载对应系统和python版本的mysql -connector  安装完成之后会在pip list发现mysql-connect-python,就可以直接使用了.
# 优点,效率高  缺点:不好找对应版本.名字歧义(mysql官网和pypi平台上叫mysql-connect-python安装完叫mysql-connect-python ,代码文件夹叫MySQLDB)如果从源码编译,又需要下载VC编译器成本.

# 方法二:  可以到https://www.lfd.uci.edu/~gohlke/pythonlibs/  下载编译好的包 mysql-python. c写的包根据python版本跟系统版本编译后的二进制文件后缀为.whl.平时安装的.py文件也会转换成whl文件   下载对应版本的.whl文件  pip install  xxx.whl  安装完成后会发现叫mysql-connect-python

# 由于历史原因名字歧义.难安装,但企业使用较多
# py2   从mysql官网安装exe安装  python 从mysql官网或下载.whl 或pip install MySQLclient

# 方法三(推荐):pymysql包 ,基于python与数据库接口交互标准书写,纯python书写,兼容mysqldb 直接pip install pymysql    新项目或个人项目建议pymysql



import MySQLdb
import pymysql
pymysql.install_as_MySQLdb()        #兼容MySQLdb

#其他数据库 oracle,postgresql


























