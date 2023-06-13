from SinglyList import LinkedList as SingleLinkedList

def test_single_linked_list():
    # Create an empty linked list
    list = SingleLinkedList()

    # Test push_front() and print_list()
    list.push_front(10)
    list.push_front(20)
    list.push_front(30)
    print("Linked list after push_front():")
    list.print_list()  # Output: 30 20 10

    # Test push_back() and print_list()
    list.push_back(40)
    list.push_back(50)
    print("Linked list after push_back():")
    list.print_list()  # Output: 30 20 10 40 50

    # Test insert() and print_list()
    list.insert(3, 35)
    list.insert(1, 25)
    print("Linked list after insert():")
    list.print_list()  # Output: 30 25 20 10 35 40 50

    # Test find()
    index = list.find(20)
    print("Element with value 20:", index)  # Output: 2

    # Test delete() and print_list()
    list.delete(4)
    list.delete(1)
    print("Linked list after delete():")
    list.print_list()  # Output: 30 20 10 40 50

    # Test pop_front(), pop_back(), and print_list()
    list.pop_front()
    list.pop_back()
    print("Linked list after pop_front() and pop_back():")
    list.print_list()  # Output: 20 10 40

    # Test sort() and print_list()
    list.sort()
    print("Linked list after sort():")
    list.print_list()  # Output: 10 20 40

    # Create another linked list
    list2 = SingleLinkedList()
    list2.push_back(15)
    list2.push_back(25)
    list2.push_back(45)

    # Test merge() and print_list()
    list.merge(list2)
    print("Linked list after merge():")
    list.print_list()  # Output: 10 20 40 15 25 45

    # Test clear() and print_list()
    list.clear()
    print("Linked list after clear():")
    list.print_list()  # Output:

test_single_linked_list()