#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/6 11:08 
# @Author : dxc
# @File : facade.py
"""
外观模式
    子系统中的一种接口提供一致的界面 外观模式定义了一个高层接口 这个接口使得这一子系统更加容易使用
"""


class CPU:
    def run(self):
        print("CPU开始工作")

    def stop(self):
        print("CPU停止工作")


class Disk:

    def run(self):
        print("硬盘开始工作")

    def stop(self):
        print("硬盘停止工作")


class Memory:

    def run(self):
        print("内存开始工作")

    def stop(self):
        print("内存停止工作")


class Computer:
    """
    计算机类

    方法封装统一使用
    """

    def __init__(self):
        self.cpu = CPU()
        self.disk = Disk()
        self.memory = Memory()

    def run(self):
        self.cpu.run()
        self.disk.run()
        self.memory.run()

    def stop(self):
        self.cpu.stop()
        self.disk.stop()
        self.memory.stop()


if __name__ == '__main__':
    com = Computer()
    com.stop()
