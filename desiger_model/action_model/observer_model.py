#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/7 14:46 
# @Author : dxc
# @File : observer_model.py
"""
观察者模式
    定义对象间的一种一对多的依赖关系，当一个对象的状态发生改变时，所有依赖它的对象都得到通知并自动更新 观察者又叫发布订阅模式
"""
from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    """
    观察者 接口
    """

    @abstractmethod
    def update(self, notice):  # notice 是消息对象
        pass


class Notice:
    """
    发布者 抽象
    """

    def __init__(self):
        # 存储所有的观察者
        self.observer = []

    def attach(self, objs):
        """
        订阅者
        :param objs:
        :return:
        """
        self.observer.append(objs)

    def detach(self, objs):
        """
        解除绑定
        :param obj:
        :return:
        """
        self.observer.remove(objs)

    def notify(self):
        """
        通知
        :return:
        """
        for obj in self.observer:
            obj.update(self)


class StaffNotice(Notice):
    """
    具体发布者
    """

    def __init__(self, company_info=None):
        super().__init__()
        self.__company_info = company_info

    @property
    def company_info(self):
        return self.__company_info

    @company_info.setter
    def company_info(self, info):
        self.__company_info = info
        self.notify()


class Staff(Observer):
    """
    接收者
    """

    def __init__(self):
        self.company_info = None

    def update(self, notice):
        self.company_info = notice.company_info


if __name__ == '__main__':
    notice = StaffNotice("初始公司信息")
    s1 = Staff()
    s2 = Staff()
    notice.attach(s1)
    notice.attach(s2)
    notice.company_info = "今年业绩好 发奖金"
    print(s1.company_info)
    print(s2.company_info)
