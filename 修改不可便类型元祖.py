# def __new__()
class IntTuple(tuple):
    def __new__(cls, iterable):
        g = (x for x in iterable if isinstance(x,int) and x>0)
        return super(IntTuple, cls).__new__(cls,g)


    def __init__(self, f):
        super(IntTuple, self).__init__()

t = IntTuple([12,-2,'wer'])

print(t)
