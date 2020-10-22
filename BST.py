class Node:
    """ A node in a BST. It may have left and right subtrees """
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    """ An implementation of a Binary Search Tree """
    def __init__(self):
        self.root = None

    def add(self, item):
        """ Add this item to its correct position on the tree """
        # This is a non recursive add method. A recursive method would be cleaner.
        if self.root == None: # ... Empty tree ...
            self.root = Node(item, None, None) # ... so, make this the root
        else:
            # Find where to put the item
            child_tree = self.root
            while child_tree != None:
                parent = child_tree
                if item < child_tree.item: # If smaller ... 
                    child_tree = child_tree.left # ... move to the left
                else:
                    child_tree = child_tree.right

            # child_tree should be pointing to the new node, but we've gone too far
            # we need to modify the parent nodes
            if item < parent.item:
                parent.left = Node(item, None, None)
            else:
                parent.right = Node(item, None, None)
                
    def recursive_count(self, ptr):
        if ptr == None:  # Base Case
            return 0
        else:
            return(1 + self.recursive_count(ptr.left) + self.recursive_count(ptr.right))

    def count(self, lo, hi):
        return self.recurs_count_lo_hi(self.root, lo, hi)

    def recurs_count_lo_hi(self, ptr, lo, hi):
        if ptr == None:
            return 0
        elif (lo <= ptr.item) and (ptr.item <= hi):
            return(1 + self.recurs_count_lo_hi(ptr.left, lo, hi) + self.recurs_count_lo_hi(ptr.right, lo, hi))
        elif lo <= ptr.item:
            return(0 + self.recurs_count_lo_hi(ptr.left, lo, hi))
        else:
            return(0 + self.recurs_count_lo_hi(ptr.right, lo,hi))

    def height(self):
        return self.recursive_height(self.root)

    def recursive_height(self, ptr):
        if ptr == None:
            return 0
        else:
            return max(1 + self.recursive_height(ptr.left), 1 + self.recursive_height(ptr.right))

    def total(self):
        return self.total_recursive(self.root)

    def total_recursive(self, ptr):
        if ptr == None:
            return 0
        else:
            return (ptr.item + self.total_recursive(ptr.left) + self.total_recursive(ptr.right))

    def is_present(self, num):
        return self.recursive_is_present(self.root, num)

    def recursive_is_present(self, ptr, num):
        if ptr == None:
            return False
        elif ptr.item == num:
            return True
        else:
            return self.recursive_is_present(ptr.left, num) or self.recursive_is_present(ptr.right, num)

    def count_leaves(self):
        return self.recursive_count_leaves(self.root)

    def recursive_count_leaves(self, ptr):
        if ptr == None:
            return 0
        if ptr.left == None and ptr.right == None:
            return 1
        else:
            return self.recursive_count_leaves(ptr.left) + self.recursive_count_leaves(ptr.right)

    def in_order(self):
        print(self.recurs_in_order(self.root, lst=[]))

    def recurs_in_order(self, ptr, lst):
        if ptr:
            self.recurs_in_order(ptr.left, lst)
            lst.append(str(ptr.item))
            self.recurs_in_order(ptr.right, lst)
        return(" ".join(lst) + " ")

    def pre_order(self):
        print(self.recurs_post_order(self.root, lst=[]))

    def recurs_pre_order(self, ptr, lst):
        if ptr:
            lst.append(str(ptr.item))
            self.recurs_in_order(ptr.left, lst)
            self.recurs_in_order(ptr.right, lst)
        return(" ".join(lst) + " ")

    def recurs_count(self):
        return self.recurs_odd(self.root)

    def recurs_odd(self, ptr):
        if ptr == None:
            return 0
        if ptr.item % 2 != 0:
            return 1 + self.recurs_odd(ptr.left) + self.recurs_odd(ptr.right)
        else:
            return self.recurs_odd(ptr.left) + self.recurs_odd(ptr.right)
