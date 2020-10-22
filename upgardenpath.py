class BST:
    """ An implementation of a Binary Search Tree """
    def __init__(self, lst = None):
        self.root = None
        if lst != None:
            for item in lst:
                self.add(item)

    # Non recursive add method, easier to work out the path to the parent        
    def add(self, item):
        """ Add this item to its correct position on the tree """
        # This is a non recursive add method.
        if self.root == None: # ... Empty tree ...
            self.root = Node(item, None, None) # ... so, make this the root
        else:
            # Find where to put the item
            l = []
            child_tree = self.root
            while child_tree != None:
                l.append(child_tree.item)
                parent = child_tree
                if item < child_tree.item: # If smaller ... 
                    #l.append(child_tree.item)
                    child_tree = child_tree.left # ... move to the left
                else:
                    child_tree = child_tree.right

            # child_tree should be pointing to the new node, but we've gone too far
            # we need to modify the parent nodes
            if item < parent.item:
                parent.left = Node(item, None, None)
            else:
                parent.right = Node(item, None, None)

        return l

import sys
from BST import BST

def main():
    # Read each test case
    line = sys.stdin.readline()
    items = line.strip().split()
    nums = [int(item) for item in items]

    tree = BST(nums[:-1])

    lst = tree.add(nums[-1])
    print(lst)

if __name__ == "__main__":
    main()
