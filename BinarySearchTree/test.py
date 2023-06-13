from Tree import BinarySearchTree, Node

def test_binary_search_tree():
    bst = BinarySearchTree()

    # Add nodes to the tree
    bst.add(5)
    bst.add(3)
    bst.add(7)
    bst.add(2)
    bst.add(4)
    bst.add(6)
    bst.add(8)

    # Test isEmpty()
    assert bst.isEmpty() == False

    # # Test getHeight()
    assert bst.getHeight() == 3

    # # Test getNumberOfNodes()
    assert bst.getNumberOfNodes() == 7

    # Test getRootData()
    assert bst.getRootData() == 5

    # Test setRootData()
    bst.setRootData(10)
    assert bst.getRootData() == 10
    
    # Test contains()
    assert bst.contains(7) == True
    assert bst.contains(9) == False

    # Test remove()
    bst.remove(7)
    assert bst.contains(7) == False
    
    # Test preorder()
    preorder_elements = bst.preorder()
    assert preorder_elements == [10, 3, 2, 8, 4, 6]

    # Test inorder()
    inorder_elements = bst.inorder()
    assert inorder_elements == [2, 3, 4, 6, 8, 10]

    # Test postorder()
    postorder_elements = bst.postorder()
    assert postorder_elements == [2, 6, 4, 8, 3, 10]

    # Test levelorder()
    levelorder_elements = bst.levelorder()
    assert levelorder_elements == [10, 3, 2, 8, 4, 6]

    # Test serialize() and deserialize()
    bst.serialize('tree.txt')
    new_bst = BinarySearchTree.deserialize('tree.txt')
    assert new_bst.inorder() == inorder_elements

    # Test clear()
    bst.clear()
    assert bst.isEmpty() == True

    print("All tests passed successfully!")
