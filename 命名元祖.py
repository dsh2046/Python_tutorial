from collections import namedtuple

student = namedtuple('student', ['name','age','sex'])
s1 = student('Jack', '18', 'male')

print(s1.name)
#Jack

print(s1)
#student(name='Jack', age='18', sex='male')
