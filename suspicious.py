import sys

with open(sys.argv[1]) as f1:
	line = f1.readline().strip()
	names = []
	while 0 < len(line):
		names.append(line)
		line = f1.readline().strip()

with open(sys.argv[2]) as f2:
	words = f2.readline().strip()
	if wor:
