class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property             ＃可像属性一样直接调用，emp_1.email
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property                  #getter
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
        
    @fullname.setter            #setter
    def fullname(self, name):
        fname, lname = name.split(' ')
        self.fname = fname
        self.lname = lname

    @fullname.deleter           #deleter
    def fullname(self):
        self.fname = None
        self.lname = None


emp_1 = Employee('John', 'Smith')

print(emp_1.fullname)          ＃直接提取full name，　不需括号   

emp_1.fullname = 'Samuel Deng'  ＃设置emp_1的全名，同时也更新 fname, lname

del emp_1.fullname           ＃删除emp_1的全名（包括 fname, lname）
