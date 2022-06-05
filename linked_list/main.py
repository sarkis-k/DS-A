from singly_linked import LinkedList
from doubly_linked import DoublyLinkedList

# llist = DoublyLinkedList()
#
# print("size: ", len(llist))
# llist.insert_head(1)
# llist.insert_head(2)
# print("size: ", len(llist))
# print(llist)
# llist.insert_head(3)
# llist.insert_head(4)
# llist.insert_head(5)
# llist.insert_head(6)
# print("List content: ", llist)
# print("popping...")
# llist.pop_head()
# print("List content: ", llist)
# print("Does list contain ")
# if llist.contains(3):
#     print("Yes")
# else:
#     print("No")
# print("Deleting ")
# llist.delete(3)
# print("List content: ", llist)
# print("insert_end another onto end.")
# llist.insert_end(56)
#
# print("List content: ", llist)
# llist.remove_head()
# print(llist)
# llist.remove_tail()
# # llist.remove_tail()
# print(llist)
#
# print(len(llist))
#
# llist.remove_value(2)
# print(llist)

llist = LinkedList()

print("size: ", len(llist))
llist.insert_head("1")
llist.insert_head("2")
print("size: ", len(llist))
print(llist)
llist.insert_head("3""4""5")
llist.insert_head("6""7")
llist.insert_head("8""9")
llist.insert_head("0""1")
print("List content: ", llist)
print("popping...")
llist.pop_head()
print("List content: ", llist)
print("Does list contain ")
if llist.contains("1"):
    print("Yes")
else:
    print("No")
print("Deleting ")
llist.delete("1")
print("List content: ", llist)
print("insert_end another onto end.")
# llist.insert_end("something")
print(llist.find_mid())
llist.reverse()
print("List content: ", llist)
