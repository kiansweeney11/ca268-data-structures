import sys

def get_sliced_lists(l):
    a = []
    last_element = l[:-1]
    a.append(last_element)
    first_last = l[1:len(l) - 1]
    a.append(first_last)
    reverse = l[::-1]
    a.append(reverse)
    return a

from numbers import get_sliced_lists

def main():
    # read the list from stdin
    nums = []
    num = int(input())
    while num != -1:
        nums.append(num)
        num = int(input())
        
    # call the student's function with the list of numbers and ...
    lists = get_sliced_lists(nums)
    # ... print the result
    for lst in lists:
        print(lst)

if __name__ == "__main__":
    main()
