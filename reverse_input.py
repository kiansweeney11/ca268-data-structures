import sys
def reverse_input(stack):
   line = sys.stdin.readline().strip()
   while 0 < len(line):
      stack.push(line)
      line = sys.stdin.readline().strip()

   string = ""
   while not stack.is_empty():
      string = string + stack.pop() + "\n"

   return string.strip()

from Stack import Stack
from reverse_input import reverse_input
stack = Stack()
print(reverse_input(stack))
