1. @classmethod     ＃相当于类的过滤函数
class Employee:

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay

    def fullname(self):
        fullname = self.fname + '.' + self.lname
        return fullname

    @classmethod
    def from_str(cls, emp_str):
        fname, lname, pay = emp_str.split('-')
        return cls(fname, lname, pay)　　　　　　　　　＃最终返回一个实例化对象

emp1_str = 'samuel-deng-9000'
emp2_str = 'mike-henry-5000'

emp1 = Employee.from_str(emp1_str)
emp2 = Employee.from_str(emp2_str)
print(emp1.fullname())
