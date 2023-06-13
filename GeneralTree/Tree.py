class Node:
    def __init__(self, func=None):
        self.function = func
        self.children = list()

    def set_function(self, func):
        self.function = func

class GeneralTree:
    def __init__(self):
        self.head = None

    def insert(self, node1, node2):
        if self.head == None and node1 == self.head:
            self.head = node2
            return
        self.find(node1).children.append(node2)

    def find(self, node):
        if self.head is not None:
            return self.__find(self.head, node)
        return None
    
    def __find(self, curr_node, node):
        if curr_node == node:
            return curr_node
        for child in curr_node.children:
            return self.__find(child, node)
        return None

    def execute(self, val):
        if self.head is not None:
            self.__execute(self.head, val) 

    def __execute(self, tmp_node, val):
        tmp_node.function = tmp_node.function(val)
        tmp_val = tmp_node.function
        for child in tmp_node.children:
            if child is not None:
                self.__execute(child, tmp_val)
    
    def print_vals(self):
        if self.head is not None:
            self.__print_vals(self.head)
    
    def __print_vals(self, tmp_node):
        print(tmp_node.function)
        for child in tmp_node.children:
            self.__print_vals(child)
    
 