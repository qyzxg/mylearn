import datetime

# x = 8
# j = 0.000000001
# guess = 0
# l = 0.0
# h = x
# ans = (l+h)/2.0
# while abs(ans**2-x) >= j:
#    print('l='+str(l)+'h='+str(h)+'ans='+str(ans))
#    guess += 1
#    if (ans**2) < x:
#        l = ans
#    else:
#       h = ans
#    ans = (l+h)/2.0
# print('numGuesses = ' + str(guess))
# print(str(ans) + ' is close to square root of ' + str(x))


# def fob(n):
#     x, y = 0, 1
#     result = []
#     while y < n:
#         result.append(y)
#         x, y = y, x+y
#     print(result)
#
#
# def fib(n):
#     if n <= 1:
#         return n
#     else:
#         return fib(n-1)+fib(n-2)
# print(fib(16))
# fob(1000)
# while True:
#     n = int(input('请输入一个整数'))
#     print(fob(n))

# def su(n):
#     result = 0
#     for i in range(n+1):
#        result += i
#     return result
# print(su(100))

# def jiec(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
#
# print(jiec(10))

# 递归求积
# def cj(a, b):
#     if b == 1:
#         return a
#     else:
#         return a + cj(a, b-1)
# print(cj(3, 5))

'''
穷举法找小偷问题
抓了a,b,c,d4名犯罪嫌疑人.其中有一名是小偷，审讯中：
a说：我不是小偷
b说：c是小偷
c说：小偷肯定是d
d说：c胡说
其中有3个人说的是实话，一个人说的是假话，编程推断谁是小偷。
'''

# ts = ['a', 'b', 'c', 'd']
# for thief in ts:
#     sums = (thief != 'a')+(thief == 'c')+(thief == 'd')+(thief != 'd')
#     if sums == 3:
#         print('小偷是:%s' % thief)
# def pf(n):
#     return n * n
# import random
# import math
# print(list(map(lambda n: pow(n, math.radians(random.random())), [i for i in range(210)])))


# list = map(str, [i for i in range(1, 501)])
# st = ''.join(list).replace('123', '``')
# print(st)
# print(datetime.datetime.now().strftime('%Y-%m-%d'))

import json, os

d = json.load(open('select.json', 'r', encoding='utf-8'))
print(d['industry'])
print(os.path.dirname(__file__))