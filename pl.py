#!/usr/bin/python
# -*- coding:utf-8 -*-

import random
import datetime

def password():
    L1 = [chr(i) for i in range(48, 57)]
    L2 = [chr(i) for i in range(65, 90)]
    L3 = [chr(i) for i in range(97, 123)]
    L = L1 + L2 +L3
    pas = random.sample(L, 20)
    pl = ''.join(pas)
    return pl

# starttime = datetime.datetime.now()
# with open(r'E:\MyProject\test\pass.txt','a') as f:
#     n = 2000000
#     while n>0:
#         f.write(password()+'\n')
#         n -= 1
#
# endtime = datetime.datetime.now()
# print((endtime - starttime).seconds)

with open(r'D:\FileManager\9位-001.txt', 'r', encoding='utf-8', errors='ignore') as f:
    for i in f.readlines()[0:5]:
        r = f.readlines()
        print(i)