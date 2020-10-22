import sys
from Stack import Stack
s = Stack()
s.push('D')
s.push('C')
s.push('B')
s.push('A')
x = s.pop()
y = s.pop()
s.push(y)
s.push(x)
s.push(x)
s.push('D')
