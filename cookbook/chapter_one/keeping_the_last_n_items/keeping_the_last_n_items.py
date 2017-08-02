#!/usr/bin/python
# -*- coding:utf-8 -*-

from collections import deque

def search(items,pattern,history = 5):
    lines = deque(maxlen=history)
    for i in items:
        if pattern in i:
            yield i, lines
            lines.append(i)

if __name__ == '__main__':
    with open('somefile.txt') as file:
        for line, prelines in search(file, 'python', 5):
            for i in prelines:
                print(i)
            print(list(prelines))
