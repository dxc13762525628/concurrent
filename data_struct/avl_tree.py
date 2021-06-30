#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/6/29 17:04 
# @Author : dxc
# @File : avl_tree.py
"""
AVL平衡二叉树
在左孩子的左叶子节点加数据 右旋
在右孩子的右=叶节点加数据 左旋
在左孩子的右叶子节点加数据 先左后右旋
在右孩子的左叶子节点加数据 先右后左旋
"""


class AVLNode:
    """
    AVLNode 类
    """

    def __init__(self, data):
        self.data = data
        self.lchild = None  # 左孩子
        self.rchild = None  # 右孩子
        self.parent = None
        self.bf = 0  # 高度差 平衡度


class AVLTree:
    """
    AVLTree 树
    """

    def __init__(self):
        self.root = None

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

    def totate_left(self, p, c):
        """
        右孩子右叶子导致的左旋
        :return:
        """
        node = c.lchild
        p.rchild = node
        if node:
            node.parent = p
        c.lchild = p
        p.parent = c

        p.bf = 0
        c.bf = 0

        return c

    def rotate_right(self, p, c):
        """
        左孩子左叶子导致的左旋
        :param p:
        :param c:
        :return:
        """
        node = c.rchild
        p.lchild = node
        if node:
            node.parent = p
        c.rchild = p
        p.parent = c

        p.bf = 0
        c.bf = 0

        return c

    def rotate_right_left(self, p, c):
        """
        右孩子左叶子导致的 右旋 左旋
        :param p:
        :param g:
        :param c:
        :return:
        """
        # 右旋
        g = c.lchild
        node_rchild = g.rchild
        c.lchild = node_rchild

        if node_rchild:
            node_rchild.parent = c

        g.rchild = c
        c.parent = g

        # 左旋
        node_lchild = g.lchild
        p.rchild = node_lchild

        if node_lchild:
            node_lchild.parent = p

        g.lchild = p
        p.parent = g

        # 更新平衡度
        if g.bf > 0:
            p.bf = -1
            c.bf = 0
        elif g.bf < 0:
            p.bf = 0
            c.bf = 1
        else:
            p.bf = 0
            c.bf = 0
        return g

    def rotate_left_right(self, p, c):
        """
        先左后右旋
        :param p:
        :param c:
        :return:
        """
        # 左旋
        g = c.rchild

        node_lchild = g.lchild
        c.rchild = node_lchild

        if node_lchild:
            node_lchild.parent = c

        g.lchild = c
        c.parent = g

        # 右旋
        node_rchild = g.rchild
        p.lchild = node_rchild

        if node_rchild:
            node_rchild.parent = p

        g.rchild = p
        p.parent = g

        if g.bf < 0:
            p.bf = 1
            c.bf = 0
        elif g.bf > 0:
            p.bf = 0
            c.bf = -1
        else:
            p.bf = 0
            c.bf = 0
        return g

    def insert_rec(self, val):
        """
        想插入在判断高度 再选择
        :param val:
        :return:
        """
        # 插入
        p = self.root
        # 空树
        if not p:
            self.root = AVLNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:
                    # 有左孩子
                    p = p.lchild
                else:
                    # 没有左孩子
                    p.lchild = AVLNode(val)
                    p.lchild.parent = p
                    node = p.lchild  # 存储的是插入的节点
                    break
            elif val > p.data:
                if p.rchild:
                    # 有右孩子
                    p = p.rchild
                else:
                    p.rchild = AVLNode(val)
                    p.rchild.parent = p
                    node = p.rchild  # 存储的插入的节点右孩子
                    break
            else:
                # 有个同样的节点
                return

        # 更新
        while node.parent:
            if node.parent.lchild == node:
                # 添加在左孩子 父节点-1
                if node.parent.bf < 0:
                    # -2的选择方式
                    # 看node的哪边跟深 左边深则是 右旋 右边深则是先左后右
                    g = node.parent.parent  # 用于连接后选择的节点的父亲
                    x = node.parent  # 选择前子树的根
                    if node.bf > 0:
                        # 先左后右
                        n = self.rotate_left_right(node.parent, node)
                    else:
                        # 右旋
                        n = self.rotate_right(node.parent, node)
                elif node.parent.bf > 0:
                    # 更新之后变成0 不再传递
                    node.parent.bf = 0
                    break
                else:
                    # 原来就是0
                    node.parent.bf = -1
                    node = node.parent
                    continue
            else:
                # 添加在右孩子 bf +1
                if node.parent.bf > 0:
                    # 原来就是1 则变成2 两种情况 右右  右左
                    g = node.parent.parent  # 用于连接后选择的节点的父亲
                    x = node.parent  # 选择前子树的根
                    if node.parent.bf > 0:
                        # 左旋
                        n = self.totate_left(node.parent, node)
                    else:
                        # 右 左
                        n = self.rotate_right_left(node.parent, node)
                elif node.parent < 0:
                    # 左边原来是-1
                    node.parent.bf = 0
                    break
                else:
                    # 原来是0
                    node.parent.bf = 1
                    node = node.parent
                    continue

            # 连接旋转后的子树
            n.parent = g
            if not g:
                self.root = n
                break
            else:
                if x == g.lchild:
                    g.lchild = n
                else:
                    g.rchild = n
                break
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/6/29 17:04
# @Author : dxc
# @File : avl_tree.py
"""
AVL平衡二叉树
在左孩子的左叶子节点加数据 右旋
在右孩子的右=叶节点加数据 左旋
在左孩子的右叶子节点加数据 先左后右旋
在右孩子的左叶子节点加数据 先右后左旋
"""


