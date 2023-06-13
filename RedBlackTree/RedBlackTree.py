class Node:
    def __init__(self, val):
        self.right = None
        self.left = None
        self.parent = None
        self.val = val
        self.color = 'r'

class RedBlackTree:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        if not self.root:
            self.root = Node(val)
            self.root.color = 'b'
            return
        self.root = self._insert(self.root, Node(val))
        self._balance(Node(val))
    
    def _insert(self, root, node):
        if not root:
            return node
        if node.val < root.val:
            if root.left:
                root.left = self._insert(root.left, node)
            else:
                root.left = node
                root.left.parent = root
        if node.val > root.val:
            if root.right:
                root.right = self._insert(root.right, node)
            else:
                root.right = node
                root.right.parent = root
        return root    
    
    def _balance(self, node):
        st = self._find(self.root, node)
        if not st or st == self.root:
            return
        if st.parent.color == 'b':
            return
        grandparent = st.parent.parent
        ultraparent = grandparent.parent
        left = None
        if ultraparent and ultraparent.left == grandparent:
            left = True
        if ultraparent and ultraparent.right == grandparent:
            left = False
        uncle = None
        if grandparent.right == st.parent:
            uncle = grandparent.left
        else:
            uncle = grandparent.right
        if st.parent and st.parent.color == 'r':
            if not uncle or uncle.color == 'b':
                if st.parent == grandparent.right:  
                    if st == st.parent.left:
                        grandparent = self.RL_rotation(grandparent)
                        grandparent.right.parent = grandparent
                        grandparent.left.parent = grandparent
                        if ultraparent:
                            if left is True:
                                ultraparent.left = grandparent
                                ultraparent.left.parent = ultraparent
                            else:
                                ultraparent.right = grandparent
                                ultraparent.right.parent = ultraparent
                        else:
                            self.root = grandparent
                    else:
                        grandparent = self.RR_rotation(grandparent) 
                        grandparent.right.parent = grandparent
                        grandparent.left.parent = grandparent
                        if ultraparent:
                            if left is True:
                                ultraparent.left = grandparent
                                ultraparent.left.parent = ultraparent
                            else:
                                ultraparent.right = grandparent
                                ultraparent.right.parent = ultraparent
                        else:
                            self.root = grandparent
                else:
                    if st == st.parent.right:
                        grandparent = self.LR_rotation(grandparent)
                        grandparent.right.parent = grandparent
                        grandparent.left.parent = grandparent
                        if ultraparent:
                            if left is True:
                                ultraparent.left = grandparent
                                ultraparent.left.parent = ultraparent
                            else:
                                ultraparent.right = grandparent
                                ultraparent.right.parent = ultraparent
                        else:
                            self.root = grandparent
                    else:
                        grandparent = self.LL_rotation(grandparent)
                        grandparent.right.parent = grandparent
                        grandparent.left.parent = grandparent
                        if ultraparent:
                            if left is True:
                                ultraparent.left = grandparent
                                ultraparent.left.parent = ultraparent
                            else:
                                ultraparent.right = grandparent
                                ultraparent.right.parent = ultraparent
                        else:
                            self.root = grandparent
                return
            
            if uncle.color == 'r':
                st.parent.color = 'b'
                uncle.color = 'b'
                
                if grandparent != self.root:
                    grandparent.color = 'r'
                
                self._balance(grandparent)

    def remove(self, val):
        node = self._find(self.root, Node(val))
        if node:
            self._remove(node)
            return "True"
        return "False"
    
    def _remove(self, node):
        if node.color == 'r':
            self.BSTremove(self.root, node)
            return
        if node.left and node.left.color == 'r':
            node.val == node.left.val
            self.BSTremove(self.root, node.left)
            return
        if node.right and node.right.color == 'r':
            node.val == node.right.val
            self.BSTremove(self.root, node.right)
            return
        node.color = 'db'
        self._coloring(node)

    def successor(self, root):
        successor = root.right
        while successor.left:
            successor = successor.left
        root.val = successor.val
        return successor
    
    def _find(self, root, node):
        if not root:
            return None
        if node.val > root.val:
            return self._find(root.right, node)
        if node.val < root.val:
            return self._find(root.left, node)
        return root
    
    def RR_rotation(self, node):
        tmp = node.right
        T2 = tmp.left
        node.right.left = node
        node.right = T2
        if T2:
            T2.parent = node
        tmp.color = 'b'
        tmp.left.color = 'r'
        return tmp
    
    def LL_rotation(self, node):
        tmp = node.left
        T2 = tmp.right
        node.left.right = node
        node.left = T2
        if T2:
            T2.parent = node
        tmp.color = 'b'
        tmp.right.color = 'r'
        return tmp
    
    def RL_rotation(self, node):
        tmp = node.right
        T2 = tmp.left
        node.right = T2
        while T2.right:
            T2 = T2.right
        T2.right = tmp
        tmp.left = None
        node = self.RR_rotation(node)
        return node

    def LR_rotation(self, node):
        tmp = node.left
        T3 = tmp.right
        node.left = T3
        while T3.left:
            T3 = T3.left
        T3.left = tmp
        tmp.right = None
        node = self.LL_rotation(node)
        return node
    
    def inorder(self):
        return self._inorder(self.root)
    
    def _inorder(self, root):
        res = list()
        if not root:
            return []
        res += self._inorder(root.left)
        if root == self.root:
            res.append((root.val, root.color, None))
        else:
            res.append((root.val, root.color, root.parent.val))
        res += self._inorder(root.right)
        return res
            
    def _coloring(self, node):
        if node.color != 'db':
            return
        if not node.parent:
            node.color = 'b'
            return
        sibling = None
        if node == node.parent.left:
            sibling = node.parent.right
        else:
            sibling = node.parent.left
        if not sibling or (sibling.left.color == 'b' and sibling.right.color == 'b'):
            node.color = 'b'
            if node.parent.color == 'b':
                node.parent.color = 'r'
            else:
                node.parent.color = 'db'
            sibling.color = 'r'
            if node.parent.color == 'db':
                self._coloring(node.parent)
            return
        if sibling.color == 'r':
            node.parent.color, sibling.color = sibling.color, node.parent.color
            self.RR_rotation(node.parent)
            self._coloring(node)
            return
        if sibling.color == 'b':
            far = None
            near = None
            if node == node.parent.left:
                far = sibling.right
                near = sibling.left
            else:
                far = sibling.left
                near = sibling.right
            if far.color == 'b':
                sibling.color, near.color = near.color, sibling.color
                self.LL_rotation(sibling)
                self._coloring(node)
            node.parent.color, sibling.color = sibling.color, node.parent.color
            self.RR_rotation(sibling)
            node.color = 'b'
            far.color = 'b'
            self._coloring(node)
    
    def BSTremove(self, root, node):
        if not root:
            return
        
        if root.val > node.val:
            root.left = self.BSTremove(root.left, node)
            return root
        if root.val < node.val:
            root.right = self.BSTremove(root.right, node)
            return root
        
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        
        successor = root.right
        while successor.left:
            successor = successor.left
        root.val = successor.val
        root.right = self.BSTremove(root.right, Node(successor.val))
        return root

    def clear(self):
        self.root = None

    def getEntry(self, node):
        if self.isEmpty():
            raise AttributeError("Tree is empty")
        if not self.contains(node.val):
            raise ValueError("Entry is not found")
        return self._getEntry(self.root, node)    

    def _getEntry(self, root, node):
        if not root:
            return False
        if root.val > node.val:
            return self._contains(root.left, node)
        if root.val < node.val:
            return self._contains(root.right, node)
        return root

    def contains(self, data):
        if self.isEmpty():
            raise AttributeError("Tree is empty")
        return self._contains(self.root, data)
    
    def _contains(self, root, data):
        if not root:
            return False
        if root.val == data:
            return True
        if root.val > data:
            return self._contains(root.left, data)
        if root.val < data:
            return self._contains(root.right, data)
        
    def isEmpty(self):  
        return self.root is None

    def getHeight(self):
        if self.isEmpty():
            return 0
        return self._getHeight(self.root)

    def _getHeight(self, root):
        if not root:
            return 0
        return 1 + max(self._getHeight(root.left), self._getHeight(root.right)) 

    def getNumberOfNodes(self):
        if self.isEmpty():
            return 0
        return self._getNumberOfNodes(self.root)

    def _getNumberOfNodes(self, root):
        if not root:
            return 0
        return 1 + self._getNumberOfNodes(root.left) + self._getNumberOfNodes(root.right)  

    def getRootData(self):
        if self.isEmpty():
            raise AttributeError("Tree is empty")
        return self.root.val

    def levelorder(self, visit=lambda x:x):
        if self.isEmpty():
            raise AttributeError("Tree is empty")
        height = self.getHeight()
        elements = list()
        for i in range(height):
            elements += self._levelorder(i, self.root, visit)
        return elements

    def _levelorder(self, height, root, key, i=0):
        res = []
        if not root:
            return [] 
        if i > height:
            return []
        if i == height:
            res.append(key(root.val))
        res += self._levelorder(height, root.left, key, i+1)
        res += self._levelorder(height, root.right, key, i+1)
        return res
