def insertion_sort(lst):
    # No swap version
    compare = 0
    moves = 0
    for todo in range(1, len(lst)):
        tobeinserted = lst[todo]
        i = todo
        compare += 1
        moves += 1
        while i > 0 and tobeinserted < lst[i-1]:
            lst[i] = lst[i-1] # Make space for the item
            i -= 1
        	if i > 0:
        		compare += 1
        lst[i] = tobeinserted
        moves += 1  # Found the place for this item, plonk it in
    return compare, moves


import sys
from insertion_sort_stats_v2 import insertion_sort

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