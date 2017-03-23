# 找出字典中的共同键 （&操作，map(), reduce()）
from random import *
from functools import reduce

s1 = {x:randint(1,4) for x in sample('abcdefg', randint(3,6))}
s2 = {x:randint(1,4) for x in sample('abcdefg', randint(3,6))}
s3 = {x:randint(1,4) for x in sample('abcdefg', randint(3,6))}

print(list(reduce(lambda x,y: x&y, map(dict.keys, [s1,s2,s3]))))
