#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/2 10:44 
# @Author : dxc
# @File : pub_serializer.py
"""
最长公共子序列
子序列 相对位置一样 及位置可以不连续
ABCD BDF 都是ABCDEFG的子序列
X=ABBCBDE
Y=DBBCDB
LCS(X,Y)=BBCD
"""


def lcs_length(x, y):
    """
    求出最长公共子序列的字符串数
    :param x:
    :param y:
    :return:
    """
    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                # 结果来着左上方
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                c[i][j] = max(c[i - 1][j], c[i][j - 1])
    return c[m][n]


def lcs(x, y):
    """
    获取位置二维列表 存储的是每个序列来自的位置
    :param x:
    :param y:
    :return:
    """
    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    b = [[0 for _ in range(n + 1)] for _ in range(m + 1)]  # 记录位置 左上 左 上
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                # 结果来着左上方
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = 1  # 左上方
            elif c[i - 1][j] > c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = 2
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = 3

    return c[m][n], b


def lcs_track_back(x, y):
    """
    回溯
    :param x:
    :param y:
    :return:
    """
    c, b = lcs(x, y)
    i = len(x)
    j = len(y)
    res = []
    while i > 0 and j > 0:
        if b[i][j] == 1:
            # 左上
            res.append(x[i - 1])
            i -= 1
            j -= 1
        elif b[i][j] == 2:
            # 上方不匹配
            i -= 1
        else:
            # 左方 不匹配
            j -= 1
    return "".join(reversed(res))


if __name__ == '__main__':
    # print(lcs_length('ABCBDA', 'BDCABA'))
    # c, b = lcs('ABCBDA', 'BDCABA')
    # print(c)
    # for i in b:
    #     print(i)
    print(lcs_track_back('ABCBDA', 'BDCABA'))
