#!/usr/bin/python
# -*- coding:utf-8 -*-

# import subprocess
#
#
# child = subprocess.Popen(['ping', '-c', '5', 'www.google.com'])
# print(child.pid)
# print('parent process')

import os
import random
import time
from multiprocessing import Pool


# def worker(sign, lock):
#     lock.acquire()
#     print(sign, os.getpid())
#     lock.release()
#     time.sleep(2)
#
#
# def pt():
#     for i in range(5):
#         print(i)
#
#
# record_t = []
# lock_t = threading.Lock()
#
# for i in range(5):
#     th = threading.Thread(target=worker, args=('thread', lock_t))
#     th.start()
#     record_t.append(th)
#
# for th in record_t:
#     th.join()
#
# p = threading.Thread(target=pt)
# p.start()
# p.join()

# if __name__ == '__main__':
#     print('main:', os.getpid())
#     record_m = []
#     lock_m = multiprocessing.Lock()
#     for i in range(5):
#         mu = multiprocessing.Process(target=worker, args=('process', lock_m))
#         mu.start()
#         record_m.append(mu)
#
#
#     for mu in record_m:
#         mu.join()

def tasks(name):
    print('run tasks {},pid = {}'.format(name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('task {} runs {:.2f} seconds'.format(name, (end - start)))


if __name__ == '__main__':
    print('parent process {} is running'.format(os.getpid()))
    p = Pool(5)
    for i in map(chr, [j for j in range(97, 104)]):
        p.apply_async(tasks, args=(i,))
    print('waitting for subprocess all done')
    p.close()
    p.join()
    print('All subprocesses done.')
