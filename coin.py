#!/usr/bin/python
# -*- coding:utf-8 -*-

import datetime
import random


# ls = []
# for i in range(1,10001):
#     ls.append(random.randint(1,6))
#
# a = {}
# for j in ls:
#     a[j] = ls.count(j)
#
# b = []
# for (k,v) in a.items():
#     b.append(int(v)/10000)
# print(b)

def coins(n, a, b):
    ls = []
    c = {}
    d = []
    for i in range(n + 1):
        ls.append(random.randint(a, b))

    for j in ls:
        c[j] = ls.count(j)

    for (k, v) in c.items():
        d.append(int(v) / n)
    return d


print('开始时间:%r' % datetime.datetime.now())
g = coins(1000000, 1, 6)
print(g)
print('结束时间:%r' % datetime.datetime.now())
