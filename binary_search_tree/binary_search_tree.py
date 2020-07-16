"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

class BSTNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare input value with value of the Node
        # if value is < Node's value
        if value < self.value:
            # go left
            # if there's no child to compare input value to
            if not self.left:
                # wrap the value in a BSTNode and park it
                self.left = BSTNode(value)
            # otherwise there is a child
            else:
                # call the left child's insert method
                self.left.insert(value)
        # otherwise value, >= Node's value
        else:
            # go right
            # if no right child wrap and park
            if not self.right:
                self.right = BSTNode(value)
            # otherwise thehe is a child
            else:
                # call right child's insert method
                self.right.insert(value)
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # 1. Base case
        if self.value == target:
            return True
        # 2. "How move closer to base case?"
        # compare target against value to determine direction
        if target < self.value:
            # move left
            # is no left
            if not self.left:
                return False
            else:
                # call contains again on this child
                return self.left.contains(target) # using return becuase we are looking for some sort of answer
        else:
            # move right
            # is no right
            if not self.right:
                return False
            # is a right
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # RECURSIVE 
        # --------------------------
        if not self.right:
            return self.value

        return self.right.get_max()

        # ITERATION
        # --------------------------
        # current = self

        # while not current.right:
        #     current = current.right
        
        # return current.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


bst = BSTNode(10)
bst.insert(11)
bst.insert(4)
print(bst.get_max())
