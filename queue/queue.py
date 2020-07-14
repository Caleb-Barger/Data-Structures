"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         # adds and item
#         self.size += 1
#         self.storage.insert(0, value)

#     def dequeue(self):
#         # pops the last value and shifts everything along
#         if not self.storage:
#             return None
#         self.size -= 1
#         return self.storage.pop(-1)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        # self.storage = ?

    def _is_empty(self):
        if self.head is None and self.tail is None:
            return True
        return False

    def __len__(self):
        # if self._is_empty():
        #     return 0
        # if self.head == self.tail:
        #     return 1
        # current_node = self.head
        # while current_node.next is not None:
        #     current_node = current_node.next
        #     self.size += 1
        # return self.size + 1
        return self.size

    def enqueue(self, value):
        # 1) Make a new Node
        new_node = Node(value)
        # 2) Check if there is a head and tail
        if self._is_empty():
            # 2a) if there is no head or tail set the head as the current node
            self.head = new_node
            # set the tail as the current node
            self.tail = new_node
            self.size = 1
        # 3) set the old tail next value to the new node
        self.tail.next = new_node
        # 2) Set the tail value as this new node
        self.tail = new_node
        self.size += 1

    def dequeue(self):

        # 1) Check if the list is empty
        if self._is_empty():
            # 1a) return None
            self.head = None
            self.tail = None
            return None

        # 2) Hold a refrence to the old head
        old_head = self.head

        new_head = self.head.next
        self.head = new_head

        if not self.head:
            self.tail = None
            self.size = 0

        self.size -= 1
        return old_head.value




