#!/usr/bin/python
# -*- coding:utf-8 -*-


# 快排
def qsort(lst):
    if len(lst) == 0:
        return []
    else:
        seq = lst[0]
        lesser = qsort([i for i in lst[1:] if i < seq])
        greater = qsort([i for i in lst[1:] if i > seq])
        return lesser + [seq] + greater


# 二分法查找
def bsearch(array, key):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = low + int((high - low) / 2)
        if key < array[mid]:
            high = mid - 1
        elif key > array[mid]:
            low = mid + 1
        else:
            return mid
    return -1


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


def isPrime(n):
    # 判断是否是素数
    flag = True
    if n <= 1:
        flag = False
    i = 2
    while i * i <= n:
        if n % i == 0:
            flag = False
            break
        i += 1
    return flag


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


def bubble_sort(l, desc=True):
    # 冒泡排序,接收一个list,默认降序排列
    lenth = len(l)
    if lenth <= 1:
        return l
    for i in range(lenth):
        for j in range(1, lenth - i):
            if l[j - 1] < l[j]:
                l[j - 1], l[j] = l[j], l[j - 1]
    if desc:
        return l
    else:
        return l[::-1]


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
    print(bubble_sort([1], desc=False))
