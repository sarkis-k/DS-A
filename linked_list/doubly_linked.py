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


    def 