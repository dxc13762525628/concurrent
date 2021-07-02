#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/1 15:04 
# @Author : dxc
# @File : steel_bar_dp.py
"""
钢条切割问题
给定一个钢条的长度获取最大的收益
1  2  3  4  5  6  7  8  9  10
1  5  8  9  10 17 17 20 24 30

"""

p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]


def cut_rod_recurision(p, n):
    """
    使用递归 通式 res = max(pn,ri+r(n-i))  自顶向下
    :param p:
    :param n:
    :return:
    """
    if n == 0:
        return 0
    else:
        res = p[n]
        for i in range(1, n):
            res = max(res, cut_rod_recurision(p, i) + cut_rod_recurision(p, n - i))
        return res


def cut_rod_dp(p, n):
    """
    动态规划 自底向上
    :param p:
    :param n:
    :return:
    """
    r = [0]
    for i in range(1, n + 1):
        # 每次都求的那个最优解
        res = 0
        for j in range(1, i + 1):
            res = max(res, p[j] + r[(i - j)])
        r.append(res)
    return r[n]


def cut_rod_extend(p, n):
    """
    获取最优左边的位置
    :param p:
    :param n:
    :return:
    """
    r = [0]
    s = [0]
    for i in range(1, n + 1):
        res_r = 0
        res_s = 0
        for j in range(1, i + 1):
            if p[j] + r[i - j] > res_r:
                res_r = p[j] + r[i - j]
                res_s = j
        r.append(res_r)
        s.append(res_s)
    return r[n], s


def cut_rod_solution(p, n):
    """
    获取两个位置
    :param p:
    :param n:
    :return:
    """
    r, s = cut_rod_extend(p, n)
    ans = []
    while n > 0:
        ans.append(s[n])
        n -= s[n]
    return ans


if __name__ == '__main__':
    # print(cut_rod_recurision(p, 9))
    # print(cut_rod_dp(p, 8))
    # print(cut_rod_extend(p, 8))
    print(cut_rod_solution(p, 7))
