from sys import exit


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class BST:

    def __init__(self, root):
        self.root = root
        self.inorder_list: list = []

    def len_tree(self, root):
        if root is None:
            return 0
        return 1 + self.len_tree(root.left) + self.len_tree(root.right)

    def len_leaves(self, root):
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 1
        else:
            return self.len_leaves(root.left) + self.len_leaves(root.right)

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            self.inorder_list.append(root.data)
            self.inorder(root.right)
        return self.inorder_list

    def insert(self, key):
        new = Node(key)
        current = self.root
        if self.root is None:
            self.root = new
            return
        while current:
            if current.data > key:
                if current.left is None:
                    current.left = new
                    break
                else:
                    current = current.left
            elif current.data < key:
                if current.right is None:
                    current.right = new
                    break
                else:
                    current = current.right
            else:
                print("Same old data!!!")

    def search(self, root, key):
        current = root
        try:
            while True:
                if current.data == key:
                    return current
                elif current.data > key:
                    current = current.left
                    self.search(current, key)
                elif current.data < key:
                    current = current.right
                    self.search(current, key)
        except AttributeError:
            print("Value doesn't exist!!!")
            exit()


    def height(self, node):
        if node is None:
            return 0
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return max(left_height, right_height) + 1




