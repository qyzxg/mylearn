#!/usr/bin/python
# -*- coding:utf-8 -*-

from collections import Counter


def count(file_path):
    l = []
    d = {}
    with open(file_path, 'r') as file:
        for line in file.readlines():
            if line.split():
                for word in line.split():
                    l.append(word.lower().strip().replace('"', '').replace('?', ''))
    # 方法1
    # for i in l:
    #     if not i in d.keys():
    #         d[i] = 1
    #     else:
    #         d[i] += 1
    #
    # ls = [(k, v) for (k, v) in d.items()]
    # result = sorted(ls, key=lambda l: l[1], reverse=True)
    # return result

    # 方法2
    word_counts = Counter(l)
    result = word_counts.most_common()
    return result


if __name__ == '__main__':
    print(count('./text/The Old Man and the Sea.txt'))
