#!/usr/bin/python
# -*- coding:utf-8 -*-

import random
import math
import time
import unittest
import inspect
from functools import wraps, reduce


# 二分法查找
def bsearch(lst, target):
    if not all([lst, isinstance(target, (int, float))]):
        return '数组为空或target不为数字'
    lst.sort()
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] > target:
            high = mid - 1
        elif lst[mid] < target:
            low = mid + 1
        else:
            return '{}在数组中的索引位置是{}'.format(target, mid)
    return '{}没找到'.format(target)


class MyStack():
    def __init__(self):
        '''初始化'''
        self._items = []

    def isempty(self):
        '''判断栈是否为空'''
        return self._items == []

    def push(self, value):
        '''向栈内添加元素'''
        self._items.append(value)

    def pop(self):
        '''返回并弹出栈底元素'''
        return self._items.pop()

    def peek(self):
        '''返回栈顶元素'''
        return self._items[len(self._items) - 1]

    def size(self):
        '''返回栈大小'''
        return len(self._items)

    def lst(self):
        return self._items


class MyQueue():
    def __init__(self):
        self._items = []

    def isempty(self):
        return self._items == []

    def addfront(self, value):
        self._items.insert(0, value)

    def addend(self, value):
        self._items.append(value)

    def removefront(self):
        return self._items.pop(0)

    def removeend(self):
        return self._items.pop()

    def size(self):
        return len(self._items)


def restring(mystr):
    # 利用栈反转字符串
    s = MyStack()
    output = ''
    for i in mystr:
        s.push(i)
    while not s.isempty():
        output += s.pop()
    return output


def baseConverter(dec_number, base):
    # 利用栈做10进制到任意进制的转换
    base_str = '0123456789ABCDEF'
    s = MyStack()
    new_string = ''

    while dec_number > 0:
        mod = dec_number % base
        s.push(mod)
        dec_number = dec_number // base

    while not s.isempty():
        new_string += base_str[s.pop()]

    return new_string


def palcheker(my_str):
    char_queue = MyQueue()
    for i in my_str:
        char_queue.addend(i)
    flag = True
    while char_queue.size() > 1 and flag:
        front = char_queue.removefront()
        end = char_queue.removeend()
        if front != end:
            flag = False
    return flag


def is_prime(n):
    if not type(n) == int:
        raise ValueError
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# def change(coins, num):
#     # 找零问题
#     alist = [0] * (num + 1)
#     for i in range(1, num + 1):
#         temp = num
#         j = 0
#         while j <= len(coins) - 1 and i >= coins[j]:
#             temp = min(alist[i - coins[j]], temp)
#             j += 1
#         alist[i] = temp + 1
#     return alist.pop(), alist

def coin_change(coins, money):
    """
    背包问题解法?
    :param values: [25, 21, 10, 5, 1]
    :param money:  63
    :return: {1:1, 2:2, 3:3, 4:4, 5:1, ..., 63:3}
    """
    coin_count = {i: 0 for i in range(money + 1)}
    for cents in range(1, money + 1):
        min_coins = cents  # 从第一个开始到money的所有情况初始
        for value in coins:
            if value <= cents:
                temp = coin_count[cents - value] + 1  # 这不是经典的背包?
                if temp < min_coins:
                    min_coins = temp
        coin_count[cents] = min_coins
    print('面值为：{0} 的最小硬币数目为：{1} '.format(cents, coin_count[cents]))


# 排序算法
# 0x01 冒泡排序
def bubble_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                if lst[i] > lst[j]:
                    lst[i], lst[j] = lst[j], lst[i]
    return lst


# 0x02 快速排序 去重
def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    temp = random.choice(lst)
    lesser = quick_sort([i for i in lst if i < temp])
    greater = quick_sort([i for i in lst if i > temp])
    return lesser + [temp] + greater


