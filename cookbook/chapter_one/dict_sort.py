#!/usr/bin/python
# -*- coding:utf-8 -*-

import random, string

l = [1, 2, 3, 4]
x = random.sample(string.ascii_lowercase, 8)
d = {''.join(random.sample(string.ascii_lowercase, 3)): ''.join(random.sample(string.ascii_lowercase, 8)) for i in range(100)}
# d = {'gei': 'tqxrhuil', 'mhk': 'vmopkawn', 'ynw': 'lnmxqfpz', 'own': 'fnwqmdrt', 'gsz': 'acrfxpqk', 'fuc': 'luftjdem',
#      'rbx': 'fgyvmhru', 'qoa': 'olnhwxvy', 'vxr': 'cyopwxlb', 'kug': 'ojsnckup'}
print(sorted(d.items(), key=lambda d: d[0]))  # 按字典key排序
print(sorted(d.items(), key=lambda d: d[1]))  # 按字典value排序
