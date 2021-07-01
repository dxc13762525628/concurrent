#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/6/30 16:10 
# @Author : dxc
# @File : change_money.py
"""
面额问题 有 100 50 20 10 5 2 1
372 找最少张
贪心算法
"""


class ChangeMoney:
    """
    面额问题
    """

    def __init__(self):
        self.amount = [100, 50, 20, 10, 5, 2, 1]

    def cal_num(self, money):
        """
        计算面额
        :param money:
        :return:
        """
        m = [0 for _ in range(len(self.amount))]
        for i, amount in enumerate(self.amount):
            m[i] = money // amount
            money = money % amount
        return m, money


if __name__ == '__main__':
    change = ChangeMoney()
    print(change.cal_num(372))