# 0x03 快速排序 不去重
def quick_sort1(lst):
    if len(lst) <= 1:
        return lst
    temp = random.choice(lst)
    lesser = [i for i in lst if i < temp]
    medium = [i for i in lst if i == temp]
    greater = [i for i in lst if i > temp]
    return quick_sort(lesser) + medium + quick_sort(greater)


# 0x04 插入排序
def insert_sort(lst):
    if len(lst) <= 1:
        return lst
    for i in range(1, len(lst)):
        k = lst[i]
        j = i - 1
        while j >= 0:
            if lst[j] > k:
                lst[j + 1] = lst[j]
                lst[j] = k
            j -= 1
    return lst


def fib(n):
    a, b = 0, 1
    while n > 0:
        yield a
        a, b = b, a + b
        n -= 1


def fib1(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib1(n - 2) + fib1(n - 1)


#
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return True


def get_current_func_name():
    return inspect.stack()[1][3]


# class TestBsearch(unittest.TestCase):
#     # def setUp(self):
#     #     print('Start test...')
#     #
#     # def tearDown(self):
#     #     print('Finish test...')
#
#     def test_error(self):
#         print('Start test {}...'.format(get_current_func_name()))
#         self.assertEqual(bsearch([], 4), '数组为空或target不为数字')
#         self.assertEqual(bsearch([], 4.5), '数组为空或target不为数字')
#         self.assertEqual(bsearch([1, 3, 4], 'a'), '数组为空或target不为数字')
#         self.assertEqual(bsearch([2.1, 7.8], '2.1'), '数组为空或target不为数字')
#
#     def test_found(self):
#         print('Start test {}...'.format(get_current_func_name()))
#         self.assertEqual(bsearch([1, 3, 4], 3), '3在数组中的索引位置是1')
#         self.assertEqual(bsearch([2.1, 7.8], 2.1), '2.1在数组中的索引位置是0')
#
#     def test_not_found(self):
#         print('Start test {}...'.format(get_current_func_name()))
#         self.assertEqual(bsearch([2.1, 7.8], 2.3), '2.3没找到')


def hello():
    print('正在调用函数{}'.format(inspect.stack()[0][3]))


def singleton(cls):
    '''装饰器实现单例模式'''
    instance = {}

    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return get_instance


@singleton
class MyClass(object):
    pass


class SingleTon(object):
    '''使用元类实现单例模式'''
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SingleTon, cls).__new__(cls, *args, **kwargs)
            return cls._instance


class MyClass1(object):
    __metaclass__ = SingleTon


def args_check():
    def decorator(func):
        @wraps(func)
        def wrapper(*arg, **kwargs):
            pass


def timeit(process_time=False):
    t = time.clock if process_time else time.time

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = t()
            f = func(*args, **kwargs)
            print(t() - start)
            return f

        return wrapper

    return decorator


@timeit(True)
def check():
    time.sleep(2)



if __name__ == '__main__':
    # l = [i for i in range(-4, 25)]
    # print(l)
    # random.shuffle(l)
    # print(l)
    # l2 = qsort(l)
    # print(l2)
    # p = bsearch(l2, 5)
    # print(p)

    # print(restring('abc,wewwewewewewewewew'))
    # print(baseConverter(100, 3))
    # for i in range(2, 17):
    #     n = 520
    #     print('{}转换为{}进制是:'.format(n, i), baseConverter(n, int(i)))
    # print(palcheker('er45re'))
    # print(list(filter(isPrime, range(1001))))
    # coin_change([1, 5, 10, 20], 55)
    # print(bubble_sort([1], desc=False))

    # print(list(filter(is_prime, range(100))))
    # print(fn(, map(fib1, range(30))))
    # from operator import add, mul
    #
    # print(sum(map(fib1, range(300))))
    # print(reduce(mul, range(1, 31)))
    # print(list(filter(lambda x: x % 2 == 0, range(30))))
    # print(list(filter(is_prime, range(300000000)))[-10:])
    # print(is_prime(355678565343567676444535635354656565653434545656553134343331))
    check()
