#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/7 15:27 
# @Author : dxc
# @File : strategy.py
"""
策略模式
    定义一系列算法，把他们封装起来可以相互替换，本模式使得算法可独立于使用它的客户变化

"""
from abc import ABCMeta, abstractmethod


class Strategy(metaclass=ABCMeta):

    @abstractmethod
    def execute(self, data):
        pass


class FastStrategy(Strategy):
    """
    策略1
    """

    def execute(self, data):
        print("用较快的算法处理数据{}".format(data))


class SlowStrategy(Strategy):
    """
    策略2
    """

    def execute(self, data):
        print("用较慢的算法处理数据{}".format(data))


class Context:
    """
    封装无关的数据
    """
    def __init__(self, strategy, data):
        self.data = data
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def do_strategy(self):
        self.strategy.execute(self.data)


if __name__ == '__main__':
    data = "这是数据"
    s1 = FastStrategy()
    s2 = SlowStrategy()
    context = Context(s1, data)
    context.do_strategy()
    context.set_strategy(s2)
    context.do_strategy()
