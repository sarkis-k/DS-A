from binary_search_tree import BST

bst = BST()

bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)
bst.inorder()
print()
bst.preorder()
print()
bst.postorder()
print()
print("height: " + str(bst.find_height()))
bst.insert(15)
bst.inorder()
print()
print("height: " + str(bst.find_height()))
bst.delete(20)
print("height: " + str(bst.find_height()))


