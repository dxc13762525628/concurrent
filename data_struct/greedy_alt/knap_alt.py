#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/6/30 16:19 
# @Author : dxc
# @File : knap_alt.py
"""
背包问题
给定一组物品，每种物品都有自己的重量和价格，在限定的总重量内，我们如何选择，才能使得物品的总价格最高
"""

goods = [(60, 10), (100, 20), (140, 30)]
goods.sort(key=lambda x: x[0] / x[1], reverse=True)


def fractional_back(goods, w):
    """
    计算拿最多
    :param goods:
    :param w:
    :return:
    """
    m = [0 for _ in range(len(goods))]
    total_v = 0
    for i, (prize, weight) in enumerate(goods):
        if w > weight:
            m[i] = 1
            total_v += prize
            w -= weight
        else:
            m[i] = w / weight
            total_v += m[i] * prize
            w = 0
            break
    return total_v, m


if __name__ == '__main__':
    print(fractional_back(goods, 50))
