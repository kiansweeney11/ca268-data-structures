from Queue import Queue

import sys
def print_queue(data, front, back):
   q = Queue()
   




from Queue import Queue 
from print_queue import print_queue

def main():
   size = int(input())
   q = Queue(size)

   command = input()
   while len(command) > 0:
      if command[0] == 'a': # add
         item = command.split()[1]
         q.enqueue(int(item));
      elif command[0] == 'r': # remove
         q.dequeue();
      else:
         print("Unknown command!")
      command = input()

   print_queue(q.data, q.front, q.back)

if __name__ == "__main__":
   main()
