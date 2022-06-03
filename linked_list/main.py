from singly_linked import LinkedList

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
llist.insert_end("something")

print("List content: ", llist)
