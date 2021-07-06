#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/5 10:58 
# @Author : dxc
# @File : factory_method.py
"""
工厂方法模式
    设计一个工厂的抽象方法 抽象接口 新的功能直接新添一个类实现抽象方法就好了
"""

from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    """
    接口类
    """

    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):
    """
    支付宝类
    """

    def pay(self, money):
        print("支付宝支付:{}".format(money))


class WechatPay(Payment):
    """
    微信支付类
    """

    def pay(self, money):
        print("微信支付:{}".format(money))


class PaymentFactory(metaclass=ABCMeta):
    """
    创建工厂的抽象方法
    """

    @abstractmethod
    def create_payment(self):
        pass


class AlipayFactory(PaymentFactory):
    """
    创建支付宝的类
    """

    def create_payment(self):
        return Alipay()


class WechatFactory(PaymentFactory):
    """
    创建微信的类
    """

    def create_payment(self):
        return WechatPay()


if __name__ == '__main__':
    # pay = AlipayFactory()
    factory = WechatFactory()
    pay = factory.create_payment()
    pay.pay(100)
