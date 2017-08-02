#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import sys

file_seek = 0


class Tail(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def read_add(self):
        with open(self.file_name, 'r', encoding='utf-8') as file:
            global file_seek
            file.seek(file_seek, 0)
            while True:
                _row = file.readline()
                if _row:
                    file_seek += len(_row)
                    print(_row)
                else:
                    print('没有新增内容')
                    break

    def follow(self, n=10):
        i = n
        with open(self.file_name, 'rb+') as file:
            b = len(file.readline())  # 得到第一行的字符数
            try:
                file.seek(-(b * n * 2), os.SEEK_END)  # 取最后面的b*n*2个字符
            except:
                pass
            for _row in file.readlines()[-n:]:
                # print(_row.decode('utf_8', errors='ignore').split())
                sys.stdout.write('倒数第%d行--->' % i + _row.decode('utf_8', errors='ignore'))
                i -= 1

    def head(self, n=10):
        with open(self.file_name, 'rb+') as file:
            file.seek(len(file.readline()), 0)  # 去掉第一行表头
            for i in range(1, n + 1):
                sys.stdout.write('正数第%d行--->' % i + file.readline().decode('utf_8', errors='ignore'))


if __name__ == '__main__':
    tail = Tail('./image_net/fall11_urls.txt')
    # tail.head()
    tail.follow(10)
    # while True:
    #     tail.read_add()
    #     time.sleep(10)
