#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/6/25 14:29 
# @Author : dxc
# @File : stack_queue_demo.py
"""
迷宫问题
给出一个二维列表 表示迷宫
0 表示通道
1表示围墙
给出算法 求出可以通过的路径

思路一 回溯法  深度优先
    从一个节点开始走 直到走到不能走的再倒回去找第二条 栈存储当前路径
"""
from collections import deque


class StackMazePath:
    """
    路径搜索  栈实现
    栈空表示没有路
    """

    def __init__(self, maze, x1, y1, x2, y2):
        """
        初始化数据
        :param maze:  二维列表
        :param x1: 起始坐标x
        :param y1: 起始坐标y
        :param x2: 终点坐标x
        :param y2: 终点坐标y
        """
        self.maze = maze
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.stack = []
        self.stack.append((x1, y1))
        self.position = [
            lambda x, y: (x + 1, y),
            lambda x, y: (x - 1, y),
            lambda x, y: (x, y + 1),
            lambda x, y: (x, y - 1),
        ]

    def maze_alt(self):
        """
        搜索算法
        :return:
        """
        while len(self.stack) > 0:
            cur_node = self.stack[-1]  # 获取路径的最后一个位置
            # 判断是否到终点
            if cur_node[0] == self.x2 and cur_node[1] == self.y2:
                # 到终点 返回路径
                return self.stack
            # 4个方向去找路径
            for pos in self.position:
                next_node = pos(cur_node[0], cur_node[1])
                if self.maze[next_node[0]][next_node[1]] == 0:
                    self.stack.append(next_node)
                    self.maze[next_node[0]][next_node[1]] = 2  # 标记当前位置走过
                    break
            else:
                # 一个都没找到 回退一个继续找
                node = self.stack.pop()
                self.maze[node[0]][node[1]] = 2
        else:
            return False


class QueueMazePath:
    """
    队列实现 广度优先
    """

    def __init__(self, maze, x1, y1, x2, y2):
        """
        初始化数据
        :param maze:  二维列表
        :param x1: 起始坐标x
        :param y1: 起始坐标y
        :param x2: 终点坐标x
        :param y2: 终点坐标y
        """
        self.maze = maze
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.queue = deque()
        self.position = [
            lambda x, y: (x + 1, y),
            lambda x, y: (x - 1, y),
            lambda x, y: (x, y + 1),
            lambda x, y: (x, y - 1),
        ]

    def maze_alt(self):
        """
        实现算法
        :return:
        """
        self.queue.append((self.x1, self.y1, -1))  # 存储坐标及他的上个节点位置
        path = []
        while len(self.queue) > 0:
            cur_node = self.queue.pop()
            path.append(cur_node)
            if cur_node[0] == self.x2 and cur_node[1] == self.y2:
                # 找到位置 获取走的路径
                index = cur_node[2]
                while index > 0:
                    next_pos = path[index]
                    print(next_pos[0], next_pos[1])
                    index = next_pos[2]
                return True
            # 去寻找可以走的路径
            for pos in self.position:
                next_node = pos(cur_node[0], cur_node[1])
                # 坐标有可以使用的
                if self.maze[next_node[0]][next_node[1]] == 0:
                    self.queue.append((next_node[0], next_node[1], len(path) - 1))  # 加入到队列
                    self.maze[next_node[0]][next_node[1]] = 2  # 标记已经走过
        else:
            return False


if __name__ == '__main__':
    maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            ]
    # maze = StackMazePath(maze, 1, 1, 10, 12)
    # print(maze.maze_alt())

    maze = QueueMazePath(maze, 1, 1, 10, 12)
    print(maze.maze_alt())
