#!/usr/bin/python
# -*- coding:utf-8 -*-
import re

reg = r'<img alt.*? src="(.*?)".*?/>'
p = re.compile(reg)

s = '''
<p>个&ldquo;user_collect_food&rdquo;表<br />
如此一来我们需要三个表：<br />
user(&nbsp;主键user_id,user_name,password)，<br />
food(&nbsp;主键food_id,description,operation)，<br />
user_collect_food(&nbsp;联合主键（user_id,food_id）,collect_time)，在此基础上，我们来实现它吧<br />
<br />
效果：点一下&ldquo;收藏&rdquo;，再点一下取消&ldquo;收藏&ldquo;，同时完成对数据库的操作<br />
<br />
(许多其它功能，比如&rdquo;喜爱&ldquo;&rdquo;评论个数&ldquo;等实现过程与这个相类似~)<br />
<br />
下面的效果图是我实现的另一个页面的效果图，放在这里只是为了说明收藏图标的点亮效果</p>

<p><strong>标签：</strong>&nbsp;&lt;无&gt;</p><img alt="" src="https://static.oschina.net/uploa25191443_eP0s.jpg" />

<h2>代码片段(6)<a href="https://www.oschina.net/code/piece_full?code=37538" target="_blank">[全屏查看所有代码]</a></h2>

<h3>1.&nbsp;[图片]&nbsp;效果_副本.png<a name="55304"></a>&nbsp;&nbsp;&nbsp;&nbsp;</h3>

<p><img alt="" src="https://static.oschina.net/uploads/code/201407/25191443_eP0s.png" /></p>
'''
import random


#
#
# # print(p.search(s).group(1))
# class MyIter(object):
#     '''生成器类,返回n个随机整型'''
#
#     def __init__(self, n):
#         self.n = n
#         self.i = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.i += 1
#         if self.i > self.n:
#             raise StopIteration
#         return random.randint(0, self.n)
#
#
# class MyOpen:
#     def __init__(self, filename, mode, encoding):
#         self.filename = filename
#         self.mode = mode
#         self.encoding = encoding
#         self.file = open(self.filename, mode=self.mode, encoding=self.encoding)
#         self.file.readline()
#
#     def read(self):
#         return self.file.read()
#
#     def write(self, content):
#         self.file.write(content + '\n')
#
#     def __enter__(self):
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()
#
#     def __str__(self):
#         return self.filename
#
#     def __call__(self, *args, **kwargs):
#         return self.read()
#
# f = MyOpen('access.log', 'r', 'utf-8')
# print(f())

class MyIter:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i > self.n:
            raise StopIteration
        return random.randint(1, self.n)


for i in MyIter(10):
    print(i)
