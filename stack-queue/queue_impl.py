

# class Node:
#     def __init__(self, data) -> None:
#         self.data = data
#         self.next = None

# class Queue:
#     def __init__(self) -> None:
        

# n1 = Node("n1")
# n2 = Node("n2")
# n3 = Node("n3")

# n1.next = n2
# n2.next = n3

# thisval = n1

# while thisval:
#     print(thisval.data)
#     thisval = thisval.next

# # Queue using list

# queue = []

# # adding ellement to queue 
# queue.append("1st")
# queue.append("2nd")

# print(queue)

# # removing 
# queue.pop(0)

# print(queue)

# queue using Queue lib

from queue import Queue

q = Queue(maxsize=5)

print(q.qsize())


q.put("n1")
q.put(5)
q.put("n23")

print(q.get())
print(q.get())

print(q.qsize())

