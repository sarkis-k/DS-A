# Node implementation

class Node(object):
    def __init__(self, data=None, next_el=None) -> None:
        self.data = data
        self.next = next_el

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

    def __str__(self):
        return str(self.data)


