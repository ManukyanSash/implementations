class Node:
    def __init__(self, data, next=None):
        self.next = next
        self.data = data
  

class LinkedList:
    def __init__(self):
        """Constructor"""
        self.__head = None
        self.__count = 0
    
    def __iter__(self):
        """Creating iterator"""
        self.current = self.get_head()
        return self

    def __next__(self):
        """Iterating"""
        if self.current is None:
            raise StopIteration
        data = self.current.data
        self.current = self.current.next
        return data
    
    def __len__(self):
        """len() function"""
        return self.get_count()

    def __add__(self, obj):
        """Operator +"""
        self.merge(obj)

    def __contains__(self, val):
        "Operator in"
        return self.find(val) != None

    def get_head(self):
        """Get head of list"""
        return self.__head

    def set_head(self, head):
        """Set head of list"""
        self.__head = head

    def get_count(self):
        """Get count of list"""
        return self.__count

    def __set_count(self, val):
        """Set count of list"""
        self.__count = val

    def insert(self, index, data):
        """Insert data to list by index"""
        if index < 0 or index >= self.get_count():
            raise IndexError("Wrong index")
        ins_node = Node(data)
        if index == 0:
            ins_node.next = self.get_head()
            self.__set_count(self.get_count() + 1)
            self.set_head(ins_node)
            return
        curr = self.get_head()
        curr_next = curr.next
        for i in range(index - 1):
            curr = curr.next
            curr_next = curr_next.next
        curr.next = ins_node
        ins_node.next = curr_next
        self.__set_count(self.get_count() + 1)

    def delete(self, index):
        """Delete element by index"""
        if index < 0 or index >= self.get_count():
            raise IndexError("Wrong index")
        curr = self.get_head()
        curr_next = curr.next
        if index == 0:
            self.set_head(curr.next)
            curr.next = None
            self.__set_count(self.get_count() - 1)
            return
        for i in range(index - 1):
            curr = curr_next
            curr_next = curr_next.next
        curr.next = curr_next.next
        curr_next.next = None    
        self.__set_count(self.get_count() - 1)

    def find(self, data):
        """Find element by data"""
        tmp = self.get_head()
        count = self.get_count()
        for i in range(count):
            if tmp.data == data:
                return tmp
            tmp = tmp.next
        return None

    def print_list(self):
        """Print all elements of list"""
        tmp = self.get_head()
        res = str()
        for i in range(self.get_count()):
            res += str(tmp.data) + " "
            tmp = tmp.next
        print(res)

    def push_back(self, data):
        """Add element to the end"""
        tmp = self.get_head()
        count = self.get_count()
        if count == 0:
            self.set_head(Node(data))
            self.__set_count(count + 1)
            return

        for i in range(count - 1):
            tmp = tmp.next
        tmp.next = Node(data)
        self.__set_count(count + 1)
    
    def pop_back(self):
        """Remove element from the end"""
        self.delete(self.get_count() - 1)         

    def push_front(self, val):
        """Add element to start"""
        tmp = Node(val)
        tmp.next = self.get_head()  
        self.set_head(tmp) 
        self.__set_count(self.get_count() + 1)


    def pop_front(self):
        """Remove element from the beginning"""
        self.delete(0)

    def sort(self):
        """Sorting list"""
        curr = self.get_head()
        elements = list()
        count = self.get_count()
        for i in range(count):
            elements.append(curr)
            curr = curr.next

        elements.sort(key = lambda x : x.data)        

        self.set_head(elements[0])
        for i in range(len(elements) - 1):
            elements[i].next = elements[i + 1]
    
    def clear(self):
        """Remove all from list"""
        current = self.get_head()
        while current is not None:
            next_node = current.next
            current.next = None
            current = next_node
        self.set_head(None)
        self.__set_count(0)

    def merge(self, obj):
        """Merge two lists"""
        tmp = obj.get_head()
        while tmp != None:
            self.push_back(tmp.data)
            tmp = tmp.next
        obj.clear()

