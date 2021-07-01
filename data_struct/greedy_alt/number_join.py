#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/6/30 17:36 
# @Author : dxc
# @File : number_join.py
"""
连接最大字符串 将数字连接成最大字符串
"""

from functools import cmp_to_key

li = [32, 94, 128, 1286, 6, 71]


def xy_cmp(x, y):
    """
    比较大小
    :param x:
    :param y:
    :return:
    """
    if x + y < y + x:
        return 1
    elif x + y > y + x:
        return -1
    else:
        return 0


def number_join(li):
    """
    输出连接的数据
    :param li:
    :return:
    """
    li = list(map(str, li))
    li.sort(key=cmp_to_key(xy_cmp))
    return "".join(li)


if __name__ == '__main__':
    print(number_join(li))
