def insertion_sort(lst):
    # At each pass ensure that that section is sorted.
    comparison = 0
    swap = 0
    for todo in range(1, len(lst)):
        # Find correct position for lst[todo].
        i = todo
        comparison += 1
        while i > 0 and lst[i] < lst[i-1]:
            lst[i], lst[i-1] = lst[i-1], lst[i] # Swap it down towards the correct position
            i -= 1
            if i > 0:
                comparison += 1
            swap += 1
    return comparison, swap


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
