#!/usr/bin/python
# -*- coding:utf-8 -*-

import datetime
import time

# print(time.time(),datetime.timedelta)
# rt = 1246
# ct = 3
# pt = 7
# x = (datetime.datetime.now() - datetime.datetime(2017, 6, 5, 1, 21, 14)).total_seconds()
# # y = math.log(31003099, 2)*3
# y = x / 600
# z = (rt * pow(2, 2) + ct * pow(3.6, 2) + pt * pow(2.9, 2)) / pow(int(y) + 2, 1.2)
# print(x, y, z)
def time_tans(s):
    '''时间戳转换'''
    tl = time.localtime(float(s))
    ts = time.strftime('%Y-%m-%d %H:%M:%S', tl)
    ds = datetime.datetime.strptime(ts, '%Y-%m-%d %H:%M:%S')
    now = datetime.datetime.now()
    return int((now-ds).days)

print('http://xiaorui.cc/2017/09/15/python-requests-response%E5%80%BC%E5%88%A4%E6%96%AD/'.split('/'))