class AVLNode:
    """
    AVLNode 类
    """

    def __init__(self, data):
        self.data = data
        self.lchild = None  # 左孩子
        self.rchild = None  # 右孩子
        self.parent = None
        self.bf = 0  # 高度差 平衡度


class AVLTree:
    """
    AVLTree 树
    """

    def __init__(self):
        self.root = None

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

    def totate_left(self, p, c):
        """
        右孩子右叶子导致的左旋
        :return:
        """
        node = c.lchild
        p.rchild = node
        if node:
            node.parent = p
        c.lchild = p
        p.parent = c

        p.bf = 0
        c.bf = 0

        return c

    def rotate_right(self, p, c):
        """
        左孩子左叶子导致的左旋
        :param p:
        :param c:
        :return:
        """
        node = c.rchild
        p.lchild = node
        if node:
            node.parent = p
        c.rchild = p
        p.parent = c

        p.bf = 0
        c.bf = 0

        return c

    def rotate_right_left(self, p, c):
        """
        右孩子左叶子导致的 右旋 左旋
        :param p:
        :param g:
        :param c:
        :return:
        """
        # 右旋
        g = c.lchild
        node_rchild = g.rchild
        c.lchild = node_rchild

        if node_rchild:
            node_rchild.parent = c

        g.rchild = c
        c.parent = g

        # 左旋
        node_lchild = g.lchild
        p.rchild = node_lchild

        if node_lchild:
            node_lchild.parent = p

        g.lchild = p
        p.parent = g

        # 更新平衡度
        if g.bf > 0:
            p.bf = -1
            c.bf = 0
        elif g.bf < 0:
            p.bf = 0
            c.bf = 1
        else:
            p.bf = 0
            c.bf = 0
        return g

    def rotate_left_right(self, p, c):
        """
        先左后右旋
        :param p:
        :param c:
        :return:
        """
        # 左旋
        g = c.rchild

        node_lchild = g.lchild
        c.rchild = node_lchild

        if node_lchild:
            node_lchild.parent = c

        g.lchild = c
        c.parent = g

        # 右旋
        node_rchild = g.rchild
        p.lchild = node_rchild

        if node_rchild:
            node_rchild.parent = p

        g.rchild = p
        p.parent = g

        if g.bf < 0:
            p.bf = 1
            c.bf = 0
        elif g.bf > 0:
            p.bf = 0
            c.bf = -1
        else:
            p.bf = 0
            c.bf = 0
        return g

    def insert_rec(self, val):
        """
        想插入在判断高度 再选择
        :param val:
        :return:
        """
        # 插入
        p = self.root
        # 空树
        if not p:
            self.root = AVLNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:
                    # 有左孩子
                    p = p.lchild
                else:
                    # 没有左孩子
                    p.lchild = AVLNode(val)
                    p.lchild.parent = p
                    node = p.lchild  # 存储的是插入的节点
                    break
            elif val > p.data:
                if p.rchild:
                    # 有右孩子
                    p = p.rchild
                else:
                    p.rchild = AVLNode(val)
                    p.rchild.parent = p
                    node = p.rchild  # 存储的插入的节点右孩子
                    break
            else:
                # 有个同样的节点
                return

        # 更新
        while node.parent:
            if node.parent.lchild == node:
                # 添加在左孩子 父节点-1
                if node.parent.bf < 0:
                    # -2的选择方式
                    # 看node的哪边跟深 左边深则是 右旋 右边深则是先左后右
                    g = node.parent.parent  # 用于连接后选择的节点的父亲
                    x = node.parent  # 选择前子树的根
                    if node.bf > 0:
                        # 先左后右
                        n = self.rotate_left_right(node.parent, node)
                    else:
                        # 右旋
                        n = self.rotate_right(node.parent, node)
                elif node.parent.bf > 0:
                    # 更新之后变成0 不再传递
                    node.parent.bf = 0
                    break
                else:
                    # 原来就是0
                    node.parent.bf = -1
                    node = node.parent
                    continue
            else:
                # 添加在右孩子 bf +1
                if node.parent.bf > 0:
                    # 原来就是1 则变成2 两种情况 右右  右左
                    g = node.parent.parent  # 用于连接后选择的节点的父亲
                    x = node.parent  # 选择前子树的根
                    if node.parent.bf > 0:
                        # 左旋
                        n = self.totate_left(node.parent, node)
                    else:
                        # 右 左
                        n = self.rotate_right_left(node.parent, node)
                elif node.parent < 0:
                    # 左边原来是-1
                    node.parent.bf = 0
                    break
                else:
                    # 原来是0
                    node.parent.bf = 1
                    node = node.parent
                    continue

            # 连接旋转后的子树
            n.parent = g
            if not g:
                self.root = n
                break
            else:
                if x == g.lchild:
                    g.lchild = n
                else:
                    g.rchild = n
                break
