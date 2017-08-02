#!/usr/bin/python
# -*- coding:utf-8 -*-

# def setupmethod(f):
#     def wrapper_func(self,*args,**kwargs):
#         if self.debug and self._got_first_request:
#             raise self.AessertionError('A setup functionj...')
#         return f(self,*args,**kwargs)
#     return update_wrapper(wrapper_func(),f)
#
#
# def route(self,rule,**options):
#     def decorator(f):
#         endpoint = options.pop('endpoint',None)
#         self.add_url_rule(rule,endpoint,f,**options)
#         return f
#     return decorator
# def atestDe1(func):
#     def de(a, b, c):
#         func(a, b, c)
#         print('1')
#     print('2')
#     return de
# @atestDe1
# def atest2(a, b, c):
#     print(a+b+c)
#
# if __name__ == '__main__':
#     atest2(1,2,3)

# def route(self, rule, **options):
#     def decorator(f):
#         endpoint = options.pop("endpoint", None)
#         self.add_url_rule(rule, endpoint, f, **options)
#         return f
#
#     return decorator
#
#
# def route(self, rule, **options):
#     def decorator(f):
#         endpoint = options.pop('endpoint', None)
#         self.add_url_rule(rule, endpoint, f, **options)
#         return decorator
n = 0


def natuals():
    global n
    while True:
        n += 1
        yield n


for i in natuals():
    print(i)
