#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/6/25 10:55 
# @Author : dxc
# @File : stack_demo.py
"""
栈解决括号匹配问题 左括号进栈 右边出栈
"""
from stack_struct import StackStruct


class MatchBrackets:
    """
    利用进行括号匹配
    """

    def __init__(self):
        self.left_standard = ["(", "[", "{", ]
        self.right_standard = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        self.stack = StackStruct()

    def match(self, target_str):
        """
        匹配目标字符串
        :param target_str:
        :return:
        """
        for i in target_str:
            # 将'('入栈
            if i in self.left_standard:
                self.stack.push(i)
            # 出栈校验
            else:
                if self.stack.is_empty():
                    return False
                elif self.right_standard[i] == self.stack.get_top():
                    self.stack.pop()
                else:
                    return False
        if self.stack.is_empty():
            return True
        else:
            return False


if __name__ == '__main__':
    str_demo = '([{})'
    match_brackets = MatchBrackets()
    res = match_brackets.match(str_demo)
    print(res)
