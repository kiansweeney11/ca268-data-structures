import sys
def get_evenodd_list():
	odd = []
	even = []
	number = int(sys.stdin.readline().strip())
	while number != -1:
		if number % 2 != 0:
			odd.append(number)
			number = int(sys.stdin.readline().strip())
		else:
			even.append(number)
			number = int(sys.stdin.readline().strip())

	return odd, even

from numbers import get_evenodd_list

def main():
    # call the get_odd_list function and print the result
    odds, evens = get_evenodd_list()
    print(odds)
    print(evens)

if __name__ == "__main__":
    main()