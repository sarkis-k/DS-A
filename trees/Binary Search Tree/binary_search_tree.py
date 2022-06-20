from node import Node


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            self.root.insert(data)
        else:
            self.root = Node(data)

    def delete(self, data):
        if self.root:
            self.root = self.root.delete(data)

    def find(self, data):
        if self.root:
            return self.root.find(data)
        return False

    def inorder(self):
        if self.root:
            self.root.inorder(self.root)

    def preorder(self):
        if self.root:
            self.root.preorder(self.root)

    def postorder(self):
        if self.root:
            self.root.postorder(self.root)

    def find_height(self):
        if self.root:
            return self.root.find_height(self.root)
        return -1
