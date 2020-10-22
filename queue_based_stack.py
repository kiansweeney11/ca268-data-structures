from Stack import Stack
import sys

class Queue:
    def __init__(self):
        self.enq_stack = Stack()
        self.deq_stack = Stack()
 
    def is_empty(self):
        return self.enq_stack.is_empty() and self.deq_stack.is_empty()
 
    def enqueue(self, item):
        self.enq_stack.push(item)

    def dequeue(self):
        if not self.deq_stack.is_empty():
            return self.deq_stack.pop()
 # Reverse the enqueue stack onto the dequeue stack
        while not self.enq_stack.is_empty():
            self.deq_stack.push(self.enq_stack.pop())

        return self.deq_stack.pop()

def main():
    q = Queue()
    for letter in "samp":
        q.enqueue(letter)

    top = q.dequeue()
    print(top)

    for i in range(3):
        x = q.dequeue()

    for letter in "abc":
        q.enqueue(x)
        q.enqueue(letter)
        
    q.enqueue(top)
 
    while not q.is_empty():
        print(q.dequeue())

if __name__ == '__main__':
    main()
