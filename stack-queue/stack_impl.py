# Stack implementation using singly Linked-List

# Single Node holding data and next
class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None


# Stack class with basic functions is_empty, peek, push, pop
class Stack:
    def __init__(self) -> None:
        self.top = None

    def is_empty(self) -> bool:
        return self.top == None

    def peek(self) -> int:
        if self.top != None:
            return self.top.data
        return None

    def push(self, data: int) -> None:
        node = Node(data)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node

    def pop(self) -> int:
        if self.top:
            data = self.top.data
            self.top = self.top.next
            return data
        else:
            return None


# Test cases
s = Stack()

print(s.is_empty())

s.push(5)

print(s.is_empty())
s.push(10)
print(s.peek())
s.pop()
print(s.peek())
s.pop()
print(s.peek())
print(s.is_empty())
