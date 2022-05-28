# Queue implementation using singly Linked-List

# Single Node holding data and next
class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None


# Queue class with basic functions is_empty,peek, add, remove
class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def is_empty(self) -> bool:
        return self.head == None

    def peek(self) -> int:
        return self.head.data

    def add(self, data: int) -> None:
        node = Node(data)
        if self.tail == None:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        self.tail = node

    def remove(self) -> int:
        if self.is_empty():
            return None
        temp = self.head
        self.head = temp.next
        if self.head == None:
            self.tail = None
        return temp.data


q = Queue()

print(q.is_empty())

q.add(5)
q.add(10)
q.add(24)

print(q.peek())

print(q.is_empty())

print(q.remove())
print(q.remove())
print(q.remove())
print(q.is_empty())
