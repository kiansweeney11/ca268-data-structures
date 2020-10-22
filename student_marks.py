import sys
def make_map():
	line = sys.stdin.readline().strip()
	student = {}
	while 0 < len(line):
		line = line.split()
		student[line[0]] = line[1]
		line = sys.stdin.readline().strip()
	return student


# import the student function
from student_marks import make_map
from sys import argv  # Even though we don't need argv in this exercise

def main(argv):
    student = make_map() # Call the student function
    print(type(student)) # check the type ... should be a map (or in python, dict)
    names = student.keys()   # get all names
    for name in sorted(names): # sort the names
        print(name + " has mark " + student[name]) # print the names and marks
    
if __name__ == "__main__":
    main(sys.argv[1:])
