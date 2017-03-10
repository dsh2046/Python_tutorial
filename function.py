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
