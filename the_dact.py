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
