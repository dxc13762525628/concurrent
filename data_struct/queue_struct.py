#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/6/25 11:25 
# @Author : dxc
# @File : queue_struct.py
"""
队列特点 先进先出
"""


class QueueStruct:
    """
    环形队列
    """

    def __init__(self, size=100):
        """
        初始化列表100的队列
        :param size:
        """
        self.queue = [0 for _ in range(100)]
        self.size = size
        self.rear = 0  # 队尾指针
        self.front = 0  # 队首指针

    def push(self, ele):
        """
        进队
        :param ele:
        :return:
        """
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear].append(ele)

    def pop(self):
        """
        出队
        :return:
        """
        if not self.is_empty():
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]
        else:
            return False

    def is_empty(self):
        """
        判断为空
        :return:
        """
        return self.rear == self.front

    def is_filled(self):
        """
        判断是否队列满了
        :return:
        """
        return (self.rear + 1) % self.size == self.front
