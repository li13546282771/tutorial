#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os


print(__file__)
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# C:/Users/asus/Desktop/tutorial/测试/s.py
# C:\Users\asus\Desktop\tutorial\测试\s.py
# C:\Users\asus\Desktop\tutorial\测试
# C:\Users\asus\Desktop\tutorial