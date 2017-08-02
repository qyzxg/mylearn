#!/usr/bin/python
# -*- coding:utf-8 -*-

import sqlite3
from collections import Iterable

import matplotlib.pyplot as plt


def fatten(items, filts=(str, bytes)):
    for i in items:
        if isinstance(i, Iterable) and not isinstance(i, filts):
            yield from fatten(i)
        else:
            yield i


conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM traffic WHERE `if`=2')
values = cursor.fetchall()
print(values)
for i in fatten(values):
    print(i, end=',')
ds = {i: 0 for i in range(1, 8)}  # 统计每月发送的流量
dr = {i: 0 for i in range(1, 8)}  # 统计每月接收的流量
for i in values:
    for j in range(1, 8):
        if i[2] == j:
            ds[j] += i[4]
            dr[j] += i[5]
drg = {i: int(j / 1024 / 1024 / 1024) for (i, j) in dr.items()}
dsg = {i: int(j / 1024 / 1024 / 1024) for (i, j) in ds.items()}
print(drg)
print(dsg)

plt.plot(list(drg.keys()), list(drg.values()))
plt.plot(list(dsg.keys()), list(dsg.values()))
plt.axis([0, 8, 0, 200])
plt.show()
