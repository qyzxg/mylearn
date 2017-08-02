#!/usr/bin/python
# -*- coding:utf-8 -*-

import os


# for root, dirs, files in os.walk(os.getcwd()):
#     for file in files:
#         print(os.path.join(root, file))
def tree(path, depth=0):
    prefix = depth * '| ' + '| -'
    if os.path.isdir(path):
        print(prefix, os.path.basename(path))
        try:
            for item in os.listdir(path):
                tree(os.path.join(path, item), depth + 1)
        except Exception as e:
            print(e)
    else:
        print(prefix, os.path.basename(path))


if __name__ == '__main__':
    tree(os.getcwd())
