#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/7 14:10 
# @Author : dxc
# @File : chain_of_responsibility.py
"""
代理模式
    为其他对象提供一种代理以控制对这个对象的访问

"""
from abc import ABCMeta, abstractmethod


class Subject(metaclass=ABCMeta):
    """
    接口
    """

    @abstractmethod
    def get_content(self):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class RealSubject(Subject):
    """
    实际对象
    """

    def __init__(self, filename):
        self.filename = filename
        f = open(filename)
        self.content = f.read()
        f.close()

    def get_content(self):
        return self.content

    def set_content(self, content):
        f = open(self.filename, 'w', encoding='utf-8')
        f.write(content)
        f.close()


class VirtualProxy(Subject):
    """
    虚代理
    调用才读取数据
    """

    def __init__(self, filename):
        self.filename = filename
        self.subj = None

    def get_content(self):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.get_content()

    def set_content(self, content):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.set_content(content=content)


class ProtectedProxy(Subject):
    """
    保护代理
    只读不可写
    """

    def __init__(self, filename):
        self.subj = RealSubject(filename)

    def get_content(self):
        return self.subj.get_content()

    def set_content(self, content):
        raise PermissionError("无权写入")
