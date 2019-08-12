#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
from datetime import datetime,timedelta

# 1(常用) datetime.now()返回当前时间
print(datetime.now())    #2019-07-08 18:55:50.133538
# 2创建datetime对象
dt = datetime(2019,7,8,18,56)
print(dt.year)    #年
print(dt.month)   #月
print(dt.day)     #日
# 3日期加减.  场景:判断活动截止;定时任务    当前时间的前一天前十小时
print(datetime.now()-timedelta(days=1,hours=10))
# 4(常用)格式化输出strftime  format  对象转字符串
print(datetime.now().strftime("%Y-%m-%d  %H:%M:%S"))#2019-07-08  19:02:50
# %Y 2018年   %y 18  year
# %m month  月
# %d day   日
# %H hour  小时
# %M minute  分钟
# %S seconds 秒

# 时间戳转datetime对象
# print(datetime.fromtimestamp(6531651313))
#字符串转时间对象
# dtstr = '2018-10-06T09:25:03.401Z'
# dt = datetime.strptime(dtstr, '%Y-%m-%dT%H:%M:%S.%fZ')
# print(type(dtstr))
# print(type(dt))
# print(dt)

# time

# 1(常用)生成当前时间的时间戳
# 整数形式的时间戳 timestamp：当前时间 减去 1970-1-1 0:0:0 的秒数，形如1540368793。把时间量化成数字，比较时间先后顺序，计算转换有优势。缺点可读性差，默认长度只能表示到2038年。
# print(time.time())#1562584461.1636276


# 2> 生成本地时间  GTM+8  zh   返回结构化时间
# print(time.localtime())#time.struct_time(tm_year=2019, tm_mon=7, tm_mday=8, tm_hour=19, tm_min=14, tm_sec=21, tm_wday=0, tm_yday=189, tm_isdst=0)

# 3>  (常用)格式化时间
# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# 4> 字符串转time结构
# tmobj = time.strptime('2018-10-06T09:25:03.401Z', '%Y-%m-%dT%H:%M:%S.%fZ')
# print(tmobj)
# 5> 从time结构对象生成数字时间戳   make
# print(time.mktime(tmobj))
# 6> time.sleep()   函数推迟调用线程的运行
# time.sleep(5)