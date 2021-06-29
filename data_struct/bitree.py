#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/6/28 15:40 
# @Author : dxc
# @File : bitree.py
from collections import deque


class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None  # 左孩子
        self.rchild = None  # 右孩子


class BiTree:
    def pre_order(self, root):
        """
        前序遍历 先访问根节点 在访问左子树 再访问右子树
        :param root:
        :return:
        """
        if root:
            print(root.data, end=",")
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    def in_order(self, root):
        """
        中序遍历 先左子树 在自己 在右字数
        :param root:
        :return:
        """
        if root:
            self.pre_order(root.lchild)
            print(root.data, end=",")
            self.pre_order(root.rchild)

    def post_order(self, root):
        """
        后序遍历 先左子树 在右字数 在自己
        :param root:
        :return:
        """
        if root:
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)
            print(root.data, end=",")

    def level_order(self, root):
        """
        层次遍历 思路使用队列 首先跟节点入队 再跟阶段出队 根节点的左右孩子入队
        :param root:
        :return:
        """
        queue = deque()
        queue.append(root)
        while len(queue) > 0:
            node = queue.popleft()
            print(node.data, end=',')
            if node.lchild:
                queue.append(node.lchild)
            if node.rchild:
                queue.append(node.rchild)


a = BiTreeNode('A')
b = BiTreeNode('B')
c = BiTreeNode('C')
d = BiTreeNode('D')
e = BiTreeNode('E')
f = BiTreeNode('F')
g = BiTreeNode('G')

e.lchild = a
e.rchild = g
a.rchild = c
c.lchild = b
c.rchild = d
g.rchild = f

root = e

if __name__ == '__main__':
    tree = BiTree()
    # tree.pre_order(root)
    # tree.in_order(root)
    # tree.post_order(root)
    tree.level_order(root)
