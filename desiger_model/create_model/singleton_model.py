#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/5 17:45 
# @Author : dxc
# @File : singleton_model.py
"""
单例模式
    类的对象只有一个
"""
from abc import ABCMeta, abstractmethod


class Singleton:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            # 没有就创建一个 掉用父类方法创建一个实例
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class MyClass(Singleton):

    def __init__(self, g):
        self.g = g


if __name__ == '__main__':

    a = MyClass(10)
    b = MyClass(20)
    print(a.g)
    print(b.g)
    print(id(a))
    print(id(b))