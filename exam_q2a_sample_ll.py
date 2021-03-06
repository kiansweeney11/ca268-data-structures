class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        self.head = Node(item, self.head)

    def remove(self):
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next    # remove the item by moving the head pointer
            return item

    def is_empty(self):
        return self.head == None

    def last_element(self):
        ptr = self.head
        while ptr.next != None:
            prev = ptr
            ptr = ptr.next
        prev.next = None

    def __str__(self):
        tmp_str = ""
        ptr = self.head
        while ptr != None:
            tmp_str += ptr.item + " "
            ptr = ptr.next
            
        return tmp_str

import sys
from exam_q2a_sample_ll import LinkedList

def main():
    # Read data from input
    ll = LinkedList()
    ll.add('1')
    ll.add('2')
    ll.add('3')
    ll.add('4')
    print(ll)
    #print(str(ll.remove()) + '\n')
    ll.last_element()
    print(ll)


if __name__ == "__main__":
    main()
