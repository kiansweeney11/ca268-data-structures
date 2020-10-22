import sys

def unique_list(lst):
	


from sets import unique_list

def main():
    # Read in a list of strings
    lst = sys.stdin.readline().strip().split()

    # call the student's function ...
    answer = unique_list(lst)
    print(type(answer)) # should be a list
    answer.sort()
    print(answer)

if __name__ == "__main__":
    main()