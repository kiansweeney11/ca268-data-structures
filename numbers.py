import sys
def get_counts(words):
	lengthlst = []
	lengthlst = [0] * 10
	lines = sys.stdin.readlines()
	k = 0
	while k < len(lines):
		lengthlst[len(lines[k])] += 1

	return lengthlst

import sys
from numbers import get_counts

def main():
    # read the list of words from stdin
    line = sys.stdin.readline()
    line = line.strip()
    words = line.split()

    # call the student's function and ...
    counts = get_counts(words)
    # ... print the result
    for length in range(10):
        print(str(length) + ": " + str(counts[length]))

if __name__ == "__main__":
    main()
