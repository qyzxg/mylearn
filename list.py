#!/usr/bin/python
# _*_ coding:utf-8 _*_

# t1 = (1, 'de', '3e3')
# print (t1)
# t2 = (t1, 'ff')
# print((t2+t1)[4])
# print(t1[1])
# t3 = ('five', )
# print(t3)

# 求最大公约数
# def findDivisors(n1, n2):
#     divisor = []  # 用来存放所有公约数
#     for i in range(1, min(n1, n2) + 1):
#         if n1 % i == 0 and n2 % i == 0:
#             divisor.append(i)
#     return max(divisor)
#
# # 最小公倍数
# def lcm(n1, n2):
#     tmp = findDivisors(n1, n2)
#     return print(int(n1*n2/tmp))
# lcm(20, 100)
#

# 递归求最大公约数
# def gcd(n1, n2):
#     if n2 == 0:
#         return n1
#     elif n1 >= n2:
#         return gcd(n1, n1 % n2)
#     else:
#         return gcd(n2, n2 % n1)
# print(gcd(100, 20))

# alist = [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]
# alist.sort(key = lambda x: -x["age"])
# print (alist)
r = (85 - 72) / 72
hello = 'hello'
print('小明的成绩提高了{:.2%}'.format(r))
