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
        # call anon func on self.value
        fn(self.value)
        # if the node has a left child pass the anon func to it
        if self.left:
            self.left.for_each(fn)
        # if the node has a right child pass the anon func to it
        if self.right:
            self.right.for_each(fn)

    def iterative_depth_first_for_each(self, fn):
        # DFT - depth first transversal (LIFO)
        # LIFO = STACK
        stack = []
        stack.append(self)

        # as long as the stack has nodes in it
        # there are more nodes to traverse
        while len(stack) > 0:
            current = stack.pop()

            if current.right:
                stack.append(current.right)

            if current.left:
                stack.append(current.left)

            # call the anon func
            fn(current.value)

    def iterative_bredth_first_for_each(self, fn):
        from collections import deque
        # BFT: FIFO
        # queue data structure to do this
        queue = deque()
        queue.append(self)

        # continue to travel as long as there are more nodes
        while len(queue) > 0:
            current = queue.popleft()

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

            fn(current.value)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # if node left than call self with node.left
        if node.left:
            self.in_order_print(node.left)
        # if not a node.right or is a node.right print self
        if not node.right or node.right:
            print(node.value)
        # if node.right call self with node.right
        if node.right:
            self.in_order_print(node.right)
        
        
       




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


bst = BSTNode(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.in_order_print(bst)


