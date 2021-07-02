#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/1 14:44 
# @Author : dxc
# @File : fibnacci.py
"""
斐波那契数列
"""


def fib_alt(n):
    """
    斐波那契数列
    递归思想
    :param n:
    :return:
    """
    if n == 1 or n == 2:
        return n
    else:
        return fib_alt(n - 1) + fib_alt(n - 2)


# 动态规划
# 最优子问题 递推式
def fib_func(n):
    """
    常规思想
    :param n:
    :return:
    """
    f = [0, 1, 1]
    if n > 2:
        for i in range(n - 2):
            num = f[-1] + f[-2]
            f.append(num)
    return f[n]


if __name__ == '__main__':
    # print(fib_alt(5))
    print(fib_func(5))
