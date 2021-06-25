#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/6/25 10:49 
# @Author : dxc
# @File : stack_struct.py


class StackStruct:
    """
    栈
    先进后出
    """

    def __init__(self):
        """
        定义一个栈
        """
        self.stack = []

    def push(self, ele):
        """
        入栈
        :param ele:元素
        :return:
        """
        self.stack.append(ele)

    def pop(self):
        """
        出栈
        :return:
        """
        return self.stack.pop()

    def get_top(self):
        """
        或者栈顶元素
        :return:
        """
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return 0

    def is_empty(self):
        """
        判断是否为空
        :return:
        """
        return len(self.stack) == 0
