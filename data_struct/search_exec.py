#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/6/24 14:40 
# @Author : dxc
# @File : search_exec.py
"""
查找相关算法题
"""


class SearchExercise:
    """
    查找相关的算法题
    """

    @staticmethod
    def binary_search(target_set, left, right, value):
        """
        二分查找
        :param target_set:  目标集合
        :param value:  要查找的值
        :return: 索引
        """
        while left <= right:
            mid = (left + right) // 2
            if target_set[mid] == value:
                return mid
            elif target_set[mid] > value:
                right = mid - 1
            else:
                left = mid + 1

    @staticmethod
    def exercise_demo01(s, t):
        """
        给两个字符串s,t,判断t是否为s的重新排列组合后的单词
        s = 'anagram'
        t = 'nagaram'
        返回true
        :return:
        """
        # 思路一 先转成列表 在对列表进行排序如果两个排序后的列表一样则是true
        # ss = list(s)
        # tt = list(t)
        # ss.sort()
        # tt.sort()
        # return ss == tt

        # 思路二 两个字符串的字母出现的数量和个数是一样的
        dict_s = {}
        dict_t = {}
        for ch in s:
            dict_s[ch] = dict_s.get(ch, 0) + 1
        for ch in t:
            dict_t[ch] = dict_t.get(ch, 0) + 1
        return dict_s == dict_t

    @staticmethod
    def exercise_demo02(m, num):
        """
        给定一个二维列表m*n,查询一个数是否存在，
        列表有以下特性
            每一列都是从左到右排序好
            每一行第一个数比上一行最后一个打
        :return:
        """
        # 思路一 先一列一列查找到准备的那一行
        # for index in range(len(m)):
        #     if m[index][0] > num:
        #         for i in m[index - 1]:
        #             if i == num:
        #                 return True
        #     elif m[index][-1] > num:
        #         for i in m[index]:
        #             if i == num:
        #                 return True
        # return False

        # 思路二 二分查找
        h = len(m)  # 行
        w = len(m[0])  # 列表
        left = 0
        right = w * h - 1
        while left <= right:
            mid = (left + right) // 2
            i = mid // w  # x轴坐标
            j = mid % w  # y轴坐标
            if m[i][j] == num:
                return True
            elif m[i][j] > num:
                right = mid - 1
            else:
                left = mid + 1
        return False

    def exercise_demo03(self, li, num):
        """
        给定一个列表和一个整数，设置算法找到两个数的下标使得两个数之和为给定的整数，保证肯定只有一个结果 排好序的
        列表[1,2,5,4]与目标整数3 1+2=3结果返回0,1这个下标
        :return:
        """
        # 思路一 直接遍历
        # for i in range(len(li) - 1):
        #     for j in range(i + 1, len(li)):
        #         if li[i] + li[j] == num:
        #             return i, j
        # return False

        # 思路二 二分查找
        i = 0
        j = 0
        for i in range(len(li)):
            a = li[i]
            b = num - a  # 要找的数
            if b > a:
                j = self.binary_search(li, i + 1, len(li) - 1, b)
            else:
                j = self.binary_search(li, 0, i - 1, b)
            if j:
                break
        return sorted([i + 1, j + 1])


if __name__ == '__main__':
    search = SearchExercise()

    # res = search.exercise_demo01('anagram', 'nagaram')
    # print(res)

    # m = [
    #     [1, 3, 5, 7],
    #     [10, 11, 16, 20],
    #     [23, 30, 34, 50]
    # ]
    # num = 31
    # res = search.exercise_demo02(m, num)
    # print(res)

    li = [1, 2, 4, 5]
    num = 9
    res = search.exercise_demo03(li, num)
    print(res)
