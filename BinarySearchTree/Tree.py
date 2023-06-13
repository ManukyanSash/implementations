class Node:
    def __init__(self, val = 0):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, root=None):
        """Constructor for binary tree."""
        self.root = root

    def __add__(self, rhs):
        """Operator '+' for binary tree."""
        if isinstance(rhs, Node):
            self.add(rhs.val)
            return
        self.add(rhs)

    def __contains__(self, rhs):
        """Operator 'in' for binary tree."""
        if isinstance(rhs, Node):
            return self.getEntry(rhs) is not None
        return self.contains(rhs)
    
    def isEmpty(self):  
        """Tests whether binary tree is empty."""
        return self.root is None

    def getHeight(self):
        """Gets the height of binary tree."""
        if self.isEmpty():
            return 0
        return self.__getHeight(self.root)

    def __getHeight(self, root):
        if not root:
            return 0
        return 1 + max(self.__getHeight(root.left), self.__getHeight(root.right)) 

    def getNumberOfNodes(self):
        """Gets the number of nodes in binary tree."""
        if self.isEmpty():
            return 0
        return self.__getNumberOfNodes(self.root)

    def __getNumberOfNodes(self, root):
        if not root:
            return 0
        return 1 + self.__getNumberOfNodes(root.left) + self.__getNumberOfNodes(root.right)  

    def getRootData(self):
        """Gets the data that is in the root of binary tree."""
        if self.isEmpty():
            raise AttributeError("Tree is empty")
        return self.root.val

    def setRootData(self, data):
        """Replaces the data item in the root of binary tree with newData. If the tree is empty inserts a new root node whose data item."""
        if self.isEmpty():
            self.root = Node(data) 
            return
        elements = self.levelorder()
        elements[0] = data
        self.clear()
        for el in elements:
            self.add(el)
        
    def add(self, data):
        """Adds a new node containing a given data item to binary tree."""
        if self.isEmpty():
            self.root = Node(data)
            return
        self.__add(self.root, data)
        
        
    def __add(self, root, data):
        if not root:
            return Node(data)
        if root.val > data:
            root.left = self.__add(root.left, data)
        if root.val < data:
            root.right = self.__add(root.right, data) 
        return root
    
    def remove(self, data):
        """Removes the node containing the given data item from binary tree."""
        if self.isEmpty():
            raise AttributeError("Tree is empty")
        self.__remove(self.root, Node(data))

    def __remove(self, root, node):
        if not root:
            return
        
        if root.val > node.val:
            root.left = self.__remove(root.left, node)
            return root
        if root.val < node.val:
            root.right = self.__remove(root.right, node)
            return root
        
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        
        successor = root.right
        while successor.left:
            successor = successor.left
        root.val = successor.val
        root.right = self.__remove(root.right, Node(successor.val))

        return root

    def clear(self):
        """Removes all nodes from binary tree."""
        self.root = None

    def getEntry(self, node):
        """Gets a specific entry in binary tree."""
        if self.isEmpty():
            raise AttributeError("Tree is empty")
        if not self.contains(node.val):
            raise ValueError("Entry is not found")
        return self.__getEntry(self.root, node)    

    def __getEntry(self, root, node):
        if not root:
            return False
        if root.val > node.val:
            return self.__contains(root.left, node)
        if root.val < node.val:
            return self.__contains(root.right, node)
        return root

    def contains(self, data):
        """Tests whether the given data item occurs in binary tree."""
        if self.isEmpty():
            raise AttributeError("Tree is empty")
        return self.__contains(self.root, data)
    
    def __contains(self, root, data):
        if not root:
            return False
        if root.val == data:
            return True
        if root.val > data:
            return self.__contains(root.left, data)
        if root.val < data:
            return self.__contains(root.right, data)
        # return True
    
    def preorder(self, visit=lambda x:x):
        """Traverses binary tree in preorder and calls the function visit once for each node."""
        if self.isEmpty():
            raise AttributeError("Tree is empty")
        elements = self.__preorder(self.root, visit)
        return elements

    def __preorder(self, root, key):
        res = list()
        if not root:
            return []
        res.append(key(root.val))
        res += self.__preorder(root.left, key)
        res += self.__preorder(root.right, key)
        return res
    
    def inorder(self, visit=lambda x:x):
        """Traverses binary tree in inorder and calls the function visit once for each node."""
        if self.isEmpty():
            raise AttributeError("Tree is empty")
        elements = self.__inorder(self.root, visit)
        return elements

    def __inorder(self, root, key):
        res = list()
        if not root:
            return []
        res += self.__inorder(root.left, key)
        res.append(key(root.val))
        res += self.__inorder(root.right, key)
        return res

    def postorder(self, visit=lambda x:x):
        """Traverses binary tree in postorder and calls the function visit once for each node."""
        if self.isEmpty():
            raise AttributeError("Tree is empty")
        elements = self.__postorder(self.root, visit)
        return elements

    def __postorder(self, root, key):
        res = list()
        if not root:
            return []
        res += self.__postorder(root.left, key)
        res += self.__postorder(root.right, key)
        res.append(key(root.val))
        return res

    def levelorder(self, visit=lambda x:x):
        """Traverses binary tree in levelorder and calls the function visit once for each node."""
        if self.isEmpty():
            raise AttributeError("Tree is empty")
        height = self.getHeight()
        elements = list()
        for i in range(height):
            elements += self.__levelorder(i, self.root, visit)
        return elements

    def __levelorder(self, height, root, key, i=0):
        res = []
        if not root:
            return [] 
        if i > height:
            return []
        if i == height:
            res.append(key(root.val))
        res += self.__levelorder(height, root.left, key, i+1)
        res += self.__levelorder(height, root.right, key, i+1)
        return res

    def serialize(self, file='tree.txt'):
        """Serialize binary tree."""
        if self.isEmpty():
            raise AttributeError("Tree is empty")
        self.__serialize(self.root, file)

    def __serialize(self, root, file):
        if not root:
            return
        elements = self.preorder()
        with open(file, 'w') as f:
            for el in elements:
                f.write(str(el) + '\n')

    @staticmethod
    def deserialize(file='tree.txt'):
        """Deserialize binary tree."""
        elements = list()
        with open(file, 'r') as f:
            for line in f:
                elements.append(int(line))
        new_tree = BinarySearchTree()
        for el in elements:
            new_tree.add(el)
        return new_tree            
