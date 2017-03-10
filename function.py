#可接受任意数量参数的函数

1.#任意数量的位置参数
def add(first, *rest):
    return first+rest
    
print add(1,2,3,4)
#输出10
