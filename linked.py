class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.tail = Node(None, None)
        self.head = Node(None, self.tail)
        self.len = 0
    
    def append(self, data):
        current = self.head
        for i in range(self.len+1):
            current = current.next
        new = Node(current.data, current.next)
        current.next = new
        current.data = data
        self.len += 1

    def insert(self, data, index):
        current = self.head
        for i in range(index+1):
            current = current.next
        new = Node(current.data, current.next)
        current.next = new
        current.data = data
        self.len += 1

    def print(self):
        current = self.head.next
        while current.data is not None:
            print(current.data, end=" ")
            if current.next.data is not None:
                print("-> ", end="")
            current = current.next
        print("")

    def index(self, data):
        current = self.head
        index = -1
        try:
            while current.data != data:
                current = current.next
                index += 1
            if current.data == data:
                return index
            else:
                index = -1
        except:
            pass
        return -1

    def delete(self, index):
        current = self.head
        try:
            for i in range(index+1):
                current = current.next
            current.data = current.next.data
            current.next = current.next.next
            self.len -= 1
        except:
            pass



if __name__ == "__main__":
    L = LinkedList()
    L.append(1)
    L.append(3)
    L.print()           # 1 -> 3
    L.insert(10, 1)
    L.insert(15, 0)
    L.print()           # 15 -> 1 -> 10 -> 3
    print(L.index(1))   # 1
    L.delete(0)
    L.print()           # 1 -> 10 -> 3