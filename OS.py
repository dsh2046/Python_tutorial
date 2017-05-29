import os

1. os.getcwd()      获得当前工作路径
2. os.chdir('./')   改变路径
3. os.listdir('./') 列出路径的文件和文件夹
4. os.stat('test.txt') 列出文件的信息
5. os.rename('','')  重命名文件

6. os.walk
for dirpath, dirnames, filenames in os.walk('./'):
  print(....)    #列出路径下的（包括子路径）的所有文件，　用于遍历文件或者寻找文件
