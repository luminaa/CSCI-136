class Node:
    def __init__(self, value=None, parent=None, left = None, right = None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

class BST:
    def __init__(self, root=None):
        self.root = root
    
    def inorder(self, root):
        if not root:
            return []
        return self.inorder(root.left) + [root.value] + self.inorder(root.right)
    
    def insert(self, value):
        if self.root == None:
            self.root = Node(value) # BST with only one node
        else:
            curr = self.root
            while curr != None:
                if value < curr.value: # value is smaller than the current node value 
                    if curr.left == None: 
                        curr.left = Node(value, curr) # insert the value as the left child of the current node
                        break
                    else:
                        curr = curr.left # continue to traverse the left subtree
                else: # value is larger than the current node value
                    if curr.right == None:
                        curr.right = Node(value, curr) # insert the value as the right child of the current node
                        break
                    else:
                        curr = curr.right # continue to traverse the right subtree
    
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
    
    def successor(self, node):
        if node == None: # node is not in the tree
            return None
        if node.right != None: # node has a right subtree
            curr = node.right
            while curr.left != None:
                curr = curr.left # find the smallest node value that is larger than the node value (next value inorder)
            return curr
        elif node.parent != None: # node has no right subtree, find the first ancestor that is larger than the node value
            while node.parent != None and node.parent.right == node:
                node = node.parent
            return node.parent
        return
    
    def predecessor(self, node):
        if node is None: # node is not in the tree
            return None
        if node.left is not None: # node has a left subtree
            curr = node.left
            while curr.right is not None:
                curr = curr.right # find the largest node value that is smaller than the node value (prev value inorder)
            return curr
        elif node.parent is not None: # node has no left subtree, find the first ancestor that is smaller than the node value
            while node.parent is not None and node.parent.left == node:
                node = node.parent
            return node.parent
        return
    
    def delete(self, value):
        node = self.find(value)
        if node == None:
            return
        
        # scenario 1: node has no children
        if node.left == None and node.right == None:
            # print("scenario 1")
            if node.parent == None:
                self.root = None
            elif node.parent.left == node:
                node.parent.left = None
            else:
                node.parent.right = None
        
        # scenario 2: node has one child
        elif node.left == None or node.right == None:
            # print("scenario 2")
            if node.parent == None:
                if node.left == None:
                    self.root = node.right
                else:   
                    self.root = node.left
            elif node.parent.left == node:
                if node.left == None:
                    node.parent.left = node.right
                else:
                    node.parent.left = node.left
            else:
                if node.left == None:
                    node.parent.right = node.right
                else:
                    node.parent.right = node.left
        
        # scenario 3: node has two children
        else:
            # print("scenario 3")
            successor = self.successor(node)
            node.value = successor.value
            if successor.parent.left == successor:
                successor.parent.left = successor.right
            else:
                successor.parent.right = successor.right

    def minimun(self):
        curr = self.root
        while curr.left:
            curr = curr.left
        return curr.value
    
    def maximum(self):
        curr = self.root
        while curr.right:
            curr = curr.right
        return curr.value



# Question 1
tree = BST()
values = [15,10,12,5,2,7,20,25]
for v in values:
    tree.insert(v)
print(tree.inorder(tree.root))

# Question 2
tree.insert(11)
tree.insert(23)
print(tree.inorder(tree.root))

# Question 3
tree.delete(12)
print(tree.inorder(tree.root))

# Question 4
print(tree.minimun())

# Question 5
print(tree.maximum())

# Question 6
print(tree.successor(tree.find(10)).value)

# Question 7
print(tree.predecessor(tree.find(11)).value)