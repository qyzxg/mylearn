#!/usr/bin/python
# -*- coding:utf-8 -*-

import multiprocessing
import os
import uuid

import requests


# def worker():
#     with open('./image_net/fall11_urls.txt', 'rb+') as urls:
#         while True:
#             line = urls.readline()
#             l = line.decode('utf-8', errors='ignore').split()
#             print('正在下载:', l[0], l[1],os.getpid())
#             if not os.path.exists(os.path.join(os.getcwd(), l[0][:9])):
#                 os.makedirs(l[0][:9])
#             dir = os.path.join(os.getcwd(), l[0][:9])
#             file = os.path.join(dir, l[0] + '.jpg')
#             try:
#                 r = requests.get(l[1],timeout=1)
#                 with open(file, 'wb') as pic:
#                     pic.write(r.content)
#             except Exception as e:
#                 print(e)

def download(url):
    print('正在下载:', url, os.getpid())
    _dir = os.path.join(os.getcwd(), 'images')
    if not os.path.exists(_dir):
        os.makedirs(_dir)
    img = requests.get(url)
    filename = uuid.uuid1()
    file = os.path.join(_dir, str(filename) + '.jpg')

    try:
        r = requests.get(url, timeout=1)
        with open(file, 'wb') as pic:
            pic.write(r.content)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    p = multiprocessing.Pool(10)
    with open('./image_net/fall11_urls.txt', 'rb+') as urls:
        while True:
            line = urls.readline()
            l = line.decode('utf-8', errors='ignore').split()
            p.apply_async(download, args=(l[1],))
    p.close()
    p.join()
