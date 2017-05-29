#!/usr/bin/ python3.5
# -*- coding: utf-8 -*-

def decorator(original_func):
     def wrapper(*args, **kwargs):
          print("Wrapper content")
          original_func(*args, **kwargs)
     return wrapper

@decorator
def test(arg):
     print(arg)

test('Hi Im original function')
