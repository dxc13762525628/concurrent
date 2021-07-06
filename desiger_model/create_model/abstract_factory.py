#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/5 11:24 
# @Author : dxc
# @File : abstract_factory.py
"""
抽象工厂
定义一个接口 用来创建一系列的对象
"""
from abc import abstractmethod, ABCMeta


# 抽象产品
class PhoneShell(metaclass=ABCMeta):
    """
    屏幕抽象类
    """

    @abstractmethod
    def show_shell(self):
        pass


class CPU(metaclass=ABCMeta):
    """
    cpu抽象类
    """

    @abstractmethod
    def show_cpu(self):
        pass


class OS(metaclass=ABCMeta):
    """
    操作系统抽象类
    """

    @abstractmethod
    def show_os(self):
        pass


# 抽象工厂
class PhoneFactory(metaclass=ABCMeta):
    """
    抽象工厂
    """

    @abstractmethod
    def make_shell(self):
        pass

    @abstractmethod
    def make_cpu(self):
        pass

    @abstractmethod
    def make_os(self):
        pass


# 具体产品
class SmallShell(PhoneShell):

    def show_shell(self):
        print("小手机壳")


class BigShell(PhoneShell):
    def show_shell(self):
        print("大手机壳")


class AppleShell(PhoneShell):
    def show_shell(self):
        print("苹果手机壳")


class SnapDragonCPU(CPU):
    def show_cpu(self):
        print("晓龙cpu")


class MediaTeCPU(CPU):
    def show_cpu(self):
        print("联发科cpu")


class AppleCPU(CPU):
    def show_cpu(self):
        print("苹果cpu")


class Android(OS):

    def show_os(self):
        print("安卓系统")


class IOS(OS):
    def show_os(self):
        print("ios系统")


# 具体工厂
class MiFactory(PhoneFactory):
    """
    小米
    """

    def make_shell(self):
        return SmallShell()

    def make_cpu(self):
        return SnapDragonCPU()

    def make_os(self):
        return Android()


class HuaweiFactory(PhoneFactory):
    """
    华为
    """

    def make_shell(self):
        return SmallShell()

    def make_cpu(self):
        return MediaTeCPU()

    def make_os(self):
        return Android()


class IPhoneFactory(PhoneFactory):
    """
    苹果
    """

    def make_shell(self):
        return AppleShell()

    def make_cpu(self):
        return AppleCPU()

    def make_os(self):
        return IOS()


# 客户端
class Phone:
    """
    手机类
    """
    def __init__(self, cpu, os, shell):
        self.cpu = cpu
        self.os = os
        self.shell = shell

    def show_info(self):
        self.cpu.show_cpu()
        self.os.show_os()
        self.shell.show_shell()


def make_phone(factory):
    """
    做手机函数
    :param factory:
    :return:
    """
    cpu = factory.make_cpu()
    os = factory.make_os()
    shell = factory.make_shell()
    return Phone(cpu, os, shell)


if __name__ == '__main__':
    p1 = make_phone(MiFactory())
    p1.show_info()
