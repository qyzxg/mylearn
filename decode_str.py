#!/usr/bin/python
# -*- coding:utf-8 -*-
import itertools
from functools import reduce

from mysql.connector import connect
from sqlalchemy.ext.declarative import declarative_base

def decode_str(s):
    tem = []
    result = []
    for i in s:
        try:
            int(i)
            tem.append(i + ' ')
        except:
            tem.append(i)
    for j in ''.join(tem).split():
        j = int(j[-1]) * j[:-1]
        result.append(j)
    return ''.join(result)




def encode_int(n, x=5, y=10):
    tem = []
    for i in str(n):
        i = str((int(i) + x) % y)
        tem.append(i)
    return int(''.join(tem[::-1]))


def permutation_str(s, n):
    l = itertools.permutations(list(str(s)), n)
    for i in l:
        yield ''.join(list(i))


def sum_int(n):
    s = reduce(lambda x, y: x + y, range(1, n))
    return s


if __name__ == '__main__':
    print(decode_str('s2df4rcd7fd5'))
    print(encode_int(12345, 1, 7))
    for i in permutation_str(12345, 2):
        print(i)
    print(sum_int(12))
    db = connect(host='localhost', user='root', password='qyzxg', database='blog')
    cur = db.cursor()
    cur.execute('select * from users')
    for i in cur:
        print(i)