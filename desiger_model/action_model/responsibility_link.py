#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/7 14:30 
# @Author : dxc
# @File : responsibility_link.py
"""
责任链模式
    使多个请求都有机会处理请求，从而避免请求的发送者和接受者的直接耦合，将这些对象连城一条链，并沿着这条链传递改请求
    直到处理完为止
"""
from abc import ABCMeta, abstractmethod


class Handle(metaclass=ABCMeta):

    @abstractmethod
    def handle_level(self, day):
        pass


class GeneralManager(Handle):
    """
    总经理
    """

    def handle_level(self, day):
        if day <= 10:
            print("总经理批假{}天".format(day))
        else:
            print("不批 直接走人")


class DepartmentManager(Handle):
    """
    部门经理
    """

    def __init__(self):
        self.next = GeneralManager()

    def handle_level(self, day):
        if day <= 5:
            print("部门经理批假{}".format(day))
        else:
            print("部门经理权限不够")
            self.next.handle_level(day)


class ProjectDirector(Handle):
    """
    项目经理
    """

    def __init__(self):
        self.next = DepartmentManager()

    def handle_level(self, day):
        if day <= 3:
            print("项目经理批假{}".format(day))
        else:
            print("项目经理权限不够")
            self.next.handle_level(day)


if __name__ == '__main__':
    pro = ProjectDirector()
    pro.handle_level(1)
    pro.handle_level(4)
    pro.handle_level(11)