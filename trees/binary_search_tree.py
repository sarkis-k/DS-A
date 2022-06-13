from node import Node


class BST(Node):
    def __init__(self, root_value: int):
        super().__init__(root_value)
        # self.root = Node(root_value)

    def find_node(self, root, value: int) -> Node:
        while root:
            cur_val = root.get_value()
            if cur_val == value:
                break
            if cur_val < value:
                root = root.get_right()
            else:  # cur_val > value
                root = root.get_left()
        return root

    def tree_height(self, node: Node):
        if not node:
            return 0
        return 1 + max(self.tree_height(node.get_left()), self.tree_height(node.get_right()))

    def insert_node(self, root, value: int):
        if not root:
            return Node(value)
        else:
            if root.data == value:
                return root
            elif root.data < value:
                root.right = self.insert_node(root.right, value)
            else:
                root.left = self.insert_node(root.left, value)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.get_value())
            self.inorder(root.right)

    def min_value(self, root):
        current = root
        while current.left:
            current = current.left
        return current.data

    def delete_node(self, root, value):
        if not root:
            return root

        if value < root.data:
            root.left = self.delete_node(root.left, value)
            return root
        elif value> root.data:
            root.right = self.delete_node(root.right, value)
            return root

        if not root.left and not root.right:
            return None


        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp

        succ_parent = root

        succ = root.right

        while succ.left:
            succ_parent = succ
            succ = succ.left

        if succ_parent != root:
            succ_parent.left = succ.right
        else:
            succ_parent.right = succ.right

        # temp = self.min_value(root.right)
        # root.data = temp
        # root.right = self.delete_node(root.right, temp)
        root.data = succ.data

        return root


