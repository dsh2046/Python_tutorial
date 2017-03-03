#coding:utf-8
#!/usr/bin/python

1. #四舍五入
print round(1.234,2)
# 1.23

2. #更改文件权限
import os

os.chmod('script.py', 0o755)

3. #进制转换
bin(x)  or  format(x, 'b')  #二进制
oct(x)  or  format(x, 'o')  #八进制
hex(x)  or  format(x, 'x')  #十六进制

4. #数组
import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print np.where(a<7, 2, 3)
# [[2 2 2 2]
# [2 2 3 3]
# [3 3 3 3]]
print a[:,1]
# [2,6,10]
