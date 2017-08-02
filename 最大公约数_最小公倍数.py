#!/usr/bin/python
# -*- coding:utf-8 -*-

# 最大公约数
def gcd(x, y):
    if x < y:
        smaller = x
    else:
        smaller = y
    for i in range(1, smaller + 1):
        if x % i == 0 and y % i == 0:
            _gcd = i
    return _gcd


# 最小公倍数
def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    gen = (i for i in range(x * y, greater - 1, -greater))
    for i in gen:
        if i % x == 0 and i % y == 0:
            _lcm = i
    return _lcm


if __name__ == '__main__':
    while True:
        x = int(input('请输入一个整数x:'))
        if x == 0:
            print('程序退出')
            break
        y = int(input('请输入另一个整数y:'))
        print('{},{}的最大公约数是{}'.format(x, y, gcd(x, y)))
        print('{},{}的最小公倍数是{}'.format(x, y, lcm(x, y)))
        if x == 0:
            print('程序退出')
            break
