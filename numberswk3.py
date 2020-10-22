import sys
def get_odd_list():
	odds = []
	number = int(sys.stdin.readline().strip())
	while number != -1:
		if number % 2 != 0:
			odds.append(number)
			number = int(sys.stdin.readline().strip())
		else:
			number = int(sys.stdin.readline().strip())

	return odds

from numberswk3 import get_odd_list

def main():
    # call the get_odd_list function and print the result
    odds = get_odd_list()
    print(odds)

if __name__ == "__main__":
    main()
