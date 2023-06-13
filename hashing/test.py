from HashTable import HashTable

def test_hash_table():
    # Create a hash table
    hash_table = HashTable()

    # Insert key-value pairs
    hash_table.insert("apple", 1)
    hash_table.insert("banana", 2)
    hash_table.insert("orange", 3)

    # Find values by keys
    print(hash_table.find("apple"))    # Output: 1
    print(hash_table.find("banana"))   # Output: 2
    print(hash_table.find("orange"))   # Output: 3

    # Update value for a key
    hash_table.insert("apple", 4)
    print(hash_table.find("apple"))    # Output: 4

    # Delete a key-value pair
    hash_table.delete("banana")
    try:
        print(hash_table.find("banana"))
    except ValueError as e:
        print(str(e))   # Output: No such element.

test_hash_table()