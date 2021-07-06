#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/5 17:28 
# @Author : dxc
# @File : build_model.py
"""
建造者模式

"""
from abc import ABCMeta, abstractmethod


class Player:
    """
    角色类
    """

    def __init__(self, face=None, body=None, arm=None, leg=None):
        self.face = face
        self.body = body
        self.arm = arm
        self.leg = leg

    def __str__(self):
        return "%s,%s,%s,%s" % (self.face, self.body, self.arm, self.leg)


class PlayerBuilder(metaclass=ABCMeta):
    """
    抽象建造者类
    """

    @abstractmethod
    def build_face(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def build_arm(self):
        pass

    @abstractmethod
    def build_leg(self):
        pass


class SexGirlBuilder(PlayerBuilder):
    """
    创建的一个女孩 具体实现
    """

    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = '漂亮脸蛋'

    def build_body(self):
        self.player.body = "瘦小身材"

    def build_arm(self):
        self.player.arm = '小手臂'

    def build_leg(self):
        self.player.leg = '小腿'


class Monster(PlayerBuilder):
    """
    猴子 具体实现
    """

    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = '园的脸'

    def build_body(self):
        self.player.body = "大身材"

    def build_arm(self):
        self.player.arm = '大手臂'

    def build_leg(self):
        self.player.leg = '大腿'


class PlayerDirector:
    """
    控制组装顺序
    """
    def build_player(self,build):
        build.build_body()
        build.build_face()
        build.build_arm()
        build.build_leg()
        return build.player


if __name__ == '__main__':
    builder = SexGirlBuilder()
    director=PlayerDirector()
    player = director.build_player(builder)
    print(player)





