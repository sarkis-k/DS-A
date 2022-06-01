from node import Node

class LinkedList(object):
    def __init__(self):
        self.head = None

    def set_head(self, head_node):
        self.head = head_node

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.get_next()
        return count
    def __str__(self):
        current = self.head
        output = ""
        while current:
            output += str(current) + " -> "
            current = current.get_next()
        return output
