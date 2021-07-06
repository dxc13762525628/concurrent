#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/5 10:48 
# @Author : dxc
# @File : simple_factory.py
"""
简单工厂模式
    不止阶向客户端暴露对象创建的细节，而是通过一个方法来创建对象
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


class PaymentFactory:
    """
    创建一个工厂
    """
    def create_payment(self, method):
        if method == 'alipay':
            return Alipay()
        elif method == 'wechat':
            return WechatPay()
        else:
            raise TypeError("No such class")


if __name__ == '__main__':
    payment = PaymentFactory()
    # pay = payment.create_payment('alipay')
    pay = payment.create_payment('wechat')
    pay.pay(100)
