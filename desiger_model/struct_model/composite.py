#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/6 10:46 
# @Author : dxc
# @File : composite.py
"""
组合模式
"""
from abc import ABCMeta, abstractmethod


class Graphic(metaclass=ABCMeta):
    """
    抽象接口
    """

    @abstractmethod
    def draw(self):
        pass


class Point(Graphic):
    """
    点
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "点({},{})".format(self.x, self.y)

    def draw(self):
        print(str(self))


class Line(Graphic):
    """
    线
    """

    def __init__(self, x1, y1):
        self.p1 = x1
        self.p2 = y1

    def __str__(self):
        return "线({},{})".format(self.p1, self.p2)

    def draw(self):
        print(str(self))


class Picture(Graphic):
    """"
    复合组件
    """
    def __init__(self, iter):
        self.children = []
        for g in iter:
            self.add(g)

    def add(self, g):
        self.children.append(g)

    def draw(self):
        for g in self.children:
            g.draw()


if __name__ == '__main__':
    p1 = Point(2, 3)
    l1 = Line(Point(3, 4), Point(6, 7))
    l2 = Line(Point(1, 5), Point(2, 8))
    pic = Picture([p1, l1, l2])
    pic.draw()
