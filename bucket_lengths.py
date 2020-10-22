from LinkedList import LinkedList

class HashSet:
    def __init__(self, capacity=10):
        # Create a list to use as the hash table
        self.table = [None] * capacity

    def add(self, item):
        # Find the hash code
        h = hash(item)
        index = h % len(self.table)

        # Check is it empty
        if self.table[index] == None:
            self.table[index] = LinkedList() # Need a new linked list for this entry

        if item not in self.table[index]:
            # Only add it if not already there (this is a set)
            self.table[index].add(item)

    def average_bucket_length(self):
        lst = []
        for buckets in self.table:
            if buckets != None:
                lst.append(len(buckets))

        return float(sum(lst) // len(lst))

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
