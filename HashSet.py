from LinkedList import LinkedList

class HashSet:
    def __init__(self, capacity=10):
        # Create a list to use as the hash table
        self.table = [None] * capacity

    def add(self, item):
        # Find the hash code
        h = hash(item)
        index = h % len(self.table)
        check = 0
        # Check is it empty
        if self.table[index] == None:
            self.table[index] = LinkedList() # Need a new linked list for this entry
        else:
            check = 1

        if item not in self.table[index]:
            # Only add it if not already there (this is a set)
            self.table[index].add(item)
        if check:
            return index, item

    def average_bucket_length(self):
        lengths = []
        for bucket in self.table:
            if bucket != None:
                lengths.append(len(bucket))

        return float(sum(lengths) / len(lengths))

    def min_max_bucket_length(self):
        mx_min = []
        for bucket in self.table:
            if bucket != None:
                mx_min.append(len(bucket))
        return min(mx_min), max(mx_min)

    def __iter__(self):
        table = []
        ptr = None
        for i in range(0, len(self.table)):
            if self.table[i]:
                ptr = self.table[i].head
                while ptr != None:
                    table.append(ptr.item)
                    ptr = ptr.next
        return iter(sorted(table))

import sys
from HashSet import HashSet

def main():
    # Read each test case
    line = sys.stdin.readline()
    items = line.strip().split()
    nums = [int(item) for item in items]
    
    # First number is the capacity
    numset = HashSet(nums[0])

    for x in nums[1:]:
        print(str(numset.add(x)) + " ", end="")

    print()

if __name__ == "__main__":
    main()
