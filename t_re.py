#!/usr/bin/python
# -*- coding:utf-8 -*-

import re
l = []
# p = re.compile(r'^a\w*') #匹配所有以a开头的单词
# p = re.compile(r'[\u4e00-\u9fa5]+') #匹配所有中文
# p = re.compile(r'.') #'.'匹配换行符以外的任意字符
# p = re.compile(r'^[as]\w+')#[]以a或s开头的单词,表示字符集,对应的位置可以是[]中的任意字符
# p = re.compile(r'^(av)\w+')#()表示分组,以'av'开头的单词
p = re.compile(r'^\d{6,10}$')
'''\d表示数字,{}表示6位到10位,可以用来匹配QQ号,^表示匹配开头,$表示结尾,这句的意思是
只单独匹配6-10位的数字'''
with open('re.txt', 'r', encoding='utf-8') as file:
    for s in file.read().replace('，', ',').split():
        print(s)
        f = re.match(p,s)
        if f:
            l.append(f.group())

print(l)
