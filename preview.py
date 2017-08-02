#!/usr/bin/python
# -*- coding:utf-8 -*-

import os


def print_directory_contents(sPath):
    if os.path.exists(sPath):
        for dir_path, subdir_list, file_list in os.walk(sPath):
            for file_name in file_list:
                full_path = os.path.join(dir_path, file_name)
                print(full_path)
    else:
        print('路径错误,文件夹不存在')


def print_directory_contents_1(sPath):
    import os
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath, sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)


def func(*args, **kwargs):
    print(args, kwargs)


class MyClass(object):
    def __init__(self):
        self._some_property = "properties are nice"
        self._some_other_property = "VERY nice"

    def instance_method(*args, **kwargs):
        print('called instance_method({},{})'.format(args, kwargs))

    @classmethod
    def class_method(*args, **kwargs):
        print('called class_method({},{})'.format(args, kwargs))

    @staticmethod
    def static_method(*args, **kwargs):
        print('called static_method({},{})'.format(args, kwargs))

    @property
    def some_property(self, *args, **kwargs):
        print("called some_property getter({0},{1},{2})".format(self, args, kwargs))
        return self._some_property

    @some_property.setter
    def some_property(self, *args, **kwargs):
        print("called some_property setter({0},{1},{2})".format(self, args, kwargs))
        self._some_property = args[0]


if __name__ == '__main__':
    """"""
    # print_directory_contents('.')
    l = [i for i in range(10)]
    d = {'a': 1, 'B': 2, 'c': 3, 'C': 4}
    d1 = {k.lower(): d.get(k, 0) + d.get(k.upper(), 0) for (k, v) in d.items()}
    m = MyClass()
    m.instance_method(1, 23, 3, a=1)
    m.class_method(1, 23, 3, a=1)
    m.static_method(1, 23, 3, a=1)
    print(m.some_property)
