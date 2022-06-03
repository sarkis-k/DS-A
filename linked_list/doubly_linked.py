from double_node import DoubleNode
from singly_linked import LinkedList


class DoublyLinkedList(LinkedList):
    def __init__(self):
        super().__init__()
        self.tail = None

    def remove_head(self):
        if self.head:
            temp = self.head
            temp.next.prev = None
            self.head = temp.next
            temp.next = None
            return temp.data
        else:
            raise IndexError("Unable to pop from empty list")

    def remove_tail(self):
        if not self.tail:
            raise IndexError("List is empty")
        else:
            temp = self.tail
            temp.prev.next = None
            self.tail = temp.prev
            temp.prev = None
            return temp.data

    def remove_value(self, value):
        if not self.head:
            raise IndexError("List is empty")
        else:
            temp = self.head
            while temp:
                if temp.data == value:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    return temp.data
                temp = temp.get_next()

    def insert_head(self, value):
        node = DoubleNode(value)
        node.set_next(self.head)

        if self.head:
            self.head.prev = node
            self.head = node
            node.prev = None
        else:
            self.head = node
            self.tail = node
            node.prev = None

    def insert_end(self, value):
        node = DoubleNode(value)
        node.set_previous(self.tail)

        if not self.tail:
            self.head = node
            self.tail = node
            node.set_next(None)
        else:
            self.tail.next = node
            node.set_next(None)
            self.tail = node


    # def insert_value(self, value):
    #     pass