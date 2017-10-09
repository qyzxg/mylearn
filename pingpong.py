#!/usr/bin/python
# -*- coding:utf-8 -*-


def has_n(k, n):
    if not all([0 <= n <= 9, isinstance(k, int), isinstance(n, int)]):
        raise ValueError
    if k % 10 == n:
        return True
    elif k < 10:
        return False
    else:
        return has_n(k // 10, n)


def pingpong(n, m):
    def helper(k, direction, ret):
        if k == n:
            return ret + direction
        elif k % m == 0 or has_n(k, m):
            return helper(k + 1, -direction, ret + direction)
        else:
            return helper(k + 1, direction, ret + direction)

    return helper(1, 1, 0)


for i in range(1, 454):
    print(pingpong(i, 6))
