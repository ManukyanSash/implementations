class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class HashTable:
    def __init__(self, size=20):
        self.size = size
        self.arr = [None] * self.size

    def hash_function(self, key):
        res = 0
        bytes_arr = key.encode("utf-8")
        for char in bytes_arr:
            res += char
        return res % self.size

    def insert(self, key, value):
        ind = self.hash_function(key)
        if not self.arr[ind]:
            self.arr[ind] = Pair(key, value)
            return
        tmp = self.arr[ind]
        while tmp != None:
            if tmp.key == key:
                tmp.val = value
                return
            if not tmp.next:
                tmp.next = Pair(key, value)
                return
            tmp = tmp.next
        tmp.next = Pair(key, value)

    def delete(self, key):
        ind = self.hash_function(key)
        prev = self.arr[ind]
        tmp = self.arr[ind]
        while tmp and tmp.key != key:
            prev = tmp
            tmp = tmp.next
        if not tmp:
            raise ValueError("No such element.")   
        if tmp == prev:
            self.arr[ind] = tmp.next
        else:
            prev.next = tmp.next

    def find(self, key):
        ind = self.hash_function(key)
        tmp = self.arr[ind]
        while tmp and tmp.key != key:
            tmp = tmp.next
        if not tmp:
            raise ValueError("No such element.")
        return tmp.val
