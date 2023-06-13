import os
import sys
import test
from Tree import GeneralTree, Node

if __name__ == "__main__":
    node1 = Node(lambda x: x + 1)
    node2 = Node(lambda x: x * 2)
    node3 = Node(lambda x: x ** 2)
    node4 = Node(lambda x: x - 1)

    tree = GeneralTree()
    tree.insert(None, node1)
    tree.insert(node1, node2)
    tree.insert(node1, node3)
    tree.insert(node2, node4)
    tree.execute(5)
    tree.serialize()