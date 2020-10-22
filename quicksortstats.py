def partition(lst, lo, hi):
    part = lo
    global compare, moves
    while lo < hi:
        compare += 1
        while lst[lo] <= lst[part] and lo < hi:
            lo += 1
            compare += 1
        compare += 1
        while lst[hi] > lst[part]: # Don't have to check for hi >= 0 cos part is there as a sentinel.
            hi -= 1
            compare += 1

        if lo < hi:
            # Swap the two entries
            lst[hi], lst[lo] = lst[lo], lst[hi]
            moves += 3

    compare += 1
    # Swap part into position
    if lst[part] > lst[hi]: # (this may happen of the array is small (size 2))
        lst[part], lst[hi] = lst[hi], lst[part]  # swap
        moves += 3
    return hi

#The function returns the pivot. The partition function can be combined with the qsort code to recursively
#sort a list:

def rec_qsort(lst, lo, hi):
    if lo < hi:
        pivot = partition(lst, lo, hi)
        rec_qsort(lst, lo, pivot - 1)
        rec_qsort(lst, pivot + 1, hi)

def qsort(lst):
    global compare, moves
    compare = 0
    moves = 0
    rec_qsort(lst, 0, len(lst) - 1)
    return compare, moves

import sys
from quicksortstats import qsort

def main():
    # Read each test case
    line = sys.stdin.readline()
    items = line.strip().split()
    
    orig = list(items)

    result = qsort(items)
    if items != sorted(orig):
        print("The list is not sorted.")
    else:
        print(result)

if __name__ == "__main__":
    main()
