# Node implementation

class Node:
    def __init__(self, data=None, next_node=None) -> None:
        self.data = data
        self.next = next_node

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, next_node):
        self.next = next_node

    def __str__(self):
        return str(self.data)
