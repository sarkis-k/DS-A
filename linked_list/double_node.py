from node import Node


class DoubleNode(Node):
    def __int__(self, data=None, next_node=None, prev_node=None) -> None:
        super().__init__(data, next_node)
        self.prev = prev_node

    def get_previous(self):
        return self.prev

    def set_previous(self, prev_node):
        self.prev = prev_node
