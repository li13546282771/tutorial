#!/usr/bin/env python
# -*- coding:utf-8 -*-
#魔法方法:__init__  初始参数  __new__生成实例  __del__  __repr__
class Animal(object):
    def __init__(self,name):#初始参数
        self.name= name
    def run(self):
        print('动物再跑')
    def __str__(self):
        #print(对象) 打印信息
        return '<class Animal {}>'.format(self.name)
class Dog(Animal):
    pass
class Cat(Animal):
    def run(self):
        print('猫在跑')
dog=Dog('小黄')
cat = Cat('小花')
print(dir(dog))#dir()把类中的所有方法属性打印出来
print(cat)
print(Cat.mro())#[<class '__main__.Cat'>, <class '__main__.Animal'>, <class 'object'>]