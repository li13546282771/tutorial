#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pyexcel_io import save_data
sheet=[['id', 'name', 'password', 'role'], [1, '小明', 2313, '普通用户'], [2, 'admin', 123456, '管理员']]
save_data(data=sheet,afile='2.xlsx')