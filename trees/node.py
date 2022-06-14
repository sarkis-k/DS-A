class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.left = None
        self.right = None

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_value(self):
        return self.data

    def insert(self, data):
        if self.data == data:
            raise Exception("Data already exist")
        elif self.data > data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)

    def delete(self, data):
        if data < self.data and self.left:
            self.left = self.left.delete(data)
        elif data > self.data and self.right:
            self.right = self.right.delete(data)
        else:
            if self.data == data:
                if self.left and self.right:
                    min_val = self.right.find_min()
                    self.data = min_val
                    self.right = self.right.delete(min_val)
                elif self.left:
                    return self.left
                elif self.right:
                    return self.right
                else:
                    return None
        return self

    def find_min(self):
        current = self
        while current:
            current = current.left
        return current.data

    def find(self, data):
        if self.data == data:
            return True
        elif data < self.data and self.left:
            return self.left.find(data)
        elif data > self.data and self.right:
            return self.right.find(data)
        else:
            return False

    def inorder(self, cur_node):
        if cur_node:
            self.inorder(cur_node.left)
            print(cur_node.data, end=" ")
            self.inorder(cur_node.right)

    def preorder(self, cur_node):
        if cur_node:
            print(cur_node.data, end=" ")
            self.inorder(cur_node.left)
            self.inorder(cur_node.right)

    def postorder(self, cur_node):
        if cur_node:
            self.inorder(cur_node.left)
            self.inorder(cur_node.right)
            print(cur_node.data, end=" ")

    def find_height(self, cur_node):
        if not cur_node:
            return -1
        left_height = self.find_height(cur_node.left)
        right_height = self.find_height(cur_node.right)
        return max(left_height, right_height) + 1
