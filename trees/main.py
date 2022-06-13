from binary_search_tree import BST

r = BST(50)
r.insert_node(r, 30)
r.insert_node(r, 20)
r.insert_node(r, 40)
r.insert_node(r, 70)
r.insert_node(r, 60)
r.insert_node(r, 80)
r.insert_node(r, 90)

r.inorder(r)

found = r.find_node(r, 80)
print(found.left)

print(r.min_value(r))

r.delete_node(r, 50)

r.inorder(r)

