#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/2 14:11 
# @Author : dxc
# @File : gcd.py
"""
欧几里得算法
gcd()
"""


def gcd(a, b):
    """
    欧几里得算法 递归
    :param a:
    :param b:
    :return:
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def gcd_(a, b):
    """
    欧几里得算法
    :param a:
    :param b:
    :return:
    """
    while b > 0:
        r = a % b
        a = b
        b = r
    return a


if __name__ == '__main__':
    # print(gcd(12, 16))
    print(gcd_(12, 16))
