#!/usr/bin/python
# -*- coding:utf-8 -*-

# class A(object):
#     def __init__(self):
#         print('sA')
#
# class B(A):
#     def __init__(self):
#         super().__init__()
#         print('B')
#
# class C(B,A):
#     def __init__(self):
#         super().__init__()
#         print('C')
#
# # a = A()
# # b = B()
# c = C()

# class People(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return self.name + ':' + str(self.age)
#
#     def __lt__(self, other):
#         '如果名字不一样则按照名字排序,否则按年龄排'
#         return self.name < other.name if self.name != other.name else self.age < other.age
#
#
# print('\t'.join([str(i) for i in sorted([People("abc", 18),
#                                          People("abe", 19),
#                                          People("abe", 12),
#                                          People("abc", 17)])]))

import random
import re

import jieba
import nltk

file = open('Walden.txt', 'r', encoding='utf-8')
walden = file.read()
r1 = u'[a-zA-Z0-9’!"#$%&\'()*+,-./:;<=>?@?★、…【】《》？“”‘’！[\\]^_`{|}~]+'
tem = re.sub(r1, '', walden)
walden = jieba.lcut(tem, cut_all=False)
print(walden)


def makePairs(arr):
    pairs = []
    for i in range(len(arr)):
        if i < len(arr) - 1:
            temp = (arr[i], arr[i + 1])
            pairs.append(temp)
    return pairs


def generate(cfd, word='我', num=100):
    for i in range(num):
        # make an array with the words shown by proper count
        arr = []
        for j in cfd[word]:
            for k in range(cfd[word][j]):
                arr.append(j)
        print(word, end='')

        # choose the word randomly from the conditional distribution
        word = arr[int((len(arr)) * random.random())]


pairs = makePairs(walden)
cfd = nltk.ConditionalFreqDist(pairs)
print(list(cfd))
generate(cfd)
