#!/usr/bin/python
# -*- coding:utf-8 -*-

classmates = [i for i in range(1, 21)]
print(len(classmates))
print(classmates[:])  # 复制一个新列表
print(classmates[-1])  # 取列表的最后一个元素
print(classmates[::-1])  # 列表倒序
print(classmates[0])  # 取第一个元素
print(classmates[::2])#取奇数
print(classmates[1::2])#取偶数
print(classmates.pop())#默认删除最后一个元素并返回,pop(i)表示删除指定索引的元素
classmates.append("hello")
print(classmates)
classmates.insert(4,'world') #按索引插入元素
print(classmates)

