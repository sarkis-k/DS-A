from singly_linked import LinkedList

llist = LinkedList()

print("size: ", len(llist))
llist.push("something")
llist.push("something")
print("size: ", len(llist))
print(llist)
llist.push("something""something""something")
llist.push("something""something")
llist.push("something""something")
llist.push("something""something")
print("List content: ", llist)
print("popping...")
llist.pop()
print("List content: ", llist)
print("Does list contain ")
if llist.contains("something""something"):
    print("Yes")
else:
    print("No")
print("Deleting ")
llist.delete("something""something")
print("List content: ", llist)
print("Pushing another onto end.")
llist.append("something")

print("List content: ", llist)
