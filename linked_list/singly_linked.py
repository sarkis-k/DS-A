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
        output += "NULL"
        return output

    def pop_head(self):
        if self.head:
            self.head = self.head.get_next()
        else:
            raise IndexError("Unable to pop from empty list")

    def contains(self, value):
        found = False
        current = self.head
        while current and not found:
            if current.get_data() == value:
                found = True
            else:
                current = current.get_next()
        return found

    def delete(self, value):
        current = self.head
        prev = None
        while current:
            if current.get_data() == value:
                if prev:
                    prev.set_next(current.get_next())
                else:
                    self.head = current.get_next()
            else:
                prev = current
            current = current.get_next()

    def insert_head(self, value):
        node = Node(value)
        node.set_next(self.head)
        self.set_head(node)

    def insert_end(self, value):
        node = Node(value)
        current = self.head
        if not current:
            self.head = node
            return
        while current.get_next():
            current = current.get_next()
        current.set_next(node)

    def insert_value_after(self, after_value, insert_value):
        current = self.head
        while current:
            if current.get_data() == after_value:
                next_node = current.get_next()
                new_node = Node(insert_value)
                current.set_next(new_node)
                new_node.set_next(next_node)
                return
            current = current.get_next()

    def find_mid(self) -> Node:
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

