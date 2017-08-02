#!/usr/bin/python
# -*- coding:utf-8 -*-

# from wxpy import *
#
# bot = Bot()
# myself = bot.self
# myself.send('hello')
#
# @bot.register(except_self=True)
# def print_messages(msg):
#     print(msg)
# bot.join()


def jiec_1(n):  # 递归
    if n == 1:
        return n
    else:
        return jiec_1(n - 1) * n


def jiec_2(n):  # 迭代
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def jiec_3(n):  # 自增
    result = 1
    i = 1
    while i < n + 1:
        result *= i
        i += 1
    return result


def jiec_4(n):  # 自增
    result = 1
    i = n
    while not i < 1:
        result *= i
        i -= 1
    return result


for func in [jiec_1, jiec_2, jiec_3, jiec_4]:
    for i in range(5, 11):
        print(func(i))
