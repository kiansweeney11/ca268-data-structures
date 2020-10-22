import LinkedList

class Queue:
    """ A linked list based queue """
    def __init__(self):
        self.length = 0
        self.linkedlist = LinkedList.LinkedList()

    def enqueue(self, item):
        self.linkedlist.addlast(item)
        self.length += 1

    def dequeue(self):
        self.length -= 1
        return self.linkedlist.remove()

    # Examine the front of the queue without removing anything.
    def first(self):
        return self.linkedlist.peek()

    def isempty(self):
        return self.linkedlist.isempty()

    def __len__(self):
        return self.length


def main():
    q = Queue()
    q.enqueue('4')
    q.enqueue('3')
    q.enqueue('2')
    q.enqueue('1')
    x = q.dequeue()
    y = q.dequeue()

    q.enqueue(y)
    q.enqueue(y)
    q.enqueue('3')
    
    str = ''
    while not q.is_empty():
        str += q.dequeue()
    print(str, end='')


if __name__ == '__main__':
    main()
