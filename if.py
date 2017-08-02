#!/usr/bin/python
# # -*- coding:utf-8 -*-
# L1 = ['adam', 'LISA', 'barT']
# def normalize(name):
#     return name[0].upper()+name[1:]
#
# L2 = list(map(normalize,L
# 1))
# print(L2)



L = [('Bob', 75), ('adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(L, key=lambda t: t[0].lower()))
