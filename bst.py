class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

    def __repr__(self):
        return f"Node({self.value})"
    
class BST:
    def __init__(self, root=None):
        self.root = root

    def inorder(self, node):
        if node == None:
            return []
        return self.inorder(node.left) + [node.value] + self.inorder(node.right)
    
    def preorder(self, node):
        if node == None:
            return []
        return [node.value] + self.preorder(node.left) + self.preorder(node.right)
    
    def postorder(self, node):
        if node == None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.value]

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            curr = self.root
            while curr != None:
                if value < curr.value:
                    if curr.left == None:
                        curr.left = Node(value, curr)
                        return
                    else:
                        curr = curr.left
                else:
                    if curr.right == None:
                        curr.right = Node(value, curr)
                        return
                    else:
                        curr = curr.right
    
    def minimun(self):
        curr = self.root
        while curr.left != None:
            curr = curr.left
        return curr.value
    
    def maximum(self):
        curr = self.root
        while curr.right != None:
            curr = curr.right
        return curr.value
    
    def find(self, value):
        curr = self.root
        while curr != None:
            if curr.value == value:
                return curr
            elif value < curr.value:
                curr = curr.left
            else:
                curr = curr.right
        return None
    
    def delete(self, value):
        node = self.find(value)
        if node == None:
            raise ValueError("Value not found")
        
        # scenario 1: node has no children
        if node.left == None and node.right == None:
            print("scenario 1")
            if node.parent == None:
                self.root = None
            elif node.parent.left == node:
                node.parent.left = None
            else:
                node.parent.right = None
        
        # scenario 2: node has one child
        elif node.left == None or node.right == None:
            print("scenario 2")
            if node.parent == None:
                self.root = node.right
            elif node.parent.left == node:
                node.parent.left = node.right
            else:
                node.parent.right = node.right
        
        # scenario 3: node has two children
        else:
            print("scenario 3")
            successor = node.right
            while successor.left != None:
                successor = successor.left #smallest value on the right subtree (the value will bt the next biggest value)
            node.value = successor.value
            if successor.parent.left == successor:
                successor.parent.left = successor.right
            else:
                successor.parent.right = successor.right
        

values = [5,3,2,4,7,9]
tree = BST()
for value in values:
    tree.insert(value)
print(tree.inorder(tree.root))
print(tree.preorder(tree.root))
print(tree.postorder(tree.root))
tree.delete(3)
print(tree.inorder(tree.root))