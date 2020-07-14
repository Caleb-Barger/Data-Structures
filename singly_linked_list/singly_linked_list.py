class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node

    def __str__ (self):
        return f"{self.value} -> {self.next}"

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def _check_is_empty(self):
        if self.head is None and self.tail is None:
            return True
        return False

    def add_to_tail(self, value):

        new_node = Node(value)
        if self._check_is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self):
        if not self.head:
            return None
        if not self.head.get_next():
            head = self.head
            self.head = None
            self.tail = None
            return head.get_value()

        old_head = self.head.get_value()
        self.head = self.head.get_next()
        return old_head

    def remove_tail(self):
        if not self._check_is_empty():
            current_node = self.head

            while current_node.get_next() is not self.tail:
                current_node = current_node.get_next()

            old_tail = self.tail.get_value()
            self.tail = None
            self.tail = current_node

            return old_tail
        return 

    def __str__(self):
        return f"{self.head}....{self.tail}"


ll = LinkedList()

ll.add_to_tail(10)
ll.add_to_tail(100)
ll.add_to_tail(10000)
print(ll.tail.value)







