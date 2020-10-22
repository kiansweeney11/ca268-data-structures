from Queue import Queue

def mergesort(q):
    if len(s) < 2:
        return # Base case. No work to do for one element.

    # Split q into two smaller queues
    q1, q2 = split(q) # You will supply the split function

    # recursively sort these as well
    mergesort(q1)
    mergesort(q2)

    # Now, merge these together back into q
    merge(q1, q2, q)

def split(q):
    part1 = q


from Queue import Queue
from student import split
#
#   Make a queue from a lst
#
def make_q(lst):
    q = Queue()
    for x in lst:
        q.enqueue(x)
    return q

def main():
    lst = [10 * x for x in range(10)]
    q = make_q(lst)
    # Call the student's split function
    q1, q2 = split(q)
    if abs(len(q1) - len(q2)) > 1:
        print("The lengths of your two queues should not differ by more than 1.")
    elif len(q1) + len(q2) > len(lst):
        print("There are too many elements in your queues")
    elif len(q1) + len(q2) < len(lst):
        #print(len(q1), len(q2), len(lst))
        print("There are too few elements in your queues")
    else:
# There are the right number of elements, check if the elements themselves are correct
        qlist = []
        # First add everything from q1
        while not q1.isempty():
            qlist.append(q1.dequeue())
        # Now add everything from q2
        while not q2.isempty():
            qlist.append(q2.dequeue())

        # Check the elements match
        if sorted(qlist) == sorted(lst):# Easiest way to compare two lists for contents is to sort them both.
            print("All tests passed")
        else:
            print("Your queues do not contain the right elements")

if __name__ == "__main__":
    main()
