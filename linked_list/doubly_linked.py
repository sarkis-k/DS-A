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
        if self.head:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                temp = self.tail.prev
                self.tail.prev.next = None
                self.tail.prev = None
                self.tail = temp

    def remove_value(self, value):

        current = self.head
        node_deleted = False
        
        if current is None:
            node_deleted = False

        elif current.data == value:
            self.head = current.next
            self.head.prev = None
            node_deleted = True

        elif self.tail.data == value:
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True

        else:
            while current:
                print("data" + str(current.data))
                if current.data == value:
                    print("here")
                    print(current.data)
                    current.prev.set_next(current.next)
                    print("prev next" + str(current.prev.next))
                    current.next.set_previous(current.prev)
                    print("next prev" + str(current.next.prev))
                    current = None
                    node_deleted = True
                    break
                current = current.next
        return node_deleted

        # if not self.head:
        #     raise IndexError("List is empty")
        # else:
        #     temp = self.head
        #     while temp:
        #         print(temp.data)
        #         if temp.data == value:
        #             temp.prev.next = temp.next
        #             temp.next.prev = temp.prev
        #             return temp.data
        #         temp = temp.get_next()

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

    def insert_value_after(self, after_value, insert_value):
        current = self.head
        while current:
            if current.get_data() == after_value:
                next_node = current.get_next()
                new_node = DoubleNode(insert_value)
                current.set_next(new_node)
                new_node.set_next(next_node)
                new_node.set_previous(current)
                next_node.set_previous(new_node)
                return
            current = current.get_next()

    def insert_value_before(self, before_value, insert_value):
        current = self.head
        while current:
            if current.get_data() == before_value:
                new_node = DoubleNode(insert_value)
                current.previous.next = new_node
                new_node.set_previous(current.get_previous())
                new_node.set_next(current)
                current.set_previous(new_node)
                return
            current = current.get_next()

    def reverse(self):
        previous = None
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            current.prev = next_node
            previous = current
            current = next_node
        self.head = previous

