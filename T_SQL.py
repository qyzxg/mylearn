#!/usr/bin/python
# -*- coding:utf-8 -*-

l = [str('name'), str('value')]
with open('data.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        a = dict(zip(l, [line.split()[0], int(line.split()[1].replace(',', ''))]))
        print(a, ',')
