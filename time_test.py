#!/usr/bin/python
# -*- coding:utf-8 -*-

import datetime

str_t = '19/May/2017:04:07:32'
date = datetime.datetime.strptime(str_t, '%d/%b/%Y:%H:%M:%S')
print(date)
