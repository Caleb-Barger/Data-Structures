"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def _with_one_element(self, new_node):

        # assign this new node to the head and tail
        self.head = new_node
        self.tail = new_node

        # link nodes together
        self.head.next = new_node
        self.head.prev = None
        self.tail.next = None
        self.tail.prev = new_node

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # make a new node
        new_node = ListNode(value)

        # if there is no head then
        if self.head is None:
            self._with_one_element(new_node)

        # if head is pointing to a value that is not none then
        if self.head.next is not None:
            
            # assign the currrent head's prev value to the new_node
            self.head.prev = new_node
            # assign the new node's next value to the current head
            new_node.next = self.head
            # assign the current head to the new node
            self.head = new_node

            # increment length
            self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):

        # if the current head is None
        if not self.head:
            return None

        # store a refrence to the old_head
        value = self.head
        # set the new head as whaterver the .next prop was on the old_head
        self.head = self.head.next
        # set the .prev prop on the new head to None
        self.head.prev = None

        # decrement length
        self.length -= 1

        # return the old_head
        return value.value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):

        # create a new node
        new_node = ListNode(value)

        # check if tail is None
        if not self.tail:
            # call the _with_one_element method
            # passing in new node
            self._with_one_element(new_node)
            
        # if tail is not None then
        if self.tail is not None:
            # set tail.next to the new node
            self.tail.next = new_node
            # set the new_node.prev to the tail
            new_node.prev = self.tail
            # set the tail to new_node
            self.tail = new_node
            # set tail.next to none
            self.tail.next = None
            
        # increment length
        self.length += 1
    
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # if the tail is None
        if not self.tail:
            return None
   
        # store refrence to tail
        value = self.tail
        # set tail as old tail .prev
        self.tail = value.prev
        # set tail .next to None
        self.tail.next = None

        # decrement length
        self.length -= 1

        # return old tail
        return value.value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
            
        # check if node is head or tail
        # & handle accordingly
        if self.head == node:
            return
        if self.tail == node:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            # set node.prev.next to node.next
            node.prev.next = node.next

        # set node.next to head
        self.head.prev = node
        # set node.prev to None        
        node.next = self.head
        # set head.prev to node        
        node.prev = None
        # set head to node        
        self.head = node

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        # check if the node passed is the tail node
        if self.tail == node:
            return 
        if self.head == node:
            self.head = self.head.next
            self.head.prev = None
        else:
            # set node.prev.next to node.next
            node.prev.next = node.next
        
        self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node


    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.head == node:
            self.head = self.head.next
            self.head.prev = None
        elif self.tail == node:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node.prev.next = node.next

        del node

        self.length -= 1        

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):

        current_node = self.head
        greatest_value = current_node.value

        while current_node.next is not None:

            if current_node.value > greatest_value:
                greatest_value = current_node.value

            current_node = current_node.next
        
        if self.tail.value > greatest_value:
            greatest_value = self.tail.value
        
        return greatest_value


dll = DoublyLinkedList()
dll.add_to_tail(0)
dll.add_to_tail(100)
dll.add_to_tail(0)
dll.add_to_tail(0)

print(dll.get_max())