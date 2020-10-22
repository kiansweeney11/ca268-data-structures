""" Selection sort algorithm """
def selection_sort(lst):
    compare = 0
    moves = 0
    for i in range(len(lst) - 1):
        # Find the smallest item in the lst starting at i
        min_index = i
        for j in range(min_index + 1, len(lst)):
            compare += 1
            if lst[j] < lst[min_index]:
                min_index = j
        # place smallest at the beginning (swap min index with i)
        lst[i], lst[min_index] = lst[min_index], lst[i]
        moves += 3
    return compare, moves

import sys
from selectionstats import selection_sort

def main():
    # Read each test case
    line = sys.stdin.readline()
    items = line.strip().split()
    
    orig = list(items)

    result = selection_sort(items)
    if items != sorted(orig):
        print("The list is not sorted.")
    else:
        print(result)

if __name__ == "__main__":
    main()
