#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/6 10:09 
# @Author : dxc
# @File : adapter.py
"""
适配器模式
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


class BankPay:
    """
    银联支付 用户通过调用pay会报错
    """

    def cost(self, money):
        print("银联支付:{}".format(money))


class ApplePay:
    """
    苹果支付
    """
    def cost(self, money):
        print("苹果支付", money)


class NewBankPay(BankPay, Payment):
    """
    类适配器
    适配器模式类 直接复用bankPay的方法 这样用户可以统一调用 pay方法
    方式一:只有一个的时候
    """

    def pay(self, money):
        return self.cost(money)


class PaymentAdapter(Payment):
    """
    方式二  多个需要适配器的时候
        对象适配器
    """
    def __init__(self, payment):
        """
        支付的对象
        :param payment:
        """
        self.payment = payment

    def pay(self, money):
        self.payment.cost(money)


if __name__ == '__main__':
    # pay = PaymentAdapter(ApplePay())
    pay = PaymentAdapter(BankPay())
    pay.pay(100)
