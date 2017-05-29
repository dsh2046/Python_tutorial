#!/usr/bin/ python3.5
# -*- coding: utf-8 -*-
1. 基础用法
# Function decorator
def decorator(original_func):
     def wrapper(*args, **kwargs):
          print("Wrapper content")
          original_func(*args, **kwargs)
     return wrapper

# Class decorator
class decorator_class(object):
     def __init__(self, original_func):
          self.original_func = original_func

     def __call__(self, *args, **kwargs):
          print("call method content")
          return self.original_func(*args, **kwargs)

@decorator  # Or @decorator_class
def test(arg):
     print(arg)

test('Hi Im original function')

2. 一般用发
from functools import wraps

# 记录Ｌｏｇ日志，　生成ｌｏｇ文件
def my_logger(orig_func):
     import logging
     logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)
     @wraps(orig_func)
     def wrapper(*args, **kwargs):
          logging.info('ran with args: {}, and kwargs: {}'.format(args, kwargs))
          return orig_func(*args, **kwargs)
     return wrapper

# 计时
def my_timer(orig_func):
     import time
     @wraps(orig_func)
     def wrapper(*args, **kwargs):
          t1 = time.time()
          orig_func(*args, **kwargs)
          t2 = time.time() - t1
          print('Time used: {}'.format(t2))
     return wrapper

@my_timer
@my_logger                # 相当于 test = my_timer(my_logger(test))
def test(*arg, **kwargs):
     print(arg, kwargs)

test(12,34)
