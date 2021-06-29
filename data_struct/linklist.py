#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/6/28 10:19 
# @Author : dxc
# @File : linklist.py
"""
链表
"""


class Node:
    """
    节点类
    """

    def __init__(self, item):
        self.item = item
        self.next = None
        self.font = None


class LinkStruct:
    """
    链表
    """

    def __init__(self, li):
        """
        初始化数据
        :param li:可迭代对象
        """
        self.li = li

    def create_link_head(self):
        """
        从头部插入节点
        :return:
        """
        head = Node(self.li[0])
        for item in self.li[1:]:
            node = Node(item)
            node.next = head
            head = node
        return head

    def create_link_tail(self):
        """
        从尾部插入
        :return:
        """
        head = Node(self.li[0])
        tail = head
        for item in self.li[1:]:
            node = Node(item)
            tail.next = node
            tail = node
        return head

    def insert_node(self, p, q):
        """
        插入一个元素
        :param p:要插入的元素
        :param q:要插入的元素的前一个结点
        :return:
        """
        p.next = q.next
        q.next = p

    def delete_node(self, p, q):
        """
        删除一个节点
        :param p: 要删除的节点
        :param q: 要删除的节点的前一个节点
        :return:
        """
        p = q.next
        q.next = q.next.next
        del p

    @staticmethod
    def get_data(head):
        """
        遍历
        :param head:
        :return:
        """
        while head:
            print(head.item)
            head = head.next


class LinkedListStruct:
    """
    双向链表
    """

    def __init__(self, li):
        self.li = li

    def create_link_head(self):
        """
        头部插入
        :return:
        """
        head = Node(self.li[0])
        for item in self.li[1:]:
            node = Node(item)
            node.next = head
            head.font = node
            head = node
        return head

    def insert_node(self, p, q):
        """
        插入一个节点
        :param p: 要插入的节点
        :param q: 要插入的当前节点
        :return:
        """
        p.next = q.next
        q.next.font = p
        q.next = p
        p.font = q

    def delete_node(self, p, q):
        """
        插入一个节点
        :param p: 要插入的节点
        :param q: 要插入的当前节点
        :return:
        """
        p = q.next
        q.next = p.next
        q = p.next.font
        p.next.font = q
        del p


if __name__ == '__main__':
    # link = LinkStruct([1, 2, 3])
    # # head = link.create_link_head()
    # head = link.create_link_tail()
    # link.get_data(head)

    link = LinkedListStruct([1, 2, 3])
    head = link.create_link_head()
    print(head.item)
    print(head.next.font.item)
