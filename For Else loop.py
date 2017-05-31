a = ['john', 'mike', 'corey']
flag = ''
for x in a:
    if 'john' in x:
        print('yes')
        break
else:                 ＃for/else loop中的else相当于'no break'声明，即＇no break＇才会执行else中的语句
    flag = 'no'
    print(flag)
