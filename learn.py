#coding:utf-8
#!/usr/bin/python
# Filename: map.py
from PIL import Image

1. # 类的使用 #
class Student(object):
    def __init__(self, name, age):     
        self.__name=name
        self.age=age

    def getname(self):
        print self.__name

james = Student("james", 15)
mike = Student("mike", 20)

2. # @property的使用 #
class Screen(object):

    @property
    def width(self):
        print self._width

    @width.setter
    def width(self,value):
        self._width=value

s = Screen()
s.width=100
s.width          # 输出100
