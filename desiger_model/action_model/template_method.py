#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/7 16:07 
# @Author : dxc
# @File : template_method.py
"""
模板方法
"""

from abc import ABCMeta, abstractmethod
from time import sleep


class Window(metaclass=ABCMeta):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def repaint(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def run(self):  # 模板方法
        self.start()
        while True:
            try:
                self.repaint()
                sleep(1)
            except KeyboardInterrupt:
                break
        self.stop()


class MyWindow(Window):
    """
    自己实现
    """
    def __init__(self,msg):
        self.msg=msg

    def start(self):
        print("窗口开始运行")

    def repaint(self):
        print(self.msg)

    def stop(self):
        print("窗口结束运行")


if __name__ == '__main__':
    my = MyWindow('开始测试')
    my.run()
