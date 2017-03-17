可接受任意数量参数的函数

1.任意数量的位置参数 *

def add(first, *rest):
    return first+rest
    
print add(1,2,3,4)
#输出10

2.任意数量的关键字参数 **

def dd(**attrs):         #attrs是一个包含所有被传入进来的关键字参数的字典
    return attrs.items()

print dd(name='jack', age=18)
#输出[('name','jack'), ('age', 18)]
#一个*参数只能出现在函数定义中最后一个位置参数后面，而 **参数只能出现在最后一个参数


3.强制关键字参数

def recv(maxsize, *, block):
    'Receives a message'
    pass

recv(1024, True) # TypeError
recv(1024, block=True) # Ok

4.Lambda

l = []
li = [lambda x,y=n:x+y for n in range(5)]
for x in li:
    l.append(x(2))

print ','.join((str(x) for x in l))
    
#输出 2,3,4,5,6


5.减少函数的参数个数
#比较两点距离并排序  #妙用Partial函数  # 利用 partial() 函数来固定某些参数值

import math
from functools import partial

points = [ (1, 2), (3, 4), (5, 6), (7, 8) ]
pt = (4, 3)
def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 - x1, y2 - y1)

def dis(p):                          # 此处可用partial()代替
    return distance(pt,p)            
points.sort(key=dis)                 # points.sort(key=partial(distance, pt))
print points                         # 结果相等
# [(3, 4), (1, 2), (5, 6), (7, 8)]   # 另用lambda函数也可实现： points.sort(key=lambda x: distance(pt,x))


6.闭包，装饰器
def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

@makebold
@makeitalic
def hello():
    return "hello world"

print hello()
#输出 <b><i>hello world</i></b>


7.装饰器：计算函数运行时间

import time
from functools import wraps

def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(end-start)
        return result
    return wrapper

@timethis
def abc(x, y):
    z = x*x+y*y
    return z

print(abc(12,34))


8.使用装饰器拓充类的功能:  类的装饰器
def log_getattribute(cls):
    orig_getattribute = cls.__getattribute__

    def new_getattribute(self, name):
        print('getting:', name)
        return orig_getattribute(self, name)

    cls.__getattribute__ = new_getattribute
    return cls

@log_getattribute
class A:
    def __init__(self,x):
        self.x = x
    def spam(self):
        pass
    
a = A(42)
print (a.x)
print (a.spam())

#getting: x
#42
#getting: spam
#None
