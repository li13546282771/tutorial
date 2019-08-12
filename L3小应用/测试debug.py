#!/usr/bin/env python
# -*- coding:utf-8 -*-
def foo():
    print('hell')
    a = 1
    b = 2
    c = b
    d = a + c


def boo():
    for i in range(5):
        foo()

if __name__ == '__main__':
    print('hello world')
    print('hello world')
    print('hello world')
    boo()
    print('hello world')
    print('hello world')