#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/4/30 14:41 
# @Author : dxc
# @File : search_ar.py


# 顺序查找
def linear_search(data_set, value):
    """
    顺序查找
    :param data_set:
    :param value:
    :return:
    """
    for ind, v in enumerate(data_set):
        if v == value:
            return ind


def binary_search(target_set, value):
    """
    二分查找
    :param target_set:  目标集合
    :param value:  要查找的值
    :return: 索引
    """
    left = 0
    right = len(target_set) - 1

    while left <= right:
        mid = (left + right) // 2
        if target_set[mid] == value:
            return mid
        elif target_set[mid] > value:
            right = mid - 1
        else:
            left = mid + 1



if __name__ == '__main__':
    target_list = [1, 5, 7, 8, 9, 55, 12, 46]
    value = 7
    num1 = linear_search(target_list, value)
    num2 = binary_search(target_list, value)
    print(num2)
    print(num1)
