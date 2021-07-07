#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/6 10:23 
# @Author : dxc
# @File : bridge.py
"""
桥模式
二个维度方便扩展
    将一个事物两个维度进行分离 方便扩展
"""
from abc import ABCMeta, abstractmethod


# 抽象接口
class Shape(metaclass=ABCMeta):
    """
    颜色作为形状的属性
    """

    def __init__(self, color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass


class Color(metaclass=ABCMeta):

    @abstractmethod
    def paint(self, shape):
        pass


class Rectangle(Shape):
    """
    长方形
    """
    name = "长方形"

    def draw(self):
        self.color.paint(self)


class Circle(Shape):
    """
    圆形
    """
    name = "圆形"

    def draw(self):
        self.color.paint(self)


class Red(Color):
    """
    红色
    """

    def paint(self, shape):
        print("红色{}".format(shape.name))


class Green(Color):
    """
    绿色
    """

    def paint(self, shape):
        print("绿色" % shape.name)


if __name__ == '__main__':

    re = Rectangle(Red())
    re.draw()
