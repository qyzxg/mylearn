#!/usr/bin/python
# -*- coding:utf-8 -*-

import time
import datetime
import math

# print(time.time(),datetime.timedelta)
rt = 1246
ct = 3
pt = 7
x = (datetime.datetime.now() - datetime.datetime(2017, 6, 5, 1, 21, 14)).total_seconds()
# y = math.log(31003099, 2)*3
y = x / 600
z = (rt * pow(2, 2) + ct * pow(3.6, 2) + pt * pow(2.9, 2)) / pow(int(y) + 2, 1.2)
print(x, y, z)
