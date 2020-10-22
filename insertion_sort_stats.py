def insertion_sort(lst):
    # At each pass ensure that that section is sorted.
    compare = 0
    moves = 0
    for todo in range(1, len(lst)):
        # Find correct position for lst[todo].
        i = todo
        compare += 1
        while i > 0 and lst[i] < lst[i-1]:
            lst[i], lst[i-1] = lst[i-1], lst[i] # Swap it down towards the correct position
            i -= 1
            if i > 0:
                compare += 1
            moves += 1
    return compare, moves

import sys
from insertion_sort import insertion_sort

def main():
    # Read each test case
    line = sys.stdin.readline()
    items = line.strip().split()
    
    orig = list(items)

    result = insertion_sort(items)
    if items != sorted(orig):
        print("The list is not sorted.")
    else:
        print(result)

if __name__ == "__main__":
    main()
