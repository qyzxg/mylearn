#!/usr/bin/python
# -*- coding:utf-8 -*-

from functools import  wraps
# def log(func):
#     @wraps(func)
#     def wrapper(*args, **kw):
#         print('call: %s()' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
#
#
# def logs(func):
#     @wraps(func)
#     def wrapper(a, b, **kw):
#         if isinstance(a, (int,float)) and isinstance(b, (int,float)):
#             func(a,b, **kw)
#         else:
#             print('参数必须是整数')
#     return wrapper

def logs(start='start',end='end'):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kw):
            print('%s call:%s()' % (start, func.__name__))
            func(*args, **kw)
            print('%s call:%s()' % (end, func.__name__))
        return wrapper
    return decorator

@logs()
def add(a, b):
    print(a+b)


add(1, 434.4)
