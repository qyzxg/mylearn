#!/usr/bin/python
# -*- coding:utf-8 -*-

import random

# str_len = 60
#
# # random_str = ''.join([random.choice(string.ascii_letters+'0123456789@#$%&?') for i in range(str_len)])
# n = 0
# while True:
#     # random_str = ''.join([random.choice(string.ascii_letters + '0123456789@#$%&?') for i in range(str_len)])
#     # random_str = ''.join(random.sample(string.ascii_letters+'0123456789@#$%&?', str_len))
#     random_str = random.sample([1, 2, 2, 2], 3)
#     n += 1
#     print('第%d次:   ' % n, random_str)

l = [1,2,3]
random.shuffle(l)
print(l)