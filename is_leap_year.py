#!/usr/bin/python
# -*- coding:utf-8 -*-
import random
import unittest


def q_sort(item):
    '''不去重'''
    if len(item) < 2:
        return item
    else:
        pivot = random.choice(item)
        lesser = [i for i in item if i < pivot]
        medium = [i for i in item if i == pivot]
        greatter = [i for i in item if i > pivot]
        return q_sort(lesser) + medium + q_sort(greatter)


def q_sort_nd(item):
    '''去重 no duplicate'''
    if len(item) < 2:
        return item
    else:
        pivot = item[0]
        lesser = q_sort_nd([i for i in item if i < pivot])
        greatter = q_sort_nd([i for i in item if i > pivot])
        return lesser + [pivot] + greatter


def is_leap_year(n):
    year = int(n)
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


def find(item, target):
    trow = len(item)  # 总行数
    tcol = len(item[0])  # 总列数
    row = 0
    col = tcol - 1
    while row < trow and col >= 0:
        if item[row][col] == target:  # 从左上角开始找
            return '{}找到了,在第{}行,第{}列'.format(target, row + 1, col + 1)
        elif item[row][col] > target:
            col -= 1
        else:
            row += 1
    return '{}没找到'.format(target)


class TestLeap(unittest.TestCase):
    def setUp(self):
        self.f_list = [[i for i in range(1, 5)],
                       [i for i in range(6, 10)]]
        self.s_list = [1, 9, 3, 17, 8, 13, 11, 86, 2, 3, 2]
        print('测试开始')

    def tearDown(self):
        print('测试结束')

    def test_is_leap_year(self):
        '''测试函数is_leap_year(n)'''
        self.assertFalse(is_leap_year(1999))
        self.assertFalse(is_leap_year(200))
        self.assertTrue(is_leap_year(2000))
        self.assertTrue(is_leap_year(1996))
        self.assertFalse(is_leap_year(1700))

    def test_find(self):
        '''测试函数find(item, target)'''
        self.assertEqual(find(self.f_list, 8), '8找到了,在第2行,第3列')
        self.assertEqual(find(self.f_list, 17), '17没找到')
        self.assertEqual(find(self.f_list, -5), '-5没找到')

    def test_q_sort(self):
        '''测试函数q_sort(item)'''
        self.assertListEqual(q_sort(self.s_list), [1, 2, 2, 3, 3, 8, 9, 11, 13, 17, 86])

    def test_q_sort_nd(self):
        '''测试函数q_sort(item)'''
        self.assertListEqual(q_sort_nd(self.s_list), [1, 2, 3, 8, 9, 11, 13, 17, 86])


if __name__ == '__main__':
    unittest.main(verbosity=2)
