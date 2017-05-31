from collections import namedtuple


Color = namedtuple('Color2', ['red', 'green', 'blue'])

abc = Color(10, 23, 45)

print(abc.red)
