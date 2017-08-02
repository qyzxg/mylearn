#!/usr/bin/python
# -*- coding:utf-8 -*-

names = ['Michael', 'Bob', 'Tracy']
scores = ['89', '56', '78']
# student = {k:v for k in names for v in scores} #错误
student = dict(zip(names, scores))
print(student)
t = tuple(zip(names, scores))
print(t)
s1 = sorted(t, key=lambda s: s[1], reverse=True)
s2 = sorted(t, key=lambda s: s[0].lower())
print(s1)
print(s2)

d = {'OTHERS': 103508, 'RH-': 1936, 'MNSSU': 1784, 'P': 228, 'B': 16670, 'A': 15542, 'O': 40216, 'AB': 11548}
for k,v in d.items():
    s = "{name:'%s', value:%d}," % (k,v)
    print(s)

print(d.keys())
# print(d.values())
