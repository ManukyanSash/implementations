from Tree import GeneralTree, Node

def test_tree_functionality():
    node1 = Node(lambda x: x + 1)
    node2 = Node(lambda x: x * 2)
    node3 = Node(lambda x: x ** 2)
    node4 = Node(lambda x: x - 1)

    tree = GeneralTree()
    tree.insert(None, node1)
    tree.insert(node1, node2)
    tree.insert(node1, node3)
    tree.insert(node2, node4)

    tree.execute(3)
    tree.print_vals() # output should be 4 8 7 16