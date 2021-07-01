#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/6/30 17:49 
# @Author : dxc
# @File : activity_select.py

# 活动时间
activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
# 保证活动按结束时间排序
activities.sort(key=lambda x: x[1])


def activities_select(a):
    """
    获取最合适的时间
    :param a:
    :return:
    """
    res = [a[0]]
    for i in range(1, len(a)):
        if a[i][0] >= res[-1][1]:
            res.append(a[i])
    return res


print(activities_select(activities))
