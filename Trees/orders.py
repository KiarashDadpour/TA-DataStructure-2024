class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self) -> None:
        self.inorder_list: list = []
        self.postorder_list: list = []
        self.preorder_list: list = []
      

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            self.inorder_list.append(root.data)
            self.inorder(root.right)
        return self.inorder_list

    def postorder(self, root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            self.postorder_list.append(root.data)
        return self.postorder_list

    def preorder(self, root):
        if root is not None:
            self.preorder_list.append(root.data)
            self.preorder(root.left)
            self.preorder(root.right)
        return self.preorder_list


# Example 
r = Node(50)
r.left = Node(40)
r.right = Node(60)
r.left.right = Node(45)
r.left.left = Node(30)
r.left.left.left = Node(20)
r.left.left.left.right = Node(25)
r.right.left = Node(55)
r.right.left.left = Node(53)
r.right.right = Node(70)

bst = Tree()
print(f"inorder: {bst.inorder(r)}")
print(f"postorder: {bst.postorder(r)}")
print(f"preorder: {bst.preorder(r)}")
