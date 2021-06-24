#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/4/30 15:23 
# @Author : dxc
# @File : sort_alt.py
"""
十大排序算法

垃圾三人排序算法
冒泡，选择，插入

牛逼三人组排序算法
快速，堆，归并排序(python 默认排序算法)
"""


def bubble_sort(target_list):
    """
    冒泡排序
    :param target_list:
    :return:
    """
    length = len(target_list) - 1
    for i in range(length):
        # 优化版
        count = True
        for j in range(length - i):
            if target_list[j] < target_list[j + 1]:
                count = False
                target_list[j], target_list[j + 1] = target_list[j + 1], target_list[j]
        if count:
            break


def select_sort(li):
    """
    选择排序
    :param li:
    :return:
    """
    length = len(li)
    for i in range(length - 1):
        for j in range(i + 1, length):
            if li[i] > li[j]:
                li[i], li[j] = li[j], li[i]


def insert_sort(li):
    """
    插入排序
    :param li:列表
    :return: 排序好的列表
    """
    for i in range(1, len(li)):
        temp = li[i]
        j = i - 1
        while j >= 0 and li[j] > temp:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = temp


def quick_partition(li, left, right):
    """
    快速排序
    :param li:
    :return:
    """
    temp = li[left]
    while left < right:
        while left < right and li[right] >= temp:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= temp:
            left += 1
        li[right] = li[left]
    li[left] = temp
    return left


def quick_main_sort(li, left, right):
    """
    快速排序算法
    :param li:
    :return:
    """
    if left < right:
        mid = quick_partition(li, left, right)
        quick_main_sort(li, left, mid - 1)
        quick_main_sort(li, mid + 1, right)


def sift(li, low, height):
    """
    调整函数
    :param li:  列表
    :param low:  堆顶位置
    :param height: 根节点位置
    :return: 新堆
    """
    i = low
    j = 2 * i + 1
    tmp = li[low]
    while j <= height:
        if j + 1 <= height and li[j] < li[j + 1]:
            j = j + 1
        if li[j] > tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            break
    li[i] = tmp


def heap_sort(li):
    """
    堆排序
    :param li:
    :return:
    """
    n = len(li)
    # 构建一个堆
    for i in range((n - 2) // 2, -1, -1):
        sift(li, i, n - 1)
    # 建堆完成开始排序
    for i in range(n - 1, -1, -1):
        li[i], li[0] = li[0], li[i]
        sift(li, 0, i - 1)


def merge(li, low, mid, high):
    """
    归并排序的归并
    :param li:
    :param low:
    :param mid:
    :param high:
    :return:
    """
    i = low
    j = mid + 1
    lmid = []
    while i <= mid and j <= high:
        if li[i] < li[j]:
            lmid.append(li[i])
            i += 1
        else:
            lmid.append(li[j])
            j += 1

    # 可能有一半没有跑完
    while i <= mid:
        lmid.append(li[i])
        i += 1
    while j <= high:
        lmid.append(li[j])
        j += 1

    li[low:high + 1] = lmid


def merge_sort(li, low, high):
    """
    归并排序 稳定 挨着换是稳定的
    :param li:
    :param low:
    :param high:
    :return:
    """
    if low < high:
        mid = (low + high) // 2
        merge_sort(li, low, mid)
        merge_sort(li, mid + 1, high)
        merge(li, low, mid, high)


def insert_sort_gap(li, gap):
    """
    :param li:
    :param gap:
    :return:
    """
    for i in range(gap, len(li)):
        temp = li[i]
        j = i - gap
        while j >= 0 and li[j] > temp:
            li[j + gap] = li[j]
            j -= gap
        li[j + gap] = temp


def shell_sort(li):
    """
    希尔排序
    :param li:
    :return:
    """
    d = len(li) // 2
    while d >= 1:
        insert_sort_gap(li, d)
        d //= 2


def count_sort(li, max_count=100):
    """
    计数排序 先得知道数的范围
    :param li:
    :param max_count:
    :return:
    """
    count_list = [0 for _ in range(max_count + 1)]
    # 开始计数
    for val in li:
        count_list[val] += 1
    li.clear()
    # 开始排序
    for ind, val in enumerate(count_list):
        for i in range(val):
            li.append(ind)


def bucket_sort(li, n=10, max_num=100):
    """
    桶排序
    :param li:
    :param n:
    :param max_num:
    :return:
    """
    buckets = [[] for _ in range(n)]  # 构建一个桶
    for var in li:
        i = min(var // (max_num // n), n - 1)  # i表示var放哪个通
        buckets[i].append(var)
        # 排序
        for j in range(len(buckets[i]) - 1, 0, -1):
            if buckets[i][j] < buckets[i][j - 1]:
                buckets[i][j], buckets[i][j - 1] = buckets[i][j - 1], buckets[i][j]
            else:
                break
    sorted_list = []
    for buc in buckets:
        sorted_list.extend(buc)
    return sorted_list


def radix_sort(li):
    """
    基数排序
    :param li:
    :return:
    """
    max_num = max(li)
    it = 0
    while 10 ** it <= max_num:
        buckets = [[] for _ in range(10)]
        for var in li:
            digit = (var // 10 ** it) % 10
            buckets[digit].append(var)
        # 分桶完成
        li.clear()
        # 将数据写回列表
        for buc in buckets:
            li.extend(buc)
        it += 1


if __name__ == '__main__':
    target_list = [89, 5, 7, 8, 1, 12, 45, 52, 23]
    # bubble_sort(target_list)
    # select_sort(target_list)
    # insert_sort(target_list)
    # quick_main_sort(target_list, 0, len(target_list) - 1)
    # heap_sort(target_list)
    # merge_sort(target_list, 0, len(target_list) - 1)
    # shell_sort(target_list)
    # count_sort(target_list)
    # res = bucket_sort(target_list)
    radix_sort(target_list)
    print(target_list)
