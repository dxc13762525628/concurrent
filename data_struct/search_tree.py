#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/6/28 16:56 
# @Author : dxc
# @File : search_tree.py
"""
二叉搜索树
"""


class BiTreeNode:
    """
    二叉树
    """

    def __init__(self, data):
        self.data = data
        self.lchild = None  # 左孩子
        self.rchild = None  # 右孩子
        self.parent = None


class BiTree:
    """
    二叉搜索树
    """

    def __init__(self, li=None):
        self.root = None

    def insert(self, node, val):
        """
        插入数据
        :param node:
        :param val:
        :return:
        """
        if not node:
            node = BiTreeNode(val)
        elif val < node.data:
            node.lchild = self.insert(node.lchild, val)
            node.lchild.parent = node
        elif val > node.data:
            node.rchild = self.insert(node.rchild, val)
            node.rchild.parent = node
        else:
            return node

    def query(self, node, val):
        """
        查询元素
        :param node: 根节点
        :param val: 值
        :return:
        """
        if not node:
            return None
        if node.data < val:
            return self.query(node.rchild, val)
        elif node.data > val:
            return self.query(node.lchild, val)
        else:
            return node

    def delete_node(self, node):
        """
        是叶子节点直接删除 没有孩子的节点
        :param node:
        :return:
        """
        if not node.parent:
            # 根节点 直接删除
            self.root = None
        if node == node.parent.lchild:
            # 左孩子
            node.parent.lchild = None
        else:
            # 右孩子
            node.parent.rchild = None

    def delete_node_lchild(self, node):
        """
        要删除的节点有一个左孩子
        :param node:
        :return:
        """
        if not node.parent:
            # 删除跟节点
            self.root = node.lchild
            node.lchild.parent = None
        elif node == node.parent.lchild:
            # 删除左孩子 将要删除的节点的左孩子变成根节点的左孩子
            node.parent.lchild = node.lchild
            # 节点的父亲 变成节点的左孩子的父亲
            # node.lchild.parent = node.parent
        else:
            # 删除的是右孩子 则右孩子的的左孩子节点变成新的节点的父亲的右节点
            node.parent.rchild = node.lchild
            # node.lchild.parent = node.parent
        node.lchild.parent = node.parent

    def delete_node_rchild(self, node):
        """
        删除的孩子只有一个右孩子
        :param node:
        :return:
        """
        if not node.parent:
            # 删除根节点
            self.root = node.lchild
            node.rchild.parent = None
        elif node == node.parent.lchild:
            # 删除根节点的左孩子 根节点的左孩子变成 节点的右孩子  节点的右孩子的父亲变成节点的父亲
            node.parent.lchild = node.rchild
            # node.rchild.parent = node.parent
        else:
            # 删除的右孩子 同理
            node.parent.rchild = node.rchild
            # node.rchild.parent=node.parent
        node.rchild.parent = node.parent

    def delete_ele(self, val):
        """
        删除元素
        :return:
        """
        node = BiTreeNode(val)
        node = self.query(node, val)
        if not node:
            # 不存在
            return False
        elif not node.lchild and not node.rchild:
            # 没有左右孩子
            self.delete_node(node)
        elif not node.lchild:
            # 没有做孩子
            self.delete_node_rchild(node)
        elif not node.rchild:
            # 没有右孩子
            self.delete_node_lchild(node)
        else:
            # 两个孩子都有 找最小的那一个
            min_node = node.rchild
            while min_node.lchild:
                min_node = min_node.lchild
            # 找到最小的替换数值
            node.data = min_node.data
            # 删除这个节点
            if min_node.rchild:
                self.delete_node_rchild(min_node)
            else:
                self.delete_node(min_node)
