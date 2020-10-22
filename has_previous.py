import sys
line = sys.stdin.readline().strip()
lst = []
while line != -1:
	lst.append(line)
	line = sys.stdin.readline().strip()

previous = []
for j in lst:
	if j in lst:
		previous.append(j)

k = 0
while k < len(previous):
	print(previous[k])
	k += 1
